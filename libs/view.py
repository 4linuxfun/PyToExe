#!/usr/bin/env python3
# coding=utf-8

from multiprocessing.dummy import Process
from functools import partial
from loguru import logger
import wx

from . import common
from .source_view import MyFrame


class LogToText(object):
    """
    把日志输出到textCtrl中
    """

    def __init__(self, text):
        self.textCtrl = text

    def write(self, msg):
        self.textCtrl.write(msg)


class PyToExeGUI(MyFrame):
    def __init__(self):
        super().__init__(None)
        self.pyinstaller_args = {'config': {'--noconfirm': True,
                                            '--windowed': True,
                                            'other_args': ''},
                                 'spec': {}}
        # 捆绑btn到对应的txt控件，完成联动操作
        self.python_select_btn.Bind(wx.EVT_BUTTON, partial(self.select_file, txt=self.python_txt))
        self.package_select_btn.Bind(wx.EVT_BUTTON, partial(self.select_file, txt=self.package_txt))
        self.upx_select_btn.Bind(wx.EVT_BUTTON, partial(self.select_dir, txt=self.upx_txt))
        self.spec_python_btn.Bind(wx.EVT_BUTTON, partial(self.select_file, txt=self.spec_python_txt))
        self.spec_select_btn.Bind(wx.EVT_BUTTON, partial(self.select_file, txt=self.spec_specfile_txt))
        self.config_generate_btn.Bind(wx.EVT_BUTTON, partial(self.run_pyinstaller, panel='config'))
        self.spec_generate_btn.Bind(wx.EVT_BUTTON, partial(self.run_pyinstaller, panel='spec'))
        self.icon_select_btn.Bind(wx.EVT_BUTTON, partial(self.select_file, txt=self.icon_txt))
        logger.remove(0)
        # 日志输出到logtxt控件中
        logger.add(LogToText(self.log_textCtrl).write, level='DEBUG',
                   format="{time:YYYY-MM-DD HH:mm:ss} {message}")

    def select_file(self, event: wx.EVT_BUTTON, txt=None):
        """
        文件选择按钮触发事件处理
        :param event:按钮触发事件
        :param txt:关联的txtCtrl对象，可用于内容关联填充
        """
        with wx.FileDialog(self, "选择文件") as dialog:
            if dialog.ShowModal() == wx.ID_CANCEL:
                return
            txt.Value = dialog.Path

    def select_dir(self, event: wx.Event, txt=None):
        """
        目录选择按钮事件处理
        :param event:按钮触发事件
        :param txt:关联的txtCtrl对象，可用于内容关联填充
        :return:
        """
        with wx.DirDialog(self, "选择目录") as dialog:
            if dialog.ShowModal() == wx.ID_CANCEL:
                return
            txt.Value = dialog.Path

    def run_pyinstaller(self, event, panel=None):
        """
        “生成”按钮触发事件
        :param panel:
        :param event
        """
        obj = event.EventObject
        obj.Label = '生成中'
        obj.Disable()
        logger.debug(self.pyinstaller_args)
        # pyinstaller = self.pyinstaller_args.pop('pyinstaller')
        # package = self.pyinstaller_args.pop('package')
        if panel == 'config':
            args = self.pyinstaller_args['config'].copy()
        else:
            args = self.pyinstaller_args['spec'].copy()
        run_thread = Process(target=common.run_command,
                             args=(args, panel, obj))
        run_thread.start()

    def update_args(self, event):
        """
        所有需要实时更新self.pyinstaller_args的，需要调用此方法
        :param event:
        """
        obj = event.EventObject

        if obj is self.python_txt:
            logger.debug('python txt')
            self.pyinstaller_args['config']['python'] = self.python_txt.Value
        elif obj is self.package_txt:
            self.pyinstaller_args['config']['package'] = self.package_txt.Value
        elif obj is self.upx_txt:
            self.pyinstaller_args['config']['--upx-dir'] = self.upx_txt.Value
        elif obj is self.icon_txt:
            self.pyinstaller_args['config']['--icon'] = self.icon_txt.Value
        elif obj is self.log_level_choice:
            self.pyinstaller_args['config']['--log-level'] = self.log_level_choice.GetString(
                self.log_level_choice.Selection)
        elif obj is self.clean_choice:
            self.pyinstaller_args['config']['--clean'] = True if self.clean_choice.Selection == 0 else False
        elif obj is self.type_radio:
            logger.debug('type radio对象')
            if self.type_radio.Selection == 0:
                if '--onedir' in self.pyinstaller_args:
                    del self.pyinstaller_args['config']['--onedir']
                self.pyinstaller_args['config']['--onefile'] = True
            elif self.type_radio.Selection == 1:
                if '--onefile' in self.pyinstaller_args:
                    del self.pyinstaller_args['config']['--onefile']
                self.pyinstaller_args['config']['--onedir'] = True
        elif obj is self.console_radio:
            logger.debug('console radio对象')
            if self.console_radio.Selection == 0:
                if '--windowed' in self.pyinstaller_args:
                    del self.pyinstaller_args['config']['--windowed']
                self.pyinstaller_args['--console'] = True
            else:
                if '--console' in self.pyinstaller_args:
                    del self.pyinstaller_args['config']['--console']
                self.pyinstaller_args['--windowed'] = True
        elif obj is self.name_txt:
            self.pyinstaller_args['config']['--name'] = self.name_txt.Value
        elif obj is self.spec_python_txt:
            self.pyinstaller_args['spec']['python'] = self.spec_python_txt.Value
        elif obj is self.spec_specfile_txt:
            self.pyinstaller_args['spec']['spec_file'] = self.spec_specfile_txt.Value
        elif obj is self.args_txt:
            self.pyinstaller_args['config']['other_args'] = self.args_txt.Value

    def select_spec_file(self, event, txt=None):
        """
        spec选项页“生成”按钮触发事件处理
        :param event:
        :param txt: 绑定的txtCtrl对象
        :return:
        """
        with wx.FileDialog(self, "选择spec文件") as dialog:
            if dialog.ShowModal() == wx.ID_CANCEL:
                return
            txt.Value = dialog.Path
