from controller.user import UserController

user_controller = UserController()
class UserView(object):
    def show_welcome(self):
        selection = int(input('Bienvenido, presiona 1 para logearte, si no tienes cuenta presiona 2 >  '))
        user_controller.choose(selection)
        

        
