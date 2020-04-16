score = eval(input())
if score >= 90:
    grade= "a"
elif score >= 80:
    grade= "b"
elif score <= 80:
    grade= "c"
print("{}".format(grade))