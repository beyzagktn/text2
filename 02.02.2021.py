#!/usr/bin/env python
# coding: utf-8

# In[20]:


#importsuz hesap machine
print(""" 
Hesap Makinesi
toplama için 1 e basınız
çıkartma için 2 ye basınız
çarpma için 3 e basınız
bölme için 4  basınız
üs alma için 5 e basınız
kare alma için 6 ya basınız
küp alma için 7 ye basınız

""")

islem=str(input("yapmak istediğiniz işlemi seçiniz: "))
while True:
    #toplama
    if (islem=="1"):
        sayi1=float(input("sayı1: "))
        sayi2=float(input("sayı2: "))
        toplam=sayi1+sayi2
        print("Toplam: {}".format(toplam))
        break
    #çıkarma 
    elif (islem=="2"):
        cıkarma=sayi1-sayi2
        print("cıkarma: {}".format(cıkarma))
        break
    #çarpma
    elif (islem=="3"):
        carpma=sayi1*sayi2
        print("çarpma: {}".format(carpma))
        break
    #bölme
    elif (islem=="4"):
        bolme=sayi1/sayi2
        print("bölme: {}".format(bolme))
        break
    #üs alma
    elif (islem=="5"):
        us=sayi1**sayi2
        print("üs: {}".format(us))
        break
    #kare alma
    elif (islem=="6"):
        kare1=sayi1**2
        kare2=sayi2**2
        print("kare1: {} , kare2: {}".format(kare1,kare2))
        break
    #küp alma
    elif (islem=="7"):
        kup1=sayi1**3
        kup2=sayi2**3
        print("küp1: {} , küp2: {}".format(kup1,kup2))
        break


# In[ ]:


from math import*
import time
def toplama():
    sayi1=float(input("sayı1: "))
    sayi2=float(input("sayı2: "))
    toplama=sayi1+sayi2
    print(toplama)
def cıkarma():
    sayi1=float(input("sayı1: "))
    sayi2=float(input("sayı2: "))
    cıkarma=sayi1-sayi2
    print(cıkarma)
def carpma():
    sayi1=float(input("sayı1: "))
    sayi2=float(input("sayı2: "))
    carpma=sayi1*sayi2
    print(carpma)
def bolme():
    sayi1=float(input("sayı1: "))
    sayi2=float(input("sayı2: "))
    bolme=sayi1/sayi2
    print(bolme)
print("""
toplama için 1 
çıkarma için 2
çarpma için 3 
bölme için 4
çıkmak için q
""")

while True:
    islem=input("işlemi seçiniz: ")
    if (islem=="q"):
        time.sleep(10)
        print("çıkış yapıldı")
        break
    elif (islem=="1"):
        toplama()
    elif (islem=="2"):
        cıkarma()
    elif (islem=="3"):
        carpma()
    elif (islem=="4"):
        bolme()
    else:
        print("yanlış işlem girdiniz.")


# In[ ]:




