def pda_1(string):
    machine = {
        0:{
            'a':{'':[0,'A'],'A':[0,'AA']},
            'b':{'':[2,'A'],'A':[1,'']}
        },
        1:{
            'a':{'':[2,'A'],'A':[2,'A']},
            'b':{'':[2,'A'],'A':[1,'']}
        },
        2:{
            'a':{'':[2,'A'],'A':[2,'A']},
            'b':{'':[2,'A'],'A':[2,'A']}
        }
    }
    start = 0
    state = start
    stack = ''
    empty = True
    for elem in string:
        if empty: change = machine[state][elem]['']
        else: change = machine[state][elem][stack[-1]]
        state = change[0]
        if empty:
            stack = stack + change[1]
            empty = False
        else:
            list1 = list(stack)
            del list1[-1]
            stack = ''.join(list1[i] for i in range(len(list1)))
            stack = stack + change[1]
            if len(stack) == 0: empty = True
    return empty
print('Testing whether the string is of the form a^n b^n')
print('aaabbb',pda_1('aaabbb'))
print('aaabb',pda_1('aaabb'))
print('aaabba',pda_1('aaabba'))