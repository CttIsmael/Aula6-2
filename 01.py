def soma_numeros():
    soma = 0
    while True:
        nm = int(input())
        soma += nm
        if nm == 0: break
    return soma

def main():
    s = soma_numeros()
    print(f'{s}')


if __name__ == '__main__':
    main()
