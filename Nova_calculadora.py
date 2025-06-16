# calculadora  em py


import re

# o simbolo | tem a função "e/ou"

operação = input('Qual operação?')
conta = re.search (r'^(\d|\d\d|\d\d\d)+(\+|\-|\*|\/)+(\d|\d\d|\d\d\d)$',operação)
#quantidade de (\d) indica com quantos digitos a calculadora consegue operar ex:(\d contas com um digito apenas, \d\d contas com dois digitos...)
#ainda preciso entender porque quando digito mais numeros no a, e menos no c, ele nao entende e faz a operação com a menor quantidade de digitos.
#exemplo 5*200=1000, porem 200*5=0, ele entende apenas o ultimo digito do (a) e um digito do (c), se fosse 222*10 o resultado seria 220, pois multiplicou os dois ultimos digitos de (a) 22 no caso por 10.

a = float(conta.group(1)) #.group(1) se refere ao primeiro parentese do re.search (\d) no caso
b = str(conta.group(2)) #.group(2) se refere ao segundo parentese do re.search (\+|...) str(string)
c = float(conta.group(3)) #.group(3) se refere ao terceiro parentese do re.search (\d)

# a  primeira operação é sempre if, e a ultima sempre else, as demais elif.

if b == '+':
	resultado = a + c

elif b == '-':
	resultado = a - c

elif b == '*':
	resultado = a * c

else:
	resultado = a / c

print('O resultado é: ',resultado)

#aquivo . py
