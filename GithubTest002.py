import os
import numpy as np
import clsSensing
import FileControl


data_folder = "D:/Project Python/002 PycharmGithubTest/BOTDR실험181010"
data_file_name = "Raw data.txt"
file_list = FileControl.find_all_files(data_folder, data_file_name)

ss = []

for fn in file_list:
    ss.append(clsSensing.Sensing(fn))

ss[3].show_graph_simple()
ss[4].show_graph_simple()
ss[5].show_graph_simple()
ss[6].show_graph_simple()

ss[7].show_graph_simple()


# list_data_file = file_all_botdr_data_files(data_folder)
# s1 = clsSensing.Sensing("D:/Project Python/002 PycharmGithubTest/BOTDR실험181010/2-0/2018-10-10 오후 3-46-09\\Raw data.txt")
# s1.show_graph_simple()

# s1 = clsSensing.Sensing(list_data_file[0])
# s2 = clsSensing.Sensing("Raw data - 복사본.txt")
# s1.show_graph_paper_style()
# s2.show_graph_paper_style()

# ReadBotdrData(s1, BOTDR_DataFileName)


def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        print(full_filename)


def read_first_line(fn):
    f = open(fn, 'r')
    line = f.readline()
    print(line)
    f.close()


def read_all_lines(FN):
    f = open(BOTDR_DataFileName, 'r')
    while True:
        line = f.readline()
        if not line:
            break
        print(line)
    f.close()


def ReadAllLines2(FN):
    f = open(BOTDR_DataFileName, 'r')
    lines = f.readlines()
    for line in lines:
        print(line)
    f.close()


def ReadValues(FN):
    with open(FN, 'r') as f:
        title = f.readline()
        # print(title)
        data = f.readlines(1)
        for line in data:
            line = line.strip()
            for number in line.split():
                print(number)
        #    line = line.strip()
        #    for number in line.split():
        #        yield float(number)


# nparray 예제
def nparray_example():
    # 1차원 배열 만들기
    data = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    answer = data * 2
    print(answer)
    print(answer[0]), print(answer[1]), print(answer[9])

    # 벡터화 연산
    eqs = data == 2
    print(eqs)

    # 2차원 배열 만들기
    c = np.array([[0, 1, 2], [3, 4, 5]])  # 2x3 array
    print(c)
    print('nRow =', len(c))  # 행의 갯수
    print('nCol =', len(c[0]))  # 열의 갯수

    # 배열의 차원과 크기 쿼리
    print('ar.ndim =', c.ndim)
    print('ar.shape =', c.shape)
    print(c[1, 1])
    print(c[0, :])  # 첫번째 행 전체
    print(c[0, 1:3])












