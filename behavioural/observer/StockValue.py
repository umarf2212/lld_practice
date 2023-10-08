# Observer interface
class StockValueObserver:
    def onValueChange(self, value: float):
        pass


# Concrete Observer - Change Graphs
class GraphUpdater(StockValueObserver):
    def onValueChange(self, value: float):
        print("Graph updated with value:", value)

# Concrete Observer - Trigger Email Service
class TriggerEmail(StockValueObserver):
    def onValueChange(self, value: float):
        print("Sending emails with new stock value:", value)

# Subject Class - Stock
class Stock:
    def __init__(self, initialvalue: int):
        self._value = initialvalue
        self._valueChangeObservers: StockValueObserver  = []
    
    def addValueChangeObserver(self, observer: StockValueObserver):
        self._valueChangeObservers.append(observer)
    
    def getValue(self) -> int:
        return self._value

    def setValue(self, newValue):
        self._value = newValue

        for observer in self._valueChangeObservers:
            observer.onValueChange(self._value)

# Client Code
    
if __name__ == "__main__":

    stock = Stock(100)

    stock.addValueChangeObserver( GraphUpdater() )
    stock.addValueChangeObserver( TriggerEmail() )

    stock.setValue(115)
    stock.setValue(85)
    