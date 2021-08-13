'''TABUADA V2.0'''


num = int(input('Digite um numero para a sua tabuada: '))
print('-=-'*8)
for t in range(1,11):
    print('{}  x {:2} = {}'.format(num, t, num*t))
print('-=-'*8)
