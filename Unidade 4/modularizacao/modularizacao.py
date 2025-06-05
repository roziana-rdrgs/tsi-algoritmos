# Criar uma função que calcule e retorne o MAIOR entre dois valores recebidos como
# parâmetro. Um algoritmo para testar tal função deve ser criado.
import math


def maior_valor(valor_um, valor_dois):
    if valor_um == valor_dois: return "Os valores são iguais"
    return valor_um if valor_um > valor_dois else valor_dois

def exercicio_um():
    print("\n**** Exercício Um ****")
    primeiro_valor = int(input("Informe o primeiro valor: "))
    segundo_valor = int(input("Informe o segundo valor: "))

    print("O maior valor dentre os informados é:", maior_valor(primeiro_valor, segundo_valor))


# Escreva um procedimento que receba um número inteiro e imprima o mês
# correspondente ao número. Por exemplo, 2 corresponde à “fevereiro”. O
# procedimento deve mostrar uma mensagem de erro caso o número recebido não
# faça sentido.
# Gere também um algoritmo que leia um valor e chame o procedimento criado.

def nome_mes(valor: int):
  if valor <=0 or valor > 12: return "invalido"
  meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
           "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
  return meses[valor - 1]

def exercicio_dois():
    print("\n**** Exercício Dois ****")
    valor = int(input("Informe um valor: "))
    mes = nome_mes(valor)
    if "invalido" in mes:
        print("Mês inválido. Deve ser entre 1 e 12.")
    else:
        print(f"O mês correspondente ao valor {valor} é: {mes}")    


# Escreva um procedimento que gere um cabeçalho para um relatório. Esse
# procedimento deve receber um literal (string, ou cadeia de caracteres) como
# parâmetro. O cabeçalho tem a seguinte forma:
#  ============================================
#  IFC – Camboriú
#  Curso Superior de Tecnologia em Sistemas para Internet
#  Disciplina de Algoritmos e Técnicas de Programação
#  Nome: <seu_nome>
#  ============================================ ,
# onde <seu_nome>, corresponde ao parâmetro passado.

def cabecalho(nome: str):
    print("============================================")
    print("IFC – Camboriú")
    print("Curso Superior de Tecnologia em Sistemas para Internet")
    print("Disciplina de Algoritmos e Técnicas de Programação")
    print(f"Nome: {nome}")
    print("============================================")

def exercicio_tres():
    print("\n**** Exercício Três ****")
    nome = input("Informe seu nome: ")
    cabecalho(nome)    


# Escreva um procedimento que receba um número inteiro e o imprima na forma
# extensa. Por exemplo, para 1 a saída desejada é “Um”. A função deve ser capaz de
# gerar o extenso dos números de 0 até 10, inclusive. Caso um número não
# compatível seja recebido o procedimento deve mostrar uma mensagem de erro.
# Crie também um algoritmo que leia um valor inteiro e chame o procedimento criado
# acima para a impressão do número extenso.

def numero_extenso(valor: int):
    if valor < 0 or valor > 10:
        return "Número inválido. Informe um número entre 0 e 10."
    numeros = [
        "zero",
        "um",
        "dois",
        "três",
        "quatro",
        "cinco",
        "seis",
        "sete",
        "oito",
        "nove",
        "dez"
    ]
    return  numeros[valor] 

def exercicio_quatro():
    print("\n**** Exercício Quatro ****")
    valor = int(input("Informe um número: "))
    extenso = numero_extenso(valor)
    
    print(f"O número {valor} por extenso é: {extenso}")

# Escreva um procedimento que receba um número natural e imprima os três
# primeiros caracteres do dia da semana correspondente ao número. Por exemplo, 7
# corresponde à “SAB”. O procedimento deve mostrar uma mensagem de erro caso o
# número recebido não corresponda a um dia da semana.
# Gere também um algoritmo que utilize esse procedimento, chamando-o, mas antes
# lendo um valor para passagem de parâmetro.

def dia_semana(valor: int):
    if valor < 1 or valor > 7:
        return "Número inválido. Informe um número entre 1 e 7."
    dias = ["DOM", "SEG", "TER", "QUA", "QUI","SEX", "SAB"]
    return dias[valor - 1]

def exercicio_cinco():
    print("\n**** Exercício Cinco ****")
    valor = int(input("Informe um número: "))
    dia = dia_semana(valor)
    
    print(f"O dia da semana correspondente ao número {valor} é: {dia}")


# Escreva uma função que receba um número inteiro. Esta função deve verificar se tal
# número é primo. No caso positivo, a função deve retornar 1, caso contrário zero.
# Escreva também um algoritmo para testar tal função.

def verifica_primo(numero: int):
    if numero == 2:
        return 1
    if numero < 2 or numero % 2 == 0:
        return 0
    for i in range(3, int(math.sqrt(numero)) + 1, 2):
        if numero % i == 0:
            return 0
    return 1

def exercicio_seis():
    print("\n**** Exercício Seis ****")
    numero = int(input("Informe um número inteiro: "))
    if verifica_primo(numero):
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")


# Escreva uma função que receba dois números inteiros x e y. Essa função deve
# verificar se x é divisível por y. No caso positivo, a função deve retornar 1, caso
# contrário zero.
# Escreva também um algoritmo para testar tal função

def verifica_divisivel(x: int, y: int):
    if y == 0:
        return "Divisão por zero não é permitida."
    return 1 if x % y == 0 else 0

