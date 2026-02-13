n = int(input())
grouped_m = 1
previous_m = input().strip()

for i in range(1,n):
    current_m = input().strip()
    if current_m != previous_m:
        grouped_m += 1
    previous_m = current_m

print(grouped_m)
