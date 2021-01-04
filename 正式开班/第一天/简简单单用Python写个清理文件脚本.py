import os

all_file = []  # 用来装地址的容器


def dir_list(path):
    filenames = os.listdir(path)  # 返回path指定的文件夹包含的文件或文件夹的名字的列表。
    for filename in filenames:  # 遍历这个目录的名字
        filepath = os.path.join(path, filename)  # os.path获取文件的属性信息 并且连接起来
        if os.path.isdir(filepath):  # 判断是否为目录的输出结果
            dir_list(filepath)  # 如果是目录就继续输出此目录的文件或文件夹名字
        else:  # 如果不是的话就添加在allfiles列表里面
            all_file.append(filepath)


def remove(str):
    """
    :param str:是你要删除的文件的特点 比如 这些文件都有‘.+’ 那么就传入'.+'
    :return: 无
    """
    for i in all_file:
        if str in i:
            os.remove(i)


if __name__ == '__main__':
    print(all_file)
    dir_list('E:\\')
    remove('._')
    dir_list('E:\\')
    print(all_file)
