# calculadora  em py

{
import re

# o simbolo | tem a função "e/ou"

operação = input'Qual operação?'
conta = re.search r'^(\d|\d\d|\d\d\d)+(\+|\-|\*|\/)+(\d|\d\d|\d\d\d)$',operação

a = float conta.group1
b = str conta.group2
c = float conta.group3

# a  primeira operação é sempre if, e a ultima sempre else, as demais elif.

if b == '+':
	resultado = a + c

`elif b == '-':
	resultado = a - c

`elif b == '*':
	resultado = a * c

else:
		resultado = a / c

print'O resultado é: ',resultado

#arquivo.sh
