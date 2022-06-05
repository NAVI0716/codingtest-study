# 2530. 인공지능 시계
[문제](https://www.acmicpc.net/problem/8958)

KOI 전자에서는 건강에 좋고 맛있는 훈제오리구이 요리를 간편하게 만드는 인공지능 오븐을 개발하려고 한다. 인공지능 오븐을 사용하는 방법은 적당한 양의 오리 훈제 재료를 인공지능 오븐에 넣으면 된다. 그러면 인공지능 오븐은 오븐구이가 끝나는 시간을 초 단위로 자동적으로 계산한다. 

또한, KOI 전자의 인공지능 오븐 앞면에는 사용자에게 훈제오리구이 요리가 끝나는 시각을 알려 주는 디지털 시계가 있다.  

훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 초 단위로 주어졌을 때, 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.

### 입력
첫째 줄에는 현재 시각이 나온다. 현재 시각은 시 A (0 ≤ A ≤ 23), 분 B (0 ≤ B ≤ 59)와 초 C (0 ≤ C ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다. 두 번째 줄에는 요리하는 데 필요한 시간 D (0 ≤ D ≤ 500,000)가 초 단위로 주어진다.

```
# 입력 예시
14 30 0
200
```



### 출력
첫째 줄에 종료되는 시각의 시, 분, 초을 공백을 사이에 두고 출력한다. (단, 시는 0부터 23까지의 정수이며, 분, 초는 0부터 59까지의 정수이다. 디지털 시계는 23시 59분 59초에서 1초가 지나면 0시 0분 0초가 된다.)

```
#출력 예시
14 33 20
```



### 풀이

입력예제 하나만 보고 날빌로 풀었다가 틀렸습니다.

그 다음엔 틀리기 싫어서 아예 꼼꼼하게 필터에 필터를 걸쳐 풀었습니다.

```python

# 입력
h, m, s = map(int, input().split()) # 현재 시, 분, 초
t = int(input()) # 초 단위

# 계산
plus_h = 0
plus_m = 0
plus_s = 0

if t >= 3600: # 한 시간보다 크면
    plus_h += t // 3600 # 3600초로 나눈 값 plus_h에 저장
    t = t % 3600 # 3600으로 나눈 나머지 t.

if t >= 60: # 1분보다 크면
    plus_m += t // 60 # 60초로 나눈 값 plus_m에 저장
    t = t % 60 # 60으로 나눈 나머지 t.

plus_s += t # 이후 초 - 분 - 시 순으로 더해주고, 
		   #60 넘으면 상위 단위+1 하는 식으로

s += plus_s
if s >= 60:
    s = s % 60
    plus_m += 1

m += plus_m
if m >= 60:
    m = m % 60
    plus_h += 1

h += plus_h
if h >= 24:
   while h >= 24:
       h = h % 24


# 출력
print(h,m,s)
```