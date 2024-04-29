
"""
 Kesikli Olasılık Dağılımı
    Bernoulli
    Binom
    Poisson

 Sürekli Olasılık Dağılımları
    Normal Dağılım ( Genelde en fazla karşımıza cıkan bu)
    Üniform Dağılım
    Üstel Dağılım
 """


"""
-------------------------------
from scipy.stats import bernoulli
p = 0.6
rv = bernoulli(p)
print(rv.pmf(k = 0))
-------------------------------
"""
"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# Büyük Sayılar Yasası
"""
        Burada ki kodda şu denmektedir ;
    
     2 zar attığımızda  yazı gelme olasılıgı 1/2 yani %50 dir 
     ama  16 kere üst üste zar attığımızda yazı gelme oranı  %43,75 dir.
"""

"""
import numpy as np
rng = np.random.RandomState(123)
for i in np.arange(1, 21):
    deney_sayisi = 2**i
    yazı_turalar = rng.randint(0, 2,size =deney_sayisi)
    yazı_olasikleri = np.mean(yazı_turalar)
    print("Atış Sayısı: ",deney_sayisi ,"---",'Yazı Olasılığı: %.2f'  % (yazı_olasikleri * 100 ))
"""
"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""




#Tek Örnekleme Oran Testi
    #HO: P 0.125
    #H1::P!= 125
from statsmodels.stats.proportion import proportions_ztest
count = 40
nobs = 500
value = 0.125
print(proportions_ztest(count,nobs,value))
 # count = Başarı Sayısını baz alır
 #nobs = Gercekleştirilen gözlem sayısını baz alır
 #value = Test edilmek istenilen değer baz alır