import json

from mongoengine import connect
from mongoengine import Document, StringField

connect('openfaastest2', host='mongodb://host.docker.internal/openfaastest2')

class User(Document):
    email = StringField(required=True)

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    args = json.loads(req)
    User(email=args['email']).save()

    return 'success'
