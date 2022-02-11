salario = float(input())

if salario <= 1751.81:
  desconto = salario*0.08
elif salario <= 2919.72:
  desconto = salario*0.09
elif salario <= 5839.45:
  desconto = salario*0.11
else:
  desconto = 642.34

print("Desconto do INSS: R$ {:.2f}".format(desconto))
