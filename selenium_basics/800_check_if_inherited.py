def check_inheritance(obj, class_):
    return any(class_ in cls.__mro__ for cls in type(obj).__mro__)

if __name__=="__main__":
    class Base:
        pass
    a = Base()
    b = [1, 2]
    c = False
    for x in [a, b, c]:
        if check_inheritance(x, int):
            print(f"{x} was inherited from {int.__name__}")
        if check_inheritance(x, list):
            print(f"{x} was inherited from {list.__name__}")
        if check_inheritance(x, Base):
            print(f"{x} was inherited from {Base.__name__}")
        if check_inheritance(x, object):
            print(f"{x} was inherited from {object.__name__}")