# coding = utf-8
# /usr/bin/env python

"""
--------------------------------------
- Author: YiJunYu                    
- Email: yijunyu9628@163.com         
--------------------------------------
- Date: 2022-10-14 -- 上午 10:38 
- Desc: uic_local.py                   
--------------------------------------
"""

'''
查看UTC(通用协调时间)
'''

from PyQt6.QtCore import QDateTime, Qt


class UTC_TIME:
	
	def __init__( self ):
		self.now = None
	
	def current_time( self ):
		self.now = QDateTime.currentDateTime()
		
		print('Local DateTime: ', self.now.toString(Qt.DateFormat.ISODateWithMs))
		print('Universal DateTime: ', self.now.toUTC().toString(Qt.DateFormat.ISODate))
		
		print(f'The offset from UTC is: {self.now.offsetFromUtc()} seconds')
		
		print('Local DateTime: ', self.now.toString(Qt.DateFormat.ISODate))


if __name__ == '__main__':
	UT = UTC_TIME()
	UT.current_time()
