# Interface
class PushNotificationInterface:
    def sendPushNotification(self, message: str):
        pass

# for IOS users
class IOSPushNotificationStrategy(PushNotificationInterface):
    def sendPushNotification(self, message: str):
        print("A message for Apple fanboys: ", message)

# for Android users
class AndroidPushNotificationStrategy(PushNotificationInterface):
    def sendPushNotification(self, message: str):
        print("Something cool for Android chads: ", message)

# for Windows users
class WindowsPushNotificationStrategy(PushNotificationInterface):
    def sendPushNotification(self, message: str):
        print("Another useless notification for Windows: ", message)

class PushNotificationContext:
    _notificationStrategy: PushNotificationInterface

    # Initialisation
    def __init__(self, strategy: PushNotificationInterface):
        self._notificationStrategy = strategy
    
    # changing strategy on runtime
    def setPushNotificationStrategy(self, strategy: PushNotificationInterface):
        self._notificationStrategy = strategy

    # send push notification through the set strategy
    def sendPushNotification(self, message: str):
        self._notificationStrategy.sendPushNotification(message)
    
# Mobile App Service (can also be considered as client)
class MobileApp:
    _context: PushNotificationContext

    def __init__(self, strategy: PushNotificationInterface):
        self._context = PushNotificationContext(strategy)
    
    def setPushNotificationStrategy(self, strategy: PushNotificationInterface):
        self._context.setPushNotificationStrategy(strategy)
    
    def sendPushNotification(self, message: str):
        self._context.sendPushNotification(message)

if __name__ == "__main__":

    # set default push notification service for IOS
    app = MobileApp( IOSPushNotificationStrategy() )
    app.sendPushNotification("Apple Sucks!")

    # change strategy to send to Android users
    app.setPushNotificationStrategy( AndroidPushNotificationStrategy() )
    app.sendPushNotification("Android Gigachads Rock!")

    # change strategy to windows, useless though
    app.setPushNotificationStrategy( WindowsPushNotificationStrategy() )
    app.sendPushNotification("This msg will be lost forever, never to be read.")






