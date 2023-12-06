from django.http import StreamingHttpResponse
import time
import json

def sse(request):
    response = StreamingHttpResponse(streaming_content=sse_generator())
    response['Content-Type'] = 'text/event-stream'
    return response

def sse_generator():
    counter = 0
    while True:
        time.sleep(1)
        data = {"message": f"Evento número {counter}"}
        yield f"data: {json.dumps(data)}\n\n"
        counter += 1
