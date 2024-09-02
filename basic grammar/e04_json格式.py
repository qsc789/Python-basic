import json
# 列表或字典转化为字符串
# 列表内每个元素都是字典
data=[{"name":"aaa","age":11},
      {"name":"bbb","age":12},
      {"name":"ccc","age":13}]
json_str=json.dumps(data,ensure_ascii=False)# 帮助正常显示中文
print(json_str)

# 纯字典也行
d={"name":"ddd","age":14}
json_str=json.dumps(d,ensure_ascii=False)
print(json_str)

# 字符串转化为列表或字典
s='[{"name": "aaa", "age": 11}, {"name": "bbb", "age": 12}, {"name": "ccc", "age": 13}]'
print(json.loads(s))
print(type(json.loads(s)))

s='{"name":"ddd","age":14}'
print(json.loads(s))
print(type(json.loads(s)))