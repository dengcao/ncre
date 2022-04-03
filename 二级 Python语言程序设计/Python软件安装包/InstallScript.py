import os
libs = ["future-0.16.0.tar.gz", "pefile-2018.8.8.tar.gz",\
        "jieba-0.39.zip", "PyInstaller-3.3.1.tar.gz"]
try:
    for lib in libs:
        os.system("pip install "+lib)
    print("安装成功！")        
except:
    print("安装失败，请重试")
