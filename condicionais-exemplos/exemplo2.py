nota = float(input("Nota de aluno: "))

print(f"Nota do aluno: {nota}")

if nota >= 90:
    print("Conceito A")
elif nota >= 80: 
    print("Conceito B")
elif nota >= 70: 
    print("Conceito C")
elif nota >= 60: 
    print("Conceito D")
else:
    print("Conceito F (Reprovado)")
