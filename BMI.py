height,weight = eval(input("please input height(m) and weight(kg):\n"))
bmi = weight/pow(height,2)
print("BMI为:{:.2f}".format(bmi))
who = ""
if bmi < 18.5:
    who = "thin"
elif 18.5<= bmi < 25:
    who = "normal"
elif 25 <= bmi < 30:
    who = "overweight"
print("BMI指标为:{}".format(who))