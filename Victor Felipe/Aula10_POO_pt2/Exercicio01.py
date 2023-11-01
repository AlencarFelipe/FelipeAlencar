"""Projeto agenda, classe contato - nome, telefone e email*Atributos obrigatorios* e
Classe agenda - Metodo construtor que recebe uma lista de contatos vazia. *Metodo -Adicionar contato,
lista contatos e buscar contatos, deletar contatos"""

class Agenda:
    def __init__ (self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)
    
    def listar_contato(self):
        print(f"esses são seus conatos{self.contatos}:")
        for contato in self.contatos:
            print(contato)

    def buscar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                return contato
        return nome
    
    def remover_contato(self, nome):
        contato =  self.buscar_contato(nome)
        if contato is not nome:
            self.contatos.remove(contato)
            print(f"Contato {nome} removido  com sucesso. ")
        else:
            print(f"Contanto {nome} não encontrado")
