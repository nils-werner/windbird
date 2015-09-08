import pytest


@pytest.fixture
def config_forecast():
    return {
        'date': {
            'days': {
                'from': 1,
                'to': 1,
            },
            'hours': {
                'from': 11,
                'to': 19,
            },
        },
        'fields': {
            'windSpeed': {
                'from': 3.4,
                'to': 19,
            },
            'temperature': {
                'from': 10,
                'to': 50,
            },
        },
        'api': {
            'key': 'f5df'
        },
        'latitude': 49.130833,
        'longitude': 10.935278,
    }


@pytest.fixture
def config_twitter():
    return {
        'api': {
            'key': 'ypPlR',
            'secret': 'ddpci',
        },
        'token': {
            'key': '26835546158-yHXFhG93Mb58aR',
            'secret': 'rNwPQ',
        },
    }


@pytest.fixture
def config_pushbullet():
    return {
        'api': {
            'key': 'IuAsn15',
        },
        'target': {
            'channel_tag': 'yadd',
        },
    }
