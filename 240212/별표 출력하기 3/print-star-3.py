n = int(input())

for i in range(n): 
    # 공백
    for j in range(i):
        print(" ", end=" ")
    
    # 별표 : 행이 1씩 증가함에 따라 별은 2개씩 감소
    for j in range((2*n)-(2*i)-1):
        print("*", end=" ")
    print()