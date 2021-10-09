class Dices:
    def __init__(self, amount_of_dices, target, range):
        self.amount_of_dices = amount_of_dices
        self.target = target
        self.range = range


    def amount_of_dices(self):
        return self.amount_of_dices

    def target(self):
        return self.target

    #def range(self):

        #return self.range

amount_of_dices = Dices(int(input("Choose amount of dices: ")), int(input("Choose your target: ")),  )


print(amount_of_dices.amount_of_dices)
