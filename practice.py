#encoding=UTF-8
a = 'practice'
print a

# rawInput = raw_input('enter the file name:')
# print rawInput

print "print the %s" % a
print 1 + 2 * 4

plus = 1 + 2
print plus
minus = 5 - 3
print minus
time = 2 * 5
print time
divide = 9 / 3
print divide
remainder = int(9 % 2)
print remainder

# i = 0
# tmp = 10
# rg = range(11)
# while rg[i] <= tmp:
#     print i
#     i = i + 1

# userIsInputANumber = raw_input('Enter a num:')
# try:
#     if int(userIsInputANumber) > 0:
#         print "%s is >0" % userIsInputANumber
#     elif int(userIsInputANumber) == 0:
#         print "a"
#     elif int(userIsInputANumber) < 0:
#         print "b"
# except ValueError, e:
#     print "your input is not a number", e

aTuple = (1, 2, 3, 4, 6)
aTuplePlus = 0
for i in aTuple:
    aTuplePlus += i
    print aTuplePlus
average = float(aTuplePlus) / len(aTuple)
print average


num = ''

# 2-10


def userinput():
    num = int(raw_input('pls enter a num between 1 and 100:'))
    if num <= 100 and num >= 0:
        print "success"
    else:
        userinput()

# userinput()

# 2-11
print '\n choose 1 to calculate the five number;\n choose 2 to calculate the average of the five number;\n choose 3 to quit the program'
while True:
    flag = int(raw_input('enter your choice:'))
    if flag == 1:
        print "you choose 1"
    elif flag == 2:
        print "you choose 2"
    elif flag == 3:
        break
    else:
        print "you have entered the wrong number, try again"

# 2-15 元素排序

num1 = int(raw_input('pls enter the first number:'))
num2 = int(raw_input('pls enter the second number:'))
num3 = int(raw_input('pls enter the third number:'))
temp = ""
if num1 < num2:
    temp = num2
else:
    temp = num1
if num3 > temp:
    temp = num3
print temp
