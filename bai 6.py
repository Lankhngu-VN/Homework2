a,b,c,d = map(float, input().split())
max = a
if b > max:
    max = b
if c > max:
    max = c
if d > max:
    max = d
print(f'gia tri lon nhat la {max}')
