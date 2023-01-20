import json

from django.http import HttpResponse


def htmx_message_response(status, message, tag, **kwargs):
    data = {
        "messages": [
            {
                "message": message,
                "tags": tag,
            }
        ],
    }
    for key in kwargs:
        kwargs[key] = kwargs.get(key, None)
    data.update(kwargs)
    return HttpResponse(data, status=status, headers={"HX-Trigger": json.dumps(data)})
