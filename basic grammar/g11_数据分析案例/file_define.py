"""
和文件相关的类定义
"""
from data_define import Record
import json
# 定义一个抽象类做顶层设计，确定具体功能
class FileReader:
    def read_data(self)->list[Record]:
        # 将读到的每一行数据转换为Record对象，封装到list内返回
        pass

class TextFileReader(FileReader):
    def __init__(self,path):# 定义成员变量，记录文件路径
        self.path=path

    # 复写
    def read_data(self) ->list[Record]:
        f=open(self.path,"r",encoding="utf-8")
        record_list=[]
        for line in f.readlines():
            line=line.strip()# 去掉换行符
            record=Record(line.split(",")[0],line.split(",")[1],int(line.split(",")[2]),line.split(",")[3])
            record_list.append(record)
        f.close()
        return record_list


class JsonFileReader(FileReader):
    def __init__(self,path):
        self.path=path
    def read_data(self) ->list[Record]:
        f=open(self.path,"r",encoding="utf-8")
        record_list=[]
        for line in f.readlines():
           data_dict=json.loads(line)
           record=Record(data_dict["date"],data_dict["order_id"],data_dict["money"],data_dict["province"])
           record_list.append(record)
        f.close()
        return record_list


if __name__ == '__main__':
    text_file_reader=TextFileReader("D:/2011年1月销售数据.txt")
    json_file_reader=JsonFileReader("D:/2011年2月销售数据JSON.txt")
    list1=text_file_reader.read_data()
    list2=json_file_reader.read_data()
    for l in list1:
        print(l)
    for l in list2:
        print(l)