from django.test import TestCase
from django.utils import timezone
from hello.models import LogMessage
import datetime

class LogMessageModelTest(TestCase):

    def create_logmessage(self, message="Test mesage"):
        """
        Arrange
        Create and reture
        """
        return LogMessage.objects.create(
            message=message,
            log_date=timezone.now()
        )

    def test_logmessage_creation(self):
        """
        Act
        test creation of log message insgtance
        """
        log_message = self.create_logmessage()
        self.assertTrue(isinstance(log_message, LogMessage))

    def test_logmessage_data(self):
        #
        log_message = self.create_logmessage()
        date = timezone.localtime(log_message.log_date)

        expected_message =  f"'{log_message.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"
        self.assertEquals(str(log_message), expected_message)