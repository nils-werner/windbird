import re
import pytest
import requests
import httpretty
from contextlib import contextmanager
from windbird import forecast, twitter, telegram


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


@pytest.yield_fixture
def mock_telegram():
    with open("tests/telegram.json", "r") as myfile:
        data = myfile.read().replace('\n', '')

    with httpretty_enable():
        httpretty.register_uri(
            httpretty.POST,
            re.compile(
                "https://api\.telegram\.org/bot([0-9a-zA-Z_\-:]+)/sendMessage"
            ),
            body=data
        )
        yield


def test_forecast(mock_forecast, config_forecast):
    candidates = forecast.get_candidates(config_forecast)
    assert len(candidates) > 0


def test_twitter(mock_twitter, config_twitter):
    twitter.post(config_twitter, "test")


def test_telegram(mock_telegram, config_telegram):
    telegram.post(config_telegram, "test")
