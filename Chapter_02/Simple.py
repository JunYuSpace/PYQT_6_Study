# coding = utf-8
# /usr/bin/env python

"""
------------------------------------
- Author: YiJunYu       
- Email: yijunyu9628@163.com 
------------------------------------
-  date: 2022-10-15 -- 下午 07:41  
-  desc: Simple                    
------------------------------------
"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget


def main():
	app = QApplication(sys.argv)

	w = QWidget()
	w.resize(500, 250)
	w.move(500, 500)

	w.setWindowTitle('Simple')
	w.show()

	sys.exit(app.exec())


if __name__ == '__main__':
	main()
