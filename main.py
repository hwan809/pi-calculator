# 03-12 pi calculator
import math
import matplotlib.pyplot as plt

N = 1000000

def archimedes():
    new_pi_data = list()

    n = 6 # 정사각형에서 시작
    plt.semilogy(base=100)

    while True:
        degree = 360 / n # 정n각형의 내각 크기``
        theta = math.radians(degree / 2) # 삼각함수 각도
        
        inner_length = math.sin(theta) # 내접하는 정n각형 한 변의 길이
        outer_length = math.tan(theta) # 외접하는 정n각형 한 변의 길이
        
        inner_perimeter = n * inner_length # 내접하는 정n각형의 둘레
        outer_perimeter = n * outer_length # 외접하는 정n각형의 둘레

        new_pi = (outer_perimeter + inner_perimeter) / 2 # 두 정n각형 둘레의 평균
        new_pi_data.append(new_pi - math.pi) # 두 정n각형 둘레의 평균을 리스트에 저장

        n += 1 # n각형의 각 늘리기
        if n == N:
            break
    
    plt.plot(range(6, N), new_pi_data)

archimedes()
plt.show()