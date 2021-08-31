from flask import Flask, request

from auth import authenticate
from send_cmd import command
from get_console import console
import time

app = Flask(__name__, instance_relative_config=True)


class mcpanel():
    def __init__(self):
        self.auth = authenticate()
        self.cmd = command()
        self.con = console()

    def start_server(self):
        if self.auth.CheckPassword(request.args.get('key')) == True:
            if self.cmd.start_server():
                return "OK", 200
        return "Access Denied", 403


    def Cmd(self,command):
        if self.auth.CheckPassword(request.args.get("key")) == True:
            if self.cmd.send_command(command):
                if command == "stop":
                    self.__init__()
                    return "OK", 200
                if self.con.check_new_data():
                    return self.con.get_output(), 200
                else:
                    return "No Data", 204
        return "Access Denied", 403
    
    def get_unread(self):
        if self.auth.CheckPassword(request.args.get('key')) == True:
            if self.con.check_new_data():
                return self.con.get_output(), 200
            return "No Data", 204

    def login(self):
        if self.auth.CheckPassword(request.args.get('key')) == True:
            return "OK", 200
        return "Wrong Password", 403

Mcpanel = mcpanel()

@app.route('/start-server')
def start():
    return Mcpanel.start_server()

@app.route('/cmd/<command>')
def send_command(command):
    return Mcpanel.Cmd(command)

@app.route('/get_unread')
def get_unread():
    return Mcpanel.get_unread()

@app.route('/login')
def login():
    return Mcpanel.login()


app.run()
