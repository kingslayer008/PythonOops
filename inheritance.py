class A:
    def __init__(self):
        print("inti of A")

    def feature1(self):
        print("Feat1 A")

class B:

    def __init__(self):
        print("init of B")

    def feature1(self):
        print("Feat1 B")

class C(A, B):

    def __init__(self):
        super().__init__()
        print("init of c")

    def feat(self):
        super().feature1()

c = C()
c.feat()

#Here the out will be init of A as the method resoultion order will be from left to right of inherited classes,
#as we inherit A first then B

