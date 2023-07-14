weight = float(input())
height = float(input())

BMI = weight/height ** 2

if BMI < 18.5 :
    print("Under Weight")
elif BMI < 25 :
    print("Healthy Weight")
else :
    print("Over Weight")