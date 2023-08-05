from decimal import Decimal

def main():
    peso = Decimal(input("Escreva seu peso em quilogramas(Kg): "))
    altura = Decimal(input("Escreva sua altura em metros(m): "))

    imc = round((peso) / (altura * altura), 2)

    print(f"Seu IMC é {imc}")
    if(imc < 16):
        print("A classificação de seu IMC é Magreza grave")
    elif(imc >= 16 and imc < 17):
        print("A classificação de seu IMC é Magreza moderada")
    elif(imc >= 17 and imc < 18.5):
        print("A classificação de seu IMC é Magreza leve")
    elif(imc >= 18.5 and imc < 25):
        print("A classificação de seu IMC é Saudável")
    elif(imc >= 25 and imc < 30):
        print("A classificação de seu IMC é Sobrepeso")
    elif(imc >= 30 and imc < 35):
        print("A classificação de seu IMC é Obesidade Grau I")
    elif(imc >= 35 and imc < 40):
        print("A classificação de seu IMC é Obesidade Grau II")
    elif(imc > 40):
        print("A classificação de seu IMC é Obesidade Grau III")

if __name__ == '__main__':
    main()