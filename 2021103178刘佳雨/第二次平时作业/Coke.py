class Coke(object):
    """
    Coca-Cola tastes better than Pepsi.
    """
    def __init__(self, boo):
        self.boo = str(boo)

    def drink(self):
        tmp = "".join(f"I'd like {self.boo} bottles of coke-cola!")
        return tmp