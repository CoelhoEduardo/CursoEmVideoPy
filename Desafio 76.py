tabeladeprecos = ("Lapis",1.50,
                  "Borracha", 2,
                  "Caderno", 15.90,
                  "Estojo", 25,
                  "Transferidor", 4.20,
                  "Compasso", 9.99,
                  "Mochila",120.32,
                  "Canetas",22.30,
                  "Livro",34.90)


print('='*60)
print(f'{"PAPELARIA PYTHON":^60}')
print('='*60)
for produtos in range(0, len(tabeladeprecos)):
    if produtos % 2 == 0:
        print(f'{tabeladeprecos[produtos]:.<50}', end='')
    else:
        print(f'R$ {tabeladeprecos[produtos]:>7.2f}')
print('='*60)