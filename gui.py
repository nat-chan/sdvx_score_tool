#!/usr/bin/env python
# coding:utf-8

import wx
import os
from selenium import webdriver
from io import BytesIO
from input_panel import *
from captcha_panel import *

login_url = 'http://p.eagate.573.jp/gate/p/login.html?path='         \
            'http%3A%2F%2Fp.eagate.573.jp%2Fgame%2Fsdvx%2Fiv%2Fp%2F' \
            'playdata%2Fmusicdata%2Findex.html%3Frecent%3D1'         \
#click()
#is_selected()

#ConnectionRefusedError

class ScoreTool(wx.Frame):
	def __init__(self, parent, driver, *args, **kwargs):

		no_resize = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
		wx.Frame.__init__(self, parent, style=no_resize, size=(470,235), *args, **kwargs)
		self.driver = driver
		driver.get(login_url)

		self.screenshot = wx.Image(BytesIO(driver.get_screenshot_as_png())).ConvertToBitmap()
		self.element = self.findElement(self.driver)

		self.root_panel = wx.Panel(self, -1)

		self.panel1 = wx.Panel(self.root_panel, -1)

		self.question_bitmap = wx.StaticBitmap(
		  self.panel1
		, -1
		, self.cropBitmap(self.screenshot, self.element['question'])
		)

		self.two_line_panel = TwoLinePanel(self.panel1, -1)

		self.layout1 = wx.BoxSizer(wx.HORIZONTAL)
		self.layout1.Add(self.question_bitmap)
		self.layout1.Add(self.two_line_panel, proportion=1)
		self.panel1.SetSizer(self.layout1)

		self.bottom_panel = CaptchaPanel(
		  self.root_panel
		, [self.cropBitmap(self.screenshot, element) for element in self.element['captcha']]
		, -1
		)
		self.root_layout = wx.BoxSizer(wx.VERTICAL)
		self.root_layout.Add(self.panel1, flag=wx.GROW)
		self.root_layout.Add(self.bottom_panel)
		self.root_panel.SetSizer(self.root_layout)
		self.two_line_panel.input_panel.button.Bind(wx.EVT_BUTTON, self.OnLogin)

	def OnLogin(self, event):
		for i, button in enumerate(self.bottom_panel.bitmap_buttons):
			if button.GetValue():
				self.element['captcha'][i].click()
		self.element['KID'].send_keys(self.two_line_panel.input_panel.text_ctrl.GetValue())
		self.element['pass'].send_keys(self.two_line_panel.password_panel.text_ctrl1.GetValue())
		self.element['submit'].click()



	@staticmethod
	def findElement(driver):
		element = dict()
		element['captcha'] = driver.find_elements_by_xpath(
		                                    '//label[contains(@for, "id_kcaptcha_c")]/img')
		element['question'] = driver.find_element_by_xpath('//tbody/tr/td/div/div/div/img')
		element['KID'] = driver.find_element_by_id('KID')
		element['pass'] = driver.find_element_by_id('pass')
		element['submit'] = driver.find_element_by_xpath('//input[@class="login_btn textindent"]')
#<input value="規約に同意してログイン" class="login_btn textindent" type="submit">

		return element

	@staticmethod
	def cropBitmap(screenshot, element):
		return screenshot.GetSubBitmap(
		  (element.location['x']
		  ,element.location['y']
		  ,element.size['width']
		  ,element.size['height']
		  )
		)

if __name__ == '__main__':
	app = wx.App()
	driver = webdriver.PhantomJS(service_log_path=os.path.devnull)
	frame = ScoreTool(None, driver, -1, title='score_tool')
	frame.Show()
	app.MainLoop()
	driver.close()


