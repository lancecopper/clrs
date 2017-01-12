import random

def high(x, u):
    return x // int(pow(u, 0.5))

def low(x, u):
    return x % int(pow(u, 0.5))

def index(x, y, u):
    return x * int(pow(u, 0.5)) + y

class ProtoVEB():
    def __init__(self, u):
        self.u = u
        self.n = None
        self.summary = None
        self.cluster = None
    def member(self, x):
        return proto_veb_member(self, x)
    def minimum(self):
        return proto_veb_minimum(self)
    def maximum(self):
        return proto_veb_maximum(self)
    def successor(self, x):
        return proto_veb_successor(self, x)
    def predecessor(self, x):
        return proto_veb_predecessor(self, x)
    def insert(self, x):
        proto_veb_insert(self, x)
    def delete(self, x):
        proto_veb_delete(self, x)


def proto_veb_member(veb, x):
    if veb.u == 2:
        return veb.cluster[x]
    else:
        return proto_veb_member(veb.cluster[high(x, veb.u)], low(x, veb.u))

def proto_veb_minimum(veb):
    if veb.u == 2:
        if veb.cluster[0] == 1:
            return 0
        elif veb.cluster[1] == 1:
            return 1
        else:
            return None
    else:
        min_cluster = proto_veb_minimum(veb.summary)
        if min_cluster is None:
            return None
        else:
            offset = proto_veb_minimum(veb.cluster[min_cluster])
            return index(min_cluster, offset, veb.u)

def proto_veb_maximum(veb):
    if veb.u == 2:
        if veb.cluster[1] == 1:
            return 1
        elif veb.cluster[0] == 1:
            return 0
        else:
            return None
    else:
        max_cluster = proto_veb_maximum(veb.summary)
        if max_cluster is None:
            return None
        else:
            offset = proto_veb_maximum(veb.cluster[max_cluster])
            return index(max_cluster, offset, veb.u)


def proto_veb_successor(veb, x):
    if veb.u == 2:
        if x == 0 and veb.cluster[1] == 1:
            return 1
        else:
            return None
    else:
        offset = proto_veb_successor(veb.cluster[high(x, veb.u)], low(x, veb.u))
        if offset is not None:
            return index(high(x, veb.u), offset, veb.u)
        else:
            succ_cluster = proto_veb_successor(veb.summary, high(x, veb.u))
            if succ_cluster is None:
                return None
            else:
                offset = proto_veb_minimum(veb.cluster[succ_cluster])
                return index(succ_cluster, offset, veb.u)


def proto_veb_predecessor(veb, x):
    if veb.u == 2:
        if x == 1 and veb.cluster[0] == 1:
            return 0
        else:
            return None
    else:
        offset = proto_veb_predecessor(veb.cluster[high(x, veb.u)], low(x, veb.u))
        if offset is not None:
            return index(high(x, veb.u), offset, veb.u)
        else:
            pred_cluster = proto_veb_predecessor(veb.summary, high(x, veb.u))
            if pred_cluster is None:
                return None
            else:
                offset = proto_veb_maximum(veb.cluster[pred_cluster])
                return index(pred_cluster, offset, veb.u)

def proto_veb_insert(veb, x):
    veb.n += 1
    if veb.u == 2:
        veb.cluster[x] = 1
    else:
        proto_veb_insert(veb.cluster[high(x, veb.u)], low(x, veb.u))
        proto_veb_insert(veb.summary, high(x, veb.u))

def proto_veb_delete(veb, x):
    veb.n -= 1
    if veb.u == 2:
        if veb.cluster[x] == 1:
            veb.cluster[x] = 0
        else:
            raise ValueError("x not in veb!")
    else:
        cluster = veb.cluster[high(x, veb.u)]
        proto_veb_delete(cluster, low(x, veb.u))
        if cluster.n == 1:
            proto_veb_delete(veb.summary, high(x, veb.u))



def generate_protoveb(gath):
    #print("generage_protoveb:", gath)
    u = len(gath)
    new_proto_veb = ProtoVEB(u)
    new_proto_veb.n = 0
    for i in gath:
        if i:
            new_proto_veb.n += 1
    if u == 2:
        new_proto_veb.cluster = gath
    else:
        cluster = []
        interval = int(pow(u, 0.5))
        for i in range(interval):
            sub_gath = gath[i * interval: i * interval + interval]
            temp = generate_protoveb(sub_gath)
            cluster.append(temp)
        summary = generate_summary_from_cluster(cluster)  
        new_proto_veb.cluster = cluster
        new_proto_veb.summary = summary
    #print("completely generate protoveb :", new_proto_veb.u, new_proto_veb.summary, new_proto_veb.cluster)
    return new_proto_veb

def generate_summary_from_cluster(cluster):
    u = len(cluster)
    gath = []
    if u == 2:
        for veb in cluster:
            if sum(veb.cluster):
                gath.append(1)
            else:
                gath.append(0)
    else:
        for veb in cluster:
            gath.append(summarize(veb.summary))
    return generate_protoveb(gath)

def summarize(summary):
    if summary.u == 2 and sum(summary.cluster):
        return 1
    elif summary.u == 2:
        return 0
    else:
        return summarize(summary.summary)

def print_veb(veb):
    if veb.u == 2:
        for i in veb.cluster:
            print(i, end = "")
    else:
        for i in veb.cluster:
            print_veb(i)        


if __name__ == "__main__":
    k = 3
    u = pow(2, pow(2, k))
    a = [0] * u
    '''
    elements = [2, 3, 4, 5, 7, 14, 15]
    '''
    elements = []
    for i in range(100):
        elements.append(random.randint(0, 255))
    elements = list(set(elements))
    elements.sort()
    print("length:", len(elements))
    for i in elements:
        a[i] = 1
    print(a)
    veb = generate_protoveb(a)
    print("veb.u :", veb.u)
    print("veb.n :", veb.n)
    print("veb.summary :", end = "    ")
    print_veb(veb.summary)
    print()
    print("veb.cluster :", end = "    ")
    for i in veb.cluster:
        print_veb(i)
    print()

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
        pred = veb.predecessor(temp_ele)
        succ = veb.successor(temp_ele)
        if succ != elements[temp_index + 1] or pred != elements[temp_index - 1]:
            print("successor and predecessor test Failed!!!#####")


    print("insert and delete test...")
    for ele in elements:
        veb.delete(ele)
    for ele in elements:
        veb.insert(ele)

    print("successor and predecessor test...")
    for i in range(100):
        temp_index = random.randint(1, len(elements) - 2)
        temp_ele = elements[temp_index]
        pred = veb.predecessor(temp_ele)
        succ = veb.successor(temp_ele)
        if succ != elements[temp_index + 1] or pred != elements[temp_index - 1]:
            print("successor and predecessor test Failed!!!#####")





