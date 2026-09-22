#opnioes de grau de satisfacao tudoweb
#gabriely cezario

#contadores:
opniao_exelente = 0
opniao_ruim = 0

#pesquisa com 50 clientes
for i in range(10):

    #entrada de dados:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    opniao = int(input("Digite sua opnião: 1 para EXELENTE, 2 para BOM ou 3 para RUIM: "))

    #processamento de dados:
    if opniao == 1:
        opniao_exelente += 1

    if opniao == 3:
        opniao_ruim += 1

#saida de dados:
print(f"Foram avaliados {opniao_exelente} opniões exelente e {opniao_ruim} opniões ruins")