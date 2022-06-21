from sys import argv, exit
from PyQt5.QtWidgets import (
    QTextEdit,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QFrame,
    QProgressBar,
    QSlider,
    QMainWindow,
    QApplication,
    QFileDialog,
    QMessageBox,
    QLabel,
    QAbstractSlider,
)
from urllib.request import urlopen
from PyQt5.QtGui import (
    QPixmap,
    QIcon,
    QFont,
)
from PyQt5.QtCore import (
    Qt,
    QSize,
    QPropertyAnimation,
    QEasingCurve,
    QRect,
)
from pytube import YouTube
from downloader import Ui_Downloader
from os.path import abspath


# pyuic5 C:\Users\sauda\OneDrive\Masaüstü\SOFTWARE\WINDOWS\GUI\Downloader\downloader.ui -o C:\Users\sauda\OneDrive\Masaüstü\SOFTWARE\WINDOWS\GUI\Downloader\downloader.py
# pyrcc5 C:\Users\sauda\OneDrive\Masaüstü\SOFTWARE\WINDOWS\GUI\Downloader\icons.qrc -o C:\Users\sauda\OneDrive\Masaüstü\SOFTWARE\WINDOWS\GUI\Downloader\icons_rc.py
class MainWindow(QMainWindow, Ui_Downloader):

    get_res = 0

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.minimize.clicked.connect(self.showMinimized)
        self.closeBut.clicked.connect(self.close)
        self.pushButton_6.clicked.connect(self.shower)
        self.browsebut.clicked.connect(self.browse_folder)
        self.pushButton_7.clicked.connect(self.openClose)

        def moveWindow(event):
            if self.isMaximized() == False:
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() -
                              self.clickPosition)
                    self.clickPosition = event.globalPos()
                    event.accept()

        self.header.mouseMoveEvent = moveWindow

    def openClose(self):
        width = self.leftMenu.maximumWidth()
        if width == 0:
            newWidth = 200
        else:
            newWidth = 0

        self.animation = QPropertyAnimation(self.leftMenu, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def browse_folder(self):
        self.outputpath.setText(
            abspath(
                str(
                    QFileDialog.getExistingDirectory(
                        self, "Select Output Directory"))))

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def shower(self):
        try:
            link = self.pastelink.text()
            self.pastelink.clear()
            self.frame_2 = QFrame(self.Area)
            self.frame_2.setMinimumSize(QSize(0, 150))
            self.frame_2.setMaximumSize(QSize(16777215, 150))
            self.frame_2.setStyleSheet(
                "QLabel{border:none;}QFrame{border:none;}\n")
            self.frame_2.setFrameShape(QFrame.StyledPanel)
            self.frame_2.setFrameShadow(QFrame.Raised)
            self.frame_2.setObjectName("frame_2")
            self.horizontalLayout_8 = QHBoxLayout(self.frame_2)
            self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_8.setSpacing(10)
            self.horizontalLayout_8.setObjectName("horizontalLayout_8")
            self.label = QLabel(self.frame_2)
            self.label.setMinimumSize(QSize(200, 150))
            self.label.setMaximumSize(QSize(200, 150))
            self.label.setText("")
            self.label.setObjectName("label")
            self.horizontalLayout_8.addWidget(self.label)
            self.frame_7 = QFrame(self.frame_2)
            self.frame_7.setFrameShape(QFrame.StyledPanel)
            self.frame_7.setFrameShadow(QFrame.Raised)
            self.frame_7.setObjectName("frame_7")
            self.verticalLayout_2 = QVBoxLayout(self.frame_7)
            self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_2.setSpacing(6)
            self.verticalLayout_2.setObjectName("verticalLayout_2")
            self.frame_4 = QFrame(self.frame_7)
            self.frame_4.setFrameShape(QFrame.StyledPanel)
            self.frame_4.setFrameShadow(QFrame.Raised)
            self.frame_4.setObjectName("frame_4")
            self.frame_4.setMinimumSize(QSize(0, 112))
            self.frame_4.setMaximumSize(QSize(16777215, 112))
            self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
            self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_3.setSpacing(6)
            self.horizontalLayout_3.setObjectName("horizontalLayout_3")
            self.textEdit = QTextEdit(self.frame_4)
            self.textEdit.setMaximumSize(QSize(16777215, 100))
            font = QFont()
            font.setFamily("Calibri")
            font.setPointSize(15)
            font.setBold(False)
            font.setWeight(50)
            self.textEdit.setFont(font)
            self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.textEdit.setReadOnly(True)
            self.textEdit.setObjectName("textEdit")
            self.horizontalLayout_3.addWidget(self.textEdit)
            self.progressBar = QProgressBar(self.frame_4)
            self.progressBar.setMinimumSize(QSize(154, 31))
            self.progressBar.setMaximumSize(QSize(19, 31))
            self.progressBar.setProperty("value", 0)
            self.progressBar.setObjectName("progressBar")
            self.horizontalLayout_3.addWidget(self.progressBar)
            self.frame_10 = QFrame(self.frame_4)
            self.frame_10.setMinimumSize(QSize(62, 0))
            self.frame_10.setMaximumSize(QSize(62, 16777215))
            self.frame_10.setFrameShape(QFrame.StyledPanel)
            self.frame_10.setFrameShadow(QFrame.Raised)
            self.frame_10.setObjectName("frame_10")
            self.horizontalSlider = QSlider(self.frame_10)
            self.horizontalSlider.setGeometry(QRect(0, 40, 62, 31))
            self.horizontalSlider.setMinimumSize(QSize(62, 31))
            self.horizontalSlider.setMaximumSize(QSize(62, 31))
            self.horizontalSlider.setOrientation(Qt.Horizontal)
            self.horizontalSlider.setObjectName("horizontalSlider")
            self.sliderPos = QPushButton(self.frame_10)
            self.sliderPos.setGeometry(QRect(0, 40, 62, 31))
            self.sliderPos.setMinimumSize(QSize(62, 31))
            self.sliderPos.setMaximumSize(QSize(62, 31))
            self.sliderPos.setText("")
            self.sliderPos.setObjectName("sliderPos")
            self.horizontalLayout_3.addWidget(self.frame_10)
            self.downloadbut = QPushButton(self.frame_4)
            self.downloadbut.setText("")
            icon5 = QIcon()
            icon5.addPixmap(QPixmap(":/icons/icons/arrow-down-circle.svg"),
                            QIcon.Normal, QIcon.Off)
            self.downloadbut.setIcon(icon5)
            self.downloadbut.setIconSize(QSize(50, 50))
            self.downloadbut.setObjectName("downloadbut")
            self.horizontalLayout_3.addWidget(self.downloadbut)
            self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignTop)
            self.frame_5 = QFrame(self.frame_7)
            self.frame_5.setStyleSheet(
                "QPushButton{border:2px solid rgb(182, 182, 182);border-radius:15px;}"
            )
            self.frame_5.setFrameShape(QFrame.StyledPanel)
            self.frame_5.setFrameShadow(QFrame.Raised)
            self.frame_5.setObjectName("frame_5")
            self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
            self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_5.setObjectName("horizontalLayout_5")
            self.verticalLayout_2.addWidget(self.frame_5, 0, Qt.AlignLeft)
            self.horizontalLayout_8.addWidget(self.frame_7)
            self.verticalLayout_7.addWidget(self.frame_2)
            self.textEdit.setText(YouTube(link).title)
            self.textEdit.setMaximumWidth(200)
            self.textEdit.setMinimumWidth(200)
            self.horizontalSlider.setMinimum(0)
            self.horizontalSlider.setMaximum(1)
            self.frame_5.hide()

            def formSlider(x):
                a = QAbstractSlider.sliderPosition(x)
                if a == 0:
                    self.horizontalSlider.setSliderPosition(1)
                    x.setStyleSheet("QSlider::handle:horizontal {\n"
                                    "    image: url(:/icons/icons/film.svg);\n"
                                    "}")
                    self.frame_5.show()
                if a == 1:
                    self.horizontalSlider.setSliderPosition(0)
                    x.setStyleSheet(
                        "QSlider::handle:horizontal {\n"
                        "    image: url(:/icons/icons/music.svg);\n"
                        "}")
                    self.frame_5.hide()

            self.sliderPos.clicked.connect(
                lambda: formSlider(self.horizontalSlider))

            def getThumbnail(link):
                response = urlopen(link)
                return response

            image = QPixmap()
            image.loadFromData(
                getThumbnail(YouTube(link).thumbnail_url).read())
            self.label.setScaledContents(True)
            self.label.setPixmap(image)
            self.label.setAlignment(Qt.AlignCenter)

            self.K84320P = QPushButton(self.frame_5)
            self.K42160P = QPushButton(self.frame_5)
            self.K21440P = QPushButton(self.frame_5)
            self.HD1080P = QPushButton(self.frame_5)
            self.HD720P = QPushButton(self.frame_5)
            self.SD480P = QPushButton(self.frame_5)
            buttons = [
                self.K84320P,
                self.K42160P,
                self.K21440P,
                self.HD1080P,
                self.HD720P,
                self.SD480P,
            ]
            names = ["4320p", "2160p", "1440p", "1080p", "720p", "480p"]
            for i in range(0, 6):
                buttons[i].setCheckable(True)
                buttons[i].setChecked(False)
                buttons[i].setMinimumSize(QSize(80, 32))
                buttons[i].setMaximumSize(QSize(80, 32))
                buttons[i].setText("")
                icon = QIcon()
                icon.addPixmap(
                    QPixmap(":/icons/icons/" + names[i] + ".svg"),
                    QIcon.Normal,
                    QIcon.Off,
                )
                buttons[i].setIcon(icon)
                buttons[i].setIconSize(QSize(60, 60))
                buttons[i].setObjectName(names[i])
                self.horizontalLayout_5.addWidget(buttons[i])

            def checker(showbut):
                if showbut.isChecked() == True:
                    showbut.setStyleSheet(
                        "QPushButton{border:2px solid rgb(182, 182, 182);background-color:gray;border-radius:15px;}"
                    )
                    for but in buttons:
                        if showbut == but:
                            but.show()
                            but.setChecked(True)
                        else:
                            but.hide()
                            but.setChecked(False)

                if showbut.isChecked() == False:
                    showbut.setStyleSheet(
                        "QPushButton{border:2px solid rgb(182, 182, 182);border-radius:15px;}"
                    )
                    for but in buttons:
                        but.show()
                        but.setChecked(False)

            self.K84320P.clicked.connect(lambda: checker(self.K84320P))
            self.K42160P.clicked.connect(lambda: checker(self.K42160P))
            self.K21440P.clicked.connect(lambda: checker(self.K21440P))
            self.HD1080P.clicked.connect(lambda: checker(self.HD1080P))
            self.HD720P.clicked.connect(lambda: checker(self.HD720P))
            self.SD480P.clicked.connect(lambda: checker(self.SD480P))

            def downloader():
                if self.horizontalSlider.sliderPosition() == 0:
                    YouTube(link).streams.get_audio_only().download(
                        output_path=self.outputpath.text())
                else:
                    for but in buttons:
                        if but.isHidden() == False:
                            if (len(
                                    YouTube(link).streams.filter(
                                        res=but.objectName(),
                                        mime_type="video/mp4")) > 0):
                                YouTube(link).streams.filter(
                                    res=but.objectName(),
                                    mime_type="video/mp4")[0].download(
                                        output_path=self.outputpath.text())
                            else:
                                QMessageBox.about(
                                    self,
                                    "Warning",
                                    "<p><div style='font-size:15pt; color:black; font-weight:600;'>The video you want to download does not support "
                                    + str(but.objectName()) +
                                    " resolution.Please try again with another resolution</div></p>",
                                )
                        else:
                            pass

            self.downloadbut.clicked.connect(lambda: downloader())
        except:
            QMessageBox.about(
                self,
                "Warning",
                '<p><div style="font-size:15pt; color:black; font-weight:600;">You must enter a link.</div></p>',
            )


if __name__ == "__main__":
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec_())
