from kelimeDAL import KelimeDAL
from entity import Kelime

class KelimeBLL:

    @staticmethod
    def KelimeleriListele():
        print("kelime bll çalıştı")

        return KelimeDAL.KelimeleriListele()

    @staticmethod
    def YeniKelimeEkle(kelime,video):
        print("Kelime BLL başladı")
        return KelimeDAL.KelimeEkle(kelime,video)

    @staticmethod
    def KelimeGuncelle(duzenlenecekKelime,duzenlenecekKategori,duzenlenecekVideo,yeniKelime,yeniKategori,yeniVideo):


        KelimeDAL.KelimeGuncelle()

    @staticmethod
    def KelimeKategoriDuzenle():
        pass

    @staticmethod
    def KelimeVideoGuncelle(KelimeEntity,videoEntity):
        return KelimeDAL.KelimeGuncelle()

    @staticmethod
    def KelimeSil(KelimeEntity,VideoEntity):
        # VideoBLL.VideoSil(VideoEntity)
        return  KelimeDAL.KelimeSil(KelimeEntity)

    def KelimeKategoriEkle(self):
        pass



    def KelimeKategoriSil(self):
        pass

    @staticmethod
    def KelimeVideoBul(kelime):
        return KelimeDAL.KelimeVideoBul(kelime)

    @staticmethod
    def KelimeIDBul(Kelime):
        return KelimeDAL.KelimeIDBul(Kelime)