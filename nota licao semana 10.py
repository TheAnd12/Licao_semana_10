# 1 CRIAR AS FUNÇÕES 

def calcular_media(notas):
    return sum(notas) / len(notas) #soma as  todas as notas divide elas pela quantidade de notas e cria a média (valor final)

def verificar_aprovacao(media): #verifica aprovação se for >6 aprovado, se for >5 recuperação, se for <5 reprovado
    if media >= 6:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


# 2 PEGAR AS NOTAS

materias = ["Matemática", "Língua Portuguesa", "Ciências", "História", "Geografia"] #guarda o nome das matérias para solicitar as notas ao usuário
notas = [] #guarda o valor de cada nota digitada pelo usuário

for materia in materias:
    nota = float(input(f"Digite a nota de {materia}: "))
    notas.append(nota) #pergunta qual nota de cada matéria, e guarda o valor digitado pelo usuário na lista de notas


# 3 USAR AS FUNÇÕES

media = calcular_media(notas)
situacao = verificar_aprovacao(media)


# 4 MOSTRAR RESULTADO

print("Média:", media)
print("Situação:", situacao)