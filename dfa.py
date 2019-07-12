# A general DFA
def dfa_anystring(string):
    machine = {
        0:{
            'a':0,'b':0
        }
    }
    start = 0
    final = [0]
    state = start
    for elem in string: state = machine[state][elem]
    if state in final: return True
    else: return False
def dfa_2(string):
    machine = {
        0:{'a':2,'b':1},
        1:{'a':3,'b':0},
        2:{'a':0,'b':3},
        3:{'a':1,'b':2}
    }
    start = 0
    final = [1]
    state = start
    for elem in string: state = machine[state][elem]
    if state in final: return True
    else: return False
def dfa_3(string):
    machine = {
        0:{'a':5,'b':1},
        1:{'a':6,'b':2},
        2:{'a':7,'b':3},
        3:{'a':8,'b':4},
        4:{'a':9,'b':0},10:{'a':0,'b':11},
        5:{'a':10,'b':6},11:{'a':1,'b':12},
        6:{'a':11,'b':7},12:{'a':2,'b':13},
        7:{'a':12,'b':8},13:{'a':3,'b':14},
        8:{'a':13,'b':9},14:{'a':4,'b':10},
        9:{'a':14,'b':5}
    }
    start = 0
    final = [3,7,11]
    state = start
    for elem in string: state = machine[state][elem]
    if state in final: return True
    else: return False
def dfa_4(string):
    machine = {
        0:{'a':1,'b':0},
        1:{'a':2,'b':0},
        2:{'a':3,'b':6},
        3:{'a':6,'b':4},
        4:{'a':6,'b':5},
        5:{'a':5,'b':5},
        6:{'a':6,'b':6}
    }
    start = 0
    final = [5]
    state = start
    for elem in string: state = machine[state][elem]
    if state in final: return True
    else: return False
print('Now we are testing a DFA that accepts any string.')
print('abab',dfa_anystring('abab'))
print('Now we are testing a DFA that accepts strings with')
print('even number of \'a\'s and odd number of \'b\'s')
print('aba',dfa_2('aba'))
print('abb',dfa_2('abb'))
print('Now we are testing a DFA that accepts strings where')
print('|a| mod 3 + |b| mod 5 = 3, where |k| means number of \'k\'s')
print('ababababababbb',dfa_3('ababababababbb'))
print('abababb',dfa_3('abababb'))
print('Now we are testing a DFA that accepts strings')
print('in the regular language b*a(bb*a)*aabb(a+b)*')
print('ababaaabbbaba',dfa_4('ababaaabbbaba'))
print('abababba',dfa_4('abababba'))