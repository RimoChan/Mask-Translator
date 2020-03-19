import re

def 預處理(代碼):
    return re.findall(r'(\'\'\'|"""|\\.|.|\n)', 代碼)


def 分析(代碼):
    代碼 = 預處理(代碼)

    組 = []

    def 符號(x):
        return x in '{}[]() :\n\r.,+-=*/'

    def 引號(x):
        return x in ["'", '"', '"""', "'''"]

    def 字(x):
        return not 符號(x) and not 引號(x)

    now = ''
    狀態 = '符號'
    抵消 = None
    for i in 代碼:
        if 狀態 == '符號':
            if 符號(i):
                now += i
            if 字(i):
                組.append([狀態, now])
                now = i
                狀態 = '字'
            if 引號(i):
                組.append([狀態, now])
                now = i
                狀態 = '字符串'
                抵消 = i
            continue
        if 狀態 == '字':
            if 字(i):
                now += i
            if 符號(i):
                組.append([狀態, now])
                now = i
                狀態 = '符號'
            if 引號(i):
                now += i
                狀態 = '字符串'
                抵消 = i
            continue
        if 狀態 == '字符串':
            if i == 抵消:
                now += i
                組.append([狀態, now])
                now = ''
                狀態 = '符號'
            else:
                now += i
    組.append([狀態, now])
    return 組