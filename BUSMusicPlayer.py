import sys
from os import path, walk, getenv
from random import shuffle
from tkinter import filedialog, Tk

import pygame
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def closeEvent(self, event):
        self.player.exit()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.closeEvent = self.closeEvent
        Form.resize(350, 130)
        Form.setMinimumSize(QtCore.QSize(350, 100))
        Form.setMaximumSize(QtCore.QSize(470, 150))
        Form.setStyleSheet("* {\n"
            "    background-color: rgb(64, 64, 64);\n"
            "    color: rgb(255, 255, 255);\n"
            "    border: none;\n"
            "}\n"
            "QPushButton{\n"
            "    background-color: rgb(0, 85, 255);\n"
            "    color: rgb(255, 255, 255);\n"
            "}\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(0, 0, 127);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    background-color: rgb(0, 0, 0);\n"
        "}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(5, -1, 5, 5)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setInputMask("")
        self.lineEdit.setFrame(False)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.volume_slider = QtWidgets.QSlider(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volume_slider.sizePolicy().hasHeightForWidth())
        self.volume_slider.setSizePolicy(sizePolicy)
        self.volume_slider.setMaximum(19)
        self.volume_slider.setSingleStep(1)
        self.volume_slider.setPageStep(1)
        self.volume_slider.setProperty("value", 19)
        self.volume_slider.setOrientation(QtCore.Qt.Horizontal)
        self.volume_slider.setObjectName("volume_slider")
        self.gridLayout.addWidget(self.volume_slider, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.prev_btn = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prev_btn.sizePolicy().hasHeightForWidth())
        self.prev_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.prev_btn.setFont(font)
        self.prev_btn.setObjectName("prev_btn")
        self.horizontalLayout.addWidget(self.prev_btn)
        self.stop_btn = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_btn.sizePolicy().hasHeightForWidth())
        self.stop_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.stop_btn.setFont(font)
        self.stop_btn.setObjectName("stop_btn")
        self.horizontalLayout.addWidget(self.stop_btn)
        self.play_btn = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play_btn.sizePolicy().hasHeightForWidth())
        self.play_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.play_btn.setFont(font)
        self.play_btn.setObjectName("play_btn")
        self.horizontalLayout.addWidget(self.play_btn)
        self.pause_btn = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pause_btn.sizePolicy().hasHeightForWidth())
        self.pause_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pause_btn.setFont(font)
        self.pause_btn.setObjectName("pause_btn")
        self.horizontalLayout.addWidget(self.pause_btn)
        self.next_btn = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_btn.sizePolicy().hasHeightForWidth())
        self.next_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.next_btn.setFont(font)
        self.next_btn.setStyleSheet("")
        self.next_btn.setObjectName("next_btn")
        self.horizontalLayout.addWidget(self.next_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "BUSMusicPlayer"))
        Form.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.lineEdit.setText(_translate("Form", "Имя трека"))
        self.label.setText(_translate("Form", "Громкость"))
        self.prev_btn.setText(_translate("Form", "<<|"))
        self.stop_btn.setText(_translate("Form", "<>"))
        self.play_btn.setText(_translate("Form", "|>"))
        self.pause_btn.setText(_translate("Form", "||>"))
        self.next_btn.setText(_translate("Form", "|>>"))

        self.player = MusicPlayer(track_line=self.lineEdit)
        self.play_btn.clicked.connect(self.player.start)
        self.pause_btn.clicked.connect(self.player.pause)
        self.stop_btn.clicked.connect(self.player.stop)
        self.next_btn.clicked.connect(lambda : (self.player.next()))
        self.prev_btn.clicked.connect(lambda : (self.player.prev()))
        self.volume_slider.valueChanged.connect(self.player.set_volume)
        self.lineEdit.setText(self.player.track_name)


class MusicPlayer:

    def __init__(self, track_line=None, music_dir=path.join(getenv('userprofile'), 'Music')):
        self.current_track = 0
        self.track_line = track_line
        self.is_paused = False
        pygame.init()
        pygame.mixer.init()
        self.playlist = []
        for root, _, files in walk(music_dir):
            for file in files:
                if file.endswith('.mp3'):
                    self.playlist.append(path.join(root, file))
        if not self.playlist:
            music_dir = filedialog.askdirectory(title='Выберите папку с музыкой')
            if not music_dir:
            	self.exit()
            for root, _, files in walk(music_dir):
                for file in files:
                    if file.endswith('.mp3'):
                        self.playlist.append(path.join(root, file))
        shuffle(self.playlist)
        self.clock = pygame.time.Clock()
    
    def next(self):
        if self.current_track + 1 < len(self.playlist):
            self.current_track += 1
        else:
            self.current_track = 0
        pygame.mixer.music.unload()
        pygame.mixer.music.load(self.playlist[self.current_track])
        pygame.mixer.music.play()
        self.is_paused = False
        self.track_line.setText(path.split(self.playlist[self.current_track])[-1])

    def prev(self):
        if self.current_track > 0:
            self.current_track -= 1
        else:
            self.current_track = len(self.playlist) - 1
        pygame.mixer.music.unload()
        pygame.mixer.music.load(self.playlist[self.current_track])
        pygame.mixer.music.play()
        self.is_paused = False
        self.track_line.setText(path.split(self.playlist[self.current_track])[-1])

    def stop(self):
        pygame.mixer.music.unload()
        self.is_paused = False

    def pause(self):
        if not self.is_paused:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        self.is_paused = not self.is_paused


    def exit(self):
        pygame.mixer.music.unload()
        sys.exit(0)

    @property
    def track_name(self):
        return path.split(self.playlist[self.current_track])[-1]
    

    def set_volume(self, value):
        pygame.mixer.music.set_volume((1 / 19) * value)

    def start(self):
        self.is_paused = False
        pygame.mixer.music.load(self.playlist[self.current_track])
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(1)
        while True:
            if pygame.mixer.music.get_pos() == -1:
                self.next()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
            self.clock.tick(15)


if __name__ == "__main__":
    Tk().withdraw()
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    exit_code = app.exec_()
    sys.exit(exit_code)