import turtle

def arco_iris_color(passo):
    # Definindo as cores do arco-íris em formato RGB (red, green, blue)
    cores_arco_iris = [
        (1, 0, 0),     # Vermelho
        (1, 0.5, 0),   # Laranja
        (1, 1, 0),     # Amarelo
        (0, 1, 0),     # Verde
        (0, 0, 1),     # Azul
        (0.29, 0, 0.51), # Anil
        (0.56, 0, 1),  # Violeta
    ]
    
    # A cor muda conforme o passo (um valor entre 0 e len(cores_arco_iris)-1)
    return cores_arco_iris[passo % len(cores_arco_iris)]

def espiral_perpendicular(linha, acrescimo, passo_cor):
    if linha <= 300:
        # A cor é determinada pela função arco_iris_color
        turtle.pencolor(arco_iris_color(passo_cor))
        turtle.forward(linha)
        turtle.left(90)
        espiral_perpendicular(linha + acrescimo, acrescimo, passo_cor + 1)

def main():
    turtle.setup(1024, 768)  # Define o tamanho da janela
    turtle.bgcolor("black")  # Define o fundo preto
    turtle.speed(0.4)  # Diminui a velocidade do desenho (1 é mais lento)
    turtle.hideturtle()  # Esconde o cursor da tartaruga
    turtle.penup()  # Levanta a caneta para mover sem desenhar
    turtle.goto(0, 0)  # Move para o centro da tela
    turtle.pendown()  # Abaixa a caneta para começar a desenhar
    espiral_perpendicular(1, 4, 0)
    turtle.done()  # Finaliza o desenho

if __name__ == "__main__":
    main()
