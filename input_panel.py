#!/usr/bin/env python
# coding:utf-8

import wx

class InputPanel(wx.Panel):
	def __init__(self, parent, label_text_ctrl, label_button, *args, **kwargs):
		wx.Panel.__init__(self, parent, *args, **kwargs)
		layout = wx.BoxSizer(wx.HORIZONTAL)
		self.button = wx.Button(self, -1, label_button)
		self.text_ctrl = wx.TextCtrl(self, -1)
		layout.Add( wx.StaticText(self, -1, label_text_ctrl))
		layout.Add(self.text_ctrl, proportion=1, flag=wx.GROW)
		layout.Add(self.button)
		self.SetSizer(layout)

class PasswordPanel(wx.Panel):
	def __init__(self, parent, label_text_ctrl, label_button, *args, **kwargs):
		wx.Panel.__init__(self, parent, *args, **kwargs)
		layout = wx.BoxSizer(wx.HORIZONTAL)
		self.panel = wx.Panel(self, -1)
		self.button = wx.Button(self, -1, label_button)
		self.text_ctrl1 = wx.TextCtrl(self.panel, -1, style=wx.TE_PASSWORD, size=(234,23))
		self.text_ctrl2  = wx.TextCtrl(self.panel, -1, size=(234,23))
		layout.Add(wx.StaticText(self, -1, label_text_ctrl))
		layout.Add(self.panel, proportion=1)
		layout.Add(self.button)
		self.SetSizer(layout)
		self.button.Bind(wx.EVT_LEFT_DOWN, self.ShowPassword)
		self.button.Bind(wx.EVT_LEFT_UP, self.HidePassword)
		self.text_ctrl1.Show()
		self.text_ctrl2.Hide()

	def ShowPassword(self, event):
		self.text_ctrl2.SetValue(self.text_ctrl1.GetValue())
		self.text_ctrl2.Show()
		self.text_ctrl1.Hide()

	def HidePassword(self, event):
		self.text_ctrl1.Show()
		self.text_ctrl2.Hide()


class TwoLinePanel(wx.Panel):
	def __init__(self, parent, *args, **kwargs):
		wx.Panel.__init__(self, parent, *args, **kwargs)
		self.layout = wx.BoxSizer(wx.VERTICAL)
		self.input_panel = InputPanel(self,  "Konami ID : ", "ログイン", -1)
		self.password_panel = PasswordPanel(self, "Password  : ", "確認", -1)
		self.layout.Add(self.input_panel , flag=wx.GROW)
		self.layout.Add(self.password_panel, flag=wx.GROW)
		self.SetSizer(self.layout)

if __name__ == '__main__':
	app = wx.App()
	frame = wx.Frame(None, -1)
	panel = TwoLinePanel(frame, -1)
	frame.Show()
	app.MainLoop()

