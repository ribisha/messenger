

import pywhatkit as kit
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    if request.method == 'POST':
        message_content = request.POST.get('message')
        message_type = request.POST.get('message_type')

        now = datetime.now()

        try:
            if message_type == 'person':  
                recipient_number = request.POST.get('phone_number')
                kit.sendwhatmsg(
                    recipient_number,
                    message_content,
                    now.hour,
                    now.minute + 1  
                )
                return HttpResponse("Message to the person scheduled successfully! Check your WhatsApp.")

            elif message_type == 'group':  
                group_code = request.POST.get('group_code')
                kit.sendwhatmsg_to_group(
                    group_code,
                    message_content,
                    now.hour,
                    now.minute + 1  
                )
                return HttpResponse("Message to the group scheduled successfully! Check your WhatsApp.")
            else:
                return HttpResponse("Invalid message type selected.")

        except Exception as e:
            return HttpResponse(f"Failed to send message: {str(e)}")

    return render(request, 'index.html')

def need_help(request):
    return render(request, 'need_help.html')
