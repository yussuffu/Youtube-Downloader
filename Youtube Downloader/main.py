import sys
from pytube import YouTube                  # Diğer dosyayı ve gereken kütüphanelri burda projeme ekliyorum
from PyQt5.QtWidgets import *
from youtube_downloader_Qt import Ui_MainWindow


#Designerdan oluşturduğum ekran MainWindow olduğu için burdaki sınıfta QMainWindow u miras alıyorum
class main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.downloader=Ui_MainWindow()     #init fonksiyonunda diğer dosyadan obje oluşturuyorum ordaki nesnelere(buton,etiket) ulaşabilmek için
        self.downloader.setupUi(self)       # ve diğer doyanın ana fonksiyonunu çalıştırıyorum ekranın oluşabilmesi için

        self.downloader.pushButton.clicked.connect(self.download)       #ekrandakı butona basılınca download  fonksiyonuna git  diyorum
        
        
    def download(self):
        if self.downloader.radioButton.isChecked()==True:       #burdaki radio buton mp4 olan eğer bu buton işaretlenmişse bu fonksiona gircek
            url=self.downloader.lineEdit.text()
            exit_path=self.downloader.lineEdit_2.text()     
            video=YouTube(url)                                       #ve burda kullanıcıdan url ve exit_path alarak videoyu mp4 olarak indirmesini sağlıyorum
            stream=video.streams.get_highest_resolution()           
            stream.download(output_path=exit_path)
        elif self.downloader.radioButton_2.isChecked()==True:       #burdaki radio buton mp3 olan eğer bu buton işaretlenmişse bu fonksiona gircek
            url = self.downloader.lineEdit.text()
            exit_path = self.downloader.lineEdit_2.text()
            video = YouTube(url)
            stream = video.streams.get_audio_only()                 #ve burda kullanıcıdan url ve exit_path alarak videoyu mp3 olarak indirmesini sağlıyorum
            stream.download(output_path=exit_path)

app=QApplication([])        #burada uygulama oluşturuyorum ve main sınıfından obje oluşturup bunu show() ile ekrana gösteriyorum ve app.exec_() ile de sonsuz döngüye soluyorum sürekli ekranda kalması için
pencere=main()
pencere.show()
app.exec_()
