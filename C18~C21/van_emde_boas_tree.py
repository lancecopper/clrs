import math, random

def up_root(u):
    return u // down_root(u)
def down_root(u):
    log2u = int(math.log(u, 2))
    return pow(2, log2u // 2)
def high(x, u):
    return x // down_root(u)
def low(x, u):
    return x % down_root(u)
def index(x, y, u):
    return x * down_root(u) + y

class ProtoVEB():
    def __init__(self, u):
        self.u = u
        self.n = None
        self.summary = None
        self.cluster = None
        self.max = None
        self.min = None
    def member(self, x):
        return veb_member(self, x)
    def minimum(self):
        return veb_minimum(self)
    def maximum(self):
        return veb_maximum(self)
    def successor(self, x):
        return veb_successor(self, x)
    def predecessor(self, x):
        return veb_predecessor(self, x)
    def insert(self, x):
        veb_insert(self, x)
    def delete(self, x):
        veb_delete(self, x)

def veb_member(veb, x):
    if x == veb.min or x == veb.max:
        return True
    elif veb.u == 2:
        return False
    else:
        return veb_member(veb.cluster[high(x, veb.u)], low(x, veb.u))

def veb_minimum(veb):
    return veb.min
def veb_maximum(veb):
    return veb.max

def veb_successor(veb, x):
    '''
    print("veb_successor...:", veb.u, x)
    print("max and min...:", veb.max, veb.min)
    if veb.summary:
        print("veb.summary...", veb.summary.max, veb.summary.min)
    for i in range(0, veb.u):
        if veb.member(i):
            print("member", i)
    '''
    if veb.u == 2:
        #print("enter 1...")
        if x == 0 and veb.max == 1:
            return 1
        else:
            return None
    elif veb.min is not None and x < veb.min:
        #print("enter 2...")
        return veb.min
    else:
        #print("enter 3...")
        max_low = veb_maximum(veb.cluster[high(x, veb.u)])
        #print("maxlow", max_low, low(x, veb.u))
        if max_low is not None and low(x, veb.u) < max_low:
            '''
            print("$$$enter 31...")
            print("$$$maxlow", max_low, low(x, veb.u))
            print("$$$", veb.cluster[high(x, veb.u)].member(low(x, veb.u)))
            '''
            offset = veb_successor(veb.cluster[high(x, veb.u)], low(x, veb.u))
            #print("$$$offset", offset)
            return index(high(x, veb.u), offset, veb.u)
        else:
            #print("enter 32...")
            #print("$$$veb.summary", veb.summary.max, veb.summary.min)
            succ_cluster = veb_successor(veb.summary, high(x, veb.u))
            if succ_cluster is None:
                #print("enter 321...")
                return None
            else:
                #print("enter 322...")
                offset = veb_minimum(veb.cluster[succ_cluster])
                return index(succ_cluster, offset, veb.u)
def veb_predecessor(veb, x):
    if veb.u == 2:
        if x == 1 and veb.min == 0:
            return 0
        else:
            return None
    elif veb.max is not None and x > veb.max:
        return veb.max
    else:
        min_low = veb_minimum(veb.cluster[high(x, veb.u)])
        if min_low is not None and low(x, veb.u) > min_low:
            offset = veb_predecessor(veb.cluster[high(x, veb.u)], low(x, veb.u))
            return index(high(x, veb.u), offset, veb.u)
        else:
            pred_cluster = veb_predecessor(veb.summary, high(x, veb.u))
            if pred_cluster is None:
                if veb.min is not None and x > veb.min:
                    return veb.min
                else:
                    return None
            else:
                offset = veb_maximum(veb.cluster[pred_cluster])
                return index(pred_cluster, offset, veb.u)

def veb_empty_insert(veb, x):
    veb.min = x
    veb.max = x

def veb_insert(veb, x):
    #print("veb_insert", x)
    if veb.min is None:
        #print("enter 1...")
        veb_empty_insert(veb, x)
    else:
        #print("enter 2...")
        if x < veb.min:
            #print("enter 21...")
            x, veb.min = veb.min, x
        if veb.u > 2:
            #print("enter 22...")
            if veb_minimum(veb.cluster[high(x, veb.u)]) is None:
                #print("enter 221...")
                veb_insert(veb.summary, high(x, veb.u))
                veb_empty_insert(veb.cluster[high(x, veb.u)], low(x, veb.u))
            else:
                #print("enter 222...")
                veb_insert(veb.cluster[high(x, veb.u)], low(x, veb.u))
        if x > veb.max:
            #print("enter 23...")
            veb.max = x

def veb_delete(veb, x):
    if not veb_member(veb, x):
        raise ValueError("ele not in this veb_tree!!!")
    if veb.min == veb.max:
        veb.min = None
        veb.max = None
    elif veb.u == 2:
        if x == 0:
            veb.min = 1
        else:
            veb.min = 0
        veb.max = veb.min
    else:
        if x == veb.min:
            first_cluster = veb_minimum(veb.summary)
            x = index(first_cluster, 
                      veb_minimum(veb.cluster[first_cluster]), veb.u)
            veb.min = x
        veb_delete(veb.cluster[high(x, veb.u)], low(x, veb.u))
        if veb_minimum(veb.cluster[high(x, veb.u)]) is None:
            veb_delete(veb.summary, high(x, veb.u))
            #这里x的可能来源有两个，一个是作为函数参数来的，另一个是新晋的veb.min。
            if x == veb.max:
                summary_max = veb_maximum(veb.summary)
                if summary_max is None:
                    #是否因为新晋的min而导致整个veb中只有一个元素veb.min=veb.max
                    veb.max = veb.min
                else:
                    #作为函数参数的x恰好是之前的veb.max
                    veb.max = index(summary_max,
                        veb_maximum(veb.cluster[summary_max]), veb.u)
        elif x == veb.max:
            veb.max = index(high(x, veb.x),
                veb_maximum(veb.cluster[high(x, veb.u)]), veb.u)



def generate_veb(gath):
    #print("generage_veb:", gath)
    u = len(gath)
    new_veb = ProtoVEB(u)
    if u == 2:
        if gath == [1, 1]:
            new_veb.max = 1
            new_veb.min = 0
        elif gath == [1, 0]:
            new_veb.max = new_veb.min = 0
        elif gath == [0, 1]:
            new_veb.max = new_veb.min = 1
    else:
        eles = []
        for i in range(u):
            if gath[i]:
                eles.append(i)
        if len(eles):
            max_ele = max(eles)
            min_ele = min(eles)
            new_veb.max = max_ele
            new_veb.min = min_ele
            gath[min_ele] = 0
        cluster = []
        interval = down_root(u)
        for i in range(up_root(u)):
            sub_gath = gath[i * interval: i * interval + interval]
            temp = generate_veb(sub_gath)
            cluster.append(temp)
        summary = generate_summary_from_cluster(cluster)
        '''
        if summary.max is None and new_veb.max != new_veb.min:
            print("length:", u)
            print("max and min", new_veb.max, new_veb.min)
            print("summary:", summary.max, summary.min) 
            print("cluster...")
            for t_veb in cluster:
                print(t_veb.max, t_veb.min)
        '''
        new_veb.cluster = cluster
        new_veb.summary = summary
    return new_veb

def generate_summary_from_cluster(cluster):
    u = len(cluster)
    gath = []
    for veb in cluster:
        if veb.max is None:
            gath.append(0)
        else:
            gath.append(1)
    return generate_veb(gath)
  

if __name__ == "__main__":
    k = 8
    #k = 4
    u = pow(2, k)
    a = [0] * u
    elements = [2, 3, 4, 5, 7, 14, 15]
    elements = []
    for i in range(100):
        elements.append(random.randint(0, 255))
    elements = list(set(elements))
    elements.sort()

    for i in elements:
        a[i] = 1
    veb = generate_veb(a)
    
    '''   
    print("veb.u :", veb.u)
    print("veb.max :", veb.max)
    print("veb.min :", veb.min)
    print(len(veb.cluster))
    '''
    print("member_test...")
    for ele in elements:
        if not veb.member(ele):
            print("member_test Failed!!!#####")

    print("maximum and minimum test...")
    print(veb.minimum() is min(elements))
    print(veb.maximum() is max(elements))

    print("successor and predecessor test...")
    for i in range(100):
        temp_index = random.randint(1, len(elements) - 2)
        temp_ele = elements[temp_index]
        #print("*****", veb.member(elements[temp_index + 1]))
        pred = veb.predecessor(temp_ele)
        succ = veb.successor(temp_ele)
        if succ != elements[temp_index + 1] or pred != elements[temp_index - 1]:
            print("successor and predecessor test Failed!!!#####")    
    
    print("insert and delete test...")
    for ele in elements:
        veb.delete(ele)
    for ele in elements:
        veb.insert(ele)
        if not veb.member(ele):
            print("member_test Failed!!!#####")
        
    t_ele = []
    print("member_test...")
    for ele in elements:
        if not veb.member(ele):
            print("member_test Failed!!!#####")
            print(ele)

    
    print("successor and predecessor test...")
    for i in range(100):
        temp_index = random.randint(1, len(elements) - 2)
        temp_ele = elements[temp_index]
        pred = veb.predecessor(temp_ele)
        succ = veb.successor(temp_ele)
        if succ != elements[temp_index + 1] or pred != elements[temp_index - 1]:
            print("successor and predecessor test Failed!!!#####")  
    



