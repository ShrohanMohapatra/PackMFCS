def tm_1(string):
    machine = {
        0:{'B':['B',1,1]},
        1:{
            'X':['X',1,1],
            'a':['X',1,2],
            'B':['B',1,4]
        },
        2:{
            'X':['X',1,2],
            'a':['a',1,2],
            'b':['X',-1,3],
            'B':['B',1,5]
        },
        3:{
            'X':['X',1,1],
            'a':['a',-1,3]
        },
        5:{
            'a':['a',1,5],
            'b':['b',1,5],
            'B':['B',1,5],
            'X':['X',1,5]
        }
    }
    start = 0
    i = 0
    final = [4]
    state = start
    tape = list('B'+string+'B')
    while i<len(tape):
        try:
            print(i+1,state,''.join(tape[j] for j in range(len(tape))))
            change = machine[state][tape[i]]
            tape[i] = change[0]
            i = i + change[1]
            state = change[2]
        except:
            return True
    return state in final
def tm_2(string):
    machine = {
        0:{'B':['B',1,1]},
        1:{
            'X':['X',1,1],
            'a':['X',1,2],
            'B':['B',1,6]
        },
        2:{
            'X':['X',1,2],
            'a':['a',1,2],
            'b':['X',-1,3],
            'B':['B',1,5]
        },
        3:{
            'B':['B',1,1],
            'X':['X',-1,3],
            'a':['a',-1,4]
        },
        4:{
            'X':['X',1,1],
            'a':['a',-1,4]
        },
        5:{
            'a':['a',1,5],
            'b':['b',1,5],
            'B':['B',1,5],
            'X':['X',1,5]
        }
    }
    start = 0
    i = 0
    final = [6]
    state = start
    tape = list('B'+string+'B')
    while i<len(tape):
        try:
            change = machine[state][tape[i]]
            tape[i] = change[0]
            i = i + change[1]
            state = change[2]
        except:
            return False
    return state in final
def tm_3(string):
    machine = {
        0:{'B':['B',1,1]},
        1:{
            'X':['X',1,1],
            'a':['X',1,2],
            'B':['B',1,6],
            'b':['X',1,7],
        },
        2:{
            'a':['a',1,2],
            'b':['b',1,2],
            'B':['B',-1,3],
            'X':['X',-1,3]
        },
        3:{
            'b':['b',1,4],
            'a':['X',-1,5]
        },
        4:{
            'B':['B',1,4],
            'a':['a',1,4],
            'b':['b',1,4]
        },
        5:{
            'a':['a',-1,5],
            'b':['b',-1,5],
            'X':['X',1,1]
        },
        7:{
            'a':['a',1,7],
            'b':['b',1,7],
            'B':['B',-1,8],
            'X':['X',-1,8]
        },
        8:{
            'b':['X',-1,5],
            'a':['a',1,4]
        }
    }
    start = 0
    i = 0
    final = [6]
    state = start
    tape = list('B'+string+'B')
    while i<len(tape):
        try:
            change = machine[state][tape[i]]
            tape[i] = change[0]
            i = i + change[1]
            state = change[2]
        except:
            return False
    return state in final
def tm_4(string):
    machine = {
        0:{'B':['B',1,1]},
        1:{
            'X':['X',1,1],
            'a':['X',1,2],
            'B':['B',1,5]
        },
        2:{
            'a':['a',1,2],
            'b':['X',1,3],
            'X':['X',1,2]
        },
        3:{
            'b':['b',1,3],
            'X':['X',1,3],
            'c':['X',-1,4]
        },
        4:{
            'B':['B',1,1],
            'a':['a',-1,4],
            'b':['b',-1,4],
            'X':['X',-1,4]
        }
    }
    start = 0
    i = 0
    final = [5]
    state = start
    tape = list('B'+string+'B')
    while i<len(tape):
        try:
            change = machine[state][tape[i]]
            tape[i] = change[0]
            i = i + change[1]
            state = change[2]
        except:
            return False
    return state in final
def add_tm(string):
    machine = {
        0:{'B':['B',1,1]},
        1:{
            'B':['0',1,2],
            '0':['0',1,1]
        },
        2:{
            '0':['0',1,2],
            'B':['B',-1,3]
        },
        3:{'0':['B',1,4]}
    }
    start = 0
    i = 0
    final = 4
    state = start
    tape = list('B'+string+'B')
    while state != final:
        change = machine[state][tape[i]]
        tape[i] = change[0]
        i = i + change[1]
        state = change[2]
    return ''.join(tape[i] for i in range(len(tape)))
