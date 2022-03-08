# -*- coding: utf-8 -*-
# 创建时间：2022/2/21 17:10
# 当前的项目名：big_yellow.py
# 创建人：黄柏
# import jsonpath
#
# sumnum=[{"PV": 9256432, "PVStr": "925.6w", "DateCode": 20220214, "StatDate": "2022-02-14 00:00:00", "LiveSales": 563196845, "AwemeSales": 9035000, "OtherSales": 97404137, "TotalSales": 669635982, "LiveSalesStr": "563.2w", "AwemeSalesStr": "9.0w", "OtherSalesStr": "97.4w", "SumSalesCount": 22918, "TotalSalesStr": "669.6w", "LiveSalesCount": 19363, "LiveSalesRatio": "84.10%", "AwemeSalesCount": 317, "AwemeSalesRatio": "1.35%", "OtherSalesCount": 3238, "OtherSalesRatio": "14.55%", "SumSalesCountStr": "2.3w", "LiveSalesCountStr": "1.9w", "AwemeSalesCountStr": "317", "LiveSaleCountRatio": "84.49%", "OtherSalesCountStr": "3238", "AwemeSaleCountRatio": "1.38%", "OtherSaleCountRatio": "14.13%"}, {"PV": 8076242, "PVStr": "807.6w", "DateCode": 20220215, "StatDate": "2022-02-15 00:00:00", "LiveSales": 441221624, "AwemeSales": 9735011, "OtherSales": 71141848, "TotalSales": 522098483, "LiveSalesStr": "441.2w", "AwemeSalesStr": "9.7w", "OtherSalesStr": "71.1w", "SumSalesCount": 20546, "TotalSalesStr": "522.1w", "LiveSalesCount": 17696, "LiveSalesRatio": "84.51%", "AwemeSalesCount": 335, "AwemeSalesRatio": "1.86%", "OtherSalesCount": 2515, "OtherSalesRatio": "13.63%", "SumSalesCountStr": "2.1w", "LiveSalesCountStr": "1.8w", "AwemeSalesCountStr": "335", "LiveSaleCountRatio": "86.13%", "OtherSalesCountStr": "2515", "AwemeSaleCountRatio": "1.63%", "OtherSaleCountRatio": "12.24%"}, {"PV": 7374048, "PVStr": "737.4w", "DateCode": 20220216, "StatDate": "2022-02-16 00:00:00", "LiveSales": 459712634, "AwemeSales": 4738890, "OtherSales": 95037652, "TotalSales": 559489176, "LiveSalesStr": "459.7w", "AwemeSalesStr": "4.7w", "OtherSalesStr": "95.0w", "SumSalesCount": 21118, "TotalSalesStr": "559.5w", "LiveSalesCount": 17825, "LiveSalesRatio": "82.17%", "AwemeSalesCount": 159, "AwemeSalesRatio": "0.85%", "OtherSalesCount": 3134, "OtherSalesRatio": "16.99%", "SumSalesCountStr": "2.1w", "LiveSalesCountStr": "1.8w", "AwemeSalesCountStr": "159", "LiveSaleCountRatio": "84.41%", "OtherSalesCountStr": "3134", "AwemeSaleCountRatio": "0.75%", "OtherSaleCountRatio": "14.84%"}, {"PV": 6803094, "PVStr": "680.3w", "DateCode": 20220217, "StatDate": "2022-02-17 00:00:00", "LiveSales": 478526507, "AwemeSales": 11356900, "OtherSales": 78319486, "TotalSales": 568202893, "LiveSalesStr": "478.5w", "AwemeSalesStr": "11.4w", "OtherSalesStr": "78.3w", "SumSalesCount": 21684, "TotalSalesStr": "568.2w", "LiveSalesCount": 18434, "LiveSalesRatio": "84.22%", "AwemeSalesCount": 340, "AwemeSalesRatio": "2.00%", "OtherSalesCount": 2910, "OtherSalesRatio": "13.78%", "SumSalesCountStr": "2.2w", "LiveSalesCountStr": "1.8w", "AwemeSalesCountStr": "340", "LiveSaleCountRatio": "85.01%", "OtherSalesCountStr": "2910", "AwemeSaleCountRatio": "1.57%", "OtherSaleCountRatio": "13.42%"}, {"PV": 5606223, "PVStr": "560.6w", "DateCode": 20220218, "StatDate": "2022-02-18 00:00:00", "LiveSales": 364156465, "AwemeSales": 4161260, "OtherSales": 56289808, "TotalSales": 424607533, "LiveSalesStr": "364.2w", "AwemeSalesStr": "4.2w", "OtherSalesStr": "56.3w", "SumSalesCount": 17754, "TotalSalesStr": "424.6w", "LiveSalesCount": 15628, "LiveSalesRatio": "85.76%", "AwemeSalesCount": 148, "AwemeSalesRatio": "0.98%", "OtherSalesCount": 1978, "OtherSalesRatio": "13.26%", "SumSalesCountStr": "1.8w", "LiveSalesCountStr": "1.6w", "AwemeSalesCountStr": "148", "LiveSaleCountRatio": "88.03%", "OtherSalesCountStr": "1978", "AwemeSaleCountRatio": "0.83%", "OtherSaleCountRatio": "11.14%"}, {"PV": 8468957, "PVStr": "846.9w", "DateCode": 20220219, "StatDate": "2022-02-19 00:00:00", "LiveSales": 599432009, "AwemeSales": 5535670, "OtherSales": 86240477, "TotalSales": 691208156, "LiveSalesStr": "599.4w", "AwemeSalesStr": "5.5w", "OtherSalesStr": "86.2w", "SumSalesCount": 25923, "TotalSalesStr": "691.2w", "LiveSalesCount": 22825, "LiveSalesRatio": "86.72%", "AwemeSalesCount": 218, "AwemeSalesRatio": "0.80%", "OtherSalesCount": 2880, "OtherSalesRatio": "12.48%", "SumSalesCountStr": "2.6w", "LiveSalesCountStr": "2.3w", "AwemeSalesCountStr": "218", "LiveSaleCountRatio": "88.05%", "OtherSalesCountStr": "2880", "AwemeSaleCountRatio": "0.84%", "OtherSaleCountRatio": "11.11%"}]
# new=jsonpath.jsonpath(sumnum,"$..PV")
# new2=jsonpath.jsonpath(sumnum,"$..SumSalesCount")
# new3=sum(new)
# new4=sum(new2)
# print(new3)
# print(new4)

