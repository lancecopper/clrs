import copy
def inversion_number(l):
    length = len(l)
    result = 0
    print(l)
    for i in range(length):
        for j in range(i + 1, length):
            if int(l[i]) > int(l[j]):
                result += 1
    return result

def calc_det(l):
    #print("calc", l)
    length = len(l)
    if length == 2:
        return l[0][0] * l[1][1] - l[0][1] * l[1][0]
    else:
        l0 = l[0]
        l.remove(l[0])
        result = 0
        for i in range(length):
            a = l0[i]
            temp_l = copy.deepcopy(l)
            for ll in temp_l:
                ll.remove(ll[i])
            #print("result += {} * {} * calc_det{}".format(a, pow(-1, i), temp_l))
            result += a * pow(-1, i) * calc_det(temp_l)
            #print(result)
        return result

def issingular(l):
    return calc_det(l) == 0

if __name__ == "__main__":
    print("test for inversin_number...")
    test_ls = [list(str(123)), list(str(132))]
    print(inversion_number(test_ls[0]))
    print(inversion_number(test_ls[1]))
    print()

    print("test for calc_det...")
    d = [[1,2,-4], [-2, 2, 1], [-3, 4, -2]]
    print("###", calc_det(d) == -14)
    d1 = [[3,1,-1,2], [-5,1,3,-4], [2,0,1,-1],[1,-5,3,-3]]
    print("###", calc_det(d1) == 40)



