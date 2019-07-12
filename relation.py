# An example of a set
set_def = [1,2,3,4,5,6,7,8,9]
# An instance of a subset of 'set_def'
sub_set = [3,4,5,6]
# Instances of a relation with 'set_def'
relation_1 = {
    1:[1,2,3,4,5,6,9],
    2:[2],
    3:[2,3,4,5,6,9],
    4:[2,4],
    5:[2,4,5],
    6:[2,4,6],
    7:[1,2,3,4,5,6,7,9],
    8:[8],
    9:[2,4,9]
}
relation_2 = {
    1:[1,2,3,4,5,6,9],
    2:[2],
    3:[2,3,4,5,6,9],
    4:[2,4],
    5:[2,4,5],
    6:[2,4,5,6,9],
    7:[1,2,3,4,5,6,7,9],
    8:set_def,
    9:[2,4,5,9]
}
relation_3 = {
    1:[2,3,4,5,6,9],
    2:[],
    3:[2,4,5,6,9],
    4:[2],
    5:[2,4],
    6:[],
    7:[1,2,3,4,5,6,9],
    8:[],
    9:[2,4]
}
def subset_gen(S):
    A = []
    for num in range(2**len(S)):
        num_temp,Q = num,[]
        for k in range(len(S)):
            if num_temp % 2: Q.append(S[k])
            num_temp = num_temp / 2
        A.append(Q)
    return A
def irreflex(A,R):
    flag = True
    for i in A:
        if i in R: flag = flag and not(i in R[i])
        if not flag:
            print(i,'in reflex: Not an antireflexive relation')
            return flag
    print('The relation is anti-reflexive')
    return flag
def connex(A,R):
    flag = True
    for i in A:
        for j in A:
            if i!=j: flag = flag and (j in R[i] or i in R[j])
            if not flag:
                print(i,j,'intertwined in connex')
                return flag
    print('The relation is connex.')
    return flag
def antisymm(A,R):
    for i in A:
        if i not in R:
            print(i,'not in relation antisymmetry error')
            return False
        else:
            for j in R[i]:
                if i in R[j] and j!=i:
                    print(i,'intertwined with',j,'Antisymmetric failed')
                    return False
    print('The relation is antisymmetric.')
    return True
def transitive(A,R):
    for i in A:
        if i not in R:
            print(i,'not in relation transitivity error')
            return False
        else:
            for j in R[i]:
                for k in R[j]:
                    if k not in R[i]:
                        print(i,j,k,'transitivity error')
                        return False
    print('The relation is transitive.')
    return True
def reflexive(A,R):
    for i in A:
        if i not in R:
            print(i,'not in relation reflexivity error')
            return False
        else:
            if i not in R[i]:
                print(i,'not in relation reflexivity error')
                return False
    print('The relation is reflexive.')
    return True
def poset(A,R):
    flag = [antisymm(A,R),transitive(A,R),reflexive(A,R)]
    if flag[0] and flag[1] and flag[2]:
        print('The relation is a poset')
    else: print('The relation is not a poset')
def total_order(A,R):
    flag = [connex(A,R),transitive(A,R),reflexive(A,R)]
    if flag[0] and flag[1] and flag[2]:
        print('The relation is in total order')
    else: print('The relation is not a total order')
def quasi_order(A,R):
    flag = [irreflex(A,R),transitive(A,R)]
    if flag[0] and flag[1]:
        print('The relation is in quasi-order')
    else: print('The relation is not in quasi-order')
def least_element(S,R):
    least_element = []
    for s in S:
        flag = True
        for b in S:
            if b!=s: flag = flag and b in R[s]
        if flag: least_element.append(s)
    return least_element
# is least element of an poset unique?
def greatest_element(S,R):
    greatest_element = []
    for g in S:
        flag = True
        for b in S:
            if b!=g: flag = flag and g in R[b]
        if flag: greatest_element.append(g)
    return greatest_element
# is greatest element of an poset unique?
def well_ordered(A,R):
    Q,flag = subset_gen(A),True
    for S in Q:
        if len(S) != 0:
            extract = least_element(S,R)
            flag = flag and len(extract)>0
            if not flag:
                print('The chain is not well ordered for',S,'in',A)
                break
    if flag: print('The chain is well ordered')
print('Testing poset property for relation 1')
poset(set_def,relation_1)
print('Testing total order property for relation 2')
total_order(set_def,relation_2)
print('Testing poset property for relation 2')
poset(set_def,relation_2)
# Relation 3 is a quasi-order relation from relation 1 just by removing reflexivity
print('Testing quasi-order for relation 3')
quasi_order(set_def,relation_3)
print('The least element of subset',sub_set,'in relation 1 is',least_element(sub_set,relation_1))
print('The greatest element of subset',sub_set,'in relation 1 is',greatest_element(sub_set,relation_1))
# Testing well ordered total set
print('Testing well ordered property in relation 2')
well_ordered(set_def,relation_2)