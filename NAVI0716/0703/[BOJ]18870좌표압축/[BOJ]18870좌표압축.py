#입력
n=int(input())
목록 = list(map(int,input().split()))

#정렬
목록정렬 = sorted(목록)

인덱스목록={}
count=0
최종목록=[]
#딕셔너리로 정렬 인덱스값 지정
for i in 목록정렬:
    if i not in 인덱스목록.keys():
        인덱스목록[i]=count
        count+=1

#출력
for i in 목록:
    for j,k in 인덱스목록.items():
        if i == j:
            최종목록.append(k)
print(*최종목록)