from pymysql import Connection
conn=Connection(
    host="localhost",
    port=3306,
    user="root",
    password="Lc20050612.",
    # autocommit=True# 自动提交事务，不用手动确认
)

# print(conn.get_server_info())# 获取服务器信息(版本)

# 执行非查询性质SQL
cursor=conn.cursor()# 获取游标对象
conn.select_db("demo")# 选择数据库
cursor.execute("create table if not exists test_pymysql(id int);")

# 执行查询性质SQL
cursor.execute("select * from employees;")
res:tuple=cursor.fetchall()# 获取查询结果
for row in res:
    print(row)

# 执行插入
cursor.execute("insert into user(NAME,age,status,gender) values ('aaa',20,1,'男');")
conn.commit()# 手动提交


conn.close()# 关闭连接