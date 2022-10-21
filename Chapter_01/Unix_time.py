# coding = utf-8
# /usr/bin/env python

"""
------------------------------------
- Author: YiJunYu       
- Email: yijunyu9628@163.com 
------------------------------------
-  date: 2022-10-15 -- 下午 07:09  
-  desc: Unix_time                    
------------------------------------
"""

from PyQt6.QtCore import QDateTime, Qt


class UT:
	def __init__( self ):
		self.unixtime = None
		self.d = None
		self.now = None

	def Unix_time( self ):
		self.now = QDateTime.currentDateTime()

		self.unixtime = self.now.toSecsSinceEpoch()
		print(self.unixtime)

		self.d = QDateTime.fromSecsSinceEpoch(self.unixtime)
		print(self.d.toString(Qt.DateFormat.ISODate))


if __name__ == '__main__':
	ut = UT()
	ut.Unix_time()
