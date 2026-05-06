def trim(s):
    if len(s)==0:
        return ''
    i = 0
    while i<len(s) and s[i] == ' ':
        i+=1

    j = len(s) - 1
    while j>=0 and s[j] == ' ':
        j-=1

    return s[i:j+1]

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')