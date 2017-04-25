class TestAct(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def hello(self):
        print("This is hello function of TestAct class")
        pass

    def validate(self):
        print("This is validate function of TestAct class")
        pass

    def execute(self):
        print("This is execute method of testAct class")
        pass
