import hashlib

import models


class User(models.Model):

    username = models.String()
    _password = models.String()
    age = models.Integer()

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pw):
        if hasattr(pw, 'encode'):
            pw = pw.encode('ascii')
        pw_hash = hashlib.sha256(pw).hexdigest()
        self._password = pw_hash

    def check_password(self, pw):
        if hasattr(pw, 'encode'):
            pw = pw.encode('ascii')
        pw_hash = hashlib.sha256(pw).hexdigest()
        return pw_hash == self._password
