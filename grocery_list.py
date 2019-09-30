class GroceryList:
    def __init__(self):
        self.groceries = {}

    def removeItem(self, description):
        self.groceries.pop(description, 0)

    def changeQuantity(self, description, newQuantity):
        if self.groceries.get(description) is None:
            return
        self.groceries[description] = newQuantity

    def addItem(self, description, quantity):
        prevQuantity = self.groceries.pop(description, 0)
        self.groceries[description] = prevQuantity + quantity

    def getList(self):
        result = ""
        for grocery in self.groceries:
            result += "{}: {}\n".format(grocery, self.groceries[grocery])
        return result


if __name__ == '__main__':
    groceryList = GroceryList()
    groceryList.addItem("egg", 24)
    groceryList.addItem("egg", 12)
    groceryList.addItem("tomato", 2)

    print(groceryList.getList())
    groceryList.removeItem('egg')
    groceryList.changeQuantity("tomato", 1)
    print(groceryList.getList())

