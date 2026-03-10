class Demo:      # classmethod can be called by class name or object
    @classmethod
    def show(cls):
        print("hi")
# calling by class name (recommended)
Demo.show()
# calling by object
d = Demo()
d.show()