# import math
# import random
# a=12.52234
# b=3
# print(a/b)
# print(a*b)
# print(a+b)
# print(a-b)
# print(math.ceil(a))
# print(math.floor(a))
# print(random.random())
# print(random.randint(1,10))
# print(
#     round(a,2)

# a='hsf5201314'
# b='hsf'


# print(a*2)
# print(b+a[3:])
# print(a.replace('hsf',b))
# print(a.replace('hsf','sll'))
# print(a+b)
# print(b in a)
# print(a not in b)
# print('{}'.format('格式化1'))
# print("%s"%'格式化2')
# print(f'{a}{b}')
# p=('-'.join(b))
# print(p)

# ip = "10.100.0.233"
# print(ip.split('.'))
# s = 'asd dfdf ff'
# print(s.lower())
# print(s.upper())
# print(s.capitalize())
# print(s.lower())
# print(s.upper())
# ss=(1,2,34,5,6)
# print(ss[1])
# print(ss[2])
# print(ss[2::2])
# print(ss[1:-1])
# print(ss[1:3]+(33,44))
# print(ss*2)

# print('%d,%d,%d,%d,%d'%(ss))
# a='ssff-ssll'
# print(a.split('-'))
# print(a.rsplit('s'))
# print(a.split('s'))
# print(a.strip(''))

# print(a[1::2])
# a.append(['1','2'])
# a.insert(1,3)
# a.extend([1,3,4])
# a.append(7)
# a.insert(2,6)
# a.extend([9,8.7])

# a.sort(reverse=True)
# print(a)
# a.sort()
# print(a)
# p=[1,23,44]
# p.reverse()
# print(p)
# a={"hsf":"sll","sll":"521"}
# x = ('key1', 'key2', 'key3')#不指定值
# print(dict.fromkeys(x))
# print(dict.fromkeys(x))
# print(dict.fromkeys(x))
# a={1,2,3,4,5,"dada"}
# a.add('22')
# a.remove('dada')
# print(a)
# a=-22
# print(abs(a))
# a=[1,3,5,3,4,6,2]
# a.sort()
# a.remove(3)
# a.pop(3)
# del a[2]
# a[0]=55
# a.extend([1,3,4])
# a.append(4)
# a.reverse()
# print(a.count(4))
# print(a)

# try:
#     chengji = int(input("请输入成绩:"))
#     if chengji >= 60:
#         print("及格")
#         if chengji > 90:
#             print("优秀")
#         elif chengji > 75:
#             print("中等")
#         else:
#             print("一般")
#     else:
#         print("不及格")
# except Exception :
#     print('请输入正确的数字!')
# n=10
# while n>8:
#     n-=1
#     print(n)
# print('结束')
# # 实现1+2+3+4...+100?
# i=0
# n=0
#
# while i<100:
#     i=i+1
#     n=n+i
#     print(n)
# i=0
# while i<10:
#  i += 1
#  if i==5:
#   continue
#  sum=i+1
#  print(sum)


# i = 1
# while i < 7:
#   print(i)
#   if i == 3:
#     break
#   i += 1
# name=[11,4,22,7,88,9,-5,3]
# for o in range(0,len(name)):
#     for p in range(0,len(name)-1):
#         if name[p]>name[p+1]:
#             name[p],name[p+1]=name[p+1],name[p]
#print(name)
# for i in range(1,10):
#     for o in range(1,i+1):
#         print("{}x{}={}".format(o,i,o*i),end=' ')
#     print(" ")

