class Bottle:

    def _init_(self, fill, re_fill, empty):
        self.fill_status = fill
        self.re_fill = re_fill
        self.empty_status = empty

    def fill(self):
        return self.fill_status


class Glass(Bottle):

    def fill_glass(self):
        return f"Glass is filled with water by bottle: {self.fill()}"

class Pot(Glass):

    def refill_pot(self):
        return f"Pot is refilled with water by Glass: {self.re_fill}"


class C(Pot):

    def empty(self):
        return f"Now bottle is empty: {self.empty_status}"

# Create an instance of the Glass class
c = C("Full Water", "Put Water", "Now empty")
print(c.fill_glass())
c.empty()
