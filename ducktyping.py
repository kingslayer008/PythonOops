class Pycharm:
    def execute(self):
        print("Executing pycharm")

class Myeditor:
    def execute(self):
        print("Executing myeditor")

class Laptop:
    def code(self, ide):
        ide.execute()

ide = Myeditor()
l1 = Laptop()
l1.code(ide)

