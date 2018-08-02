#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# Created by nijianfeng at 18/7/28

import sys
import random
from enum import IntEnum
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtCore import Qt

title = '数字华容道'
count = 0


# 用枚举类表示方向
class Direction(IntEnum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class NumberHuaRong(QWidget):

    def __init__(self):
        super().__init__()

        # 后面四个数字的作用依次是 初始值 最小值 最大值 步幅
        size, ok = QInputDialog.getInt(self, title, "大小:", 4, 2, 10, 1)
        if ok:
            self.size = size
        else:
            self.close()
            sys.exit(0)

        self.blocks = []
        self.zero_row = 0
        self.zero_column = 0
        self.gltMain = QGridLayout()

        self.initUI()

    def initUI(self):
        # 设置方块间隔
        self.gltMain.setSpacing(5)

        self.onInit()

        # 设置布局
        self.setLayout(self.gltMain)
        # 设置宽和高
        self.setFixedSize(70 * self.size, 70 * self.size)
        # 设置标题
        self.setWindowTitle(title)
        # 设置背景颜色
        self.setStyleSheet("background-color:red;")
        self.show()

    # 初始化布局
    def onInit(self):
        # 产生顺序数组
        self.numbers = list(range(1, self.size ** 2))
        self.numbers.append(0)

        # 将数字添加到二维数组
        for row in range(self.size):
            self.blocks.append([])
            for column in range(self.size):
                temp = self.numbers[row * self.size + column]

                if temp == 0:
                    self.zero_row = row
                    self.zero_column = column
                self.blocks[row].append(temp)

        # 打乱数组
        for i in range(500):
            random_num = random.randint(0, 3)
            self.move(Direction(random_num))

        self.updatePanel()

    # 检测按键
    def keyPressEvent(self, event):
        global count
        key = event.key()
        if (key == Qt.Key_Up or key == Qt.Key_W):
            count += 1
            self.move(Direction.UP)
        if (key == Qt.Key_Down or key == Qt.Key_S):
            count += 1
            self.move(Direction.DOWN)
        if (key == Qt.Key_Left or key == Qt.Key_A):
            count += 1
            self.move(Direction.LEFT)
        if (key == Qt.Key_Right or key == Qt.Key_D):
            count += 1
            self.move(Direction.RIGHT)
        self.updatePanel()
        if self.checkResult():
            if QMessageBox.Ok == QMessageBox.information(self, '挑战结果', '恭喜您走了' + str(count) + '步完成挑战！'):
                self.onInit()

    # 方块移动算法
    def move(self, direction):
        if (direction == Direction.UP):  # 上
            if self.zero_row != self.size - 1:
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row + 1][self.zero_column]
                self.blocks[self.zero_row + 1][self.zero_column] = 0
                self.zero_row += 1
        if (direction == Direction.DOWN):  # 下
            if self.zero_row != 0:
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row - 1][self.zero_column]
                self.blocks[self.zero_row - 1][self.zero_column] = 0
                self.zero_row -= 1
        if (direction == Direction.LEFT):  # 左
            if self.zero_column != self.size - 1:
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row][self.zero_column + 1]
                self.blocks[self.zero_row][self.zero_column + 1] = 0
                self.zero_column += 1
        if (direction == Direction.RIGHT):  # 右
            if self.zero_column != 0:
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row][self.zero_column - 1]
                self.blocks[self.zero_row][self.zero_column - 1] = 0
                self.zero_column -= 1

    def updatePanel(self):
        for row in range(self.size):
            for column in range(self.size):
                self.gltMain.addWidget(Block(self.blocks[row][column], self.size), row, column)

        self.setLayout(self.gltMain)

    # 检测是否完成
    def checkResult(self):
        # 先检测最右下角是否为0
        if self.blocks[self.size - 1][self.size - 1] != 0:
            return False

        for row in range(self.size):
            for column in range(self.size):
                # 运行到此处说名最右下角已经为0，pass即可
                if row == self.size - 1 and column == self.size - 1:
                    pass
                # 值是否对应
                elif self.blocks[row][column] != row * self.size + column + 1:
                    return False

        return True


class Block(QLabel):
    """ 数字方块 """

    def __init__(self, number, size):
        super().__init__()

        self.number = number
        self.setFixedSize(20 + 5 * size, 20 + 5 * size)

        # 设置字体
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.setFont(font)

        # 设置字体颜色
        pa = QPalette()
        pa.setColor(QPalette.WindowText, Qt.white)
        self.setPalette(pa)

        # 设置文字位置
        self.setAlignment(Qt.AlignCenter)

        # 设置背景颜色\圆角和文本内容
        if self.number == 0:
            self.setStyleSheet("background-color:white;border-radius:10px;")
        else:
            self.setStyleSheet("background-color:green;border-radius:10px;")
            self.setText(str(self.number))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    run = NumberHuaRong()
    sys.exit(app.exec_())
