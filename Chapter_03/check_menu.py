# coding = utf-8
# /usr/bin/env python

"""
--------------------------------------
- Author: YiJunYu                    
- Email: yijunyu9628@163.com         
--------------------------------------
- Date: 2022-10-18 -- 上午 08:42 
- Desc: check_menu.py                   
--------------------------------------
"""

import sys

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow):

	def __init__( self ):
		super().__init__()

		self.initUI()

	def initUI( self ):

		self.statusbar = self.statusBar()
		self.statusbar.showMessage('Ready')

		menubar = self.menuBar()
		viewMenu = menubar.addMenu('View')

		viewStatAct = QAction('View statusbar', self, checkable = True)
		viewStatAct.setStatusTip('View statusbar')
		viewStatAct.setChecked(True)
		viewStatAct.triggered.connect(self.toggleMenu)

		viewMenu.addAction(viewStatAct)

		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('Check menu')
		self.show()

	def toggleMenu( self, state ):

		if state:
			self.statusbar.show()
		else:
			self.statusbar.hide()


def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec())


if __name__ == '__main__':
	main()