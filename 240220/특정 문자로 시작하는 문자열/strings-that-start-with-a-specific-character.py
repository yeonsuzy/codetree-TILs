n = int(input())
arr = []

for i in range(n):
    arr_new = input()
    arr.append(arr_new)
w = input()

cnt = 0
lg = 0

for i in arr:
    for j in i:
        if j==w:
            cnt+=1
            lg+=len(i)
lg = round((lg/cnt),3)
print(cnt, f"{lg:.2f}")