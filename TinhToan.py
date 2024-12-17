import tkinter as tk
from tkinter import ttk

# Tạo cửa sổ chính
win = tk.Tk()
win.title("Tính toán")

# Tạo Tab toán 
ToanTabs = ttk.Notebook(win)
ToanTabs.grid(column=0, row=0, padx=10, pady=10)



# Hình học
class HinhHoc:
    def __init__(self, tab):
        self.frame = ttk.LabelFrame(tab, text="Hình học")
        self.frame.grid(column=0, row=0, padx=10, pady=10)

        self.canh_value = tk.DoubleVar()
        self.dai_value = tk.DoubleVar()
        self.rong_value = tk.DoubleVar()
        self.bankinh_value = tk.DoubleVar()

        # Hình vuông
        ttk.Label(self.frame, text="Cạnh hình vuông").grid(column=0, row=0, padx=5, pady=5)
        ttk.Entry(self.frame, textvariable=self.canh_value, width=10).grid(column=1, row=0, padx=5, pady=5)
        ttk.Button(self.frame, text="Tính hình vuông \n S = cạnhxcạnh", command=self.tinh_hinh_vuong).grid(column=2, row=0, padx=5, pady=5)

        # Hình chữ nhật
        ttk.Label(self.frame, text="Dài HCN").grid(column=0, row=1, padx=5, pady=5)
        ttk.Entry(self.frame, textvariable=self.dai_value, width=10).grid(column=1, row=1, padx=5, pady=5)
        ttk.Label(self.frame, text="Rộng HCN").grid(column=0, row=2, padx=5, pady=5)
        ttk.Entry(self.frame, textvariable=self.rong_value, width=10).grid(column=1, row=2, padx=5, pady=5)
        ttk.Button(self.frame, text="Tính Hình chữ nhật \n S = DàixRộng", command=self.tinh_hcn).grid(column=2, row=2, padx=5, pady=5)

        # Hình tròn
        ttk.Label(self.frame, text="Bán kính hình tròn").grid(column=0, row=3, padx=5, pady=5)
        ttk.Entry(self.frame, textvariable=self.bankinh_value, width=10).grid(column=1, row=3, padx=5, pady=5)
        ttk.Button(self.frame, text="Tính Hình tròn \n S = 3.14159*R^2 ", command=self.tinh_hinh_tron).grid(column=2, row=3, padx=5, pady=5)

        # Kết quả
        self.ket_qua = ttk.Label(self.frame, text="Kết quả:")
        self.ket_qua.grid(column=0, row=4, padx=5, pady=5, columnspan=3)

    def tinh_hinh_vuong(self):
        canh = self.canh_value.get()
        ketqua = canh ** 2
        self.ket_qua.config(text=f"Kết quả: Diện tích = {ketqua}")

    def tinh_hcn(self):
        dai = self.dai_value.get()
        rong = self.rong_value.get()
        ketqua = dai * rong
        self.ket_qua.config(text=f"Kết quả: Diện tích = {ketqua}")

    def tinh_hinh_tron(self):
        bankinh = self.bankinh_value.get()
        ketqua = 3.14159 * (bankinh ** 2)
        self.ket_qua.config(text=f"Kết quả: Diện tích = {ketqua}")

# Tạo các tab 

tabhinhhoc = ttk.Frame(ToanTabs)


ToanTabs.add(tabhinhhoc, text="Diện tích")


HinhHoc(tabhinhhoc)


win.mainloop()
