# 查看现在日期/时间

from PyQt6.QtCore import QDate, QTime, QDateTime, Qt


class Qt_DateTime:
	
	def __init__( self ):
		self.datetime = None
		self.now = None
		self.time = None
	
	def DateTime( self ):
		self.now = QDate.currentDate()
		
		print(self.now.toString(Qt.DateFormat.ISODate))
		print(self.now.toString(Qt.DateFormat.RFC2822Date))
		
		self.datetime = QDateTime.currentDateTime()
		
		print(self.datetime.toString())
		
		self.time = QTime.currentTime()
		print(self.time.toString(Qt.DateFormat.ISODate))


if __name__ == '__main__':
	QDT = Qt_DateTime()
	QDT.DateTime()
