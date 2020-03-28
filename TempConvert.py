# val = input("请输入带温度表示符号的温度值（例如：32C）：")
# if val[-1] in ['C','c']:
#     f = 1.8*float(val[0:1])+32
#     print("转换后的温度为：%.2fF"%f)
# elif val[-1] in ['F','f']:
#     c = (float(val[0:-1]) - 32)
#     print("转换后的温度为:%.2fC"%c)
# else:
#     print("输入有误")


#TempConvert
Temp = input("请输入温度:\n")
if Temp[-1] in ['F','f']:
    C = (eval(Temp[0:-1])-32)/1.8
    print ("转换后的温度{:.2f}C".format(C))
elif Temp[-1] in ['C','c']:
    F = 1.8*eval(Temp[0:-1]) + 32
    print ("转换后的温度为{:.2f}F".format(F))
else:
    print("输入错误\n")