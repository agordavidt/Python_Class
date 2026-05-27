# Setters and Getters

class Robot():

    def __init__(self, name=None, build_year=None):
        self.name = name

    def hello(self):
        if self.name: # That is if a name is provided for the object
            print(f"Hello! My name is {self.name}")
        else:
            print(f"I am a robot without a name")
    
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_build_year(self, build_year):
        self.build_year = build_year

    def get_build_year(self):
        return self.build_year



    # use the above and then add build_year attribute as well.


x = Robot()
print(x.__dict__)

x.set_name('Julie')
x.set_build_year(2008)


print(f'Hello, my name is {x.get_name()}, I was built in {x.get_build_year()}')