def exercicio_sete():
    print("\n**** Exercício Sete ****")
    x = int(input("Informe o primeiro número (x): "))
    y = int(input("Informe o segundo número (y): "))
    
    resultado = verifica_divisivel(x, y)
    if resultado== 1:
        print(f"{x} é divisível por {y}.")
    else:
        print(f"{x} não é divisível por {y}.")

# Criar uma função que verifique quantas vezes um número inteiro x é divisível por um
# número inteiro y. A função deve retornar -1 caso não seja possível calcular.
# Escreva também um algoritmo para testar tal função

def verifica_quantidade_divisoes(x: int, y: int):
    if y == 0:
        return -1
    count = 0
    while x >= y:
        x -= y
        count += 1
    return count

def exercicio_oito(): 
    print("\n**** Exercício Oito ****")

    x = int(input("Informe o primeiro número (x): "))
    y = int(input("Informe o segundo número (y): "))
    
    resultado = verifica_quantidade_divisoes(x, y)
    if resultado == -1:
        print("Divisão por zero não é permitida.")
    else:
        print(f"{x} é divisível por {y} um total de {resultado} vezes.")


# Criar uma função que receba um número inteiro e retorne o seu valor por extenso.
# Por exemplo, para 5 o valor de retorno desejado é “cinco”. A função deve ser capaz
# de gerar o valor por extenso para os 50 primeiros inteiros. Uma mensagem de erro
# deve ser mostrada caso um número fora dessa faixa seja recebido.
# Escreva também um algoritmo para testar a função.

def numero_por_extenso(valor: int):
    if valor < 0 or valor > 50:
        return "Número inválido. Informe um número entre 0 e 50."
    
    numeros = [
        "zero", "um", "dois", "três", "quatro", "cinco",
        "seis", "sete", "oito", "nove", "dez",
        "onze", "doze", "treze", "quatorze", "quinze",
        "dezesseis", "dezessete", "dezoito", "dezenove",
        "vinte", "vinte e um", "vinte e dois", "vinte e três",
        "vinte e quatro", "vinte e cinco", "vinte e seis",
        "vinte e sete", "vinte e oito", "vinte e nove",
        "trinta", "trinta e um", "trinta e dois",
        "trinta e três", "trinta e quatro", 
        "trinta e cinco", "trinta e seis",
        "trinta e sete", "trinta e oito",
        "trinta e nove", 
        "quarenta", 
        "quarenta e um",
        "quarenta e dois",
        "quarenta e três",
        "quarenta e quatro",
        "quarenta e cinco",
        "quarenta e seis",
        "quarenta e sete",
        "quarenta e oito",
        "quarenta e nove",
        "cinquenta"
    ]
    
    return numeros[valor] 

def exercicio_nove():
    print("\n**** Exercício Nove ****")
    valor = int(input("Informe um número entre 0 e 50: "))
    extenso = numero_por_extenso(valor)
    
    print(f"O número {valor} por extenso é: {extenso}")   
 
 
# Escreva um procedimento que receba um número arábico inteiro e imprima o
# correspondente número em romano. Por exemplo, para 5 a saída desejada é “V”. A
# função deve ser capaz de gerar o número romano para os 50 primeiros inteiros.
# Uma mensagem de erro deve ser mostrada caso um número fora dessa faixa seja
# recebido.
# Crie também um algoritmo que leia um valor inteiro e chame o procedimento criado
# acima para a impressão do número romano.

def numero_romano(valor: int):
    if valor < 1 or valor > 50:
        return "Número inválido. Informe um número entre 1 e 50."
    
    romanos = [
        "", "I", "II", "III", "IV", "V",
        "VI", "VII", "VIII", "IX", "X",
        "XI", "XII", "XIII", "XIV", "XV",
        "XVI", "XVII", "XVIII", "XIX", "XX",
        "XXI", "XXII", "XXIII", "XXIV", 
        "XXV", "XXVI", "XXVII", 
        "XXVIII", "XXIX",
        "XXX", 
        "XXXI",
        "XXXII",
        "XXXIII",
        "XXXIV",
        "XXXV",
        "XXXVI",
        "XXXVII",
        "XXXVIII",
        "XXXIX",
        "XL",
        "XLI",
        "XLII",
        "XLIII",
        "XLIV",
        "XLV",
        "XLVI",
        "XLVII",
        "XLVIII",
        "XLIX",
        "L"
    ]
    
    return romanos[valor]

def exercicio_dez():
    print("\n**** Exercício Dez ****")
    valor = int(input("Informe um número entre 1 e 50: "))
    romano = numero_romano(valor)
    
    print(f"O número {valor} em romano é: {romano}")  

def main_menu():
  while True:
    print("\nQual exercicio deseja executar?")
    print("[opções 1 a 10]")
    print("[0 - sair]")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
      exercicio_um()

    elif escolha == "2":
      exercicio_dois()

    elif escolha == "3":
      exercicio_tres()

    elif escolha == "4":
      exercicio_quatro() 

    elif escolha == "5":    
       exercicio_cinco()   

    elif escolha == "6":  
      exercicio_seis()

    elif escolha == "7":
      exercicio_sete()

    elif escolha == "8":  
      exercicio_oito()

    elif escolha == "9":
      exercicio_nove()  

    elif escolha == "10":
      exercicio_dez() 
      
    elif escolha == "0":
      print("Saindo...")
      break 
    else:
      print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
  main_menu()