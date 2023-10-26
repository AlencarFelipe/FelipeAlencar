from cadastro import Cadastro
class Login:   
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def efetua_login(self, email, senha):

        self.email= input("Digite seu email")
        self.senha= input("Digite sua senha")
       
        if( email == email):
            if(senha == senha):
                print("Login Efetuado com sucesso")

            else:
                print("Senha ou email incorretos")