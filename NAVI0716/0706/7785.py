import sys
input = sys.stdin.readline
n=int(input())
enterlist= {}
for _ in range(n):
    people = input().split()
    if people[1] == "enter":
        enterlist[people[0]]="enter"
    else:
        del enterlist[people[0]]
result= sorted(enterlist.keys(),reverse=True)
for i in result:
    print(i)