#!/usr/bin/env python
# coding: utf-8

# In[13]:


#sanaaaaat <3
import time
while True:
    secim=input("şekli seçiniz: ")
    if secim=="q":
        print("çıkış yapılıyor...")
        time.sleep(5)
        print("güle güle ")
        break
    elif secim=="1":
        print("üçgen")
        secim1=int(input("kenar1: "))
        secim2=int(input("kenar2: "))
        secim3=int(input("kenar3: "))
        if (secim1>0 and secim2>0 and secim3>0):
            if (abs(secim2-secim3)<secim1<secim2+secim3) or (abs(secim1-secim3)<secim2<secim1+secim3) or (abs(secim1-secim2)<secim3<secim1+secim2):
                if (secim1==secim2 or secim1==secim3 or secim2==secim3):
                    if (secim1==secim2 and secim1==secim3 and secim2==secim3):
                        print("eşkenar üçgen")
                    else:
                        print("ikizkenar üçgen")
  
                elif secim1!=secim2 and secim1!=secim3 and secim2!=secim3:
                    print("sıradan üçgen")     
            else:
                print("üçgen belirtmiyor")  
        else:
            print("geçerisiz değerler girdiniz")
        
    elif secim=="2":
        print("dörtgen")
        secim4=int(input("kenar4: "))
        secim5=int(input("kenar5: "))
        secim6=int(input("kenar6: "))
        secim7=int(input("kenar7: "))
        if (secim4>0 and secim5>0 and secim6>0 and secim7>0):
            if (secim4==secim5 or secim5==secim6 or secim6==secim7 or secim4==secim6 or secim4==secim7 or secim5==secim7):
                if (secim4==secim5 and secim5==secim6 and secim6==secim7 and secim4==secim6 and secim4==secim7 and secim5==secim7): 
                    print("kare")
                elif (secim4==secim5 and secim6==secim7) or (secim4==secim6 and secim5==secim7) or (secim4==secim7 and secim5==secim6):   
                    print("dikdörtgen")
                else:
                    print("sıradan dörtgen")
            elif (secim4!=secim5 and secim5!=secim6 and secim6!=secim7 and secim4!=secim6 and secim4!=secim7 and secim5!=secim7):
                print("sıradan dörtgen")
        else:
            print("geçersiz değerler girdiniz")
        
    else:
        print("geçersiz seçim yaptınız")

    


# In[ ]:




