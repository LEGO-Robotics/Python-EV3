# -*- coding: utf8
import array
import time
import unittest

from ev3.rawdevice import lcd


menu_width=16
menu_height=132
menu_bits = array.array('B',[
  0x00, 0x00, 0x00, 0x00, 0x00, 0x08, 0x00, 0x2A, 0x00, 0x1C, 0x00, 0x3E, 
  0x00, 0x1C, 0x00, 0x2A, 0x00, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x08, 0x0E, 0x2A, 0x11, 0x1C, 0x11, 
  0xBE, 0x3F, 0x9C, 0x31, 0xAA, 0x3B, 0x88, 0x31, 0x80, 0x31, 0x00, 0x1F, 
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0E, 0x00, 0x11, 0x00, 0x11, 
  0x80, 0x3F, 0x80, 0x31, 0x80, 0x3B, 0x80, 0x31, 0x80, 0x31, 0x00, 0x1F, 
  0xFC, 0x07, 0x02, 0x08, 0x02, 0x08, 0x02, 0x08, 0x02, 0x08, 0x02, 0x08, 
  0x06, 0x0C, 0xF8, 0x03, 0xFC, 0x07, 0x56, 0x0D, 0xAB, 0x1A, 0xFF, 0x1F, 
  0x00, 0x03, 0xF0, 0x03, 0x08, 0x04, 0x08, 0x04, 0x08, 0x04, 0x08, 0x04, 
  0xF8, 0x07, 0x58, 0x07, 0xB8, 0x06, 0x58, 0x07, 0xF8, 0x07, 0xF0, 0x03, 
  0xF8, 0x03, 0x08, 0x02, 0x08, 0x02, 0x0C, 0x06, 0x0C, 0x06, 0xFC, 0x07, 
  0x54, 0x04, 0xE4, 0x04, 0x44, 0x04, 0x04, 0x04, 0xF8, 0x03, 0xF8, 0x03, 
  0x00, 0x00, 0x08, 0x0E, 0x18, 0x1B, 0x29, 0x1B, 0x4A, 0x18, 0x2C, 0x0C, 
  0x18, 0x06, 0x2C, 0x06, 0x4A, 0x00, 0x29, 0x06, 0x18, 0x06, 0x08, 0x00, 
  0x00, 0x00, 0x00, 0xF0, 0x00, 0xE0, 0xC0, 0xF0, 0x20, 0xBB, 0x10, 0x1C, 
  0x90, 0xFF, 0x50, 0x40, 0x30, 0x20, 0x10, 0x10, 0xF0, 0x0F, 0x00, 0x00, 
  0x00, 0x00, 0xFF, 0x07, 0x01, 0x04, 0x01, 0x04, 0x01, 0x04, 0x01, 0x04, 
  0x01, 0x04, 0x01, 0x04, 0x01, 0x04, 0x01, 0x04, 0xFF, 0x07, 0x00, 0x00, 
  0x00, 0x00, 0xFF, 0x07, 0x01, 0x04, 0x01, 0x05, 0x81, 0x05, 0xC5, 0x04, 
  0x6D, 0x04, 0x39, 0x04, 0x11, 0x04, 0x01, 0x04, 0xFF, 0x07, 0x00, 0x00, 
  0x00, 0x00, 0xFF, 0x07, 0x01, 0x04, 0x8D, 0x05, 0xD9, 0x04, 0x71, 0x04, 
  0x71, 0x04, 0xD9, 0x04, 0x8D, 0x05, 0x01, 0x04, 0xFF, 0x07, 0x00, 0x00, 
  ]);
class TestLCD(unittest.TestCase):

    def setUp(self):
        lcd.open_device()

    
    def test_lcd(self):
        print "lcd black!"
        lcd.black()
        time.sleep(2)
        print "lcd white!"
        lcd.white()
        time.sleep(2)
        print "lcd draw image!"
        lcd.draw_image(menu_bits,0,0,16,132,0,0,16,64)
        

    def tearDown(self):
        lcd.close_device()


if __name__ == '__main__':
    unittest.main()