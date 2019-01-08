from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5.QtCore import Qt, QBasicTimer, QRect, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPixmap

from Weapon import Weapon
from settings import *
import os



class Player(QWidget): #player1 or player2

    livesSignal = pyqtSignal(int)
    pointsSignal = pyqtSignal(int)

    def __init__(self, parent, playerId):

        super().__init__(parent)

        self.isDead = False
        self.playerId = playerId
        self.playerImg_normal = IMAGES_DIR + playerId + '.png'
        self.playerImg_left = IMAGES_DIR + playerId + '_left.png'
        self.playerImg_right = IMAGES_DIR + playerId +  '_right.png'
        self.player = QLabel(parent)
        self.initialPositionX = None
        self.initialPositionY = None
        #self.weapon = None
        self.PixMap = QPixmap(self.playerImg_normal)
        #self.drawPlayer('normal')

        self.Normal = True
        self.Left = False
        self.Right = False
        self.Heigth = 50
        self.Width = 50

        self.lifes = 3
        self.score = 0

        self.timer = QBasicTimer()
        self.timer.start(32, self)

        if self.playerId == 'player1':
            #self.player.setPixmap(QPixmap(playerImg_normal
            self.PositionX = 50
            self.initialPositionX = 50
            self.PositionY = PLAYER_HEIGTH
            #self.player.setGeometry(50, 400, 50, 50)
        elif self.playerId =='player2':
            self.PositionX = 700
            self.initialPositionX = 700
            self.PositionY = PLAYER_HEIGTH
            #self.player.setGeometry(700, 400, 50, 50)
        self.weapon = Weapon(self)
    def timerEvent(self, event):
        self.weapon.update()
        self.displayWeapon = self.weapon.weapon
    def shoot(self):
        #self.weapon = Weapon(self)
        self.weapon.isActive = True
        #self.weapon.update()

    def drawPlayer(self, orientation):
        #result = ''
        if orientation == 'normal':
            self.Normal = True
            self.Left = False
            self.Right = False
            self.PixMap = QPixmap(self.playerImg_normal)

        elif orientation == 'left':
            self.Normal = False
            self.Left = True
            self.Right = False
            self.PixMap = QPixmap(self.playerImg_left)
        elif orientation == 'right':
            self.Normal = False
            self.Left = False
            self.Right = True
            self.PixMap = QPixmap(self.playerImg_right)


        self.player.setPixmap(self.PixMap)
       # pix = QPixmap(result)
       # self.player.setPixmap(pix)

    def update(self, key):

        if self.playerId == 'player1':
            if key == Qt.Key_Space: #and not self.weapon.isActive:
                    self.shoot()
            elif key == Qt.Key_Right:
                if self.PositionX + self.Width < WINDOWWIDTH-13:
                    self.drawPlayer('right')
                    self.PositionX += 5
                    self.player.setGeometry(self.PositionX, self.PositionY, self.Width, self.Heigth)

            elif key == Qt.Key_Left:
                if self.PositionX - 5 > 20:
                    self.drawPlayer('left')
                    self.PositionX -= 5
                    self.player.setGeometry(self.PositionX, self.PositionY, self.Width, self.Heigth)
            elif key == Qt.Key_Minus:
                self.drawPlayer('normal')
                self.player.setGeometry(self.PositionX, self.PositionY, self.Width, self.Heigth)

        elif self.playerId == 'player2':
            if key == Qt.Key_Shift:
                    self.shoot()
            elif key == Qt.Key_D:
                if self.PositionX + self.Width < WINDOWWIDTH-13:
                    self.drawPlayer('right')
                    self.PositionX += 5
                    self.player.setGeometry(self.PositionX, self.PositionY, self.Width, self.Heigth)
            elif key == Qt.Key_A:
                if self.PositionX - 5 > 20:
                    self.drawPlayer('left')
                    self.PositionX -= 5
                    self.player.setGeometry(self.PositionX, self.PositionY, self.Width, self.Heigth)
            elif key == Qt.Key_Minus:
                self.drawPlayer('normal')
                self.player.setGeometry(self.PositionX, self.PositionY, self.Width, self.Heigth)

    def updateLives(self, num):
        self.lifes -= num
        if self.lifes == 0:
            self.isDead = True