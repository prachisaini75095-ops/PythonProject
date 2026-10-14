class animal:
    a = 12
    def __init__(self,name):
        self.name = name

    def hello(self):
        print(f"how are you and my name is{self.name}")

    @classmethod #captures the location of class
    def details(cls):
        print(f"how are you and my name is {cls.a}")

    @staticmethod #it will not target any location
    def speak():
        print("how are you i am static method")
        

obj = animal("lion")
obj.details()