import os
import subprocess
import sys
import re
from urllib.parse import unquote
from tkinter import messagebox

if len(sys.argv) < 2:
    messagebox.showinfo("Open File", "未指定文件路径")
    sys.exit(1)

file_path = sys.argv[1].encode('utf-8')
# 将 url 字符串进行解码
file_path = unquote(file_path)

# 去除字符串第一个 : 前的所有字符,并将前缀同一改成 open: 
file_path = "open:" + file_path.split(':',1)[1]

# 去除前缀 open:、open:/、open://、open:\、open:\\
regex = r"open:(?://|/|\\\\|\\)?"
file_path = re.sub(regex, "", file_path)
# 去除路径前后的（'、"、\、‘、’、“、”）会导致文件路径识别错误
file_path = file_path.strip("'\"\\‘’“”")
# 规范化路径
file_path = os.path.normpath(file_path)


# debugger
# print(sys.argv[1])
# print('----------------')
# print(file_path)

try:
    # 如果文件不存在，则抛出异常
    if not os.path.exists(file_path):
        raise FileNotFoundError
    # 使用 Windows 资源管理器打开文件
    subprocess.run(['explorer.exe', file_path])

except FileNotFoundError:
    # 文件不存在，打印错误信息并退出程序
    # 弹出错误窗口
    messagebox.showinfo("Open File", file_path + "\n文件或文件夹不存在")
    sys.exit(1)