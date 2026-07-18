class demo:
    value = 10

    def __init__(self,no1,no2):
        self.no1 = no1
        self.no2 = no2

    def fun(self):
        print(f"Inside fun\nNo1 : {self.no1}\nNo2 : {self.no2}")

    def gun(self):
        print(f"Inside gun\nNo1 : {self.no1}\nNo2 : {self.no2}")

obj1 = demo(11,21)
obj2 = demo(51,101)

obj1.fun()
obj2.fun()
obj1.gun()
obj2.gun()

'''
Output:
Inside fun
No1 : 11
No2 : 21
Inside fun
No1 : 51
No2 : 101
Inside gun
No1 : 11
No2 : 21
Inside gun
No1 : 51
No2 : 101
'''