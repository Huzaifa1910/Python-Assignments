menu = {"Burger": 400,"Juice":500,"Roll": 170}
menu_keys = list(menu)
bill = 0
print("Menu    Price:")
for i in range(len(menu)):
    print(i+1,menu_keys[i],menu[menu_keys[i]])
while(True):
    print("=============================")
    userinp = int(input("Select ur item: "))
    if userinp == 1 or 2 or 3:
        print("=============================")
        bill += menu[menu_keys[userinp-1]]
        print("You have selected",menu_keys[userinp-1],"\nYour Bill: ",bill,"\nDo you want to shop More?")
        print("=============================")
    ask = input("Y or N: ")
    if ask.upper() == "N":
        print("=============================")
        print("Thank you for choosing us \n your bill is: ", bill)
        break
    else:
        continue
