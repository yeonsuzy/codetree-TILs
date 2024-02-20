arr = input()
re = []

for i in range(len(arr)):
    if i%2==1:
        re.append(arr[i])

for i in range(1,len(re)+1):
    print(re[-i], end='')