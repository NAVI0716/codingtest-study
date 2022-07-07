import sys
input = sys.stdin.readline
#초기값
인덱스목록={}
count=0
최종목록=[]

#입력
n=int(input())
목록 = list(map(int,input().split()))
# print(목록)

#정렬
목록정렬 = sorted(목록)
# print(목록정렬)

#딕셔너리로 정렬 인덱스값 지정
for i in 목록정렬:
    if i not in 인덱스목록.keys():
        인덱스목록[i]=count
        count+=1
# print(인덱스목록)

#출력
for i in 목록:
    for j,k in 인덱스목록.items():
        if i == j:
            최종목록.append(k)
print(*최종목록)