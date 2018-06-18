# -*- coding: utf-8 -*-

#带_example的是原文的参考答案

#第一题
def accum(s):
    #accum('abcd')      # 'A-Bb-Ccc-Dddd'
    #accum('cwAt')      # 'C-Ww-Aaa-Tttt'
    return '-'.join((ch * (i+1)).capitalize() for i, ch in enumerate(s) )

def accum_example(s):
    return '-'.join(y.upper() + y.lower() * x for x, y in enumerate(s))

#第二题
# get_sum(1, 0) == 1 // 1 + 0 = 1
# get_sum(1, 2) == 3 // 1 + 2 = 3
# get_sum(0, 1) == 1 // 0 + 1 = 1
# get_sum(1, 1) == 1 // 1  Since both are same
# get_sum(-1, 0) == -1 // -1 + 0 = -1
# get_sum(-1, 2) == 2 // -1 + 0 + 1 + 2= 2
    
def get_sum(a, b):
    return sum([x for x in range(min(a,b), max(a,b) + 1)])

def get_sum_example(a, b):
    return sum(range(min(a, b), max(a, b) + 1))

#第三题
#实现功能：给你一串字符串，你要返回他所有重复的字幕的个数，不区分大小写
# test.assert_equal(duplicate_count('abcd'), 0)
# test.assert_equal(duplicate_count('abcdea'), 1)
# test.assert_equal(duplicate_count('indivisibility'), 0)
def duplicate_count(s):
    repeat_num_dict = {}
    lower_str = s.lower()
    for ch in lower_str:
        if lower_str.count(ch) > 1:
            repeat_num_dict[ch] = 1
    return len(repeat_num_dict)

def duplicate_count_example(text):
    text = text.lower()
    texts = set(text)
    lists = []
    for i in texts:
        numbers = text.count(i)
        if numbers != 1:
            lists.append(numbers)
    return len(lists)

#第四题
#likes[]   // must be "no one likes this"
#likes ['Peter']  // must be "peter likes this"
#likes ['Jacob', 'Alex'] // must be "Jacob and Alex like this"
#likes ['Max', 'John', 'Mark'] // must be "Max, John and Mark like this"
#likes ['Jacob', 'Alex', 'Mark', 'Max'] // must be "Alex, Jacob and 2 others like this"
def likes(l):
    ver = 'likes'
    if l is None:
        l = []
    if len(l) > 1:
        ver = 'like'
    if len(l) == 0:
        peoples = "no one"
    elif len(l) == 1:
        peoples = l[0]
    elif len(l) == 2:
        peoples = l[0] + ' and ' + l[1]
    elif len(l) == 3:
        peoples = l[0] + ',' + l[1] + ' and ' + l[2]
    else:
        peoples = l[0] + ',' + l[1] + ' and ' + str(len(l) - 2) + 'others'
    
    result = 'must be %r %s this' % (peoples, ver)
    return result

def likes_example(names):
    if names:
        if len(names) == 1:
            return names[0] + ' likes this'
        elif len(names) == 2:
            return names[0] + ' and ' + names[1] + ' like this'
        elif len(names) == 3:
            return names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
        else:
            return names[0] + ', ' + names[1] + ' and ' + str(len(names) - 2) + ' others like this'
    else:
        return 'no one like this'

# 第五题
#将任何非负整数作为参数，并以降序的数字返回他
#例子：
#输入：21445 输出：54421
#输入：145263 输出：654321
#输入：1254859723 输出：9875543221
def Descending_Order(num):
    return int(''.join(sorted(list(str(num)),reverse=True)))

def Descending_Order_example(num):
    return int(''.join(sorted(str(num),reverse=True)))

#第六题
#给定一个包含名称的散列的数组
#返回：格式为由逗号分隔的名称列表的字符串， 最后两个名称，用&分隔
#例子：
# namelist([{'name':'Bart'},{'name':'Lisa'}, {'name':'Maggie'}])
# return 'Bart, Lisa & Maggie'
# namelist([{'name':'Bart'},{'name':'Lisa'}])
# return 'Bart & Lisa'
# namelist([{'name':'Bart'}])
# return 'Bart'
# namelist([])
# return 'Bart'

