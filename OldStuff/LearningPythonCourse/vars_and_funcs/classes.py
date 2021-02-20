

class MyClass():
    def method1(self):
        print("myCalss method1")

    def method2(self, some_string):
        print("myCalss method2 " + some_string)

class AnotherClass(MyClass):
    def method1(self):
        MyClass.method1(self)
        print("\nAnotherCalss method1")

    def method2(self, some_string):
        print("AnotherCalss method2")

def main():
    c = MyClass()
    c.method1()
    c.method2("This is a string")

    ac = AnotherClass()
    ac.method1()
    ac.method2("This is a string")




if __name__ == '__main__':
    main()