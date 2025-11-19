# 将用户名和密码 按行多次写入csv文件中
import csv
import os


def reg(username, password):
    # 判断当前文件夹下是否存在user.csv
    if not os.path.exists('user.csv'):
        with open('user.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            # 可选：写入表头 writer.writerow(['username', 'password'])
            pass
    # 获取文件内容 判断用户名是否存在  如果存在 返回false
    with open('user.csv', 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            if line and line[0] == username:
                print(username, '用户名已存在')
                return False
    with open('user.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([username, password])
        print(username, '注册成功')
        return True

# 获取csv文件信息   然后对比你传入的数据  如果存在 返回true


def login(username, password):
    with open('user.csv', 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            if line[0] == username and line[1] == password:
                print(username, '登录成功')
                return True
        print(username, '登录失败')
        return False

# 获取csv文件的信息 然后通过username 找到这条数据 改变password的值
# 然后再次存入user.csv
def change_password(username, new_password):
    with open('user.csv', 'r') as f:
        reader = csv.reader(f)
        lines = list(reader)
        for i in range(len(lines)):
            print(lines[i][0] == username)
            if lines[i][0] == username:
                lines[i][1] = new_password
                with open('user.csv', 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(lines)
                print(username, '修改密码成功')
                return True
        print(username, '修改密码失败')
        return False

# 调用注册的函数
reg('admin', '123456')
reg('11', '123456')