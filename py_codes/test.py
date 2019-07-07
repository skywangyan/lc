class Test:
    classAttr = 1
    classAttr2 = []
    def __init__(self, v):
        self.insAttr = v

t1 = Test(2)
t2 = Test(4)
print t1.insAttr
print t2.insAttr
print Test.classAttr
t1.classAttr2.append(2)
t1.classAttr = 3
print t1.classAttr
print t2.classAttr
print t1.classAttr2
print t2.classAttr2