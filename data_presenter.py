open_cupcakes = open("CupcakeInvoices.csv")

# for line in open_cupcakes:
#     print(line)

# for line in open_cupcakes:
#     line = line.split(',')
#     print(line[2])

# for line in open_cupcakes:
#     line = line.rstrip('\n').split(',')
#     print(round(float(line[3]) * float(line[4]), 2))

# combined_invoice = 0

# for line in open_cupcakes:
#     line = line.rstrip('\n').split(',')
#     combined_invoice += float(line[3]) * float(line[4])

# combined_invoice = round(combined_invoice, 2)

vanilla_income = 0
vanilla_sold = 0
chocolate_income = 0
chocolate_sold = 0
strawberry_income = 0
strawberry_sold = 0

for line in open_cupcakes:
    line = line.rstrip('\n').split(',')
    if line[2] == "Vanilla":
        vanilla_income += float(line[3]) * float(line[4])
        vanilla_sold += float(line[3])
    elif line[2] == "Chocolate":
        chocolate_income += float(line[3]) * float(line[4])
        chocolate_sold += float(line[3])
    elif line[2] == "Strawberry":
        strawberry_income += float(line[3]) * float(line[4])
        strawberry_sold += float(line[3])

vanilla_income = round(vanilla_income, 2)
chocolate_income = round(chocolate_income, 2)
strawberry_income = round(strawberry_income, 2)

print(strawberry_income)
print(chocolate_income)
print(vanilla_income)
print(vanilla_sold, chocolate_sold, strawberry_sold)