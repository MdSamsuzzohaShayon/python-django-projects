from django.shortcuts import render
import time
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
from django.http import JsonResponse
from .thread import *

# Create your views here.
# http://localhost:8000/
async def home(request):
    for i in range(1, 10):
        channel_layer = get_channel_layer()
        data = {'count': i}
        await (channel_layer.group_send)(
            'new_consumer_group', {
                'type': 'send_notification',
                'value': json.dumps(data)
            }
        )
        time.sleep(1)

    return render(request, 'home.html')


# url example for this method http://localhost:8000/students/?total=5
def generate_student_data(request):
    total = request.GET.get('total')
    CreateStudentsThread(int(total)).start()
    return JsonResponse({"status": 200})