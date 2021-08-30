from config import PASSWORD_HASHED
import hashlib


class authenticate():

    def CheckPassword(self, pwd):
        if pwd:
            pwd = hashlib.pbkdf2_hmac(
                'sha256',
                pwd.encode('utf-8'),
                bytes.fromhex(PASSWORD_HASHED[:64]),
                100000)
            if pwd == bytes.fromhex(PASSWORD_HASHED[64:]):
                return True
            else:
                return False
        return False
        
