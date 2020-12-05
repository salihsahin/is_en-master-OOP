from kategoriDAL import KategoriDAL
from kelimeBLL import  KelimeBLL
from entity import Kategori
from entity import Kelime

class KategoriBLL:

    @staticmethod
    def KategorileriListele():
        print("Kategori Listele Bll Çalıştı")
        return KategoriDAL.KategorileriListele()

    @staticmethod
    def KategoriKelimeIdEkle(eklenenKelimeId,kategori):
        print("Kategori EKleme  başlayacak")
        return KategoriDAL.KategoriKelimeIdEkle(eklenenKelimeId,kategori)


    def KategoriSil(self):
        pass

    @staticmethod
    def KelimeyeAitKategoriBul(Kelime):
        print("Kategori Bul Bll Çalıştı")
        KelimeBLL.KelimeIDBul(Kelime)
        print("Kelime ID BUl Bitti")
        print("Kategori Id bul Bitti:")
        print(Kelime.kelime)
        print(Kelime.kelimeId)
        print("kelimeye ait Kategoriler bulunacak")

        return  KategoriDAL.KelimeyeAitKategoriBul(Kelime)

    @staticmethod
    def KategoriKelimeIdGuncelle(kelime, kategori):
        KategoriBLL.KategoriKelimeIdSil(kelime)
        print("Kategori eklenecek : ")
        print(kelime.kelimeId)

        kategori.kategoriler = kategori.duzenlenecekYeniKategoriler
        print(kategori.kategoriler)
        return KategoriDAL.KategoriKelimeIdEkle(kelime.kelimeId, kategori)

    @staticmethod
    def KategoriKelimeIdSil(kelime=Kelime):
        KategoriDAL.KategoriKelimeIdSil(kelime)
