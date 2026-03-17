a, b = map(float, input().split())
if a == 0:
    if b == 0:
        print("phuong trinh co vo so nghiem")
    else:
        print("phuong trinh vo nghiem")
else:
    x = -b/a
    print(f'pt co nghiem duy nhat x = {x}')

