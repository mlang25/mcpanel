import requests
from test_config import *
import pytest
import subprocess
import time
from mcstatus import MinecraftServer


@pytest.fixture(scope="module")
def setup_module():
    print("Starting Server")
    server = subprocess.Popen(["python3", "mcpanel/app.py"])
    time.sleep(1)
    yield server
    print("Stopping Server")
    server.kill()
    print("Stopped Server")


def test_start(setup_module):
    assert requests.get(SERVER_URL+"/start-server?key=" +
                        PASSWORD).status_code == 200
    time.sleep(70)
    ser = MinecraftServer.lookup(SERVER_ADDRESS)
    res = ser.status()
    assert res.latency > 0


def test_stop(setup_module):
    assert requests.get(SERVER_URL+"/cmd/stop?key=" +
                        PASSWORD).status_code != 500
    ser = MinecraftServer.lookup(SERVER_ADDRESS)
    try:
        time.sleep(2)
        res = ser.status()
    except ConnectionAbortedError:
        pass
