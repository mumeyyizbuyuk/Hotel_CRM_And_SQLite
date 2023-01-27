from functions import *
#burada * koyarak her şeyi çağırdık

import streamlit as st

import pandas as pd

tablo=pd.DataFrame(verigetir("odalar"))
tablo.columns=["Oda Numarası","Kişi Sayısı","Fiyat"]
st.table(tablo)


st.subheader("Oda Sil")
col1,col2=st.columns(2)
with col1 :
    odasec=st.selectbox("Silinecek odaları seçiniz", odalar())
with col2:
    st.write("İşlem geri döndürülemez. Dikkatli olun!")
    sil=st.checkbox("Odayı Sil")
    #sil=st.button("Odayı Sil")
    if sil:
        st.warning("Silme İşlemi Gerçekleştirilecek. Bu işlem geri döndürülemez. Emin misiniz?")
        sile=st.button("Evet")
        silh = st.button("Hayır")
        if sile:
            odasil(odasec)
            st.success("Oda Başarılı Şekilde Silindi")
        if silh:
            st.write("Girdiğiniz değeri kontrol ediniz!")


st.subheader("Fiyat Düzenle")
col1,col2,col3=st.columns(3)
with col1 :
    odasec=st.selectbox("Fiyatı düzenlenecek odayı seçiniz", odalar())
with col2:
    fiyat=st.number_input("Yeni Fiyat")
with col3:
    st.write("Geçmiş Randevular Eski Fiyat Üzerinden Hesaplanacaktır")
    duzenle=st.button("Fiyat Düzenle")
    if duzenle:
        odafiyatduzenle(odasec,fiyat)
        st.success("Oda Fiyatı Değiştirildi")

