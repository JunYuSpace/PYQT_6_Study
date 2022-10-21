# coding = utf-8
# /usr/bin/env python

"""
--------------------------------------
- Author: YiJunYu                    
- Email: yijunyu9628@163.com         
--------------------------------------
- Date: 2022-10-14 -- 上午 11:01 
- Desc: n_to_days.py                   
--------------------------------------
"""

from PyQt6.QtCore import Qt, QDate


class N_Of_Days:
	def __init__( self ):
		self.d = None
		self.now = None
	
	def n_of_days( self ):
		self.now = QDate.currentDate()
		self.d = QDate(2022, 10, 4)
		print(f'Days in month: {self.d.daysInMonth()}')
		print(f'Days in year: {self.d.daysInYear()}')


if __name__ == '__main__':
	NOD = N_Of_Days()
	NOD.n_of_days()
