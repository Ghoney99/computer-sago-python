# HW 11.3 Seaborn
# Author : 장지헌
# Date : 2023. 5. 16.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 펭귄 데이터 세트 로드
df_penguins = sns.load_dataset("penguins")

# 데이터프레임의 자료형 확인
print("type(df_penguins) = ", type(df_penguins))

# 데이터프레임의 내용 출력
print("df_penguins = ")
print(df_penguins)
print()

# NaN 데이터 제거
df_penguins = df_penguins.dropna()

# 펭귄 종류별, 거주 섬(island) 별, 몸무게 (body_mass_g)에 대한 Seaborn boxplot 출력
sns.boxplot(x="species", y="body_mass_g", hue="island", data=df_penguins)
plt.title("Body Mass of Penguins on Different Islands") #제목
plt.xlabel("Species") #x축 라벨
plt.ylabel("Body Mass (g)") #y축 라벨
plt.show()



