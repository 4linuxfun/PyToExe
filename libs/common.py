#!/usr/bin/env python3
# coding=utf-8
"""
common库，用于一些常用函数的编写
"""
import os
import subprocess
from multiprocessing import Process, Queue
from loguru import logger
from pathlib import Path


def run_command(args, panel, obj):
    """
    线程执行命令
    :param args: pyinstaller的参数
    :param panel: 通过panel判断不同的参数处理逻辑，可选：config、spec
    :param obj: 日志队列，用于线程之间传递信息，方便主线程打印
    :return:
    """
    python_path = args.pop('python')
    command = python_path + ' -m PyInstaller '
    if panel == 'config':
        other_args = args.pop('other_args')
        script_path = args.pop('package')
        script_name = Path(script_path).name
        script_dir = Path(script_path).parent
        os.chdir(script_dir)
        logger.debug(f"current dir is:{script_dir}")
        command = python_path + ' -m PyInstaller '
        for key, value in args.items():
            if value is True:
                command += ' ' + key
            elif value:
                command += ' ' + key + ' ' + value
        command += f" {other_args} {script_name}"
    elif panel == 'spec':
        spec_path = args.pop('spec_file')
        spec_dir = Path(spec_path).parent
        os.chdir(spec_dir)
        logger.debug(f"current dir is:{spec_dir}")
        for key, value in args.items():
            if value is True:
                command += ' ' + key
            elif value:
                command += ' ' + key + ' ' + value
        command += f" {spec_path}"

    logger.debug('start to run subprocess')
    logger.debug(command)
    try:
        process = subprocess.Popen(command, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT,
                                   text=True)
        # return_code = process.poll()
        while process.poll() is None:
            line = process.stdout.readline()
            # return_code = process.poll()
            line = line.strip()
            if line:
                logger.debug(line)
    except Exception as e:
        logger.debug(e)
    obj.Label = '生成'
    obj.Enable()


if __name__ == '__main__':
    pass
