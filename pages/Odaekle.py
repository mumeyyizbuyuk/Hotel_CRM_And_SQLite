from functions import *
#burada * koyarak her şeyi çağırdık

import streamlit as st

tabloyap("odalar","(numara INTEGER, kisi INTEGER, fiyat FLOAT)")

with st.form("odaekle",clear_on_submit=True) :
    numara=st.number_input("Oda Numarası Giriniz",step=1)
    kisi=st.number_input("Oda Kişi Sayısı",step=1)
    fiyat=st.number_input("Günlük Fiyat")
    eklebutton=st.form_submit_button("Oda Ekle")
    if eklebutton:
        veriekle("odalar",numara, kisi, fiyat)
        st.success("Oda başarılı bir şekilde eklendi.")
