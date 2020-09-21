def idades():
    soma = 0
    c = 0
    maior = 0
    menor = 0

    while True:
        idade = int(input())
        soma += idade
        c +=1
        if idade == 0:
            c -=1
            break

        if c == 1:
            maior = idade
            menor = idade
        else:
            if idade > maior:
                maior = idade
            if idade < menor:
                menor = idade
    return c, soma, maior, menor 

def main():
    people, sm, mx, mn = idades()
    
    media_idade = 0
    if sm >0:
        media_idade = sm/people

        print(f'{people}')
        print(f'{media_idade:.2f}')

    if mx != 0 and mn != 0:
        print(f'{mx}')
        print(f'{mn}')



if __name__=='__main__':
    main()
