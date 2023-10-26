def main():
    from locadora import Locadora
    
    minha_locadora = Locadora("Minha locadora")
    from filme import Filme

    filme1 = Filme ("Matrix","Ação","225")
    filme2 = Filme ("Clube da Luta","Ação","190")
    filme3 = Filme ("Interestelar","ficção cientifica","219")

    minha_locadora.adicionar_filme(filme1)
    minha_locadora.adicionar_filme(filme2)
    minha_locadora.adicionar_filme(filme3)


    while True:
        print("\n Opções")
        print("\n Opção 1 - Listar catalogo")
        print("\n Opção 2 - Alugar Filme")
        print("\n Opção 3 - Devolver Filme")
        print("\n Opção 4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            minha_locadora.listar_catalogo()

        elif opcao == '2':
            titulo = input("Digite o titulo do filme: ")
            for filme in minha_locadora.catalogo:
                if filme.titulo == titulo:
                    resultado =  filme.alugar()
                    print(resultado)
                    break
                else:
                    print(f"Filme'{titulo}'não encontrado na locadora. ")

        elif opcao == "3":
            titulo = input("Digite o titulo que deseja devolver: ")
            for filme in minha_locadora.catalogo:
                resultado = filme.devolver()
                print(resultado)
                break
            else:
                print(f"Filme '{titulo}' não encontrado na locadora")

        elif opcao == "4":
            print("Voce saiu...")
            break
        else:
            print("Opção invalida!")

if __name__ == "__main__":
    main()





