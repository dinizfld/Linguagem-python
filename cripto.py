def menu():
  print("1. Criptografar\n2. Descriptografar\n3. Sair")

def criptografar():
  mensagem=""
  palavra=input("O que quer criptografar: ")
  for i in palavra:
    mensagem = mensagem + chr(ord(i)-20)
  print(mensagem)

def descriptografar():
  mensagem=""
  palavra=input("O que quer descriptografar: ")
  for i in palavra:
    mensagem = mensagem + chr(ord(i)+20)
  print(mensagem)

def exit():
  print("1. Sair\n2. Cancelar")

opcao=1
while opcao!=3:
  menu()
  opcao=int(input("Digite sua opção: "))

  if opcao==1:
    criptografar()

  elif opcao==2:
    descriptografar()

  elif opcao==3:
    exit()
    opcao=int(input("Deseja sair? "))
    if opcao==1:
      print("Exit")
      break  

  else:
    print("Opção inválida")
    break
