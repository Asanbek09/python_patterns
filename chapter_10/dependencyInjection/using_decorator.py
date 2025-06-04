from typing import Protocol

class NotificationSender(Protocol):
    def send(self, message: str):
        """"Send a notification with the given message"""
        ...


def inject_sender(sender_cls):
    def decorator(cls):
        cls.sender = sender_cls()
        return cls
    
    return decorator

class EmailSender:
    def send(self, message: str):
        print(f"Sending Email: {message}")

class SMSSender:
    def send(self, message: str):
        print(f"Sending SMS: {message}")


#@inject_sender(EmailSender)
@inject_sender(SMSSender)
class NotificationService:
    sender: NotificationSender = None

    def notify(self, message):
        self.sender.send(message)


if __name__ == "__main__":
    service = NotificationService()
    service.notify("Hello, this is a test notification!")