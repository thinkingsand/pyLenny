#!/bin/python3

from PyQt5 import QtWidgets, QtCore, QtGui, uic
from fbs_runtime.application_context.PyQt5 import ApplicationContext
import sys
import random
import pygame

class MainWindow(QtWidgets.QMainWindow):   
    def stopPlay(self):
        pygame.mixer.stop()
    
    def autoLenny(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("AutoLenny™")
        msg.setText("Not yet implemented")
        x = msg.exec()
        
    def playPause(self):
        global paused
        if channel.get_sound != None:
            if paused == True:
                channel.unpause()
                paused = False
            elif paused == False:
                channel.pause()
                paused = True

    def volumeChanged(self):
        channel.set_volume(self.volumeSlider.value()/100)
        print(channel.get_volume())

    def randomClip(self):
        id = random.randrange(1, 16)
        sound = pygame.mixer.Sound(appctxt.get_resource("audio/lenny/" + str(id) + ".mp3"))
        channel.play(sound)

    def playLenny1(self):
        sound = pygame.mixer.Sound(appctxt.get_resource("audio/lenny/1.mp3"))
        channel.play(sound)

    def playLenny2(self):
        sound = pygame.mixer.Sound(appctxt.get_resource("audio/lenny/2.mp3"))
        channel.play(sound)

    def playLenny3(self):
        sound = pygame.mixer.Sound(appctxt.get_resource("audio/lenny/3.mp3"))
        channel.play(sound)

    def playLenny4(self):
        sound = pygame.mixer.Sound(appctxt.get_resource("audio/lenny/4.mp3"))
        channel.play(sound)

    def playLenny5(self):
        sound = pygame.mixer.Sound(appctxt.get_resource("audio/lenny/5.mp3"))
        channel.play(sound)

    def playLenny6(self):
        sound = pygame.mixer.Sound(appctxt.get_resource("audio/lenny/6.mp3"))
        channel.play(sound)

    def playLenny7(self):
        sound = pygame.mixer.Sound(appctxt.get_resource("audio/lenny/7.mp3"))
        channel.play(sound)

    def playLenny8(self):
        sound = pygame.mixer.Sound(appctxt.get_resource("audio/lenny/8.mp3"))
        channel.play(sound)

    def playLenny9(self):
        sound = pygame.mixer.Sound(appctxt.get_resource("audio/lenny/9.mp3"))
        channel.play(sound)

    def playLenny10(self):
        sound = pygame.mixer.Sound(appctxt.get_resource("audio/lenny/10.mp3"))
        channel.play(sound)

    def playLenny11(self):
        sound = pygame.mixer.Sound(appctxt.get_resource("audio/lenny/11.mp3"))
        channel.play(sound)

    def playLenny12(self):
        sound = pygame.mixer.Sound(appctxt.get_resource("audio/lenny/12.mp3"))
        channel.play(sound)

    def playLenny13(self):
        sound = pygame.mixer.Sound(appctxt.get_resource("audio/lenny/13.mp3"))
        channel.play(sound)

    def playLenny14(self):
        sound = pygame.mixer.Sound(appctxt.get_resource("audio/lenny/14.mp3"))
        channel.play(sound)

    def playLenny15(self):
        sound = pygame.mixer.Sound(appctxt.get_resource("audio/lenny/15.mp3"))
        channel.play(sound)

    def playLenny16(self):
        sound = pygame.mixer.Sound(appctxt.get_resource("audio/lenny/16.mp3"))
        channel.play(sound)

    def playExtras1(self):
        sound = pygame.mixer.Sound(appctxt.get_resource("audio/extras/1.mp3"))
        channel.play(sound)

    def playExtras2(self):
        sound = pygame.mixer.Sound(appctxt.get_resource("audio/extras/2.mp3"))
        channel.play(sound)

    def playExtras3(self):
        sound = pygame.mixer.Sound(appctxt.get_resource("audio/extras/3.mp3"))
        channel.play(sound)

    def playExtras4(self):
        sound = pygame.mixer.Sound(appctxt.get_resource("audio/extras/4.mp3"))
        channel.play(sound)

    def closeApp(self):
        sys.exit()

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        uic.loadUi(appctxt.get_resource('qt_mainwindow.ui'), self)
        
        pygame.init()
        pygame.mixer.init()
        random.seed()
        global paused, channel
        channel = pygame.mixer.Channel(1)
        channel.set_volume(0.7)
        paused = False

        self.quitBtn.clicked.connect(self.closeApp)
        self.playBtn.clicked.connect(self.playPause)
        self.stopBtn.clicked.connect(self.stopPlay)
        self.randomBtn.clicked.connect(self.randomClip)
        self.autoBtn.clicked.connect(self.autoLenny)
        self.volumeSlider.valueChanged.connect(self.volumeChanged)

        self.lenny1.clicked.connect(self.playLenny1)
        self.lenny2.clicked.connect(self.playLenny2)
        self.lenny3.clicked.connect(self.playLenny3)
        self.lenny4.clicked.connect(self.playLenny4)
        self.lenny5.clicked.connect(self.playLenny5)
        self.lenny6.clicked.connect(self.playLenny6)
        self.lenny7.clicked.connect(self.playLenny7)
        self.lenny8.clicked.connect(self.playLenny8)
        self.lenny9.clicked.connect(self.playLenny9)
        self.lenny10.clicked.connect(self.playLenny10)
        self.lenny11.clicked.connect(self.playLenny11)
        self.lenny12.clicked.connect(self.playLenny12)
        self.lenny13.clicked.connect(self.playLenny13)
        self.lenny14.clicked.connect(self.playLenny14)
        self.lenny15.clicked.connect(self.playLenny15)
        self.lenny16.clicked.connect(self.playLenny16)

        self.extras1.clicked.connect(self.playExtras1)
        self.extras2.clicked.connect(self.playExtras2)
        self.extras3.clicked.connect(self.playExtras3)
        self.extras4.clicked.connect(self.playExtras4)

if __name__ == '__main__':
    appctxt = ApplicationContext()
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
