class Demo:
    def show(self):
        print("instance show method")

    @classmethod
    def look(cls):
        print("class look method")

    @staticmethod
    def disp():
        print("disp static method")
d = Demo()
Demo().show()   # call by object
d.show()        # call by object reference
d.look()        # calling class method using object
Demo.look()     # calling class method using class
d.disp()        # calling static method using object
Demo.disp()     # calling static method using class