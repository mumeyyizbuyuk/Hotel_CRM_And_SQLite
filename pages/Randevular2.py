from functions import *
#burada * koyarak her şeyi çağırdık

import streamlit as st

import pandas as pd

tablo=pd.DataFrame(verigetir("randevular2"))
tablo.columns=["İsim","Soyisim","TCKN","Telefon","Giriş Tarihi","Çıkış Tarihi","Seçilen Oda","Fiyat"]

