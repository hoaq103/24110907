class TuLanh:
    def __init__(self, nhanhieu="Elextrolux", maso="UNKNOWN", nuocsx="Việt Nam", tkdien=True, dungtich=256, gia=7000000):
        self.__nhanhieu = nhanhieu
        self.__maso = maso
        self.__nuocsx = nuocsx
        self.__tkdien = tkdien
        self.__dungtich = dungtich
        self.__gia = gia

    def makeCopy(self, tl):
        self.__nhanhieu = tl.__nhanhieu
        self.__maso = tl.__maso
        self.__nuocsx = tl.__nuocsx
        self.__tkdien = tl.__tkdien
        self.__dungtich = tl.__dungtich
        self.__gia = tl.__gia

    def nhapThongTin(self):
        self.__nhanhieu = input()
        self.__maso = input()
        self.__nuocsx = input()
        self.__tkdien = input().strip().lower() == "true"
        self.__dungtich = int(input())
        self.__gia = int(input())

    def hienThi(self):
        print(f"Nhãn hiệu: {self.__nhanhieu}")
        print(f"Mã số: {self.__maso}")
        print(f"Nước sản xuất: {self.__nuocsx}")
        print(f"Tiết kiệm điện: {'Có' if self.__tkdien else 'Không'}")
        print(f"Dung tích: {self.__dungtich} lít")
        print(f"Giá bán: {format(self.__gia, ',')} VNĐ")

    def layNhanHieu(self):
        return self.__nhanhieu

    def layGia(self):
        return self.__gia

    def soNguoiSD(self):
        return self.__dungtich // 100

    def cungNhanHieu(self, tl):
        return self.__nhanhieu == tl.__nhanhieu

    def nhHon(self, tl):
        return self.__dungtich < tl.__dungtich


# Phần kiểm thử và nhập dữ liệu
if __name__ == "__main__":
    print("Nhập thông tin cho tủ lạnh thứ nhất (tu1):")
    tu1 = TuLanh()
    tu1.nhapThongTin()

    print("\nNhập thông tin cho tủ lạnh thứ hai (tu2):")
    tu2 = TuLanh()
    tu2.nhapThongTin()

    print("\n--- Thông tin tủ lạnh thứ nhất ---")
    tu1.hienThi()

    print("\n--- Thông tin tủ lạnh thứ hai ---")
    tu2.hienThi()

    print(f"\nSố người dùng phù hợp với tu2: {tu2.soNguoiSD()}")
    print("Cùng nhãn hiệu?", tu1.cungNhanHieu(tu2))
    print("Tu1 nhỏ hơn tu2?", tu1.nhHon(tu2))
class C002454:
    def testCase1(self):
        print("=== Test Case 1 ===")
        print("Nhập thông tin cho tủ lạnh tl1:")
        tl1 = TuLanh()
        tl1.nhapThongTin()

        tl2 = TuLanh("LG", "LG-28382", "Hàn Quốc", True, 600, 43000000)
        print("\nThông tin tl2:")
        tl2.hienThi()

        tl3 = TuLanh()
        tl3.makeCopy(tl1)
        print("\nThông tin tl3 (sao chép từ tl1):")
        tl3.hienThi()
        print()

    def testCase2(self):
        print("=== Test Case 2 ===")
        n = int(input("Nhập số lượng tủ lạnh: "))
        ds = []
        for i in range(n):
            print(f"\nNhập thông tin tủ lạnh thứ {i+1}:")
            t = TuLanh()
            t.nhapThongTin()
            ds.append(t)

        print("\nDanh sách tủ lạnh (ngược thứ tự nhập):")
        for t in reversed(ds):
            t.hienThi()
        print()

    def testCase3(self):
        print("=== Test Case 3 ===")
        n = int(input("Nhập số lượng tủ lạnh: "))
        ds = []
        for i in range(n):
            print(f"\nNhập thông tin tủ lạnh thứ {i+1}:")
            t = TuLanh()
            t.nhapThongTin()
            ds.append(t)

        ds.sort(key=lambda x: x.layGia(), reverse=True)

        print("\nDanh sách tủ lạnh (giá giảm dần):")
        for t in ds:
            t.hienThi()
        print()

    def testCase4(self):
        print("=== Test Case 4 ===")
        n = int(input("Nhập số lượng tủ lạnh: "))
        ds = []
        for i in range(n):
            print(f"\nNhập thông tin tủ lạnh thứ {i+1}:")
            t = TuLanh()
            t.nhapThongTin()
            ds.append(t)

        # Lưu vào file văn bản (không dùng json)
        with open("DsTuLanh.txt", "w", encoding="utf-8") as f:
            for t in ds:
                f.write(f"{t._TuLanh__nhanhieu}\n{t._TuLanh__maso}\n{t._TuLanh__nuocsx}\n{t._TuLanh__tkdien}\n{t._TuLanh__dungtich}\n{t._TuLanh__gia}\n")

        print("\nDanh sách đã lưu vào file DsTuLanh.txt\n")

    def testCase5(self):
        print("=== Test Case 5 ===")
        n = int(input("Nhập số lượng tủ lạnh: "))
        ds = []
        for i in range(n):
            print(f"\nNhập thông tin tủ lạnh thứ {i+1}:")
            t = TuLanh()
            t.nhapThongTin()
            ds.append(t)

        thongke = {}
        for t in ds:
            nh = t.layNhanHieu()
            if nh in thongke:
                thongke[nh] += 1
            else:
                thongke[nh] = 1

        print("\nThống kê số lượng theo nhãn hiệu:")
        for nh in sorted(thongke):
            print(f"{nh} ({thongke[nh]})")
        print()

    def main(self):
        self.testCase1()
        self.testCase2()
        self.testCase3()
        self.testCase4()
        self.testCase5()
C002454().main()
