import os

# 定义要修改的文件夹路径和文件名

old_name = '/home/runner/work/running_page/running_page/FIT_OUT/sportRecord_20240927175050.fit'
new_name = old_name + '.lock'

# 修改文件名
os.rename(old_name, new_name)
print(f'已将 {old_name} 修改为 {new_name}')
