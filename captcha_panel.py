#!/usr/bin/env python
# coding:utf-8

import wx

class CaptchaPanel(wx.Panel):
	def __init__(self, parent, bitmaps, *args, **kwargs):
		wx.Panel.__init__(self, parent, *args, **kwargs)
		self.SetBackgroundColour(wx.WHITE)
		layout = wx.BoxSizer(wx.HORIZONTAL)
		self.bitmap_buttons = [wx.BitmapToggleButton(self, -1, bitmap) for bitmap in bitmaps]
		layout.AddMany(self.bitmap_buttons)
		self.SetSizer(layout)


if __name__ == '__main__':
	import sys
	app = wx.App()
	bitmaps = [wx.Image(filename).ConvertToBitmap() for filename in sys.argv[1:]]
	frame = wx.Frame(None,-1)
	panel = CaptchaPanel(frame, bitmaps, -1)
	frame.Show()
	app.MainLoop()

