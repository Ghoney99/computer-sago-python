#  Homewrok3.1
#  작성자 : 장지헌
#  작성일자 : 2023.03.14
#  16진수 정수입력, 연산 및 출력

#Homework 3.1

#16진수 데이터 문자열을 한 줄로 입력받고
#split으로 공백을 제거한 후, a와 b변수에 넣어준다.
a, b = map(str,input("16진수 데이터를 입력하시오 (예 : 0xA3 0x3A) :").split())

#16진수 문자열 실수 표현 s로부터 실수를 계산하여 반환
a=int(float.fromhex(a))
b=int(float.fromhex(b))

#format(i, "08b")은 16진수를 나타내기 위한 표현으로 "0"을 prefix로 두어 8자리로 표현 후, 
#앞에 0b를 print문에서 표현해서 0b를 포함한 10자리로 표현
#format(i, "02X")은 16진수를 나타내기 위한 표현으로 "0"을 prefix로 두어 2자리로 표현 후, 
#앞에 0X를 print문에서 표현해서 0X를 포함한 4자리로 표현
print("a = 0x{} = {} = 0b{}".format(format(a, "02X"), format(a), format(a, "08b")))
print("b = 0x{} = {} = 0b{}".format(format(b, "02X"), format(b), format(b, "08b")))

#a, b의 bit-wise AND, bit-wise OR, bit-wise XOR 값을 계산
result_and = a&b
result_or = a|b
result_xor = a^b

#bit-wise 계산값 출력
print("a & b = 0x{} = {} = 0b{}".format(format(result_and, "02X"), format(result_and), format(result_and, "08b")))
print("a | b = 0x{} = {} = 0b{}".format(format(result_or, "02X"), format(result_or), format(result_or, "08b")))
print("a ^ b = 0x{} = {} = 0b{}".format(format(result_xor, "02X"), format(result_xor), format(result_xor, "08b")))
