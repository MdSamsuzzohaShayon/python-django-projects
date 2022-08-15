import json

from django.db import models
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

# Create your models here.

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.TextField(max_length=100)
    is_seen = models.BooleanField(default=False)

    # Whenever we save the notification we will send notification
    def save(self, *args, **kwargs):
        # print("Saved called")
        # send data to frontend
        channel_layer = get_channel_layer()
        notification_obj_count = Notification.objects.all().count()
        data = {'count': notification_obj_count, 'current_notification': self.notification}
        async_to_sync(channel_layer.group_send)(
            'test_consumer_group', {
                'type': 'send_notification',
                'value': json.dumps(data)
            }
        )
        super(Notification, self).save(*args, **kwargs)

