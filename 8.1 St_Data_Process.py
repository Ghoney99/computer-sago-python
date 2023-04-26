data_list = [] #리스트 초기화

def fread_data(file_name):
    with open(file_name, 'r') as fin: #파일 열기 (읽기모드)
        for line in fin:    #파일을 한줄씩 읽기
            name, kor, eng, math, sci= line.split() #공백을 기준으로 split
            tmp = [name, int(kor), int(eng), int(math), int(sci)]   #split한 변수들을 리스트로 저장
            data_list.append(tmp)   #리스트를 data_list에 추가 (2차원 배열)
        fin.close()
    return data_list

def fwrite_data(file_name, data_list):

    with open(file_name, 'w') as f: #파일 열기 (쓰기모드)
        #main.py에 있는 출력
        f.write("======================================\n")
        f.write("{:5s}|{:^5s}{:^5s}{:^5s}{:^5s}{:^6s}{:^6s}\n".\
            format("name", "kor", "eng", "math", "sci", "sum", "avg"))
        f.write("-----+--------------------------------\n")
        for data in data_list:
            s = ""
            s = "{0:<5s}|".format(data[0])
            s += "{0:>4},".format(data[1])
            s += "{0:>4},".format(data[2])
            s += "{0:>4},".format(data[3])
            s += "{0:>4},".format(data[4])
            s += "{0:4d},".format(data[5])
            s += "{0:6.2f}\n".format(data[6])
            f.write(s)
        f.write("======================================\n")
    f.close()

def calculate_scores(data_list):
    kor_avg=0   #각 과목의 평균값을 0으로 초기화
    eng_avg=0
    math_avg=0
    sci_avg=0

    for i in range(len(data_list)): #data_list의 행을 반복문으로 돈다
        #data_list가 2차원 배열이기때문에 행을 돌며 열에 있는 과목값을을 계산한다.
        sum = data_list[i][1]+data_list[i][2]+data_list[i][3]+data_list[i][4]
        avg = (data_list[i][1]+data_list[i][2]+data_list[i][3]+data_list[i][4])/4
        #계산된 값들은 행의 뒤에 append한다.
        data_list[i].append(sum)
        data_list[i].append(avg)
    
    for list in data_list:  #data_list를 돌며 각 과목 점수를 합한다.
        kor_avg += list[1]
        eng_avg += list[2]
        math_avg += list[3]
        sci_avg += list[4]

    #각과목의 점수를 data_list의 행의 갯수만큼 나누어 평균을 구한다.
    kor_avg = kor_avg/len(data_list)
    eng_avg = eng_avg/len(data_list)
    math_avg = math_avg/len(data_list)
    sci_avg = sci_avg/len(data_list)

    return kor_avg, eng_avg, math_avg, sci_avg