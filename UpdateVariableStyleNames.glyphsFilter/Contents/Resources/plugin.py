# encoding: utf-8

###########################################################################################################
#
#
#	Filter without dialog plug-in
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Filter%20without%20Dialog
#
#
###########################################################################################################

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *


class UpdateVariableStyleNames(FilterWithoutDialog):
	
	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			"en": "Update Variable Style Names",
			
			})

	@objc.python_method
	def filter(self, layer, inEditView, customParameters):
		
		
		elidable_prefix = customParameters[0] if customParameters else ""
		font = layer.font()

		if layer.parent != font.glyphs[0]:
			return

		for instance in font.instances:
			if instance.type == 0:
				if instance.variableStyleName:
					variable_style_name_renamed = instance.variableStyleName.replace(elidable_prefix, "").strip()
					instance.variableStyleName = variable_style_name_renamed

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
