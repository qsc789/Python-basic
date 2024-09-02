f=open("D:/test.txt","a",encoding="utf-8")# 模式为a
f.write("hello world\n")
f.flush()
f.close()


f=open("D:/test.txt","a",encoding="utf-8")
f.write("hhhh\n")
f.flush()
f.close()