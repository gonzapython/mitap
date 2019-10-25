from controller.user import UserController

class UserView(object):
    def show_welcome(self):
        selection = int(input('Bienvenido, presiona 1 para logearte, si no tienes cuenta presiona 2 >  '))
        if selection == 1:
            self._log_in()
        else:
            self._sign_in()
        
    def _log_in(self):
        print('estoy en el log in')
        
    def _sign_in(self):
        print('estoy en el SIGN in')

        
