class Mtrx:
    def __init__(self, name, n_row, n_col, L_data): #생성자
        #최초 클래스/인스탄스 속성의 초기값 설정
        self.name=name
        self.n_row=n_row
        self.n_col=n_col
        self.L_data=L_data

    def setName(self, name): # 변경자
        #클래스/인스탄스 속성의 값 변경
        self.name=name

    def __str__(self): # 행렬의 출력, return은 string 타입
        #self.name을 출력
        str=self.name+" = "
        #반복문을 통해 L_data의 원소들을 str에 추가
        for i in range(len(self.L_data)):
            #행이 바뀔때 줄바꿈
            if i%self.n_col==0:
                str += "\n"
            #format지정
            str += "{:6.2f}".format(self.L_data[i])
        str += "\n"
        return str
    
    def __add__(self, other): # 직접 구현, operator overloading of '+'
        #두 리스트를 반복문으로 돌며 덧셈값을 새로운 리스트에 추가
        result_data=[]
        for i in range(len(self.L_data)):
            result_data.append(self.L_data[i]+other.L_data[i])
        #return은 Mtrx클래스형식
        return Mtrx(self.name, self.n_row, self.n_col, result_data)
        
    def __sub__(self, other): # 직접 구현, operator overloading of '-'
        #두 리스트를 반복문으로 돌며 뺄셈값을 새로운 리스트에 추가
        result_data=[]
        for i in range(len(self.L_data)):
            result_data.append(self.L_data[i]-other.L_data[i])
        #return은 Mtrx클래스형식
        return Mtrx(self.name, self.n_row, self.n_col, result_data)

    def __mul__(self, other): # 직접 구현, operator overloading of '*'
        #행렬 곱셈을 하기전 조건을 만족하는지 검사
        if self.n_col != other.n_row:
            return None
        
        #행렬 곱셈
        result_data=[]
        for i in range(self.n_row):
            for j in range(other.n_col):
                temp_val=0
                for k in range(self.n_col):
                    temp_val += self.L_data[i*self.n_col+k]*other.L_data[k*other.n_col+j]
                result_data.append(temp_val)
        #행렬곱을 했기때문에 행은 self의 n_row가 되고 열은 other의 n_col가 되어야한다.
        return Mtrx(self.name, self.n_row, other.n_col, result_data)


def fgetMtrx(fin):
    size = fin.readline().split() # 파일에서 행렬의 크기 정보를 읽어옴
    rows = int(size[0])
    cols = int(size[1])

    L_data = [] #데이터 리스트 생성

    for i in range(rows):
        row = fin.readline().split()
        for j in range(cols):
            L_data.append(float(row[j]))

    return Mtrx("temp" ,rows, cols, L_data) #Mtrx객체형태로 return
