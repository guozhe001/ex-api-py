import os


def delete_file(abs_file_path):
    os.remove(abs_file_path)


def write(abs_file_path, context):
    mkdir_if_not_exists(get_path(abs_file_path))
    data_file = open(abs_file_path, 'a+')
    data_file.write(context)
    data_file.flush()
    data_file.close()


def exists(path):
    return os.path.exists(path)


def read_file(abs_file_path):
    with open(abs_file_path, "r") as f:
        lines = f.readlines()
        f.close()
        return lines


# 根据文件的绝对路径获取文件所在的目录
def get_path(abs_file_path):
    return os.path.dirname(os.path.abspath(abs_file_path))


def mkdir_if_not_exists(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


def cover(abs_file_path, lines):
    delete_file(abs_file_path)
    write(abs_file_path, lines)
