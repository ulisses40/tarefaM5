from fizzbuzz_utils import verificar_multiplo

def main():
    try:
        numero = int(input("Digite um número natural: "))
        if numero < 0:
            raise ValueError("O número deve ser natural (maior ou igual a zero).")
        resultado = verificar_multiplo(numero)
        print(resultado)
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
