#11.1 Pandas와 Excel 파일을 사용한 데이터 분석
# Author : 장지헌
# Date : 2023. 5. 16.

import pandas as pd
import openpyxl

# student_scores.xlsx 파일을 읽어 데이터 프레임을 생성후, 출력
df = pd.read_excel("student_scores.xlsx")
print("df =\n",df,"\n")

# Avg열을 추가하고 st_id 열을 제외하고 numeric_only를 사용해 숫자만 있는 셀을 계산, round를 사용해 소수점 셋째자리까지 표시
df['Avg'] = df.drop(columns='st_id').mean(axis=1, numeric_only=True)
#sort_values를 사용해 Avg를 기준으로 내림차순 정렬
df = df.sort_values(by='Avg', ascending=False)

# 각 과목의 평균을 계산
#st_id 열을 제외하고 numeric_only를 사용해 숫자만 있는 셀을 계산, round를 사용해 소수점 둘째자리까지 표시
avgs_per_class = df.drop(columns='st_id').mean(numeric_only=True).round(2)
print("avgs_per_class =\n",avgs_per_class,"\n")

# 데이터프레임에 평균값을 가진 새로운 행 추가
df.loc[len(df)] = avgs_per_class
# 새로 추가된 행의 'st_name' 열 값을 'Total_Avg'로 수정
df.at[len(df)-1, 'st_name'] = 'Total_Avg'

print("df_sorted_with_avg =\n", df)

print("Writing df to excel file")
#"processed_scores.xlsx" 파일에 쓰기 위한 ExcelWriter 객체를 생성
#데이터프레임을 "Students Records"라는 시트 이름으로 Excel 파일에 저장
with pd.ExcelWriter("processed_scores.xlsx") as excel_writer:
    df.to_excel(excel_writer, sheet_name='Students Records')
