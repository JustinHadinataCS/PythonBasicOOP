from foodJH import foodPriceCalculatorJH


def createTheListJH():
  foodList = []
  numberOfItems = int(input('Enter the number of items'))
  
  while numberOfItems > 1:
    print('It should be at least 1')
    numberOfItems = int(input('Enter the number of items'))

    for i in range(numberOfItems):
      print(f"it's your Items : {i} ")
      foodName = input('Enter the item name: ')
      foodAmount = float(input('Enter the amount of items in pound '))

      while foodAmount <= 0:
          foodAmount = float(input('Enter the amount of items in pound '))
  
      foodList.append(foodPriceCalculatorJH(foodName,foodAmount))
  return foodList


def displayListJH(foodList):
  print("Here's a summary of the items Purchased")
  print("---------------------------------------")

  for item in foodList:

    print(f"Item : {item.food}")
    print(f"Amount ordered: {item.amount} lbs")
    print(f"Price per pound: ${item.price}")
    print(f"Price per pound: ${item.totalCost}")


def totalJH(foodList):
    theTotalCost = 0
    for item in foodList:
       theTotalCost += item.totalCost
    print(f"the total cost : {theTotalCost}")



def testMe():
  foodlist = createTheListJH()
  testMe(foodlist)
  totalJH(foodlist)
  
