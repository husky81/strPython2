import os
import numpy as np  # Python에서 배열을 사용하기 위한 표준 패키지 NumPy

def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        print(full_filename)
def ReadFirstLine(FN):
    f = open(FN, 'r')
    line = f.readline()
    print(line)
    f.close()
def ReadAllLines(FN):
    f = open(BOTDR_DataFileName, 'r')
    while True:
        line = f.readline()
        if not line: break
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
def nparrayexample():
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

# search("c:/")
BOTDR_DataFileName = "Raw data.txt"
# Length = []

# ReadFirstLine(BOTDR_DataFileName)

# ReadValues(BOTDR_DataFileName)
nparrayexample()




























