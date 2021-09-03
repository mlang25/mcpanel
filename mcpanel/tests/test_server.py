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


def test_cmd(setup_module):
    assert requests.get(SERVER_URL+"/cmd/tps?key=" +
                        PASSWORD).status_code != 500
    time.sleep(2)

def test_unread(setup_module):
    res = requests.get(SERVER_URL+"/cmd/get_unread?key=" +
                       PASSWORD)
    assert res.status_code == 200
    assert len(res.content) != 0

def test_stop(setup_module):
    assert requests.get(SERVER_URL+"/cmd/stop?key=" +
                        PASSWORD).status_code != 500
    ser = MinecraftServer.lookup(SERVER_ADDRESS)
    try:
        time.sleep(2)
        res = ser.status()
    except ConnectionRefusedError:
        return True
    assert False
