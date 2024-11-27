import turtle

def configure_turtle():
    """
    Configura o Turtle para desenhar o fractal.
    """
    screen = turtle.Screen()
    # screen.setup(width=1200, height=800)  # Configuração de tamanho (comente/descomente conforme necessário)
    screen.bgcolor("black")
    screen.title("Fractal - Árvore Binária")
    
    t = turtle.Turtle()
    t.speed(0)  # Velocidade máxima
    t.hideturtle()
    t.penup()
    t.goto(0, -300)  # Posição inicial
    t.pendown()
    t.left(90)  # Rotação inicial para desenhar verticalmente
    return t

def make_binary_tree(t, size, limit, depth=0):
    """
    Desenha o fractal de árvore binária recursivamente.

    Args:
        t (Turtle): Objeto Turtle para desenhar.
        size (float): Tamanho inicial dos ramos.
        limit (float): Tamanho mínimo para parar a recursão.
        depth (int): Nível de profundidade atual da recursão, usado para ajustar cor e espessura.
    """
    if size <= limit:
        return
    
    # Ajuste de cor com base na profundidade
    r = int((depth * 15) % 256)
    g = int((50 + depth * 20) % 256)
    b = int((100 + depth * 10) % 256)
    t.color((r, g, b))
    
    # Ajuste de espessura
    t.pensize(max(1, int(size / 20)))
    
    # Desenho do ramo
    t.forward(size)
    
    # Ramo esquerdo
    t.left(45)
    make_binary_tree(t, size * 2 / 3, limit, depth + 1)
    
    # Ramo direito
    t.right(90)
    make_binary_tree(t, size * 2 / 3, limit, depth + 1)
    
    # Retornar ao estado inicial
    t.left(45)
    t.backward(size)

def main():
    """
    Função principal para executar o fractal.
    """
    turtle.colormode(255)  # Habilita o uso de cores RGB com valores inteiros
    t = configure_turtle()
    make_binary_tree(t, size=200, limit=10)  # Tamanho inicial e limite para os ramos
    turtle.done()

if __name__ == "__main__":
    main()
