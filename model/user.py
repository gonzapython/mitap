from customerrors.user import PasswordsNotEqual

class User(object):
    def log_in(self):
        print('estoy en el log in')
        
    def sign_in(self):
        print('Has elegido registrarte')
        username = input('Elige un nombre de usuario> ')
        password = input('Elige una contraseña')
        second_pass = input('Repite la contraseña')
        self._check_pass(password, second_pass)
    
    def _check_pass(self, first, second):
        if first != second:
            raise PasswordsNotEqual
