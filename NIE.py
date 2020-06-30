#133
dic_hundred = {'1':'one hundred ','2':'two hundred ','3':'three hundred ','4':'four hundred ','5':'five hundred ',
               '6':'six hundred ','7':'seven hundred ','8':'eight hundred ','9':'nine hundred ','0':'none'}
dic_ten = {'1':'one ','2':'twenty ','3':'thirty ','4':'fourty ','5':'fifty ','6':'sixty ','7':'seventy ',
           '8':'eighty ',
           '9':'ninty','0':'none'}
dic_once = {'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine',
            '0':'none'}
dic_sp = {'1':'eleven','2':'twelve','3':'thirteen','4':'fourteen','5':'fifteen','6':'sixteen','7':'seventeen',
          '8':'eighteen','9':'ninteen'}

def fun1(string):
    val = 'none'
    for i in dic_once:
        if i == string:
            val = dic_once[i]
    return val

def fun2(string):
    val = 'none'
    for i in dic_ten:
        if i == string:
            val = dic_ten[i]
    return val

def fun3(string):
    val = 'none'
    for i in dic_hundred:
        if i == string:
            val = dic_hundred[i]
    return val

def fun_sp(string):
    val = 'none'
    for i in dic_sp:
        if i == string:
            val = dic_sp[i]
    return val

string = input('enter the number : ')
once = string[2]
tens = string[1]
thousand = string[0]
if tens != '1':
    l = []
    st = []
    l.append(fun3(thousand))
    l.append(fun2(tens))
    l.append(fun1(once))
    for i in l:
        if i != 'none':
            st.append(i)
    string = "".join(st)
    if len(string) != 0:
        print(string)
    else:
        print('Zero')
else:
    l = []
    st = []
    l.append(fun3(thousand))
    l.append(fun_sp(once))
    for i in l:
        if i != 'none':
            st.append(i)
    string = "".join(st)
    if len(string) != 0:
        print(string)
    else:
        print('Zero')
    
    
    