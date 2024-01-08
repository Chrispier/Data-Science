#def merge(str1,str2):
 #   result = ""
 #   for index in range(len(str1)):
 #       result = result + str1[index]
 #       result = result + str2[index]
#    return result

#print(merge('coding','monkey'))
#print(merge('',''))
#print(merge('word','word'))
"""
import random
def bingo():
    width = 5
    length = 5
    print(" ------- BINGO ------- ")
    for j in range(length):
        for i in range(width):
            num = random.randint(1,99)
            if num>=10:
                print(num, end=" | ")
            else:
                print("0" + str(num), end = " | ")
        print("\n------------------------")

bingo()
""
import random
answer = random.randint(1,100)
corr = False
while corr == False:
    guess = int(input("What's your guess?"))
    if(guess == answer):
        print("Correct!")
        corr = True
    elif(guess > answer):
        print("Too high ):")
    else:
        print("Too low ):")

"""
x=4
print(str(7 + 10)+'a')
print(int('7'+'20')+7)
print('hello'.find())