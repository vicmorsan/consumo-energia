# Saudação
print("Olá! Seja Bem-Vindo ao calculador mensal de utensílios elétricos")
# Perguntas
name = input("Qual é o nome do seu aparelho? ")
potencia = float(input(f"Qual é a potência de {name} (em Watts)? "))
tempo = float(input(f"Quantas horas por dia você usa {name}? (em horas) "))
# Cálculo do consumo mensal
calculo = (potencia * tempo * 30) / 1000 
# Exibição do resultado
print(f"Aparelho: {name}")
print(f"Consumo esperado: {calculo} kWh/mês")