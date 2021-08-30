import os


class console:
    def __init__(self):
        self.file_size = 0
        print("console init")

    def check_new_data(self):
        if self.file_size == 0:
            try:
                self.f = open('logs/latest.log', 'r')
            except OSError:
                print("Log file not found")
                exit()
        if os.path.getsize('logs/latest.log') > self.file_size:
            print("new file size", os.path.getsize('logs/latest.log'))
            print("old", self.file_size)
            return True
        return False

    def get_output(self):
        self.f.seek(self.file_size)
        diff = os.path.getsize('logs/latest.log')-self.file_size
        self.file_size = os.path.getsize('logs/latest.log')
        return self.f.read(diff)

    def __del__(self):
        self.f.close()
        print("destoryed")
