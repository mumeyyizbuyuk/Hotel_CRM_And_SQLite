from functions import *
#burada * koyarak her şeyi çağırdık
import datetime
import streamlit as st

tabloyap("randevular2",
             "(isim STRING, soyisim STRING, tc INTEGER, telefon INTEGER, giris DATE, cikis DATE, oda INTEGER, fiyat FLOAT)")

with st.form("randevuekle",clear_on_submit=True) :
    isim=st.text_input("İsminizi Giriniz")
    soyisim=st.text_input("Soyisminizi Giriniz")
    tc=st.text_input("TC Giriniz")
    telefon=st.text_input("Telefon Numarası Giriniz. Başında 0 olmadan 10 hane olarak giriniz.")
    giris=st.date_input("Giriş Tarihi")
    cikis=st.date_input("Çıkış TArihi")
    oda=st.selectbox("Oda Seçiniz",odalar())
    #st.write(verigetir("odalar")[oda-1][1] + "kişilik oda seçtiniz")
    rekle=st.form_submit_button("Randevu Ekle")
    if rekle:
        gun=cikis-giris
        gun = gun.days
        if gun < 1:
            gun=1
        fiyat=verigetir("odalar")[oda-1][2] * gun
        if cikis < giris:
            st.write("Çıkış tarihi giriş tarihinden küçük olamaz.")
        elif len(telefon) != 10:
            st.write("Telefon numarası hatalı girildi")
        else:
            veriekle("randevular2", isim, soyisim, tc, telefon, giris, cikis, oda, fiyat)
            st.success("Randevu Eklendi Fiyat ")
            st.write(fiyat)



#tablo yapıp veri ekleyeceğiz

