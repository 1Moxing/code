# pip install pandas
# pip 安装工具 install 安装  pandas 模块
import pandas as pd

# 读入文件
data = pd.read_excel('shuju.xlsx')
data['year'] = data['type'].apply(lambda x:x.split('/')[0].strip())
data['c'] = data['type'].apply(lambda x:x.split('/')[1].strip())
data['t'] = data['type'].apply(lambda x:x.split('/')[2].strip())
writer = pd.ExcelWriter('temp.xlsx')
# data.to_excel(writer,sheet_name='原始数据')

# 根据年限分割
# for i in data['year'].unique():
#     data[data['year'] == i].to_excel(writer,sheet_name=i)

# 根据类型分割
type_list = set(z for i in data['t'] for z in i.split(' '))
type_list.remove('1978(中国大陆)')
for ty in type_list:
   data[data['t'].str.contains(ty)].to_excel(writer,sheet_name=ty)

writer.close()