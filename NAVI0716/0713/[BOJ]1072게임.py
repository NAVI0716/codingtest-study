import math
x,y=map(int,input().split())
result = math.trunc((y/x)*100)
z_z=0
count=0
start = 1
end =1000000000
if result >= 99:
    count=-1
else:
    while y <= x:
        if z_z > result:
            break
        else:
            count+=1
            x+=1
            y+=1
            z_z=math.trunc(y/x*100)
print(count)