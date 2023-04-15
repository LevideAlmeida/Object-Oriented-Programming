# Polymorphism - Methods with same signature
# (name, parameters and return),
# but diferentes behavior
from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, mensage) -> None:
        self.mensage = mensage

    @abstractmethod
    def send(self) -> bool: ...


class EmailNotification(Notification):
    def send(self) -> bool:
        print('Send E-mail -', self.mensage)
        return True

class SMSNotification(Notification):
    def send(self) -> bool:
        print('Send SMS -', self.mensage)
        return False


def notify(notificarion: Notification):
    notification_sent = notificarion.send()

    if notification_sent:
        print('Notification Sent')
    else:
        print('Notification Not Sent')

sms_notification = SMSNotification('Test SMS')
notify(sms_notification)

email_notification = EmailNotification('Test E-mail')
notify(email_notification)
