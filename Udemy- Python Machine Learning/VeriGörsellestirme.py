import matplotlib
# ÖNEMLİ

# Grafiğe  daha fazla boyut eklemek istiyorsak "hue" fonksiyonunu kullanıyoruz
#  ÖRNEK : sns.catplot/x= "day", y = "total_bill",kind="violin",data=df);
#   : sns.catplot/x= "day", y = "total_bill", hue = "sex",kind="violin",data=df);




#titanik dosyası ile örnek calışma
# Pratik -1




import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import warnings

df = sns.load_dataset("titanic")


sns.lmplot(x='Survived', y='Pclass', data=df)
df.head()