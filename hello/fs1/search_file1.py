
import os, sys, re

newdir = ""


# 递归搜索函数
def search(rootdir, searchdirname):
    if os.path.isdir(rootdir):
        # print rootdir
        # 分离路径和文件夹
        split1 = os.path.split(rootdir)
        # print split1[1]

        # 判断是否为指定的文件夹
        if split1[1] == searchdirname:
            print("找到文件夹：",rootdir)
            try:
                # 将文件夹名称改为新的文件夹名称
                os.rename(rootdir, split1[0] + "\\" + newdir)
                print()
                "文件夹 [%s] 已改名为 [%s]" % (rootdir, newdir)
            except:
                pass

                # 遍历指定文件夹下的内容（文件和文件夹列表）
        listnew = os.listdir(rootdir)

        for l1 in listnew:
            path = rootdir + "\\" + l1
            # 递归调用
            search(path, searchdirname)
    else:
        # print '不是文件夹：%s' % (rootdir)
        return

        # 搜索指定格式的文件


def find_file_by_pattern(pattern, base):
    '''''查找给定文件夹下面所有 '''
    re_file = re.compile(pattern)
    if base == ".":
        base = os.getcwd()

    final_file_list = []
    # print base
    cur_list = os.listdir(base)
    for item in cur_list:
        print()
        item
        full_path = os.path.join(base, item)
        if full_path.endswith(pattern):  # 不能写成单引号，单引号达不到预期的效果
            # print full_path
            # bfile = os.path.isfile(item)
            if os.path.isfile(full_path):
                if re_file.search(full_path):
                    print()
                    re_file.search(full_path).group()
                    final_file_list.append(full_path)
            else:
                final_file_list += find_file_by_pattern(pattern, full_path)
                # for filename in re_file.findall(final_file_list):
                # print filename
        else:
            continue
    return final_file_list


def serchDir(startdir, dirname):
    search(startdir, dirname)


if __name__ == '__main__':
    root = input("输入搜索目录:")
    key = input("输入待搜索的文件夹名称:")
    # newdir = raw_input("文件夹改名为：")
    # serchDir(root,key)
    base = "".join([root, key])
    fileName = input("请输入要查找的文件名称或后缀名:")
    for result in find_file_by_pattern(fileName, base):
        print()
        result
# 如果要查找指定名字的文件只需要将以下代码屏幕即可
# if full_path.endswith(pattern):  # 不能写成单引号，单引号达不到预期的效果
#     ......
# ......
# ......
# else:
# continue