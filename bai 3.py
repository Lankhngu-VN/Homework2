import math
a, b, c = map(float, input().split())
if a+b > c and a+c > b and b+c > a and a > 0 and b > 0 and c > 0:
    loai_tam_giac = ""
    if a == b == c:
        loai_tam_giac = "deu"
    elif a == b or a == c or b == c:
        loai_tam_giac = "can"
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        loai_tam_giac = "vuong"
    else:
        loai_tam_giac = "thuong"
    print(f"loai tam giac: {loai_tam_giac}")
    chu_vi = a + b + c
    print(f"chu vi: {chu_vi}")
    p = chu_vi / 2
    dien_tich = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"dien tich: {dien_tich}")
else:
    print("Khong la ba canh cua mot tam giac")