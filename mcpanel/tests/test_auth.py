import requests
from test_config import *
import pytest
import subprocess
import time

@pytest.fixture(scope="module")
def setup_module():
    print("Starting Server")
    server = subprocess.Popen(["python3", "mcpanel/app.py"])
    time.sleep(1)
    yield
    print("Stopping Server")
    server.kill()
    print("Stopped Server")


def test_bad_login(setup_module):
    assert requests.get(SERVER_URL+"/login").status_code == 403


def test_login(setup_module):
    assert requests.get(SERVER_URL+"/login"+"?key=" +
                        PASSWORD).status_code == 200