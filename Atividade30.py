nota1 = float(input("diga a 1 nota"))
nota2 = float(input("diga a 2 nota"))
nota3 = float(input("diga a 3 nota"))
media = (nota1 + nota2 + nota3) / 3
print(f"a média do aluno é: {media:.2f}")
if media>=7:
    print("aprovado")
else:
    print("reprovado")