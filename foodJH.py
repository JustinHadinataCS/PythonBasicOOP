class foodPriceCalculatorJH:
    def __init__(self, food, amount):
        self.food = food
        self.amount = amount
        self.price = 0
        self.__priceListJH()
        self.totalCost = self.calculateTheCostJH()

    def __priceListJH(self):
        if self.food == 'Dry Cured Iberian Ham':
            self.price = 177.80
        elif self.food == 'Wagyu Steaks':
            self.price = 450.00
        elif self.food == 'Matsutake Mushrooms':
            self.price = 272.00
        elif self.food == 'Kopi Luwak Coffee':
            self.price = 306.50
        elif self.food == 'Moose Cheese':
            self.price = 487.20
        elif self.food == 'White Truffles':
            self.price = 3600.00
        elif self.food == 'Blue Fin Tuna':
            self.price = 3603.00
        elif self.food == 'Le Bonnotte Potatoes':
            self.price = 270.81
        else:
            self.price = 0.00

    def calculateTheCostJH(self):
        totalCost = self.price * self.amount
        return totalCost
