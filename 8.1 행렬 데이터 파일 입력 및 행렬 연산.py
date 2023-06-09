# HW 8.2 Student data processing with text file input/output
from St_Data_Process import *
########################################### Application
def main():
    L_st_data = fread_data("st_records.txt")
    for st in L_st_data:
        print(st)
    kor_avg, eng_avg, math_avg, sci_avg = calculate_scores(L_st_data)
    print("\nAfter calculate_scores(students)")
    print("======================================")
    print("{:5s}|{:^5s}{:^5s}{:^5s}{:^5s}{:^6s}{:^6s}".\
        format("name", "kor", "eng", "math", "sci", "sum", "avg"))
    print("-----+--------------------------------")
    for data in L_st_data:
        s = ""
        s = "{0:<5s}|".format(data[0])
        s += "{0:>4},".format(data[1])
        s += "{0:>4},".format(data[2])
        s += "{0:>4},".format(data[3])
        s += "{0:>4},".format(data[4])
        s += "{0:4d},".format(data[5])
        s += "{0:6.2f}".format(data[6])
        print(s)
    print("======================================")
    fwrite_data("output.txt", L_st_data)
    print("\nAverage score of each class :")
    print("Kor_avg = {:5.2f}".format(kor_avg))
    print("Eng_avg = {:5.2f}".format(eng_avg))
    print("Math_avg = {:5.2f}".format(math_avg))
    print("Sci_avg = {:5.2f}".format(sci_avg))

if __name__ == "__main__":
    main()