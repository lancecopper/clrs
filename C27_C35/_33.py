class SegPoint():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.segment = None
        self.left = None
        self.right = None
    def set_segment(self, segment):
        self.segment = segment
    def set_left(self):
        self.left = True
    def set_right(self):
        self.right = True
    def isleft(self):
        return self.left
    def isright(self):
        return self.right
class Segment():
    def __init__(self, left, right):
        if left.x >= right.x:
            left, right = right, left
        self.left = left
        self.right = right
        self.left.set_segment(self)
        self.right.set_segment(self)
        self.left.set_left()
        self.right.set_right()

def direction(p1, p2, p0):
    '''
    # if the result > 0, segment p0->p1 is in the clockwise 
    # direction of segment p0->p2
    '''
    return (p1.x - p0.x) * (p2.y - p0.y) - \
           (p2.x - p0.x) * (p1.y - p0.y)
def on_segment(pi, pj, pk):
    if min(pi.x, pj.x) <= pk.x <= max(pi.x, pj.x) and \
        min(pi.y, pj.y) <= pk.y <= max(pi.y, pj.y):
        return True
    else:
        return False
def segments_intersect(p1, p2, p3, p4):
    d1 = direction(p3, p4, p1)
    d2 = direction(p3, p4, p2)
    d3 = direction(p1, p2, p3)
    d4 = direction(p1, p2, p4)
    if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and \
        ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
        return True
    elif d1 == 0 and on_segment(p3, p4, p1):
        return True
    elif d2 == 0 and on_segment(p3, p4, p2):
        return True
    elif d3 == 0 and on_segment(p1, p2, p3):
        return True
    elif d4 == 0 and on_segment(p1, p2, p4):
        return True
    else:
        return False
def intersect(s1, s2):
    return segments_intersect(s1.left, s1.right, s2.left, s2.right)

def sort_endpoints(p):
    # unfinished
    pass


def any_segments_intersect(s):
    t = RBTree()
    endpoints = []
    for segment in s:
        endpoints.append(segment.left)
        endpoints.append(segment.right)
    endpoints = sort_endpoints(endpoints)
    for p in endpoints:
        if p.isleft():
            t.insert(p.segment)
            ta = t.above(s)
            tb = t.below(s)
            if ta and intersect(ta, s) or tb and intersect(tb, s):
                return True
        if p.isright():
            ta = t.above(s)
            tb = t.below(s)
            if ta and tb and intersect(ta, tb):
                return True
            t.delete(s)
    return False


def granham_scan:
    pass







