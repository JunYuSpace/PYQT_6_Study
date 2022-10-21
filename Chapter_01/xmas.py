# coding = utf-8
# /usr/bin/env python

"""
--------------------------------------
- Author: YiJunYu                    
- Email: yijunyu9628@163.com         
--------------------------------------
- Date: 2022-10-14 -- 上午 11:17 
- Desc: xmas.py                   
--------------------------------------
"""

from PyQt6.QtCore import QDate, Qt


class XMAS:
	def __init__( self ):
		self.days_passed = None
		self.n_of_days = None
		self.xmas_2 = None
		self.xmas_1 = None
		self.y = None
		self.now = None
	
	def xmas( self ):
		self.now = QDate.currentDate()
		self.y = self.now.year()
		
		print(f'Today is {self.now.toString(Qt.DateFormat.ISODate)}')
		
		self.xmas_1 = QDate(self.y - 1, 12, 25)
		self.xmas_2 = QDate(self.y, 12, 25)
		
		self.days_passed = self.xmas_1.daysTo(self.now)
		print(f'{self.days_passed} days have passed since last XMas.')
		
		self.n_of_days = self.now.daysTo(self.xmas_2)
		print(f'There are {self.n_of_days} days until next XMas.')


if __name__ == '__main__':
	xm = XMAS()
	xm.xmas()
