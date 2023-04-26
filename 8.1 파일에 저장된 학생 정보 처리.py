# Homework 8.2 - Application Program of myClassMtrx
from Class_Mtrx import * # 본인이 작성한 Class_Mtrx, 보고서에 함께 제출할 것.
def main():
    fin = open("matrix_data.txt", "r")
    fout = open("result.txt", "w")
    mA = fgetMtrx(fin); mA.setName("mA"); print(mA); fout.write("{}".format(mA))
    mB = fgetMtrx(fin); mB.setName("mB"); print(mB); fout.write("{}".format(mB))
    mC = fgetMtrx(fin); mC.setName("mC"); print(mC); fout.write("{}".format(mC))
    fin.close()
    mD = mA + mB
    mD.setName("mD = mA + mB")
    print(mD); fout.write("{}".format(mD))
    mE = mA - mB
    mE.setName("mE = mA - mB")
    print(mE); fout.write("{}".format(mE))
    mF = mA * mC
    mF.setName("mF = mA * mB")
    print(mF); fout.write("{}".format(mF))
    fout.close()
if __name__ == "__main__":
    main()