# while  True:
#     try:
#         num1=float(input('请输入三角形边长第1位数：'))
#         num2=float(input('请输入三角形边长第2位数：'))
#         num3=float(input('请输入三角形边长第3位数：'))
#         if num1 + num2 > num3 or  num2 + num3 > num1 or num1 + num3 > num2:
#             if num1 == num2 == num3:
#                 print('该三角形为等边三角形')
#             elif num1==num2 or num2==num3 or num1==num3:
#                 print('该三角形为等腰三角形')
#             else:
#                 print('该三角形为一般三角形')
#             sum=num1+num2+num3
#             print('三角形边长之和为：{}cm'.format(sum))
#         else:
#         # if num1 + num2 < num3 or num2 + num3 < num1 or num1 + num3 < num2:
#             print('不能构成三角形')
#     except  Exception:
#         print('请输入有效的数字！')
# 如果输入三个不同的数，要求比较大小并按从小到大排序输出呢？如输出：a<b<c）
# num1=float(input('请输入第1位数：'))
# num2=float(input('请输入第2位数：'))
# num3=float(input('请输入第3位数：'))
# a=[num1,num2,num3]
# a.sort()
# print('{}<{}<{}'.format(a[0],a[1],a[2]))
# for r in range(0,5):
#     for e in range(0,4-r):
#         print(' ', end='')
#     for o in range(0,r*2+1):
#         print('*',end='')
#     print()
# for i in range(1,5):
#     for u in range(0,i*2-i):
#         print(" ",end='')
#     for p in range(1,10-i*2):
#         print('*', end='')
#     print()

# for i in range(1,10):
#     for o in range(1,i+1):
#             print('o{},i{}'.format(o,i),end="\t")
#     print()
    #     # print("*",end="")
    #     print('{}x{}={}'.format(o,i,i*o),end="\t")
    # print()
# name=None
# def random(name,age=18):
#     print('xiaoming{},age{}'.format(name,age))
#
# random('xiaoming',age=19)
"""
实现学生管理系统,完成对学员的增,删,改,查和退出学生管理系统。
输入0显示所有学员信息,1代表增加，2代表删除，3代表修改，4代表查询，exit代表退出学生管理系统。每一个功能定义一个自定义函数。
输入0：显示所有学员信息
输入1：添加学员编号，编号姓名，年龄
输入2: 根据学员姓名删除学员信息
输入3：修改学员姓名
输入4：根据名字查询学员姓名
输入exit退出学生管理系统11
# """
# print('**************欢迎使用学生管理系统**************')
# print('输入0：显示所有学员信息')
# print('输入1：添加学员编号，编号姓名，年龄')
# print('输入2: 根据学员姓名删除学员信息')
# print('输入3：修改学员姓名')
# print('输入4：根据名字查询学员姓名')
# print('输入5: 退出学生管理系统')
# print('**********************************************')
#
# list=[]
# def see():
#     print(list)
# def add():
#     id=int(input('请输入学生的学号：'))
#     name=input('请输入学生的姓名：')
#     age=int(input('请输入学生的年龄:'))
#     for i in list:
#         if i['id'] ==id:
#             print('该学生在系统中已存在！')
#             return
#     dic={}
#     dic['id']=id
#     dic['name']=name
#     dic['age']=age
#     list.append(dic)
#     print(list)
#
# def dell():
#     id = int(input('请输入你要删除学生的学号：'))
#     for i in list:
#         if id==i['id']:
#             list.remove(i)
#             break
#     else:
#         print('该学生不存在！')
#
# def updata():
#     id = int(input('请输入你要修改学生的学号：'))
#     for i in list:
#         if id==i["id"]:
#             name=input('请输入你要修改学生的姓名：')
#             age= int(input('请输入你要修改学生的年龄：'))
#             i['id']=id
#             i['name']=name
#             i['age']=age
#             print(list)
#             break
#         else:
#             print('该学生不存在！')
#
# def brk():
#     for i in list:
#         if i !=0:
#             break
# def search_info():
#     # 输入要查询的学员姓名
#     search_name=input('请输入要查询的学员姓名:')
#     # 检查学员是否存在  遍历  遍历什么，遍历info
#     for i in list:
#         if i['name']==search_name:
#             print(f"学员信息：学号是{i['id']},姓名是{i['name']}，年龄是{i['age']}")
#             break
#     else:
#         print('要查询的学员不存在')
#
# while True:
#     def system():
#         try:
#             num=int(input('请输入数字编号：'))
#             if num==0:
#                 print('0：显示所有学员信息')
#                 see()
#             if num==1:
#                 print('1：添加学员编号，编号姓名，年龄')
#                 add()
#             if num==2:
#                 print('2: 根据学员姓名删除学员信息')
#                 dell()
#             if num==3:
#                 print('3：修改学员姓名')
#                 updata()
#             if num==4:
#                 print('4：根据名字查询学员姓名')
#                 search_info()
#             if num==5:
#                 print('5: 退出学生管理系统')
#                 exit_flag = input('确定要退出系统吗?yes or no')
#
#
#         except Exception:
#             print('请输入正确的内容！！！！！')
#     system()