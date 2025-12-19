"""ex1_calc.py
Máy tính đơn giản: nhập 2 số và in ra tổng/hiệu/tích/thương.
Gợi ý: chạy trực tiếp hoặc gọi từ notebook bằng: %run ex1_calc.py
"""

def read_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Bạn nhập chưa phải số. Thử lại nhé.")

def main():
    a = read_number("Nhập a: ")
    b = read_number("Nhập b: ")

    print("\nKết quả:")
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    if b == 0:
        print("a / b = (không chia được vì b = 0)")
    else:
        print(f"a / b = {a / b}")

if __name__ == "__main__":
    main()
