import sys
from pytube import YouTube
from PyQt5.QtWidgets import *
from youtube_downloader_Qt import Ui_MainWindow

class main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.downloader=Ui_MainWindow()
        self.downloader.setupUi(self)

        self.downloader.pushButton.clicked.connect(self.download)
    def download(self):
        if self.downloader.radioButton.isChecked()==True:
            url=self.downloader.lineEdit.text()
            exit_path=self.downloader.lineEdit_2.text()
            video=YouTube(url)
            stream=video.streams.get_highest_resolution()
            stream.download(output_path=exit_path)
        elif self.downloader.radioButton_2.isChecked()==True:
            url = self.downloader.lineEdit.text()
            exit_path = self.downloader.lineEdit_2.text()
            video = YouTube(url)
            stream = video.streams.get_audio_only()
            stream.download(output_path=exit_path)

app=QApplication([])
pencere=main()
pencere.show()
app.exec_()