class FoodOrder:
    def __init__(self,food,amtFood):
        self.food = food
        self.amtFood = amtFood
        self.__calculatedPrice = self.CalculateFood()
        self.__priceFood = self.PriceList()


    def PriceList(self):
        if self.food == "Dry Cured Iberian Ham":
            self.__priceFood = 177.80
        elif self.food == "Wagyu Steaks":
            self.__priceFood = 450.00
        elif self.food == "Matsutake Mushrooms":
            self.__priceFood = 272.00
        elif self.food == "Kopi Luwak Coffee":
            self.__priceFood = 306.50
        elif self.food == "Moose Cheese":
            self.__priceFood = 487.20
        elif self.food == "White Truffles":
            self.__priceFood = 3600.00
        elif self.food == "Blue Fin Tuna":
            self.__priceFood = 3603.00
        elif self.food == "Le Bonnotte Potatoes":
            self.__priceFood = 270.81
        else:
            self.__priceFood = 0
        return self.__priceFood

    def CalculateFood(self):
        return round(self.amtFood * self.PriceList(),2)