def removeB_tm(string):
    machine = {
        5:{'B':['B',1,0]},
        0:{
            'a':['a',1,0],
            'b':['B',1,1],
            'B':['B',1,8]
        },
        1:{
            'a':['B',-1,2],
            'b':['B',-1,4],
            'B':['B',-1,6]
        },
        2:{'B':['a',1,3]},
        3:{'B':['B',1,1]},
        4:{'B':['b',1,3]},
        6:{'B':['B',-1,7]},
        7:{
            'a':['a',-1,7],
            'b':['b',-1,7],
            'B':['B',1,0]
        }
    }
    start = 5
    i = 0
    final = 8
    state = start
    tape = list('B'+string+'B')
    while state != final:
        change = machine[state][tape[i]]
        tape[i] = change[0]
        i = i + change[1]
        state = change[2]
    return ''.join(tape[i] for i in range(len(tape)))
def subtract_tm(string):
    machine = {
        0:{'B':['B',1,1]},
        1:{
            '0':['X',1,2],
            'B':['B',-1,6]
        },
        2:{
            '0':['0',1,2],
            'B':['B',1,3]
        },
        3:{
            'X':['X',1,3],
            '0':['X',-1,4],
            'B':['B',-1,10]
        },
        4:{
            'X':['X',-1,4],
            'B':['B',-1,5]
        },
        5:{
            '0':['0',-1,5],
            'X':['X',1,1]
        },
        6:{
            'X':['X',-1,6],
            'B':['B',1,7]
        },
        7:{
            'X':['B',1,7],
            'B':['B',1,8]
        },
        8:{
            'X':['B',1,8],
            '0':['0',1,8],
            'B':['B',1,9]
        },
        10:{
            'X':['B',-1,10],
            'B':['B',-1,11]
        },
        11:{
            'X':['B',-1,11],
            'B':['B',1,9]
        }
    }
    start = 0
    i = 0
    final = 9
    state = start
    tape = list('B'+string+'B')
    while state != final:
        change = machine[state][tape[i]]
        tape[i] = change[0]
        i = i + change[1]
        state = change[2]
    return ''.join(tape[i] for i in range(len(tape)))
def tm_02n(string):
    machine = {
        0:{'B':['B',1,1]},
        1:{
            'X':['X',1,1],
            'B':['B',-1,3],
            '0':['X',1,2]
        },
        2:{
            'X':['X',1,2],
            'B':['B',-1,4],
            '0':['0',1,1]
        },
        3:{
            'X':['X',-1,3],
            '0':['0',-1,3],
            'B':['B',1,1]
        },
        4:{
            'X':['X',-1,4],
            'B':['B',1,6],
            '0':['0',1,5]
        },
        5:{}
    }
    start = 0
    i = 0
    final = 6
    state = start
    tape = list('B'+string+'B')
    while True:
        try:
            change = machine[state][tape[i]]
            tape[i] = change[0]
            i = i + change[1]
            state = change[2]
            if state == final: return True
        except: return False
print('a^N b^N accepting Turing machine')
print('aaabbb',tm_2('aaabbb'))
print('aaabbba',tm_2('aaabbba'))
print('aaabb',tm_2('aaabb'))
print('aba',tm_2('aba'))
print('ab',tm_2('ab'))
print('',tm_2(''))
print('Palindrome accepting Turing machine')
print('abba',tm_3('abba'))
print('abbba',tm_3('abbbba'))
print('abbaabba',tm_3('abbaabba'))
print('aabb',tm_3('aabb'))
print('a^N b^N c^N accepting Turing machine')
print('abc',tm_4('abc'))
print('aaabbbccc',tm_4('aaabbbccc'))
print('aaabbccc',tm_4('aaabbccc'))
print('Addition Turing machine')
print('0B',add_tm('0B'))
print('000B00',add_tm('000B00'))
print('b-removal Turing machine')
print('aaaabbbaabbab',removeB_tm('aaaabbbaabbab'))
print('ababa',removeB_tm('ababa'))
print('aaa',removeB_tm('aaa'))
print('Subtraction Turing machine')
print('000B00',subtract_tm('000B00'))
print('000B000',subtract_tm('000B000'))
print('000B00000',subtract_tm('000B00000'))
print('B00000',subtract_tm('B00000'))
print('0B000',subtract_tm('0B000'))
print('0^(2^n) Turing machine')
print('0',tm_02n('0'))
print('00',tm_02n('00'))
print('000',tm_02n('000'))
print('0000',tm_02n('0000'))
print('00000000',tm_02n('00000000'))
print('000000',tm_02n('000000'))