#coding=utf-8
# import xlsxwriter
# 
# wordbook=xlsxwriter.Workbook("hello.xlsx") #创建一个名为hello的xlsx的文件 赋值给workbook
# worksheet=wordbook.add_worksheet()#创建一个默认的工作薄 赋值给worksheet
# 
# #worksheet.write("A1","hello world") #在A1的地方写入hello world
# #worksheet.write("B2","hello world")#在B2的地方写入hello world
# ave_formatter = wordbook.add_format()
# ItemStyle = wordbook.add_format()
# ItemStyle.set_font_size(10) #字体大小
# ItemStyle.set_bold()#是否粗体
# ItemStyle.set_bg_color('#101010')#表格背景颜色
# ItemStyle.set_font_color('#FEFEFE')#字体颜色
# ItemStyle.set_align('center')#居中对齐
# ItemStyle.set_align('vcenter')#居中对齐
# ItemStyle.set_bottom(2)#底边框
# ItemStyle.set_top(2)#上边框
# ItemStyle.set_left(2)#左边框
# ItemStyle.set_right(2)#右边框
# title_formatter = wordbook.add_format()
# title = ['业务名称','星期一','星期二','星期三','星期四','星期五','星期六','星期日','平均流量']
# buname = ['业务官网','新闻中心','购物频道','体育频道','亲子频道']
# data = [
#     [150,152,158,149,155,145,148],
#     [89,88,95,93,98,100,99],
#     [201,200,198,175,170,198,195],
#     [75,77,78,78,74,70,79],
#     [88,85,87,90,93,88,84]
# ]
# #write_row()方法可以用于向单元格一次性写入一个列表的数据  行
# worksheet.write_row('A1',title)
# #write_column()方法可以用于向单元格一次性写入一个列表的数据  列
# worksheet.write_column('A2',buname)
# for i in range(2,7):
#     worksheet.write_row('B{}'.format(i),data[i-2],ItemStyle)
#     # 计算平均流量栏数据并写入
#     worksheet.write_formula('I{}'.format(i),'=AVERAGE(B{}:H{})'.format(i,i),ave_formatter)
# wordbook.close()#关闭

with open("hello.csv") as file:
    for line in  file:
        print (line)