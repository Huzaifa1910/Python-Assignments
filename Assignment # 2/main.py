# print("hello world")
#
# a = 5
# b = 10   #RESULT: 15
# print(c)

# d = "huzaifa"
# e = "ghori" #RESULT: huzaifaghori
# c = d+e
# print(c)

# f = "4"
# g = "8"  #RESULT: 48
# h = f + g
# print(h)

# a = "10"
# b = 20   #RESULT: ERROR
# c = a + b
# print(c)

# x = 8
# y = x + 7
# z = y - x + 1 #RESULT: 8
# print(z)

# a = 12-4/2+9*5
# print(a) #RESULT: 55.0

# a = ((12-4)/(2+9)*5)
# print(a) #RESULT: 3.63636363636367

# x = 10
# y = x%3
# print(y) #RESULT: REMAINDER1

# f = 10
# f = 12
# print(f) #RESULT:12

# g = 5
# g = g + 2
# print(g) #RESULT: 7

# a = 3
# a += 3
# print(a)

# gender = input("gender?")
# if(gender == "male"):
#     print("Allow for Ride")
# else:
#     print("OKey")

# age = 14
# gender = "female"
# if age>10 or gender == "male":
#     print("Allow for ride")
# else:
#     print("ROKLo")




mrkisl = 83;
mrkEng = 73;
mrkMath = 90;

total = 300;

percent = ((mrkMath + mrkEng + mrkisl)/total)*100;
print(percent , "%")
if percent <= 100 and percent >= 80:
    print("Grade A+")
elif percent <= 79 and percent >= 70:
    print("Grade A")
elif percent <= 69 and percent >= 60:
    print("Grade B")
elif percent <= 59 and percent >= 50:
    print("Grade C")
elif percent>100:
    print("Percentage is not valid")
else:
    print("failed")