# Programa de Desconto Progressivo

    # Solicita ao usuário o valor total da compra
valor_compra = float(input("Digite o valor total da compra: R$ "))

    # Verifica qual o percentual de desconto deve ser aplicado
if  valor_compra < 200:
    desconto= 0.05      # 5% de desconto

elif valor_compra <= 300:
    desconto = 0.10     # 10% de desconto

else:
    desconto = 0.15     # 15% de desconto

    # Calcula o valor do desconto em reais
valor_desconto = valor_compra * desconto

    # Calcula o valor final da compra após o desconto
valor_final = valor_compra - valor_desconto

    # Exibe os resultados para o usuário
print(f"\nValor da compra: R$ {valor_compra:.2f}")
print(f"Percentual de desconto aplicado: {desconto*100:.0f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor total a pagar: R$ {valor_final:.2f}")




