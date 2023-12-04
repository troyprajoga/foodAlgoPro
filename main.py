from classModule import FoodOrder


def FoodList():
    foodList = []
    while True:
        try:
            num_items = int(input("How many items will you order today? "))
            if num_items >= 1:
                break
            else:
                print("Number of items must be at least 1.")
        except ValueError:
            print("Please enter a valid number.")

    for i in range(num_items):
        foodName = input("Enter food: ")

        while True:
            try:
                orderAmt = float(input("Enter amount of pounds: "))
                if orderAmt > 0:
                    break
                else:
                    print("Amount of pounds must be greater than 0.")
            except ValueError:
                print("Please enter a valid number.")

        food_order = FoodOrder(foodName, orderAmt)
        foodList.append(food_order)

    return foodList


def DisplayFood(foodList):
    print("Here's a summary of the items purchased:")
    print("----------------------------------------")
    for order in foodList:
        print(f"Item: {order.food}")
        print(f"Amount Ordered: {order.amtFood} pounds")
        print(f"Price Per Pound: ${order.PriceList()}")
        print(f"Price of order: ${order.CalculateFood()}")
        print("\n")


def CalculateTotal(foodList):
    total = 0

    for order in foodList:
        total += order.CalculateFood()

    return total


def Main():
    orderList = FoodList()
    DisplayFood(orderList)
    total_cost = CalculateTotal(orderList)
    print(f"Total cost: ${total_cost}")


Main()