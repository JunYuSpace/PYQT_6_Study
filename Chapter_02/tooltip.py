# coding = utf-8
# /usr/bin/env python

"""
------------------------------------
- Author: YiJunYu       
- Email: yijunyu9628@163.com 
------------------------------------
-  date: 2022-10-15 -- 下午 08:24  
-  desc: tooltip                    
------------------------------------
"""

import sys
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)


class Example(QWidget):
	def __int__( self ):
		super().__init__()

		self.initUI()

	def initUI( self ):
		QToolTip.setFont(QFont('SansSerif', 10))
		self.setToolTip('This is a <b>QWidget</b> widget')

		btn = QPushButton('Button', self)
		btn.setToolTip('This is a <b>QPushButton</b> widget')
		btn.resize(btn.sizeHint())
		btn.move(50, 50)

		self.setGeometry(300, 300, 300, 200)
		self.setWindowTitle('ToolTips')
		self.show()


def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec())


if __name__ == '__main__':
	main()