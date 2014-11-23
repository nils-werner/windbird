import requests
from requests.auth import HTTPBasicAuth


def post(config, message):
    requests.post(
        "https://api.pushbullet.com/v2/pushes",
        data=dict(
            {
                'type': 'note',
                'title': 'Windbird',
                'body': message
            }.items() +
            config['target'].items()
        ),
        auth=HTTPBasicAuth(config['api']['key'], '')
    )
