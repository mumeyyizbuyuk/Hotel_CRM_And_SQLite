from functions import *
#burada * koyarak her şeyi çağırdık
import streamlit as st
import pandas as pd
import datetime

with st.form("randevugetir",clear_on_submit=True) :
    tarih=st.date_input("Lütfen Tarih Seçiniz")
    rgetir = st.form_submit_button("Randevu Getir")
    if rgetir:
        tablo=pd.DataFrame(verigetir("randevular2"))
        bugun=datetime.date.today()
        tablo.columns=["İsim","Soyisim","TCKN","Telefon","Giriş Tarihi","Çıkış Tarihi","Seçilen Oda","Fiyat"]

        tablo=tablo[tablo['Giriş Tarihi']==tarih.strftime("%Y-%m-%d")]
        st.table(tablo)