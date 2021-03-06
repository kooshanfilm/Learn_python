def p_decorate(func):
    def func_wrapper(self):
        return "<p>{0}</p>".format(func(self))

    return func_wrapper


class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name + " " + self.family


# my_person = Person()
# print my_person.get_fullname()


class Jupiter:

    def hello(name="james wood"):
        print("hello {}").format(name)

    def other(func):
        print("im here in other")
        print(func())
#
# j = Jupiter()
# j.other(Jupiter.hello())



