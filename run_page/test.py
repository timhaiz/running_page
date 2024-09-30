import os

# 定义要修改的文件夹路径和文件名
f_path = '/home/runner/work/running_page/running_page/FIT_OUT/sportRecord_20240927175050.fit'
base_name = os.path.basename(f_path)
base_name = os.rename(base_name, base_name + ".lock")

print(base_name)
