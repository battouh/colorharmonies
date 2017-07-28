# -*- coding: utf-8 -*-
import unittest
from colorsharmonies import Color, complementaryColor, triadicColor, splitComplementaryColor, tetradicColor, analogousColor, monochromaticColor

class colorsHarmonies(unittest.TestCase):
	# Obtain the complementary color of a color
	def test_complementaryColor(self):
		MagentaColor = Color([255,0,255],"","")
		YellowColor = Color([255,255,0],"","")
		CyanColor = Color([0,255,255],"","")
		PurpleColor = Color([222,170,255],"","")
		self.assertEqual(complementaryColor(MagentaColor),[0,255,0])
		self.assertEqual(complementaryColor(YellowColor),[0,0,255])
		self.assertEqual(complementaryColor(CyanColor),[255,0,0])
		self.assertEqual(complementaryColor(PurpleColor),[203,255,170])

	# Obtain the triadic colors of a color
	def test_triadicColor(self):
		MagentaColor = Color([255,0,255],"","")
		YellowColor = Color([255,255,0],"","")
		CyanColor = Color([0,255,255],"","")
		PurpleColor = Color([222,170,255],"","")
		GreenColor = Color([176,230,66],"","")
		WhiteColor = Color([255,255,255],"","")
		self.assertEqual(sorted(triadicColor(MagentaColor)),sorted([[0,255,255],[255,255,0]]))
		self.assertEqual(sorted(triadicColor(YellowColor)),sorted([[255,0,255],[0,255,255]]))
		self.assertEqual(sorted(triadicColor(CyanColor)),sorted([[255,255,0],[255,0,255]]))
		self.assertEqual(sorted(triadicColor(PurpleColor)),sorted([[170,255,222],[255,222,170]]))
		self.assertEqual(sorted(triadicColor(GreenColor)),sorted([[230,66,176],[66,176,230]]))
		self.assertEqual(sorted(triadicColor(WhiteColor)),sorted([[255,255,255],[255,255,255]]))

	# Obtain the split complementary colors of a color
	def test_splitComplementaryColor(self):
		MagentaColor = Color([255,0,255],"","")
		YellowColor = Color([255,255,0],"","")
		CyanColor = Color([0,255,255],"","")
		PurpleColor = Color([222,170,255],"","")
		GreenColor = Color([176,230,66],"","")
		WhiteColor = Color([255,255,255],"","")
		self.assertEqual(sorted(splitComplementaryColor(MagentaColor)),sorted([[0,255,128],[128,255,0]]))
		self.assertEqual(sorted(splitComplementaryColor(YellowColor)),sorted([[0,127,255],[127,0,255]]))
		self.assertEqual(sorted(splitComplementaryColor(CyanColor)),sorted([[255,128,0],[255,0,128]]))
		self.assertEqual(sorted(splitComplementaryColor(PurpleColor)),sorted([[170,255,180],[245,255,170]]))
		self.assertEqual(sorted(splitComplementaryColor(GreenColor)),sorted([[66,94,230],[202,66,230]]))
		self.assertEqual(sorted(splitComplementaryColor(WhiteColor)),sorted([[255,255,255],[255,255,255]]))

	# Obtain the tetradic colors of a color
	def test_tetradicColor(self):
		MagentaColor = Color([255,0,255],"","")
		YellowColor = Color([255,255,0],"","")
		CyanColor = Color([0,255,255],"","")
		PurpleColor = Color([222,170,255],"","")
		GreenColor = Color([176,230,66],"","")
		WhiteColor = Color([255,255,255],"","")
		self.assertEqual(sorted(tetradicColor(MagentaColor)),sorted([[0,255,0],[0,255,255],[255,0,0]]))
		self.assertEqual(sorted(tetradicColor(YellowColor)),sorted([[0,0,255],[255,0,255],[0,255,0]]))
		self.assertEqual(sorted(tetradicColor(CyanColor)),sorted([[255,0,0],[255,255,0],[0,0,255]]))
		self.assertEqual(sorted(tetradicColor(PurpleColor)),sorted([[203,255,170],[170,255,222],[255,170,203]]))
		self.assertEqual(sorted(tetradicColor(GreenColor)),sorted([[120,66,230],[230,66,176],[66,230,120]]))
		self.assertEqual(sorted(tetradicColor(WhiteColor)),sorted([[255,255,255],[255,255,255],[255,255,255]]))

	# Obtain the analagous colors of a color
	def test_analogousColor(self):
		MagentaColor = Color([255,0,255],"","")
		YellowColor = Color([255,255,0],"","")
		CyanColor = Color([0,255,255],"","")
		PurpleColor = Color([222,170,255],"","")
		GreenColor = Color([176,230,66],"","")
		WhiteColor = Color([255,255,255],"","")
		self.assertEqual(sorted(analogousColor(MagentaColor)),sorted([[255,0,128],[127,0,255]]))
		self.assertEqual(sorted(analogousColor(YellowColor)),sorted([[128,255,0],[255,128,0]]))
		self.assertEqual(sorted(analogousColor(CyanColor)),sorted([[0,127,255],[0,255,128]]))
		self.assertEqual(sorted(analogousColor(PurpleColor)),sorted([[255,170,245],[180,170,255]]))
		self.assertEqual(sorted(analogousColor(GreenColor)),sorted([[94,230,66],[230,202,66]]))
		self.assertEqual(sorted(analogousColor(WhiteColor)),sorted([[255,255,255],[255,255,255]]))

	def test_monochromaticColor(self):
		MagentaColor = Color([255,0,255],"","")
		YellowColor = Color([255,255,0],"","")
		CyanColor = Color([0,255,255],"","")
		PurpleColor = Color([222,170,255],"","")
		GreenColor = Color([176,230,66],"","")
		WhiteColor = Color([255,255,255],"","")
		self.assertEqual(sorted(monochromaticColor(MagentaColor)),sorted([[255, 0, 255], [242, 0, 242], [230, 0, 230], [255, 13, 255], [242, 12, 242], [230, 11, 230], [255, 25, 255], [242, 24, 242], [230, 23, 230]]))
		self.assertEqual(sorted(monochromaticColor(YellowColor)),sorted([[255, 255, 0], [242, 242, 0], [230, 230, 0], [255, 255, 13], [242, 242, 12], [230, 230, 11], [255, 255, 25], [242, 242, 24], [230, 230, 23]]))
		self.assertEqual(sorted(monochromaticColor(CyanColor)),sorted([[0, 255, 255], [0, 242, 242], [0, 230, 230], [13, 255, 255], [12, 242, 242], [11, 230, 230], [25, 255, 255], [24, 242, 242], [23, 230, 230]]))
		self.assertEqual(sorted(monochromaticColor(PurpleColor)),sorted([[222, 170, 255], [233, 178, 255], [211, 162, 242], [244, 187, 255], [200, 153, 230], [217, 157, 255], [227, 183, 255], [228, 165, 255], [216, 174, 242], [239, 173, 255], [204, 164, 230], [212, 144, 255], [232, 195, 255], [223, 152, 255], [220, 186, 242], [233, 159, 255], [209, 176, 230]]))
		self.assertEqual(sorted(monochromaticColor(GreenColor)),sorted([[176, 230, 66], [186, 243, 70], [166, 217, 62], [196, 255, 73], [156, 204, 59], [172, 230, 55], [180, 230, 78], [182, 243, 58], [170, 217, 73], [191, 255, 61], [160, 204, 69], [168, 230, 43], [184, 230, 89], [178, 243, 45], [173, 217, 84], [187, 255, 48], [163, 204, 79]]))
		self.assertEqual(sorted(monochromaticColor(WhiteColor)),sorted([[255, 255, 255], [242, 242, 242], [230, 230, 230], [255, 242, 242], [255, 254, 254], [242, 254, 254], [230, 241, 241], [255, 230, 230], [255, 241, 241], [242, 255, 255], [255, 252, 252], [230, 252, 252]]))


if __name__ == '__main__':
    unittest.main()