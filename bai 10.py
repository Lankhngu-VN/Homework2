import math
def kt():
    xc, yc, r = map(float, input().split())
    if r <= 0:
        print("ban kinh khong duoc am")
        return
    xa, ya = map(float, input().split())
    d = math.sqrt((xa - xc) ** 2 + (ya - yc) ** 2)
    if math.isclose(d, r):
        print("diem A nam tren duong tron")
    elif d<r:
        print("diem A nam trong duong tron")
    else:
        print("diem A nam ngoai duong tron")
kt()