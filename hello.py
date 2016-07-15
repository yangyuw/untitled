# coding=UTF-8

myString = 'hello world!'
print myString
#Python的print语句,与字符串格式运算符( %)结合使用,可实现字符串替换功能.%s 表示由一个字符串来替换,而%d 表示由一个整数来替换,另外一个很常用的就是%f, 它 表示由一个浮点数来替换
print "%s is number %d!" % ("Python", 1)
#raw_input()得到用户的输入
# user = raw_input('Enter login name: ')
# print 'Your login is:', user
#获得命令帮助
help(raw_input)

#列表元素用中括号( [ ])包裹,元素的个数及元素的值可 以改变。元组元素用小括号(( ))包裹,不可以更改(尽管他们的内容可以)
aList = [1, 2, 3, 4]
print aList
print aList[0]
print aList[2:]
print aList[:3]

aTuple = ('robots', 77, 93, 'try')
print aTuple
print aTuple[:3]
#aTuple[1] = 5 不能修改元组的值

##字典
aDict = {'host': 'earth'}  #create dict
aDict['port'] = 80  # add to dict
print aDict
print aDict.keys()
print aDict['host']
for key in aDict:
    print key, aDict[key]

#if表达式不需要用大括号括起来.
x = 2
if x < .0:
    print '"x" must be atleast 0!'
elif x > 0:
    print '"x" is > 0!'

counter = 0
while counter < 3:
    print 'loop #%d' % (counter)
    counter += 1

for item in ['e-mail', 'net-surfing', 'homework', 'chat']:
    print item,

# 为了美观,带逗号的print语句输出的元素之间会自动添加一个空格.
who = 'knights'
what = 'Ni!'
print 'We are the', who, 'who say', what, what, what, what
print 'We are the %s who say %s' % (who, ((what + ' ') * 4))

# Python 提供了一个 range()内建函数来生成这种列表
for eachNum in range(3):
    print eachNum
  # range() 函数经常和len()函数一起用于字符串索引.
foo = 'abc'
for i in range(len(foo)):
    print foo[i], '(%d)' % i
for i, ch in enumerate(foo):
    print ch, '(%d)' % i

# 列表解析
squared = [x ** 2 for x in range(4)]
for i in squared:
    print i

sqdEvens = [x ** 2 for x in range(8) if x % 2]
for i in sqdEvens:
    print i

