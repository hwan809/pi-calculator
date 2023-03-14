# pi-calculator
원주율의 근사치를 구하는 아르키메데스 방법을 구현, 시각화.

## Archimedes
### 원리
<img src="https://user-images.githubusercontent.com/55339366/224528149-05ea444b-2781-44c0-99f8-bc921ab82bf6.png" width="30%" height="30%"/>
한 원에 외접하고 내접하는 정n각형을 그려 이를 원주율의 범위로 사용.

### 정n각형의 둘레를 구하는 법
![image_7235874611524232667890](https://user-images.githubusercontent.com/55339366/224528384-bc32d33e-20bc-4675-9f7e-c736c58244b4.jpg)

삼각함수를 이용해서 구할 수 있음.

### Code
```ruby
while True:
    degree = 360 / n # 정n각형의 내각 크기
    theta = math.radians(degree / 2) # 삼각함수 각도
        
    inner_length = math.sin(theta) # 내접하는 정n각형 한 변의 길이
    outer_length = math.tan(theta) # 외접하는 정n각형 한 변의 길이
        
    inner_perimeter = n * inner_length # 내접하는 정n각형의 둘레
    outer_perimeter = n * outer_length # 외접하는 정n각형의 둘레

    new_pi = (outer_perimeter + inner_perimeter) / 2 # 두 정n각형 둘레의 평균
    new_pi_data.append(new_pi - math.pi) # (두 정n각형 둘레의 평균 - 실제 원주율)을 리스트에 저장

    n += 1 # n각형의 각 늘리기
    if n == N
```

## 시각화
matplotlib 모듈을 활용해 n각형이 변해감에 따라 pi값의 오차를 그래프로 기록
정n각형의 최대 n (N) = 10^6으로 고정

### Figure_1
![Figure_1](https://user-images.githubusercontent.com/55339366/224556532-3e7ba379-f5a4-4be7-924e-76dd820699d3.png)
초반에 오차가 급격히 감소한 후 큰 변화 없음.

### Figure_2
y축(error) scale을 base=100의 log scale로 고정.

![Figure_2](https://user-images.githubusercontent.com/55339366/224557531-b593b2a2-60b3-49a8-a47b-b14d259956ed.png)
오차가 급격히 줄어들다가 점점 완만해지는 개형을 관찰할 수 있었음.

### Figure_3
base=100의 loglog plot.
![Figure_3](https://user-images.githubusercontent.com/55339366/224557026-c0e01a7c-30c7-48c7-9378-ef3ee7118490.png)
선형적인 개형을 보임.

> 정x각형과 그로 구한 파이값의 오차 y에서  
> 두 변수 x과 y는 loglog plot에서 **선형적인 관계** 임을 알 수 있음.  
> 이는 x과 y가 y = ax^n의 형태로 근사될 수 있음을 뜻함.

## 다른 방법은 없나요?
### inverse tangent
#### 원리
역삼각함수의 테일러 급수 전개.

#### Code
```ruby
new_pi = 0
now_denominator = 1

n = 0

while n < N:
    new_pi += 4 / now_denominator * (-1) ** n
    new_pi_data.append(abs(new_pi - ABSOULTE_PI))

    now_denominator += 2
    n += 1

plt.plot(new_pi_data)
```

### 두 방식을 비교하면
#### Figure_4
![Figure_4](https://user-images.githubusercontent.com/55339366/224998053-20e0195a-ccdc-4670-aea1-35c490485d66.png)
둘 모두 선형적으로 오차가 감소하나,  
아르키메데스의 방법을 이용해 구한 오차가 arctan의 오차에 비해 더 빠르게 감소하고 있는 것을  
기울기를 통해 알 수 있다.

## 결론
아르키메데스의 방법은 정n각형의 n이 증가할수록 오차가 감소하며,  
두 변수 사이에는 power relationship이 존재함을 알 수 있다.   
inverse tangent의 무한급수도 항의 개수에 대해 위와 같은 관계이나,  
아르키메데스의 방법보다 실제 값에 느리게 다가감을 학인할 수 있었다.

## 추가 연구
- 더 효율적인 원주율 계산 알고리즘
- 두 방법에 대한 시간복잡도 계산
- log-log plot으로 근사한 그래프 식 구하기 (기울기 등..)
- 병렬 처리 시스템에서의 계산 속도 차이 (단순 계산이므로 더 빠를 수 있다)

## References
- [EBS 끝없는 신비, π (2부)](https://www.ebsmath.co.kr/resource/rscView?cate=10098&cate2=10176&cate3=10189&rscTpDscd=RTP10&grdCd=MGRD01&sno=21255&historyYn=study&movieInLec=RC2)
- [log-log scale graph](https://en.wikipedia.org/wiki/Log%E2%80%93log_plot)
- [Approximating Pi with Inscribed Polygon](https://demonstrations.wolfram.com/ApproximatingPiWithInscribedPolygons/)
- [Liu Hui's pi algorithm](https://en.wikipedia.org/wiki/Liu_Hui%27s_%CF%80_algorithm)
