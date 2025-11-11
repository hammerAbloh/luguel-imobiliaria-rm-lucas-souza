# Primeiro, vamos mostrar uma mensagem de boas-vindas
print("Bem-vindo ao sistema de orçamento de aluguel da Imobiliária R.M!")

# Agora vamos perguntar ao usuário qual tipo de imóvel ele quer alugar
print("\nTipos de imóvel disponíveis:")
print("1 - Apartamento (R$ 700,00 / 1 Quarto)")
print("2 - Casa (R$ 900,00 / 1 Quarto)")
print("3 - Estúdio (R$ 1200,00)")

tipo = int(input("Digite o número do tipo de imóvel desejado: "))

# Perguntar sobre quantidade de quartos
quartos = int(input("Quantos quartos? (1 ou 2): "))

# Perguntar se quer vaga de garagem ou estacionamento
garagem = input("Deseja vaga de garagem ou estacionamento? (s/n): ").lower()

# Perguntar se tem crianças (para aplicar desconto em apartamento)
tem_criancas = input("Você tem crianças? (s/n): ").lower()

# Agora vamos calcular o valor base do aluguel
valor_base = 0

if tipo == 1:  # Apartamento
    valor_base = 700
    if quartos == 2:
        valor_base += 200
    if garagem == "s":
        valor_base += 300
    if tem_criancas == "n":
        valor_base *= 0.95  # Aplicar 5% de desconto
elif tipo == 2:  # Casa
    valor_base = 900
    if quartos == 2:
        valor_base += 250
    if garagem == "s":
        valor_base += 300
elif tipo == 3:  # Estúdio
    valor_base = 1200
    if garagem == "s":
        vagas = int(input("Quantas vagas de estacionamento? (mínimo 2): "))
        if vagas >= 2:
            valor_base += 250 + (vagas - 2) * 60

# Mostrar valor do aluguel mensal
print(f"\nValor do aluguel mensal: R$ {valor_base:.2f}")

# Valor do contrato imobiliário
valor_contrato = 2000
parcelas = int(input("Deseja dividir o contrato em quantas vezes? (1 a 5): "))
valor_parcela = valor_contrato / parcelas

print(f"Valor do contrato: R$ {valor_contrato:.2f}")
print(f"Parcelado em {parcelas}x de R$ {valor_parcela:.2f}")

# Gerar arquivo CSV com 12 meses de aluguel
import csv

with open("orcamento_aluguel.csv", mode="w", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Mês", "Valor do Aluguel", "Parcela do Contrato", "Total Mensal"])
    for mes in range(1, 13):
        total_mensal = valor_base + valor_parcela
        escritor.writerow([f"Mês {mes}", f"R$ {valor_base:.2f}", f"R$ {valor_parcela:.2f}", f"R$ {total_mensal:.2f}"])

print("\nArquivo 'orcamento_aluguel.csv' gerado com sucesso!")
