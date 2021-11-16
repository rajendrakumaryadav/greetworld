class hello_world:
    def __init__(self, name="World"):
        self.message = "Hello, {}!".format(name)

    def say_hello(self):
        return self.message
