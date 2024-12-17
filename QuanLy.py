import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import psycopg2

def connect_db(): 
    try:
        # Kết nối tới cơ sở dữ liệu PostgreSQL
        conn = psycopg2.connect(
            dbname="QuanLy",
            user="postgres",
            password="Truc111213@",
            host="localhost", 
            port="5432"
        )
        print("Kết nối cơ sở dữ liệu thành công!")
        return conn
    except Exception as e: 
        print(f"Không thể kết nối tới cơ sở dữ liệu: {e}")
        return None 

# Hàm kết nối
conn = connect_db()

# Hàm để lưu thông tin sinh viên vào cơ sở dữ liệu
def insert_student():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            # Lấy dữ liệu từ các ô nhập liệu
            name = entry_name.get()
            student_id = entry_id.get()
            password = entry_password.get()
            
            # thêm dữ liệu vào bảng 
            sql = "INSERT INTO QuanLySinhVien (MaSo, TenNguoiDung, MatKhau) VALUES (%s, %s, %s)"
            cursor.execute(sql, (student_id, name, password))
            conn.commit()   
            messagebox.showinfo("Thành công", "Dữ liệu đã được nhập thành công!")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể nhập dữ liệu: \n{e}")
        finally:
            cursor.close()
            conn.close()
    else:
        messagebox.showerror("Lỗi", "Không thể kết nối tới cơ sở dữ liệu.")

# Tạo giao diện Tkinter
win = tk.Tk()
win.title("Nhập thông tin sinh viên")

# Tạo LabelFrame mighty
mighty = ttk.LabelFrame(win, text="Thông tin sinh viên")
mighty.grid(column=0, row=0, padx=10, pady=10)

# Các nhãn và ô nhập liệu bên trong mighty
tk.Label(mighty, text="Tên sinh viên:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(mighty)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(mighty, text="Mã số sinh viên:").grid(row=1, column=0, padx=10, pady=5)
entry_id = tk.Entry(mighty)
entry_id.grid(row=1, column=1, padx=10, pady=5)

tk.Label(mighty, text="Mật khẩu:").grid(row=2, column=0, padx=10, pady=5)
entry_password = tk.Entry(mighty, show="*")
entry_password.grid(row=2, column=1, padx=10, pady=5)

# Nút nhập
btn_submit = tk.Button(mighty, text="Nhập", command=insert_student)
btn_submit.grid(row=3, columnspan=2, pady=10)

win.mainloop()
