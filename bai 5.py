a, b, c = map(float, input().split())
if a == 0:
    if b == 0:
        if c == 0:
            print("phuong trinh co vo so nghiem")
        else:
            print("pt vo nghiem")
    else:
        x = -c/b
        print(f'pt co nghiem duy nhat x = {x}')
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("pt vo nghiem")
    elif delta == 0:
        x = -b/(2*a)
        print(f'pt co nghiem kep x = {x:.2f}')
    elif delta > 0:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        print(f'pt co 2 nghiem phan biet x1 = {x1:.2f} va x2 = {x2:.2f}')

