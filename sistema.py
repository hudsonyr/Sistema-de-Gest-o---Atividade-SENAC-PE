#menu

while True:
  print('''\nOlá, o que deseja fazer hoje?
1 - Sistema de alunos
2 - Sistema de gastos
3 - Sistema de lanches
4 - Sistema de estoques
0 - Sair''')

  opcao = int(input('Informe sua opção: '))

  if opcao == 1:
    print('\nVocê escolheu o sistema de alunos')
    alunos=[]
    while True:
      print('''\nO que você deseja fazer:
  Aperte 1 para cadastrar alunos
  Aperte 2 para listar alunos
  Aperte 3 para verificar um aluno da lista
  Aperte 4 para remover um aluno da lista
  Aperte 0 para voltar ao menu principal''')
      opcao_alunos = int(input('Informe sua opção: '))
      if opcao_alunos == 1:
        nome = input('Digite o nome do aluno: ')
        alunos.append(nome)
      elif opcao_alunos == 2:
        print(f'Os alunos são: \n{alunos}\n')
      elif opcao_alunos == 3:
        nome = input('Qual o nome do aluno que você quer procurar? ')
        if nome in alunos:
          print(f'O aluno {nome} está na lista')
        else:
          print(f'O aluno {nome} não está na lista')
      elif opcao_alunos == 4:
        nome = input('Qual nome você deseja remover? ')
        if nome in alunos:
          alunos.remove(nome)
          print(f'O aluno {nome} foi removido')
        else:
          print(f'O aluno {nome} não está na lista')
      elif opcao_alunos == 0:
        break
      else:
        print('Opção inválida')

  elif opcao == 2:
    print('\nVocê escolheu o sistema de gastos')
    gastos=[]
    while True:
      print('''\nAperte 1 para cadastrar seus gastos
Aperte 2 para calcular o valor total
Aperte 3 para calcular a média dos gastos
Aperte 4 para visualizar o maior e o menor gasto
Aperte 0 para voltar ao menu principal''')
      opcao_gastos = int(input('Informe sua opção: '))
      if opcao_gastos == 1:
        valor = float(input('Digite o valor do gasto: R$ '))
        gastos.append(valor)
      elif opcao_gastos == 2:
        print(f'O valor total é R$ {sum(gastos):.2f}')
      elif opcao_gastos == 3:
        if len(gastos) > 0:
          print(f'A média dos gastos é R${sum(gastos)/len(gastos):.2f}')
        else:
          print('Não há gastos para calcular a média.')
      elif opcao_gastos == 4:
        if len(gastos) > 0:
          print(f'O maior gasto é R${max(gastos):.2f} e o menor gasto é R${min(gastos):.2f}')
        else:
          print('Não há gastos para visualizar o maior e menor.')
      elif opcao_gastos == 0:
        break
      else:
        print('Opção inválida')

  elif opcao == 3:
    print('\nVocê escolheu o sistema de lanches')
    lanches = ['1 - coxinha','2 - tapioca','3 - pão pizza','4 - bolo','5 - refrigerante']
    precos = [6,6,6,7,4.5]
    while True:
      print('\nEscolha o que vai comprar de acordo com a lista abaixo: ')
      for lanche, preco in zip(lanches, precos):
        print(f'{lanche} - R${preco:.2f}')

      itens_comprados_codigos = []
      itens_comprados_quantidades = []

      compra = int(input('Informe o código do lanche escolhido (ou 0 para voltar ao menu principal): '))
      if compra == 0:
        break

      if compra < 1 or compra > 5:
        print('Código inválido')
        continue

      quantidade = int(input('Informe a quantidade de lanches que deseja comprar: '))
      if quantidade <= 0:
        print('Quantidade inválida')
        continue

      if compra in itens_comprados_codigos:
        indice = itens_comprados_codigos.index(compra)
        itens_comprados_quantidades[indice] += quantidade
      else:
        itens_comprados_codigos.append(compra)
        itens_comprados_quantidades.append(quantidade)

      total = 0
      print('\nResumo da compra:')
      for i in range(len(itens_comprados_codigos)):
        codigo = itens_comprados_codigos[i]
        quantidade = itens_comprados_quantidades[i]
        lanche_comprado = lanches[codigo-1].split(' - ')[1]
        preco_unitario = precos[codigo-1]
        subtotal = quantidade * preco_unitario
        print(f'Você comprou {quantidade} {lanche_comprado}(s) - R${subtotal:.2f}')
        total += subtotal

      if total > 0:
        print(f'\nTotal a pagar: R${total:.2f}')
      else:
        print('Você não comprou nada.')

  elif opcao == 4:
    print('\nVocê escolheu o sistema de estoques')
    estoque = []
    while True:
      print('''\nO que você deseja fazer:
  Aperte 1 para cadastrar itens
  Aperte 2 para listar itens
  Aperte 3 para atualizar a lista
  Aperte 4 para mostrar produtos sem estoque
  Aperte 0 para voltar ao menu principal''')
      opcao_estoque = int(input('Informe sua opção: '))
      if opcao_estoque == 1:
        nome = input('Digite o nome do item: ')
        quantidade = int(input('Digite a quantidade do item: '))
        estoque.append((nome, quantidade))
      elif opcao_estoque == 2:
        for item in estoque:
          print(f'O item {item[0]} tem {item[1]} unidades')
      elif opcao_estoque == 3:
        nome = input('Digite o nome do item que deseja atualizar: ')
        for i in range(len(estoque)):
          if estoque[i][0] == nome:
            print('O que você deseja atualizar?')
            print('1 - Nome')
            print('2 - Quantidade')
            opcao_atualizar = int(input('Informe sua opção: '))
            if opcao_atualizar == 1:
              novo_nome = input('Digite o novo nome do item: ')
              estoque[i] = (novo_nome, estoque[i][1])
              print('Nome atualizado com sucesso!')
            elif opcao_atualizar == 2:
              nova_quantidade = int(input('Digite a nova quantidade do item: '))
              estoque[i] = (estoque[i][0], nova_quantidade)
              print('Quantidade atualizada com sucesso!')
            else:
              print('Opção inválida.')
            break
        else:
          print(f'O item {nome} não foi encontrado no estoque.')
      elif opcao_estoque == 4:
        for item in estoque:
          if item[1] == 0:
            print(f'O item {item[0]} está sem estoque')
      elif opcao_estoque == 0:
        break
      else:
        print('Opção inválida')

  elif opcao == 0:
    print('Saindo...')
    break

  else:
    print('Opção inválida')
