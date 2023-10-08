# Observer Interface
class ClickListener:
    def onClick(self):
        pass

# Concrete Observer - Calculator
class Calculator(ClickListener):
    def onClick(self):
        print("Performing calculations...")
    
# Concrete Observer
class DisplayUpdater(ClickListener):
    def onClick(self):
        print("Updating display..")

# Subject Class - the Button
class Button:
    def __init__(self):
        self._clickListeners: ClickListener = []
    
    def attach(self, listener: ClickListener):
        self._clickListeners.append(listener)
    
    def detach(self, listener: ClickListener):
        self._clickListeners.remove(listener)

    def click(self):
        for listener in self._clickListeners:
            listener.onClick()

if __name__ == "__main__":

    button = Button()

    button.attach( DisplayUpdater() )
    button.attach( Calculator() )

    # Simulate click
    button.click()
    