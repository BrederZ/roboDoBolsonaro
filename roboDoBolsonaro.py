arquivo = open('followers.txt')
arquivoLines = arquivo.readlines();

print("Cabeçalho")
print(arquivoLines[0])


def BuscarPessoaPorLista(listaAProcurar, pessoaAProcurar):
  for pessoa in listaAProcurar:
    dado = pessoa.split(",")
  
    if dado[1].strip() == pessoaAProcurar.strip():
      print(pessoa)

def BuscarPessoaPorId(listaAProcurar, idAProcurar):
  for pessoa in listaAProcurar:
    dado = pessoa.split(",")
  
    if dado[0] == idAProcurar:
      print(pessoa)



opcaoContinuar = "1"
while opcaoContinuar == "1":
  print("1- Buscar por Nome\n2- Buscar por ID")
  opcaoSelecionada = input()

  if opcaoSelecionada == "1":
    print("Digite o Nome")
    BuscarPessoaPorLista(arquivoLines, input())

  elif opcaoSelecionada == "2":
    print("Digite o ID")
    BuscarPessoaPorId(arquivoLines, input())
  print("1- Continuar\n0- Finalizar")
  opcaoContinuar = input()

print("Finalizado")
