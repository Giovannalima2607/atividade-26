# Inicializa uma lista para armazenar as notas
notas = []

# Loop para receber as notas dos 5 alunos
for i in range(1, 6):
    nota = float(input(f"Nota do aluno {i}: "))
    notas.append(nota)

# Calcula a maior nota, a menor nota e a média
maior_nota = max(notas)
menor_nota = min(notas)
media_nota = sum(notas) / len(notas)
