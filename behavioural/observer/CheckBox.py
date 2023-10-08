# Observer interface
class CheckboxObserver:
    def onChange(self):
        pass

# Concrete Observer - update display state
class DisplayUpdater(CheckboxObserver):
    def onChange(self, checked: bool):
        print("Checkbox is now:", "checked" if checked else "unchecked")

# Concrete Observer - update database entry
class UpdateDatabase(CheckboxObserver):
    def onChange(self, checked: bool):
        print("Database updated with checkbox state as:", "checked" if checked else "unchecked")

# Subject Class - Checkbox
class CheckBox:
    def __init__(self):
        self._checked = False
        self._observers: CheckboxObserver = []

    def subscribe(self, observer: CheckboxObserver):
        self._observers.append(observer)

    def unsubscribe(self, observer: CheckboxObserver):
        self._observers.remove(observer)
    
    def getCheckState(self) -> bool:
        return self._checked
    
    def toggleCheck(self):
        self._checked = not self._checked

        for observer in self._observers:
            observer.onChange(self._checked)

# Client code
if __name__ == "__main__":

    checkbox = CheckBox()

    checkbox.subscribe( DisplayUpdater() )
    checkbox.subscribe( UpdateDatabase() )

    # Check
    checkbox.toggleCheck()

    # Uncheck
    checkbox.toggleCheck()
