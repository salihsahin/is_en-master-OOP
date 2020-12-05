import sqlite3
conn = sqlite3.connect('Sozluk.db')
from entity import Kelime
from entity import Video
class KelimeDAL:

    @staticmethod
    def KelimeleriListele():
        print("kelime dal çalıştı")
        kelimeListesiTupple = []
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT KELIME_ADI FROM KELIMELER")
            kelimeListesiTupple = cur.fetchall()
        return kelimeListesiTupple


    @staticmethod
    def KelimeEkle(kelime=Kelime, video=Video):
        try:
            yeniKelime = kelime
            yeniVideo = video
            print("kelime EKleme  başlayacak")
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO KELIMELER (KELIME_ADI,KELIME_YOLU) VALUES(?,?)", [yeniKelime.kelime, yeniVideo.videoHedefYol])
                kelimeId = cur.lastrowid
                print("kelime eklendi")
                return kelimeId
        except Exception as exp:
            print("Kelime Dal Hata: ")
            print(exp)
            return -1

    def KelimeGuncelle():
        pass

    @staticmethod
    def KelimeSil(KelimeEntity=Kelime):
        silinecekKelime = KelimeEntity
        try:
            with conn:
                cur = conn.cursor()
                cur.execute("DELETE FROM KELIMELER Where KELIME_ADI=(?)", [silinecekKelime.kelime])
            return True
        except Exception as e:
            print(e)
            return False

    def KelimeKategoriEkle():
        pass


    def KelimeKategoriSil():
        pass

    @staticmethod
    def KelimeVideoBul(Kelime=Kelime):
        try:
            with conn:
                cur = conn.cursor()
                cur.execute("SELECT KELIME_YOLU FROM KELIMELER Where KELIME_ADI=(?)", [Kelime.kelime])
                sonuc = cur.fetchone()[0]
            return sonuc
        except Exception as exp:
            print(exp)
            return None

    @staticmethod
    def KelimeIDBul(Kelime=Kelime):
        try:
            print("kelime dal Kelime Id Bul çalıştı")
            print(Kelime.kelime)
            bulunacakKelimeId=-1

            with conn:
                cur = conn.cursor()
                cur.execute("select ID from KELIMELER where KELIME_ADI=(?)", [Kelime.kelime])
                bulunacakKelimeId = cur.fetchone()[0]
                print("Bulundu.")
        except Exception as exp:
            print(exp)
        print("kelime dal ıd bul çıkılıyor")
        print("Bulunan id ", bulunacakKelimeId)
        Kelime.kelimeId=bulunacakKelimeId
        return Kelime

    @staticmethod
    def KelimeVideoGuncelle(KelimeEntity=Kelime,VideoEntity=Video):
        print("kelimevideo güncelle dal çalıştı.")
        KelimeDAL.KelimeIDBul(KelimeEntity)

        print("Keliem İd ")
        print(KelimeEntity.kelimeId)

        try:
            with conn:
                cur = conn.cursor()
                cur.execute("update KELIMELER set KELIME_ADI=(?),KELIME_YOLU=(?) where ID=(?)", [KelimeEntity.duzenlenecekYeniKelime, VideoEntity.videoHedefYol,KelimeEntity.kelimeId])

        except Exception as exp:
            print(exp)
        print("kelime dal kelime güncelle çıkılıyor")

