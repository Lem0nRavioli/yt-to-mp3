from PyQt5 import QtCore, QtGui, QtWidgets
import pytube


class Ui_YoutubeDownloader(object):
    def setupUi(self, YoutubeDownloader):
        YoutubeDownloader.setObjectName("YoutubeDownloader")
        YoutubeDownloader.resize(738, 175)
        self.centralwidget = QtWidgets.QWidget(YoutubeDownloader)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 30, 491, 111))
        self.textEdit.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.textEdit.setObjectName("textEdit")
        self.download_button = QtWidgets.QPushButton(self.centralwidget)
        self.download_button.setGeometry(QtCore.QRect(540, 30, 161, 51))
        self.download_button.setObjectName("download_button")
        self.info_label = QtWidgets.QLabel(self.centralwidget)
        self.info_label.setGeometry(QtCore.QRect(540, 90, 161, 41))
        self.info_label.setObjectName("info_label")
        YoutubeDownloader.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(YoutubeDownloader)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 738, 21))
        self.menubar.setObjectName("menubar")
        YoutubeDownloader.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(YoutubeDownloader)
        self.statusbar.setObjectName("statusbar")
        YoutubeDownloader.setStatusBar(self.statusbar)

        self.retranslateUi(YoutubeDownloader)
        QtCore.QMetaObject.connectSlotsByName(YoutubeDownloader)

        self.download_button.clicked.connect(self.clicked_download)

    def retranslateUi(self, YoutubeDownloader):
        _translate = QtCore.QCoreApplication.translate
        YoutubeDownloader.setWindowTitle(_translate("YoutubeDownloader", "Yt-to-mp3"))
        self.download_button.setText(_translate("YoutubeDownloader", "Download"))
        self.info_label.setText(_translate("YoutubeDownloader", "Waiting for a link."))

    def clicked_download(self):
        url = self.textEdit.toPlainText()
        destination = QtWidgets.QFileDialog.getExistingDirectory()
        self.download_video(url, destination)

    def download_video(self, url, destination):
        video = pytube.YouTube(url)
        # stream = video.streams.filter(file_extension='mp4').order_by('resolution').desc().first()
        stream = video.streams.filter(type='audio').order_by('abr').desc().first()
        self.info_label.setText(f"Quality: {stream.abr}. Downloading... ")
        stream.download(destination)
        self.info_label.setText("Done !")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    YoutubeDownloader = QtWidgets.QMainWindow()
    ui = Ui_YoutubeDownloader()
    ui.setupUi(YoutubeDownloader)
    YoutubeDownloader.show()
    sys.exit(app.exec_())