def namelist(names):
    if names:
        if len(names) == 1:
            return names[0]['name']
        elif len(names) == 2:
            return names[0]['name'] + ' & ' + names[1]['name']
        else:
            return ', '.join([name['name'] for name in names[:-1]]) + ' & ' + names[-1]['name']
    else:
        return ''

def namelist_example(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(i['name'] for i in names[:-1]), names[-1]['name'])
    elif len(names) == 1:
        return names[0]['name']
    else:
        return ''

#第七题
#统计不在a-m之之间的字母的个数
#例子
# s='aaabbbbhaijjjm' error_printer(s) => '0/14'
# s='aaaxbbbbyyhwawiwjjjwwm' error_printer(s) => '8/22'

def error_printer(s):
    stand_str = 'abcdefghijkml'
    count = 0
    for ch in s:
        if ch not in stand_str:
            count += 1
    return '%s/%s' % (count, len(s))

from re import sub
def error_printer_example(s):
    return '{}/{}'.format(len(sub('[a-m]', '', s)), len(s))

#第八题
#2进制相加
#add_binary(1,1) => '10'
#add_binary(0,1) => '1'
#add_binary(1,0) => '1'
#add_binary(2,2) => '100'
#add_binary(51,12) => '111111'

def add_binary(a, b):
    return bin(a + b)[2:]

def add_binary_example(a, b):
    return bin(a + b).lstrip('0b')

def add_binary_example_1(a, b):
    return format(a + b, 'b')

#第九题
#例子
#expanded_form(12)    => '10 + 2'
#expanded_form(42)    => '40 + 2'
#expanded_form(70304)    => '70000 + 300 + 4'

def expanded_form(num):
    return ' + '.join([str(int(i) * 10 ** (len(str(num)) - 1 - index))
                        for index, i in enumerate(str(num)) if int(i) != 0 ])

def expanded_form_example(num):
    nums = str(num)
    x = []
    for i in range(0, len(nums)):
        if int(nums[i]) != 0:
            s = str(int(nums[i]) * 10 ** (len(nums) - i - 1) )
            x.append(s)
    return ' + '.join(x)

#第10题
#根据数字每位之和累加，相同的按字符串字典排序
#order_weight('2000 10003 1234000 44444444 9999 11 11 22 123')
#return ''11 11 2000 10003 22 123 1234000 44444444 9999'

def order_weight(string):
    return ' '.join(sorted(sorted(string.split()), key=lambda x : sum(int(ch) for ch in x)))
    

print order_weight('2000 10003 1234000 44444444 9999 11 11 22 123')  

#第11题
#将10进制数转换成2进制，并计算1的个数
def countBits(n):
    return bin(n).count('1')

def countBits_example(n):
    s = lambda x: sum(int(z) for z in x)
    return s(format(n, 'b'))

def countBits_example1(n):
    return format(n, 'b').count('1')

#第12题
#判断括号是否匹配
#"()"       =>  true
#")(()))"   =>  false
#"("        =>  false
#"(())((()())())" => true
def valid_parenttheset(string):
    left = []
    right = []
    for ch in string:
        if ch == '(':
            left.append(ch)
        else:
            right.append(ch)
        if len(right) > len(left):
            return False
        if left and right:
            left.pop()
            right.pop()
    if not left and not right:
        return True
    return False

def valid_parenttheset_example(string):
    cnt = 0
    for i in string:
        if i == '(':
            cnt += 1
        if i == ')':
            cnt -= 1
        if cnt < 0:
            return False
    return True if cnt == 0 else False

print valid_parenttheset_example('()')
print valid_parenttheset_example(')(()))')
print valid_parenttheset_example('(')
print valid_parenttheset_example('(())(()()())')
print valid_parenttheset_example('(())((()())())') 

