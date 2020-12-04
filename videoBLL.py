from entity import Video
import shutil
import os

class VideoBLL:

    def VideolariListele():
        pass

    @staticmethod
    def VideoSil(silinecekVideo=Video):
        try:

            print("Silinecek video")
            print(silinecekVideo.secilenKelimeVideoYol)
            if os.path.exists(silinecekVideo.secilenKelimeVideoYol):
                os.remove(silinecekVideo.secilenKelimeVideoYol)
                return 1
            else:
                print("Video bulunamadığı için Silemedim.")
                return -1
        except Exception as exp:
            print("Hata oluştuğu için video silinemedi..")
            print(exp)
            return 0


    @staticmethod
    def VideoKopyala(video):
        try:

            eklenecekVideo = video
            shutil.copy(eklenecekVideo.videoKaynakYol, eklenecekVideo.videoHedefYol)
            print("video kopyalandı.")
            return True
        except Exception as exp:
            print(exp)
            return False

    def VideoIsmiDuzenle(self):
        pass

####________Veri Tabanı İşlemleri________#####

    def VideoVeriTabaniEkle(self):
        pass

    def VideoVeriTabaniDuzenle(self):
        pass

    def VideoVeriTabaniSil(self):
        pass