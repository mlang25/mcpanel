from config import START_PATH
import subprocess

#TODO: dynamic path for start.sh



class command():

    server_status = 'STOPPED'

    def start_server(self):
        if self.server_status == 'RUNNING':
            return False
        self.server = subprocess.Popen([START_PATH],
                                       stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE,
                                       universal_newlines=True,
                                       shell=True,
                                       text=True)
        self.server_status = "RUNNING"
        return True
    
    def send_command(self,cmd):
        if self.server_status == 'STOPPED' or self.__Get_status() == False:
            return False
        if cmd == "stop":
            self.stop_server()
            return True
        self.server.stdin.writelines(cmd+"\n")
        self.server.stdin.flush()
        return True
    
    def __Get_status (self):
        self.server.poll()
        if self.server.returncode == None:
            self.server_status = "RUNNING"
            return True
        else:
            self.server_status = "STOPPED"
            return False
    
    def stop_server(self):
        self.server.stdin.writelines("stop\n")
        self.server.stdin.flush()
        self.server_status = "STOPPED"
        return True