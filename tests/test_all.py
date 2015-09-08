import re
import pytest
import requests
import httpretty
from contextlib import contextmanager
from windbird import forecast, pushbullet, twitter


@contextmanager
def httpretty_enable():
    httpretty.enable()
    yield
    httpretty.disable()
    httpretty.reset()


@pytest.yield_fixture
def mock_forecast():
    with open("tests/forecast.json", "r") as myfile:
        data = myfile.read().replace('\n', '')

    with httpretty_enable():
        httpretty.register_uri(
            httpretty.GET,
            re.compile(
                "https://api.forecast.io/forecast/([0-9a-f]+)/"
                "([0-9\.]+),([0-9\.]+)"
            ),
            body=data
        )
        yield


@pytest.yield_fixture
def mock_pushbullet():
    with open("tests/pushbullet.json", "r") as myfile:
        data = myfile.read().replace('\n', '')

    with httpretty_enable():
        httpretty.register_uri(
            httpretty.POST,
            "https://api.pushbullet.com/v2/pushes",
            body=data
        )
        yield


@pytest.yield_fixture
def mock_twitter():
    with open("tests/twitter.json", "r") as myfile:
        data = myfile.read().replace('\n', '')

    with httpretty_enable():
        httpretty.register_uri(
            httpretty.POST,
            "https://api.twitter.com/1.1/statuses/update.json",
            body=data
        )
        yield


def test_forecast(mock_forecast, config_forecast):
    candidates = forecast.get_candidates(config_forecast)
    assert len(candidates) > 0


def test_pushbullet(mock_pushbullet, config_pushbullet):
    pushbullet.post(config_pushbullet, "test")


def test_twitter(mock_twitter, config_twitter):
    twitter.post(config_twitter, "test")