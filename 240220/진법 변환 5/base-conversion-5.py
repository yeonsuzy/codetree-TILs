a,b= map(int, input().split())

import string
tmp = string.digits+string.ascii_lowercase
def convert(num,base):
    q,r = divmod(num,base)
    if q==0:
        return tmp[r]
    else:
        return convert(q,base)+tmp[r]

print(convert(a,b))