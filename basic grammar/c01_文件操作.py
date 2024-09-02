# 以下print单独运行

f=open("D:\测试.txt","r",encoding="utf-8")# r:只读，w:只写，a:追加
print(type(f))
print(f.read(10))# 读取10个字节的结果
print(f.read())# 从上次读完的地方开始读取剩余所有内容
print(f.readlines())# 读取所有行，并返回列表
print(f.readline())# 读取一行
for line in f:
    print(line)
f.close()


with open("D:\测试.txt","w",encoding="utf-8") as f:# 这种方式打开不用关闭文件
    f.write("hello world\n")# 写入时，文件存在则清空内容
    f.flush()# 内容刷新