# coding = utf-8
# /usr/bin/env python

"""
--------------------------------------
- Author: YiJunYu                    
- Email: yijunyu9628@163.com         
--------------------------------------
- Date: 2022-10-17 -- 下午 01:51 
- Desc: message_box.py                   
--------------------------------------
"""

import sys
from PyQt6.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):

	def __init__( self ):
		super().__init__()

	def initUI( self ):
		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('MessageBox')
		self.show()

	def CloseEvent( self, event ):
		reply = QMessageBox.question(
			self, 'Message', 'Are you sure to quit?', QMessageBox.standardButton.Yes | QMessageBox.StandardButton.No,
			QMessageBox.standardButton.No)
		if reply == QMessageBox.StandardButton.Yes:
			event.accept()
		else:
			event.ignore()


def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec())


if __name__ == '__main__':
	main()