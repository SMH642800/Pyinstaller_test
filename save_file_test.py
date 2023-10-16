import os

# 获取用户的文档目录
user_documents = os.path.expanduser("~\\Documents")

# 构建文件路径
location = os.path.join(user_documents, "myAppTest", "configuration")
file_path = os.path.join(location, "mydata.txt")

# 确保目录存在
os.makedirs(location, exist_ok=True)

# 写入文件
with open(file_path, "w") as file:
    file.write("This is some data that you want to save.")

print(f"File saved at: {file_path}")