# coding = utf-8
# /usr/bin/env python

"""
--------------------------------------
- Author: YiJunYu                    
- Email: yijunyu9628@163.com         
--------------------------------------
- Date: 2022-10-17 -- 下午 03:13 
- Desc: simple_menu.py                   
--------------------------------------
"""

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QIcon, QAction


class MENU(QMainWindow):

	def __init__( self ):
		super().__init__()

		self.initUI()

	def initUI( self ):
		exiAct = QAction(QIcon('Exit.png'), '&Exit', self)
		exiAct.setShortcut('Ctrl + Q')
		exiAct.setStatusTip('Exit Application!')
		exiAct.triggered.connect(QApplication.instance().quit())

		self.statusBar()

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(exiAct)

		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('Simple menu')
		self.show()


def main():
	app = QApplication(sys.argv)
	menu = MENU()
	sys.exit(app.exec())


if __name__ == '__main__':
	main()