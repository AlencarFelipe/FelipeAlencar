from cliente import Cliente
from login import Login 

cadastro_cliente = {}

class Cadastro(Cliente):
    def __init__(self, nome, endereco, email, senha):
        self.senha= senha
        super().__init__(nome, endereco, email)

    def efetua_Cadastro(self):
        
        cadastro = {}

        nome= input ("Digite o seu nome: ")
        endereco= input ("Digite o seu endereço: ")
        email=  input ("Digite seu o seu email: ")
        senha=  int(input ("Digite a sua senha: "))

        print(f"Bem vindo {nome}, ")
        print(f"Seu endereço {endereco} e {email} foram salvos com sucesso")
        print(f"A senha cadastrada é {senha} , por meios de segurança nao compartilhe-a ")

    def verifica_cadastro(self):
        print("Você já possui cadastro?")
        print("Digite 'S' para sim e 'N' para nao")
        resposta = ""
        if resposta == "S":
            from login import Login 
            login= Login()
            login.efetua_login
        
    
