import random

def simular_lancamentos(num_lancamentos, num_lados):
    contagem_faces = [0] * num_lados

    for _ in range(num_lancamentos):
        resultado = random.randint(1, num_lados)
        contagem_faces[resultado - 1] += 1

    porcentagens = [(contagem / num_lancamentos) * 100 for contagem in contagem_faces]

    return contagem_faces, porcentagens

def main():
    num_lancamentos = int(input("Digite o numero de lançamentos: "))
    num_lados = int(input("Digite o numero de lados do dado: "))

    contagem_faces, porcentagens = simular_lancamentos(num_lancamentos, num_lados)

    for i in range(num_lados):
        print(f"Face {i + 1}: {contagem_faces[i]} vezes ({porcentagens[i]:.2f}%)")

if __name__ == "__main__":
    main()
