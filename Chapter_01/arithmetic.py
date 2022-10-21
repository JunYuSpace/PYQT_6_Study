# coding = utf-8
# /usr/bin/env python

"""
--------------------------------------
- Author: YiJunYu                    
- Email: yijunyu9628@163.com         
--------------------------------------
- Date: 2022-10-14 -- 下午 01:04 
- Desc: arithmetic.py                   
--------------------------------------
"""

from PyQt6.QtCore import QDateTime, Qt


class AM:
	def __init__( self ):
		self.now = None
	
	def arithmetic( self ):
		self.now = QDateTime.currentDateTime()
		
		print(f'Today: {self.now.toString(Qt.DateFormat.ISODate)}')
		print(f'Adding 12 days: {self.now.addDays(12).toString(Qt.DateFormat.ISODate)}')
		print(f'Subtracting 22 days: {self.now.addDays(-22).toString(Qt.DateFormat.ISODate)}')
		
		print(f'Adding 50 seconds: {self.now.addSecs(50).toString(Qt.DateFormat.ISODate)}')
		print(f'Adding 3 months: {self.now.addMonths(3).toString(Qt.DateFormat.ISODate)}')
		print(f'Adding 12 years: {self.now.addYears(12).toString(Qt.DateFormat.ISODate)}')


if __name__ == '__main__':
	am = AM()
	am.arithmetic()
