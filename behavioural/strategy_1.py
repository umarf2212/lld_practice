# Interface
class ShippingCostCalculator:
    def calculateShippingCost(totalPrice):
        pass

# Free Shipping
class FreeShippingCostCalculator(ShippingCostCalculator):
    def calculateShippingCost():
        return 0

# Fixed Shipping
class FixedShippingCostCalculator(ShippingCostCalculator):
    def __init__(self, fixedShippingCost):
        self._fixedShippingCost = fixedShippingCost

    def calculateShippingCost(self):
        return self._fixedShippingCost

# Percentage Shipping
class PercentageShippingCostCalculator(ShippingCostCalculator):
    def __init__(self, percentageShippingCost):
        self._percentageShippingCost = percentageShippingCost

    def calculateShippingCost(self, totalPrice):
        return totalPrice * (self._percentageShippingCost/100)

class ShippingCostContext:
    _calculator: ShippingCostCalculator

    def __init__(self, calculator: ShippingCostCalculator):
        self._calculator = calculator
    
    def calculateShippingCost(self, totalPrice):
        return self._calculator.calculateShippingCost(totalPrice)

class Product:
    def __init__(self, productName, productPrice):
        self.productName = productName
        self.productPrice = productPrice
    
class ShoppingCart:
    _products = {}

    def addProduct(self, product: Product):
        self._products[product.productName] = product.productPrice
    
    def removeProduct(self, productName):
        del self._products[productName]

    def getTotalPrice(self) -> int:
        return sum(self._products.values())

    def getShippingCost(self, calculator: ShippingCostCalculator):
        totalPrice = self.getTotalPrice()
        context = ShippingCostContext(calculator)
        return context.calculateShippingCost(totalPrice)

if __name__ == "__main__":

    Product1 = Product("Donut", 10.0)
    Product2 = Product("Pie", 20.0)
    Product3 = Product("Pizza", 20.0)

    cart = ShoppingCart()
    cart.addProduct(Product1)
    cart.addProduct(Product2)
    cart.addProduct(Product3)

    totalPrice = cart.getTotalPrice()
    shippingCost = cart.getShippingCost(PercentageShippingCostCalculator(10))
    netPrice = totalPrice + shippingCost

    print("Total Price of the cart items:", totalPrice)
    print("Shipping cost (10% of total cost)", shippingCost)
    print("Net payable amount:", netPrice)

