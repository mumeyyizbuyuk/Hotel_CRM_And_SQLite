from functions import *
import streamlit as st
import pandas as pd
import datetime

st.subheader("Randevu Güncelleme Sayfasına Hoşgeldiniz")
tc = st.text_input("Lütfen TCKN Giriniz")
giris = st.date_input("Lütfen Yeni Giriş Tarihinizi  Seçiniz")
cikis = st.date_input("Lütfen Yeni Çıkış Tarihinizi  Seçiniz")
ilkadim=st.button("Değişiklik Yapmak İçin Kutuya Tıklayınız")
if ilkadim :
    if int(tc) not in tckn() :
        st.write("Randevu Bulunamadı. Bilgilerinizi Kontrol Ediniz.")
    else:
        #girisguncelle(tarihyenig,tckimlik)
        #cikisguncelle(tarihyenic,tckimlik)
        gun = cikis - giris
        gun = gun.days
        if gun < 1:
            gun = 1
        satir=tcninsatiri(tc)[0] #tc nin olduğu satırı getirdim
        isim=satir[0]
        soyisim = satir[1]
        telefon = satir[3]
        oda = satir[6]
        fiyat = satir[7]

        yenifiyat = verigetir("odalar")[oda][2] * gun
        veriekle("randevular2", isim, soyisim, tc, telefon, giris, cikis, oda, yenifiyat)
        st.success("Güncellemeniz başarılı şekilde gerçekleşti")
        fiyatfarki=yenifiyat-fiyat
        tcninsatirisil(tc, fiyat)
        if yenifiyat > fiyat:
            st.write("Ödemeniz gereken fiyat farkı " + str(fiyatfarki))
        elif yenifiyat == fiyat:
            st.write("Ek ödeme çıkmadı")
        else:
            st.write("Tarafınıza ödenecek fiyat farkı " +str(fiyatfarki))
        tcninsatirisil(tc,fiyat)





