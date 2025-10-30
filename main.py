import tkinter as tk
import random

# 弹窗数量
NUM_WINDOWS = 10
# 每个弹窗的宽高
WIDTH, HEIGHT = 200, 80

def create_popup():
    # 创建独立窗口
    win = tk.Toplevel()
    win.title("♡")
    win.configure(bg="#f8c8d0")  # 粉色背景
    win.geometry(f"{WIDTH}x{HEIGHT}+{random.randint(0, 800)}+{random.randint(0, 500)}")
    win.resizable(False, False)

    # 创建文字标签
    label = tk.Label(win, text="I LOVE YOU!", font=("Arial", 16, "bold"), bg="#f8c8d0", fg="white")
    label.pack(expand=True, fill="both")

    # 5秒后自动关闭
    win.after(5000, win.destroy)

# 主窗口（隐藏）
root = tk.Tk()
root.withdraw()  # 隐藏主窗口

# 连续生成弹窗
for i in range(NUM_WINDOWS):
    root.after(i * 300, create_popup)  # 每隔0.3秒弹出一个

root.mainloop()
