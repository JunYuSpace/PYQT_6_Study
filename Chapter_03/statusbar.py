# coding = utf-8
# /usr/bin/env python

"""
--------------------------------------
- Author: YiJunYu                    
- Email: yijunyu9628@163.com         
--------------------------------------
- Date: 2022-10-17 -- 下午 02:49 
- Desc: statusbar.py                   
--------------------------------------
"""

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication


class STATUSBAR(QMainWindow):

	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI( self ):

		self.statusBar().showMessage('Ready')
		# self.statusBar().showMessage('go')

		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('StatusBar')
		self.show()


def main():
	app = QApplication(sys.argv)
	ex = STATUSBAR()
	sys.exit(app.exec())


if __name__ == '__main__':
	main()
