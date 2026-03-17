a,b,c,d = map(float, input().split())
min = a
if b < min:
    min = b
if c < min:
    min = c
if d < min:
    min = d
print(f'gia tri nho nhat la {min}')
