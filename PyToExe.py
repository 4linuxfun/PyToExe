#!/usr/bin/env python3
# coding=utf-8

import wx
from libs.view import PyToExeGUI

if __name__ == '__main__':
    app = wx.App()
    frame = PyToExeGUI()
    frame.Show()
    app.MainLoop()
