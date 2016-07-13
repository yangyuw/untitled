#encoding=UTF-8
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

while