from bai1 import Point  # Đảm bảo bạn đặt file này tên là bai11.py

class ColorPoint(Point):
    def __init__(self, *args):
        if len(args) == 0:
            super().__init__()
            self.__color = "xanh"
        elif len(args) == 3:
            x, y, color = args
            super().__init__(x, y)
            self.__color = color
        elif len(args) == 1 and isinstance(args[0], ColorPoint):
            cp = args[0]
            super().__init__(cp.getX(), cp.getY())
            self.__color = cp.getColor()

    def read(self):
        while True:
            try:
                data = input("Nhập x y color (ví dụ: 3 4 xanh): ").split()
                if len(data) != 3:
                    raise ValueError("Phải nhập đúng định dạng: x y color")

                x = int(data[0])  # Nếu data[0] là &, sẽ bị lỗi ở đây
                y = int(data[1])
                color = data[2]
                self.setXY(x, y)
                self.__color = color
                break
            except ValueError as e:
                print("Lỗi:", e)
                print("Vui lòng nhập lại đúng định dạng (ví dụ: 3 4 xanh)")

        

    def print(self):
        print(f"({self.getX()}, {self.getY()}): {self.__color}")

    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

    @property
    def color(self):  # Cho phép dùng c.color
        return self.__color

    @color.setter
    def color(self, value):  # Cho phép gán c.color = "trắng"
        self.__color = value

    def setXY(self, x, y):  # Bổ sung để hỗ trợ setXY giống yêu cầu
        self._Point__x = x
        self._Point__y = y
c = ColorPoint()
print("color:", c.color)  # xanh

c2 = ColorPoint(5, 10, "cyan")
print("x:", c2.getX())
print("y:", c2.getY())
print("color:", c2.color)

c3 = ColorPoint()
c3.read()  # Nhập ví dụ: 3 4 đỏ
c3.print()

c4 = ColorPoint()
c4.setXY(5, 7)
c4.color = "white"
c4.print()  # (5, 7): white
class C002454:
    def testCase1(self):
        print("=== Test Case 1 ===")
        A = ColorPoint(5, 10, "trắng")
        A.print()

    def testCase2(self):
        print("=== Test Case 2 ===")
        B = ColorPoint()
        B.read()
        B.move(10, 8)
        B.print()

    def testCase3(self):
        print("=== Test Case 3 ===")
        C = ColorPoint(6, 3, "đen")
        D = ColorPoint(C)
        D.print()
        D.setColor("vàng")
        D.print()
        C.print()

    def main(self):
        self.testCase1()
        self.testCase2()
        self.testCase3()
if __name__ == "__main__":
    test = C002454()
    test.main()


