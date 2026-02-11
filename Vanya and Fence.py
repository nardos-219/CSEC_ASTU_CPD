n , h = map(int, input().split())
friends = list(map(int, input().split()))
count = 0
for i in range(len(friends)):
    if friends[i] > h:
        count+=2
    else:
        count+=1
print(count)    
