# Normallil
# Varyans Homejenliği
import pandas as pd

# H0: M1 = M2
# H1: M1 != M2
"""
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Create DataFrames A and B
data_A = [30, 27, 21, 27, 29, 30, 20, 20, 27, 32, 35, 22, 24, 23, 25, 27, 23, 27, 23, 25, 21, 18, 24, 26, 33, 26, 27, 28, 19, 25]
data_B = [37, 39, 31, 31, 34, 38, 30, 36, 29, 28, 38, 28, 37, 30, 31, 31, 27, 32, 33, 33, 33, 31, 32, 33, 26, 32, 33, 26, 32, 33, 29]
A = pd.DataFrame(data_A, columns=['A'])
B = pd.DataFrame(data_B, columns=['B'])

# Combine DataFrames into A_B with meaningful column names
A_B = pd.concat([A, B], axis=1, names=['Group', 'Value'])  # Clearer column names

# Display the first few rows
print(A_B.head())

# Create the boxplot with informative labels
sns.boxplot(
    x="Group",
    y="Value",
    showmeans=True,  # Display means as diamonds
    data=A_B
)

# Customize the plot (optional)
sns.despine()  # Remove unnecessary chart elements for a cleaner look
plt.title("Distribution of Values across Groups")  # Add a title
plt.xlabel("Group")  # Label the x-axis
plt.ylabel("Value")  # Label the y-axis
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust spacing for clarity

# Display the plot
plt.show()

A_B.head()
"""

""" --------------------------------------------------------------------------------------"""

""""
*
                HİPOTEZLER
                   * H0:P1 = P2
                   * H1:P1 != P2
                   * H0:P1 <= P2
                   * h1:P1 > P2
                   * H0:P1 >= P2
                   * H1:P1 <P2
*
"""


"""
*
from statsmodels.stats.proportion import proportions_ztest
import numpy as np
basari_sayisi = np.array([300,250])
gozlem_sayıları = np.array([1000,1100])
print(proportions_ztest(count=basari_sayisi,nobs=gozlem_sayıları))
*

"""