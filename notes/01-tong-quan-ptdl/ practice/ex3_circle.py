"""ex3_circle.py
Tính chu vi và diện tích hình tròn khi biết bán kính r.
"""
import math

def circle_area(r: float) -> float:
    return math.pi * r * r

def circle_circumference(r: float) -> float:
    return 2 * math.pi * r

def main():
    while True:
        try:
            r = float(input("Nhập bán kính r: "))
            if r < 0:
                print("r phải >= 0. Thử lại nhé.")
                continue
            break
        except ValueError:
            print("Bạn nhập chưa phải số. Thử lại nhé.")

    area = circle_area(r)
    c = circle_circumference(r)

    print("\nKết quả:")
    print(f"Chu vi = {c}")
    print(f"Diện tích = {area}")

if __name__ == "__main__":
    main()
