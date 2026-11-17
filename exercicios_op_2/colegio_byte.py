def calcular_media_aluno(n1, n2, n3):
    media = (n1*2 + n2*3 + n3*5) / 10

    return media

media = calcular_media_aluno(7.0, 8.0, 9.0)
print(f"A média do aluno é: {media:.2f}")

media = calcular_media_aluno(5.0, 6.0, 4.0)
print(f"A média do aluno é: {media:.2f}")

media = calcular_media_aluno(5.0, 11.0, 8.0)
print(f"A média do aluno é: {media:.2f}")