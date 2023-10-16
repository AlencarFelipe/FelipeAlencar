lista_tarefas = []
print(lista_tarefas)

while(True):
    print("Escolha uma opção \n")
    print("Opção 1: Adicionar uma tarefa \n")
    print("Opção 2: remover uma tarefa  \n")
    print("Opção 3: listar  tarefa \n")
    print("Opção 4: Sair \n")

    opcao = int(input())
    if opcao == 1:
        tarefa = input("Digite a tarefa: ")
        lista_tarefas.append(tarefa)
        print(lista_tarefas)

    elif opcao == 2:
        
         print(lista_tarefas)
         remover_tarefa = input("Digite a tarefa que deseja excluir: ")
         lista_tarefas.remove(remover_tarefa)
         print("Esta é sua nova lista" , lista_tarefas )
         
    elif opcao == 3:
       len(lista_tarefas)
       print("Esta são suas tarefas : ", lista_tarefas)
    else:
       print("Você saiu.")
       break
