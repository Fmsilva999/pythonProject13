preço = float(input("Preço das compras R$: "))
print("""FORMAS DE PAGAMENTO
[ 1 ] Á vista dinheiro/cheque
[ 2 ] Á vista cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão""")
paga = int(input("Qual é a opção)"))
op1 = preço - (preço * 10/100)
op2 = preço - (preço * 5/100)
op4 = preço + (preço * 20/100)
if paga == 1:
    print("Sua compra de {:.2f}R$ vai custar {:.2f}R$ no final".format(preço,op1))
elif paga == 2:
    print("Sua compra de {:.2f}R$ vai custar {:.2f}R$ no final".format(preço, op2))
elif paga == 3:
    print("Sua compra será parcelada em 2X de {:.2f}R$".format(preço/2))
    print("Sua compra de {:.2f}R$ vai custar {:.2f}R$ no final".format(preço,preço))
elif paga == 4:
    prest = int(input("Quantas parcelas"))
    print("Sua compra será parcelada em {}X de {:.2f}R$ COM JUROS ".format(prest, op4 / prest))
    print("Sua compra de {:.2f}R$ vai custar {:.2f}R$ no final".format(preço, op4))
else:
    print("Volte a tentar outra opção" )