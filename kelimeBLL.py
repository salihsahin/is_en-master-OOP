from kelimeDAL import KelimeDAL
from kategoriDAL import KategoriDAL
from videoBLL import VideoBLL
from entity import Kelime
from entity import Kategori
from entity import Video



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
    def KelimeVideoGuncelle(KelimeEntity,videoEntity):
        print("kelimvideogüncelle bll çalıştı.")
        KelimeDAL.KelimeVideoGuncelle(KelimeEntity,videoEntity)

    @staticmethod
    def KelimeSil(KelimeEntity,VideoEntity):

        VideoBLL.VideoSil(VideoEntity)
        KategoriDAL.KategoriKelimeIdSil(KelimeEntity)
        return KelimeDAL.KelimeSil(KelimeEntity)

    @staticmethod
    def KelimeVideoBul(kelime):
        return KelimeDAL.KelimeVideoBul(kelime)

    @staticmethod
    def KelimeIDBul(Kelime):
        return KelimeDAL.KelimeIDBul(Kelime)