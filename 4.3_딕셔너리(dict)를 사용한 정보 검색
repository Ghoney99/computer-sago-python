#  Homewrok4.3
#  작성자 : 장지헌
#  작성일자 : 2023.03.16
#  딕셔너리(dict)를 사용한 정보 검색

# Homework 4.3

# 딕셔너리에 입력받은 국가와 수도를 추가하는 함수
def insert_key_val(dict_country_capital):
    #while반복문을 돌면서 .을 입력받을 때까지 계속 입력
    while True:
        str = input("국가와 수도를 입력하시오(. to quit) : ")
        if str == ".":
            break
        #str을 공백을 기준으로 나누어 country, capital에 문자열을 저장
        country, capital = str.split()
        #딕셔너리에 country, capital을 key, value쌍으로 저장
        dict_country_capital[country] = capital

#국가 이름을 입력받아 해당 국가의 수도 이름을 찾는 함수
def search_capital(dict_country_capital):
    #while반복문을 돌면서 .을 입력받을 때까지 계속 입력
    while True:
        key = input("국가를 입력하시오(. to quit) : ")
        if key == ".":
            break

        #딕셔너리에 키가 있는지 없는지 판단
        if key in dict_country_capital:
            print("{}의 수도는 {}입니다".format(key, dict_country_capital[key]))
        else:
            print("key가 존재하지 않습니다.")

# 딕셔너리 생성
dict_country_capital = dict()

#실행
insert_key_val(dict_country_capital)
print("나라 - 수도 :",dict_country_capital)
search_capital(dict_country_capital)
