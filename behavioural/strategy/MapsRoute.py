# Interface
class RouteCalculator:
    def calculateRoute(self, start, end):
        pass

# Fastest Route Strategy
class FastestRouteCalculator(RouteCalculator):
    def calculateRoute(self, start, end):
        return "Fastest route from " + start + " to " + end

# Shortest Route Strategy
class ShortestRouteCalculator(RouteCalculator):
    def calculateRoute(self, start, end):
        return "Shortest route from " + start + " to " + end

# Scenic Route Strategy
class ScenicRouteCalculator(RouteCalculator):
    def calculateRoute(self, start, end):
        return "Scenic route from " + start + " to " + end

# Context 
class RouteCalculatorContext:
    _calculator: RouteCalculator

    def __init__(self, calculator: RouteCalculator):
        self._calculator = calculator

    def calculateRoute(self, start, end):
        return self._calculator.calculateRoute(start, end)

# Client
class GoogleMaps:
    _context: RouteCalculatorContext

    # Setting an initial route calculator
    def __init__(self, calculator: RouteCalculator):
        self._context = RouteCalculatorContext(calculator)

    # Or set a different route on run time
    def setRouteCalculator(self, calculator: RouteCalculator):
        self._context = RouteCalculatorContext(calculator)

    # Client uses context's method as per the selected route strategy
    def calculateRoute(self, start, end):
        return self._context.calculateRoute(start, end)

if __name__ == "__main__":
    
    defaultRoute = FastestRouteCalculator()
    maps = GoogleMaps(defaultRoute)

    start = "New York"
    end = "Boston"

    fastest_route = maps.calculateRoute(start, end)
    print(fastest_route)

    # Change routing strategy on run time
    shortestRoute = ShortestRouteCalculator()
    maps.setRouteCalculator(shortestRoute)

    shortest_route = maps.calculateRoute(start, end)
    print(shortest_route)

    # User wants a beautiful scenic route instead
    scenicRoute = ScenicRouteCalculator()
    maps.setRouteCalculator(scenicRoute)

    scenic_route = maps.calculateRoute(start, end)
    print(scenic_route)





    

