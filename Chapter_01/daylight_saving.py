# coding = utf-8
# /usr/bin/env python

"""
--------------------------------------
- Author: YiJunYu                    
- Email: yijunyu9628@163.com         
--------------------------------------
- Date: 2022-10-14 -- 下午 01:26 
- Desc: daylight_saving.py                   
--------------------------------------
"""

from PyQt6.QtCore import Qt, QDateTime, QTimeZone


class DS:
	def __init__( self ):
		self.now = None

	def daylight_saving( self ):
		self.now = QDateTime.currentDateTime()
		print(f'Time zone: {self.now.timeZoneAbbreviation()}')

		if self.now.isDaylightTime():
			print('The current date falls into DST time.')
		else:
			print('The current date dose not fall into DST time.')


if __name__ == '__main__':
	ds = DS()
	ds.daylight_saving()
