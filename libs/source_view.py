# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyFrame
###########################################################################

class MyFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"PyToEXE程序", pos=wx.DefaultPosition,
                          size=wx.Size(600, 750), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(600, 750), wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook1 = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panel1 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        sbSizer4 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel1, wx.ID_ANY, u"通用配置"), wx.VERTICAL)

        fgSizer3 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer3.AddGrowableCol(1)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText2 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u"python解释器：", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        fgSizer3.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.python_txt = wx.TextCtrl(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        fgSizer3.Add(self.python_txt, 0, wx.ALL | wx.EXPAND, 5)

        self.python_select_btn = wx.Button(sbSizer4.GetStaticBox(), wx.ID_ANY, u"选择", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        fgSizer3.Add(self.python_select_btn, 0, wx.ALL, 5)

        self.m_staticText3 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u"打包脚本：", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        fgSizer3.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.package_txt = wx.TextCtrl(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        fgSizer3.Add(self.package_txt, 0, wx.ALL | wx.EXPAND, 5)

        self.package_select_btn = wx.Button(sbSizer4.GetStaticBox(), wx.ID_ANY, u"选择", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        fgSizer3.Add(self.package_select_btn, 0, wx.ALL, 5)

        self.m_staticText7 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u"upx目录：", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)

        fgSizer3.Add(self.m_staticText7, 0, wx.ALL, 5)

        self.upx_txt = wx.TextCtrl(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        fgSizer3.Add(self.upx_txt, 0, wx.ALL | wx.EXPAND, 5)

        self.upx_select_btn = wx.Button(sbSizer4.GetStaticBox(), wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize,
                                        0)
        fgSizer3.Add(self.upx_select_btn, 0, wx.ALL, 5)

        self.m_staticText16 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u"icon图标：", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)

        fgSizer3.Add(self.m_staticText16, 0, wx.ALL | wx.EXPAND, 5)

        self.icon_txt = wx.TextCtrl(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        fgSizer3.Add(self.icon_txt, 1, wx.ALL | wx.EXPAND, 5)

        self.icon_select_btn = wx.Button(sbSizer4.GetStaticBox(), wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize,
                                         0)
        fgSizer3.Add(self.icon_select_btn, 0, wx.ALL, 5)

        sbSizer4.Add(fgSizer3, 1, wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText14 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u"日志级别：", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)

        bSizer5.Add(self.m_staticText14, 0, wx.ALL, 5)

        log_level_choiceChoices = [u"TRACE", u"DEBUG", u"INFO", u"WARN", u"ERROR", u"CRITICAL "]
        self.log_level_choice = wx.Choice(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                          log_level_choiceChoices, 0)
        self.log_level_choice.SetSelection(2)
        bSizer5.Add(self.log_level_choice, 0, wx.ALL, 5)

        self.m_staticText101 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u"编译前是否清理日志和临时文件：", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText101.Wrap(-1)

        bSizer5.Add(self.m_staticText101, 0, wx.ALL, 5)

        clean_choiceChoices = [u"清理", u"不清理"]
        self.clean_choice = wx.Choice(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                      clean_choiceChoices, 0)
        self.clean_choice.SetSelection(0)
        bSizer5.Add(self.clean_choice, 0, wx.ALL, 5)

        sbSizer4.Add(bSizer5, 0, wx.EXPAND, 5)

        bSizer3.Add(sbSizer4, 1, wx.EXPAND, 5)

        sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel1, wx.ID_ANY, u"生成什么"), wx.VERTICAL)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        type_radioChoices = [u"单文件", u"单目录"]
        self.type_radio = wx.RadioBox(sbSizer3.GetStaticBox(), wx.ID_ANY, u"生成类型", wx.DefaultPosition, wx.DefaultSize,
                                      type_radioChoices, 1, wx.RA_SPECIFY_ROWS)
        self.type_radio.SetSelection(1)
        bSizer8.Add(self.type_radio, 0, wx.ALL, 5)

        console_radioChoices = [u"终端", u"窗体"]
        self.console_radio = wx.RadioBox(sbSizer3.GetStaticBox(), wx.ID_ANY, u"Windwos和Mac OSX特殊选项", wx.DefaultPosition,
                                         wx.DefaultSize, console_radioChoices, 1, wx.RA_SPECIFY_ROWS)
        self.console_radio.SetSelection(1)
        bSizer8.Add(self.console_radio, 0, wx.ALL, 5)

        sbSizer3.Add(bSizer8, 0, wx.EXPAND, 5)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText161 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"其他可选参数：", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText161.Wrap(-1)

        bSizer11.Add(self.m_staticText161, 0, wx.ALL | wx.EXPAND, 5)

        self.args_txt = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        bSizer11.Add(self.args_txt, 1, wx.ALL | wx.EXPAND, 5)

        sbSizer3.Add(bSizer11, 1, wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText10 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"生成程序名：", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)

        bSizer7.Add(self.m_staticText10, 0, wx.ALL | wx.EXPAND, 5)

        self.name_txt = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        bSizer7.Add(self.name_txt, 1, wx.ALL | wx.EXPAND, 5)

        self.config_generate_btn = wx.Button(sbSizer3.GetStaticBox(), wx.ID_ANY, u"生成", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        bSizer7.Add(self.config_generate_btn, 0, wx.ALL | wx.EXPAND, 5)

        sbSizer3.Add(bSizer7, 1, wx.EXPAND, 5)

        bSizer3.Add(sbSizer3, 0, wx.ALL | wx.EXPAND, 5)

        self.m_panel1.SetSizer(bSizer3)
        self.m_panel1.Layout()
        bSizer3.Fit(self.m_panel1)
        self.m_notebook1.AddPage(self.m_panel1, u"手动配置", True)
        self.m_panel2 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer72 = wx.BoxSizer(wx.VERTICAL)

        fgSizer31 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer31.AddGrowableCol(1)
        fgSizer31.SetFlexibleDirection(wx.BOTH)
        fgSizer31.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText11 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Pyinstaller路径：", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)

        fgSizer31.Add(self.m_staticText11, 0, wx.ALL | wx.EXPAND, 5)

        self.spec_python_txt = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                           0)
        fgSizer31.Add(self.spec_python_txt, 1, wx.ALL | wx.EXPAND, 5)

        self.spec_python_btn = wx.Button(self.m_panel2, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer31.Add(self.spec_python_btn, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText102 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Spec文件：", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.m_staticText102.Wrap(-1)

        fgSizer31.Add(self.m_staticText102, 0, wx.ALL, 5)

        self.spec_specfile_txt = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        fgSizer31.Add(self.spec_specfile_txt, 1, wx.ALL | wx.EXPAND, 5)

        self.spec_select_btn = wx.Button(self.m_panel2, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer31.Add(self.spec_select_btn, 0, wx.ALL | wx.EXPAND, 5)

        bSizer72.Add(fgSizer31, 0, wx.EXPAND, 5)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        self.spec_generate_btn = wx.Button(self.m_panel2, wx.ID_ANY, u"生成", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer9.Add(self.spec_generate_btn, 0, 0, 5)

        bSizer72.Add(bSizer9, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.m_panel2.SetSizer(bSizer72)
        self.m_panel2.Layout()
        bSizer72.Fit(self.m_panel2)
        self.m_notebook1.AddPage(self.m_panel2, u"Spec 导入", False)

        bSizer1.Add(self.m_notebook1, 0, wx.EXPAND | wx.ALL, 5)

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"日志"), wx.VERTICAL)

        self.log_textCtrl = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, wx.TE_MULTILINE)
        sbSizer1.Add(self.log_textCtrl, 1, wx.EXPAND, 5)

        bSizer1.Add(sbSizer1, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.python_txt.Bind(wx.EVT_TEXT, self.update_args)
        self.python_select_btn.Bind(wx.EVT_BUTTON, self.select_file)
        self.package_txt.Bind(wx.EVT_TEXT, self.update_args)
        self.package_select_btn.Bind(wx.EVT_BUTTON, self.select_file)
        self.upx_txt.Bind(wx.EVT_TEXT, self.update_args)
        self.upx_select_btn.Bind(wx.EVT_BUTTON, self.select_dir)
        self.log_level_choice.Bind(wx.EVT_CHOICE, self.update_args)
        self.clean_choice.Bind(wx.EVT_CHOICE, self.update_args)
        self.type_radio.Bind(wx.EVT_RADIOBOX, self.update_args)
        self.console_radio.Bind(wx.EVT_RADIOBOX, self.update_args)
        self.args_txt.Bind(wx.EVT_TEXT, self.update_args)
        self.name_txt.Bind(wx.EVT_TEXT, self.update_args)
        self.config_generate_btn.Bind(wx.EVT_BUTTON, self.run_pyinstaller)
        self.spec_python_txt.Bind(wx.EVT_TEXT, self.update_args)
        self.spec_python_btn.Bind(wx.EVT_BUTTON, self.select_file)
        self.spec_specfile_txt.Bind(wx.EVT_TEXT, self.update_args)
        self.spec_select_btn.Bind(wx.EVT_BUTTON, self.select_file)
        self.spec_generate_btn.Bind(wx.EVT_BUTTON, self.run_pyinstaller)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def update_args(self, event):
        event.Skip()

    def select_file(self, event):
        event.Skip()

    def select_dir(self, event):
        event.Skip()

    def run_pyinstaller(self, event):
        event.Skip()
