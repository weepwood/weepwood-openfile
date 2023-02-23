import os
import subprocess
import sys
import re
from urllib.parse import unquote
from tkinter import messagebox

if len(sys.argv) < 2:
    sys.exit(1)

file_path = sys.argv[1].encode('utf-8')
# 将 url 字符串进行解码
file_path = unquote(file_path)

# 去除字符串第一个 : 前的所有字符
# 同一将前缀改成 open: 
# 注意该段代码会导致执行 py openfile.py C:\Users\ 这种命令出错
# 需要添加前缀例如 py openfile.py openfile:\\C:\Users\
file_path = "open:" + file_path.split(':',1)[1]

# 去除前缀 open: open:/ open:// open:\ open:\\
regex = r"open:(?://|/|\\\\|\\)?"
file_path = re.sub(regex, "", file_path)
# 将文件路径 / 统一替换成 \
file_path = file_path.replace('/', '\\')
# 踩坑点 这里 " 会导致文件路径识别错误
file_path = file_path.strip("'\"\\")

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
    messagebox.showerror("Open File", file_path + "\n文件或文件夹不存在 \nThe file or folder does not exist")
    sys.exit(1)