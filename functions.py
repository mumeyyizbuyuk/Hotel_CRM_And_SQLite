import sqlite3

conn=sqlite3.connect("vt.db")
c=conn.cursor()

def tabloyap(tabloisim,sutunlar):
  conn=sqlite3.connect("vt.db")
  c=conn.cursor()
  c.execute("CREATE TABLE IF NOT EXISTS "+tabloisim+sutunlar)
  conn.commit()

def veriekle(tabloisim,*veriler):
  conn=sqlite3.connect("vt.db")
  c=conn.cursor()
  say=len(veriler)
  sor="?,"*say
  sor=sor[:-1]
  c.execute("INSERT INTO "+tabloisim+" VALUES("+sor+")",veriler)
  conn.commit()

def verigetir(tabloisim):
  conn=sqlite3.connect("vt.db")
  c=conn.cursor()
  c.execute("SELECT * FROM "+tabloisim)
  sonuc=c.fetchall()
  return sonuc



def odalar():
  conn = sqlite3.connect("vt.db")
  c = conn.cursor()
  c.execute("SELECT numara FROM odalar")
  sonuc=c.fetchall()
  liste=[]
  for a in sonuc:
    liste.append(a[0])
  return liste

def tckn():
  conn = sqlite3.connect("vt.db")
  c = conn.cursor()
  c.execute("SELECT tc FROM randevular2")
  sonuc = c.fetchall()
  listetc = []
  for a in sonuc:
    listetc.append(a[0])
  return listetc



def giristarihi():
  conn = sqlite3.connect("vt.db")
  c = conn.cursor()
  c.execute("SELECT giris FROM randevular2")
  sonuc = c.fetchall()
  liste = []
  for a in sonuc:
    liste.append(a[0])
  return liste

def fiyatlar():
  conn = sqlite3.connect("vt.db")
  c = conn.cursor()
  c.execute("SELECT fiyat FROM odalar")
  sonuc = c.fetchall()
  liste=[]
  for i in sonuc :
    liste.append(i[0])
  return liste

def fiyathesap (gun,oda):
  conn = sqlite3.connect("vt.db")
  c = conn.cursor()
  c.execute("SELECT fiyat FROM odalar WHERE numara=?",(oda,))
  fiyat=c.fetchone()[0]
  toplamfiyat=fiyat*gun
  return toplamfiyat

def odasil(numara):
  conn = sqlite3.connect("vt.db")
  c = conn.cursor()
  c.execute("DELETE FROM odalar WHERE numara=?",(numara,))
  conn.commit()

def tcninsatirisil(tc,fiyat):
  conn = sqlite3.connect("vt.db")
  c = conn.cursor()
  c.execute("DELETE FROM randevular2 WHERE tc=? AND fiyat=?", (tc,fiyat))
  conn.commit()

def odafiyatduzenle(numara,fiyat):
  conn = sqlite3.connect("vt.db")
  c = conn.cursor()
  c.execute("UPDATE odalar SET fiyat=? WHERE numara=?",(fiyat,numara))
  conn.commit()

def tcninsatiri(tc):
  conn = sqlite3.connect("vt.db")
  c = conn.cursor()
  c.execute("SELECT * FROM randevular2 WHERE tc=?",(tc,))
  sonuc = c.fetchall()
  return sonuc

def girisguncelle(giris,tc):
  conn = sqlite3.connect("vt.db")
  c = conn.cursor()
  c.execute("UPDATE randevular2 SET giris=? WHERE tc=?",(giris,tc))
  conn.commit()

def cikisguncelle(cikis,tc):
  conn = sqlite3.connect("vt.db")
  c = conn.cursor()
  c.execute("UPDATE randevular2 SET cikis=? WHERE tc=?",(cikis,tc))
  conn.commit()
