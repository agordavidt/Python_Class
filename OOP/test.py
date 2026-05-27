class Robot():
    # define attributes of an instance right after creation using __init__

    def __init__(self, name, brand, year=2025):
        self.name = name
        self.brand = brand
        self.year = year



x1 = Robot('anna','samsung', 2026)
x2 = Robot('leo','redmi')

# __dict__ stores the attributes of a class
# print(anna.__dict__)



def hello(obj):
    print(f"Hello, my name is {obj.name}.\nI was created in {obj.year} by {obj.brand}")


hello(x1)

hello(x2)


'''
* Encapsulation: building of data wiht the methods that operate on that data.
* Information Hiding: principle that some internal information or data is hidden so that it cannot be accidentally changed.

* Data Abstraction


'''
