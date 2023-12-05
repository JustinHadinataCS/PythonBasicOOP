from foodJH import foodPriceCalculatorJH

def createTheListJH():
    AfoodList = []
    numberOfItems = 0

    while numberOfItems < 1:
        try:
            numberOfItems = int(input('How many items will you order today?'))
            if numberOfItems < 1:
                print('Number of items must be at least 1')
        except ValueError:
            print('Please enter a valid number')

    for i in range(numberOfItems):
        print(f"Item #{i + 1}")
        foodName = input('Enter food:')
        foodAmount = float(input('Enter amount of pounds'))

        while foodAmount <= 0:
            foodAmount = float(input('Enter amount of pounds '))

        AfoodList.append(foodPriceCalculatorJH(foodName, foodAmount))
    return AfoodList

def displayListJH(foodList):
    print("Here's a summary of the items Purchased")
    print("---------------------------------------")

    for item in foodList:
        print(f"Item: {item.food}")
        print(f"Amount ordered: {item.amount} lbs")
        print(f"Price per pound: ${item.price:.2f}")
        print(f"Price of order:${item.totalCost:.2f}")
        print()

def totalJH(foodList):
    theTotalCost = sum(item.totalCost for item in foodList)
    print(f"Total cost: ${theTotalCost:.2f}")

def testMeJH():
    foodlist = createTheListJH()
    displayListJH(foodlist)
    totalJH(foodlist)

testMeJH()