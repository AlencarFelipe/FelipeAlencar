from cliente import Cliente

class Cadastro(Cliente):
    def __init__(self, nome, endereco, email, senha):
        self.senha= senha
        super().__init__(nome, endereco, email)

    def efetua_Cadastro(self):
        nome= input("Digite seu nome: ")
        endereco= input("Digite seu endereço: ")
        email= input("Digite seu email: ")
        senha= int(input("Digite seu email: "))

        print(f"Bem vindo {nome}, ")
        print(f"Seu endereço {endereco} e {email} foram salvos com sucesso")
        print(f"A senha cadastrada é {senha} , por meios de segurança nao compartilhe-a ")
        



