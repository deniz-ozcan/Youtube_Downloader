from PyQt5.QtWidgets import (QLineEdit, QWidget, QSizePolicy, QHBoxLayout,
                             QVBoxLayout, QLabel, QPushButton, QFrame,
                             QScrollArea)

from PyQt5.QtGui import (
    QPixmap,
    QIcon,
    QFont,
)
from PyQt5.QtCore import (Qt, QSize, QCoreApplication, QMetaObject, QRect)
import icons_rc


class Ui_Downloader(object):

    def setupUi(self, Downloader):
        Downloader.setObjectName("Downloader")
        Downloader.resize(765, 488)
        Downloader.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addPixmap(
            QPixmap(":/icons/icons/youtube.svg"),
            QIcon.Normal,
            QIcon.Off,
        )
        Downloader.setWindowIcon(icon)
        self.centralwidget = QWidget(Downloader)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(1000, 16777215))
        font = QFont()
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(
            "*{\n"
            "    border: none;\n"
            "    color:white;\n"
            "}\n"
            "\n"
            "#centralwidget{\n"
            "background-color: rgba(24, 24, 24,255);\n"
            "border: 3px solid rgb(230, 5, 64);}\n"
            "\n"
            "#leftMenu{background-color: rgba(32, 32, 32,255);;\n"
            "border-bottom: 3px solid rgb(230, 5, 64);\n"
            "border-top: 3px solid rgb(230, 5, 64);\n"
            "border-left: 3px solid rgb(230, 5, 64);\n"
            "}\n"
            "#slideMenu{background-color: rgba(24, 24, 24,200);}\n"
            "\n"
            "#frame_7{border: none;background: rgba(24, 24, 24,255);}\n"
            "#header{background-color: rgba(32, 32, 32,255);\n"
            "border-left: 3px solid rgb(230, 5, 64);\n"
            "border-top: 3px solid rgb(230, 5, 64);\n"
            "border-right: 3px solid rgb(230, 5, 64);\n"
            "}\n"
            "\n"
            "#frame{background-color:rgb(49,49,49);border-radius: 7px;}\n"
            "\n"
            "#pastelink{\n"
            "background:rgb(18,18,18); \n"
            "max-width:250px;\n"
            "min-width:250px;\n"
            "\n"
            "color:white;\n"
            "padding: 1px;\n"
            "border-radius: 7px;\n"
            "width: 15px;\n"
            "}\n"
            "\n"
            "#footer{border:none;}\n"
            "#frame_9{\n"
            "    border:3px solid rgb(230, 5, 64) ;\n"
            "}\n"
            "#Area{background:rgb(24,24,24);}\n"
            "\n"
            "QScrollBar:vertical {\n"
            "    border-radius: 5px;\n"
            "    background:transparent;\n"
            "    width:10px;\n"
            "    margin:0px;\n"
            "}\n"
            "QScrollBar:horizontal {\n"
            "    border-radius: 5px;\n"
            "    background:transparent;\n"
            "    height:10px;\n"
            "    margin:0px;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:vertical {\n"
            "    border-radius: 5px;\n"
            "    background: rgb(35, 106, 110);\n"
            "    min-width:5px;\n"
            "    max-width:5px;\n"
            "    min-height:5px;\n"
            "    max-height:5px;\n"
            "    width:5px;\n"
            "    height:5px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    border-radius: 5px;\n"
            "    background: rgb(35, 106, 110);\n"
            "    min-width:5px;\n"
            "    max-width:5px;\n"
            "    min-height:5px;\n"
            "    max-height:5px;\n"
            "    width:5px;\n"
            "    height:5px;\n"
            "}\n"
            "QScrollBar::add-line:vertical {\n"
            "    height: 0px;\n"
            "    subcontrol-position: bottom;    \n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    height: 0px;\n"
            "    subcontrol-position: bottom;    \n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:vertical {\n"
            "    height: 0px;\n"
            "    subcontrol-position: top;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    height: 0px;\n"
            "    subcontrol-position: top;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "    background:transparent;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
            "    background:transparent;\n"
            "}\n"
            "\n"
            "#timepush{\n"
            "    border-radius:17px;\n"
            "    border:2px solid rgb(150, 150, 150);\n"
            "    background:transparent;\n"
            "}\n"
            "\n"
            "QProgressBar {\n"
            "border: 1px solid black;\n"
            "max-width:150px;\n"
            "min-width:150px;\n"
            "text-align: center;\n"
            "font-size:15px;\n"
            "color:black;\n"
            "padding: 1px;\n"
            "border-radius: 7px;\n"
            "background: qlineargradient( x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #fff,stop: 0.4999 #eee,stop: 0.5 #ddd,stop: 1 #eee );\n"
            "width: 15px;\n"
            "}\n"
            "QProgressBar::chunk {\n"
            "background: qlineargradient( x1: 0, y1: 0, x2: 1, y2: 0,stop: 0 #0000ff,stop: 1 #ff0000 );\n"
            "border-radius: 7px;\n"
            "border: 1px solid black;\n"
            "}\n"
            "\n"
            "QLineEdit{\n"
            "background:transparent;\n"
            "color:white;\n"
            "}\n"
            "\n"
            "QSlider::groove:horizontal {\n"
            "    border-radius:15px;\n"
            "    background:  rgb(217, 217, 217);\n"
            "}\n"
            "\n"
            "QSlider::handle:horizontal {\n"
            "    image: url(:/icons/icons/music.svg);\n"
            "    width:30px;\n"
            "    height:30px;\n"
            "    min-width:30px;\n"
            "    min-height:30px;\n"
            "    max-width:30px;\n"
            "    max-height:30px;\n"
            "    border-radius: 15px;\n"
            "    margin-left:2px;\n"
            "    margin-right:3px;\n"
            "}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftMenu = QFrame(self.centralwidget)
        self.leftMenu.setMaximumSize(QSize(0, 16777215))
        self.leftMenu.setStyleSheet("")
        self.leftMenu.setFrameShape(QFrame.StyledPanel)
        self.leftMenu.setFrameShadow(QFrame.Raised)
        self.leftMenu.setObjectName("leftMenu")
        self.verticalLayout_92 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_92.setSpacing(0)
        self.verticalLayout_92.setObjectName("verticalLayout_92")
        self.slideMenu_9 = QFrame(self.leftMenu)
        self.slideMenu_9.setMinimumSize(QSize(200, 0))
        font = QFont()
        font.setPointSize(7)
        self.slideMenu_9.setFont(font)
        self.slideMenu_9.setStyleSheet("")
        self.slideMenu_9.setFrameShape(QFrame.StyledPanel)
        self.slideMenu_9.setFrameShadow(QFrame.Raised)
        self.slideMenu_9.setObjectName("slideMenu_9")
        self.verticalLayout_84 = QVBoxLayout(self.slideMenu_9)
        self.verticalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_84.setSpacing(0)
        self.verticalLayout_84.setObjectName("verticalLayout_84")
        self.frame_74 = QFrame(self.slideMenu_9)
        self.frame_74.setStyleSheet("")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.frame_74.setObjectName("frame_74")
        self.horizontalLayout_30 = QHBoxLayout(self.frame_74)
        self.horizontalLayout_30.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_30.setSpacing(6)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.title = QPushButton(self.frame_74)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.horizontalLayout_30.addWidget(self.title, 0,
                                           Qt.AlignLeft | Qt.AlignTop)
        self.iconizeset = QPushButton(self.frame_74)
        self.iconizeset.setStyleSheet("")
        self.iconizeset.setText("")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/icons/icons/gear.svg"), QIcon.Normal,
                        QIcon.Off)
        self.iconizeset.setIcon(icon1)
        self.iconizeset.setIconSize(QSize(32, 32))
        self.iconizeset.setObjectName("iconizeset")
        self.horizontalLayout_30.addWidget(self.iconizeset, 0,
                                           Qt.AlignLeft | Qt.AlignTop)
        self.verticalLayout_84.addWidget(self.frame_74, 0, Qt.AlignTop)
        self.frame_75 = QFrame(self.slideMenu_9)
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.frame_75.setObjectName("frame_75")
        self.verticalLayout_85 = QVBoxLayout(self.frame_75)
        self.verticalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_85.setSpacing(10)
        self.verticalLayout_85.setObjectName("verticalLayout_85")
        self.outlabel = QLabel(self.frame_75)
        self.outlabel.setMinimumSize(QSize(200, 40))
        self.outlabel.setMaximumSize(QSize(200, 40))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.outlabel.setFont(font)
        self.outlabel.setAlignment(Qt.AlignCenter)
        self.outlabel.setObjectName("outlabel")
        self.verticalLayout_85.addWidget(self.outlabel, 0, Qt.AlignHCenter)
        self.outputpath = QLineEdit(self.frame_75)
        self.outputpath.setMinimumSize(QSize(184, 30))
        self.outputpath.setStyleSheet(
            "border: 1px solid black;\n"
            "max-width:180px;\n"
            "min-width:180px;\n"
            "text-align: center;\n"
            "font-size:15px;\n"
            "color:black;\n"
            "padding: 1px;\n"
            "border-radius: 7px;\n"
            "background: qlineargradient( x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #fff,stop: 0.4999 #eee,stop: 0.5 #ddd,stop: 1 #eee );\n"
            "width: 15px;")
        self.outputpath.setObjectName("outputpath")
        self.verticalLayout_85.addWidget(self.outputpath, 0, Qt.AlignHCenter)
        self.browsebut = QPushButton(self.frame_75)
        self.browsebut.setMinimumSize(QSize(64, 30))
        self.browsebut.setMaximumSize(QSize(19, 30))
        self.browsebut.setStyleSheet(
            "border: 1px solid black;\n"
            "max-width:60px;\n"
            "min-width:60px;\n"
            "text-align: center;\n"
            "font-size:15px;\n"
            "color:black;\n"
            "padding: 1px;\n"
            "border-radius: 7px;\n"
            "background: qlineargradient( x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #fff,stop: 0.4999 #eee,stop: 0.5 #ddd,stop: 1 #eee );\n"
            "width: 15px;")
        self.browsebut.setObjectName("browsebut")
        self.verticalLayout_85.addWidget(self.browsebut, 0, Qt.AlignHCenter)
        self.verticalLayout_84.addWidget(self.frame_75)
        self.frame_8 = QFrame(self.slideMenu_9)
        self.frame_8.setMinimumSize(QSize(0, 300))
        self.frame_8.setMaximumSize(QSize(16777215, 300))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_84.addWidget(self.frame_8)
        self.verticalLayout_92.addWidget(self.slideMenu_9)
        self.horizontalLayout.addWidget(self.leftMenu)
        self.mainMenu = QFrame(self.centralwidget)
        self.mainMenu.setMaximumSize(QSize(16777215, 16777215))
        self.mainMenu.setSizeIncrement(QSize(-10205, 0))
        self.mainMenu.setFrameShape(QFrame.StyledPanel)
        self.mainMenu.setFrameShadow(QFrame.Raised)
        self.mainMenu.setObjectName("mainMenu")
        self.verticalLayout = QVBoxLayout(self.mainMenu)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QFrame(self.mainMenu)
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_2.setSpacing(40)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_6 = QFrame(self.header)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setContentsMargins(0, 0, 6, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_7 = QPushButton(self.frame_6)
        self.pushButton_7.setMinimumSize(QSize(50, 50))
        self.pushButton_7.setMaximumSize(QSize(50, 50))
        self.pushButton_7.setText("")
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QSize(50, 50))
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_7.addWidget(self.pushButton_7)
        self.horizontalLayout_2.addWidget(self.frame_6, 0,
                                          Qt.AlignLeft | Qt.AlignTop)
        self.frame = QFrame(self.header)
        self.frame.setMinimumSize(QSize(300, 40))
        self.frame.setMaximumSize(QSize(300, 40))
        self.frame.setContextMenuPolicy(Qt.NoContextMenu)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pastelink = QLineEdit(self.frame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pastelink.sizePolicy().hasHeightForWidth())
        self.pastelink.setSizePolicy(sizePolicy)
        self.pastelink.setMinimumSize(QSize(252, 0))
        self.pastelink.setMaximumSize(QSize(17, 16777215))
        font = QFont()
        font.setPointSize(14)
        self.pastelink.setFont(font)
        self.pastelink.setObjectName("pastelink")
        self.horizontalLayout_6.addWidget(self.pastelink, 0, Qt.AlignLeft)
        self.pushButton_6 = QPushButton(self.frame)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setText("")
        icon2 = QIcon()
        icon2.addPixmap(
            QPixmap(":/icons/icons/search.svg"),
            QIcon.Normal,
            QIcon.Off,
        )
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QSize(20, 20))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_6.addWidget(self.pushButton_6)
        self.horizontalLayout_2.addWidget(self.frame, 0,
                                          Qt.AlignLeft | Qt.AlignTop)
        self.frame_3 = QFrame(self.header)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.minimize = QPushButton(self.frame_3)
        self.minimize.setText("")
        icon3 = QIcon()
        icon3.addPixmap(
            QPixmap(":/icons/icons/arrow-down-left.svg"),
            QIcon.Normal,
            QIcon.Off,
        )
        self.minimize.setIcon(icon3)
        self.minimize.setIconSize(QSize(20, 20))
        self.minimize.setObjectName("minimize")
        self.horizontalLayout_4.addWidget(self.minimize)
        self.closeBut = QPushButton(self.frame_3)
        self.closeBut.setText("")
        icon4 = QIcon()
        icon4.addPixmap(QPixmap(":/icons/icons/x.svg"), QIcon.Normal,
                        QIcon.Off)
        self.closeBut.setIcon(icon4)
        self.closeBut.setIconSize(QSize(20, 20))
        self.closeBut.setObjectName("closeBut")
        self.horizontalLayout_4.addWidget(self.closeBut)
        self.horizontalLayout_2.addWidget(self.frame_3, 0,
                                          Qt.AlignRight | Qt.AlignTop)
        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)
        self.frame_9 = QFrame(self.mainMenu)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.contents = QScrollArea(self.frame_9)
        self.contents.setStyleSheet(
            "QScrollArea{\n"
            "    border-top: 1px solid rgb(230, 5, 64);\n"
            "\n"
            "}\n"
            "#contents{\n"
            "border:none;\n"
            "\n"
            "}\n"
            "QFrame{\n"
            "    border: 3px solid rgb(230, 5, 64);\n"
            "    border-radius:20px;\n"
            "    background:transparent;\n"
            "\n"
            "}\n"
            "")
        self.contents.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.contents.setWidgetResizable(True)
        self.contents.setObjectName("contents")
        self.Area = QWidget()
        self.Area.setGeometry(QRect(0, 0, 755, 413))
        self.Area.setMinimumSize(QSize(0, 0))
        self.Area.setMaximumSize(QSize(16777215, 16777215))
        self.Area.setObjectName("Area")
        self.verticalLayout_7 = QVBoxLayout(self.Area)
        self.verticalLayout_7.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_7.setSpacing(9)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        self.contents.setWidget(self.Area)
        self.horizontalLayout_9.addWidget(self.contents)
        self.verticalLayout.addWidget(self.frame_9)
        self.horizontalLayout.addWidget(self.mainMenu)
        Downloader.setCentralWidget(self.centralwidget)

        self.retranslateUi(Downloader)
        QMetaObject.connectSlotsByName(Downloader)

    def retranslateUi(self, Downloader):
        _translate = QCoreApplication.translate
        Downloader.setWindowTitle(_translate("Downloader", "BLACK UI"))
        self.title.setText(_translate("Downloader", "Settings"))
        self.outlabel.setText(_translate("Downloader", "Output Directory"))
        self.outputpath.setText(_translate("Downloader", "C:\\"))
        self.browsebut.setText(_translate("Downloader", "Browse"))
        self.pastelink.setPlaceholderText(
            _translate("Downloader", "    Paste Link"))
