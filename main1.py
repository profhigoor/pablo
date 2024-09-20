from colorama import Fore, Style
import time
import re


class Registro:

  def __init__(self):
    self.emails = []
    self.erro_count = 0

  def validar_email(self, email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

  def validar_senha(self, senha):
    if len(senha) < 8:
      print(Fore.RED + 'Senha deve ter pelo menos 8 caracteres.' +
            Style.RESET_ALL)
      return False
    return (re.search(r'[A-Z]', senha) and re.search(r'[a-z]', senha)
            and re.search(r'[0-9]', senha)
            and re.search(r'[!@#$%^&*(),.?":{}|<>]', senha))

  def registrar(self):
    while True:
      for attempt in range(3):
        email = input('\nDigite o e-mail: ')
        if email in self.emails:
          print(Fore.LIGHTRED_EX +
                f'O e-mail: {email}, já está cadastrado, tente novamente.' +
                Style.RESET_ALL)
          self.erro_count += 1
          continue
        senha = input('Digite a senha: ')
        confirmar_senha = input('Confirme sua senha: ')

        if self.validar_email(email) and self.validar_senha(senha):
          if senha != confirmar_senha:
            print(Fore.LIGHTRED_EX + 'As senhas não coincidem.' +
                  Style.RESET_ALL)
            self.erro_count += 1
            continue
          else:
            print(Fore.GREEN + f'E-mail e senha cadastrados com sucesso!' +
                  Style.RESET_ALL)
            self.emails.append(email)
            self.erro_count = 0
            print(Fore.BLUE + "Deseja registrar outro e-mail? (s/n): " +
                  Style.RESET_ALL)
            resposta = input().lower()
            if resposta == 's':
              continue
            else:
              print(Fore.BLUE + "Processo finalizado." + Style.RESET_ALL)
              return
        else:
          print(Fore.RED + 'E-mail inválido ou senha inválida.' +
                Style.RESET_ALL)
          self.erro_count += 1

      if self.erro_count >= 3:
        print(Fore.RED +
              "Você errou 3 vezes. O processo será reiniciado em 5 segundos." +
              Style.RESET_ALL)
        for i in range(5, 0, -1):
          print(Fore.LIGHTRED_EX + f"Reiniciando em {i} segundos...",
                end='\r' + Style.RESET_ALL)
          time.sleep(1)
        print(Fore.BLUE + "Processo pausado. Deseja continuar? (s/n): " +
              Style.RESET_ALL)
        continuar = input().lower()
        if continuar == 's':
          print(Fore.GREEN + "Reiniciando..." + Style.RESET_ALL)
          self.erro_count = 0
          continue
        else:
          print(Fore.BLUE + "Processo finalizado." + Style.RESET_ALL)
          return


registro = Registro()
registro.registrar()
