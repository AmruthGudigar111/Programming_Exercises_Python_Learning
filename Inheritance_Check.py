#python class C inherits from class B which inherits from class A
class A:
    def __init__(self):
        print("A's constructor")
class B(A):
    def __init__(self):
        super().__init__()  # Call A's constructor
        print("B's constructor")
class C(B):
    def __init__(self):
        super().__init__()  # Call B's constructor
        print("C's constructor")