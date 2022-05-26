a = [["Twinkle, twinkle, little star,"],["How I wonder what you are!"],["Up above the world so high,"],["Like a diamond in the sky."],["Twinkle, twinkle, little star,"],["How I wonder what you are!"]]
b = ""
j = 0
for i in range(len(a)):
    
    if(j > 2):
        j -= 1
        print(b*j,a[i][0])
        b = ""
        j = 0
    else:
        print(b*j,a[i][0])
        b = "    "
        j += 1
##print("Twinkle, twinkle, little star,")
##print("How I wonder what you are!")
##print("Up above the world so high,")
##print("Like a diamond in the sky.")
##print("Twinkle, twinkle, little star,")
##print("How I wonder what you are")
##Twinkle, twinkle, little star,
##How I wonder what you are!
##Up above the world so high,
##Like a diamond in the sky.
##
##Twinkle, twinkle, little star,
##How I wonder what you are







