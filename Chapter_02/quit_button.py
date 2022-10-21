# coding = utf-8
# /usr/bin/env python

"""
------------------------------------
- Author: YiJunYu       
- Email: yijunyu9628@163.com 
------------------------------------
-  date: 2022-10-15 -- 下午 09:22  
-  desc: quit_button                    
------------------------------------
"""
import sys

from PyQt6.QtWidgets import QWidget, QPushButton, QApplication


class Example(QWidget):
	def __int__( self ):
		super().__init__(self)

		self.initUI()

	def initUI( self ):
		qbtn = QPushButton('Quit', self)
		qbtn.clicked(QApplication.instance().quit())
		qbtn.resize(qbtn.sizeHint())
		qbtn.move(50, 50)

		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('Quit button')
		self.show()


def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec())


if __name__ == '__main__':
	main()