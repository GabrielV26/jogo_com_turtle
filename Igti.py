import turtle
#import os

tela = turtle.Screen()
tela.title("Jogo com Turtle")
tela.bgcolor('#4f0985')
tela.setup(width=800, height=600)
tela.tracer(0)

# Barra A
barra_A = turtle.Turtle()
barra_A.speed(0)
barra_A.shape('square')
barra_A.color('#a200ff')
barra_A.shapesize(stretch_wid=8, stretch_len=0.3)
barra_A.penup()
barra_A.goto(-385, 0)

# Barra B
barra_B = turtle.Turtle()
barra_B.speed(0)
barra_B.shape('square')
barra_B.color('#a200ff')
barra_B.shapesize(stretch_wid=8, stretch_len=0.3)
barra_B.penup()
barra_B.goto(380, 0)

# Bola

bola = turtle.Turtle()
bola.speed()
bola.shape('circle')
bola.color('white')
bola.shapesize(stretch_wid=0.7)
bola.penup()
bola.goto(0, 0)

# Adicionando o movimento
bola.dx = 0.2
bola.dy = 0.2

# Atribuindo a pontuação
pontuacao_A = 0
pontuacao_B = 0

# Desenhando o placar
placar = turtle.Turtle()
placar.speed()
placar.color('white')
placar.penup()
placar.hideturtle()
placar.goto(-330, 265)
placar.write(f"Player 1: {pontuacao_A} \nPlayer 2: {pontuacao_B}", align='center',
             font=('Fixedsys', 16, 'normal'))

# temas
tema = turtle.Turtle()
tema.speed()
tema.color('white')
tema.penup()
tema.hideturtle()
tema.goto(300, 280)
tema.write("Tema: Dia", align='left', font=('Fixedsys', 15, 'normal'))


# Configurando o movimento das barras
def barra_a_cima():
    y = barra_A.ycor()
    y = y + 30
    barra_A.sety(y)


def barra_a_baixo():
    y = barra_A.ycor()
    y = y - 30
    barra_A.sety(y)


def barra_b_cima():
    y = barra_B.ycor()
    y = y + 30
    barra_B.sety(y)


def barra_b_baixo():
    y = barra_B.ycor()
    y = y - 30
    barra_B.sety(y)


def tema_um():
    tela.bgcolor('#4f0985')
    bola.color('white')
    placar.color('white')
    placar.clear()
    placar.write(f"Player 1: {pontuacao_A} \nPlayer 2: {pontuacao_B}", align='center',
                 font=('Fixedsys', 16, 'normal'))
    tema.clear()
    tema.color('white')
    tema.write(f"Tema: Dia", align='left', font=('Fixedsys', 15, 'normal'))


def tema_dois():
    tela.bgcolor('black')
    bola.color('#a200ff')
    placar.color('#a200ff')
    placar.clear()
    placar.write(f"Player 1: {pontuacao_A} \nPlayer 2: {pontuacao_B}", align='center',
                 font=('Fixedsys', 16, 'normal'))
    tema.clear()
    tema.color('#a200ff')
    tema.write("Tema: Noite", align='left', font=('Fixedsys', 15, 'normal'))


# Configurando o teclado
tela.listen()
tela.onkeypress(barra_a_cima, "w")
tela.onkeypress(barra_a_baixo, "s")
tela.onkeypress(barra_b_cima, "i")
tela.onkeypress(barra_b_baixo, "k")
tela.onkeypress(tema_um, "1")
tela.onkeypress(tema_dois, '2')

# Loop principal
while True:
    tela.update()

    # adicionando o movimento da bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # definindo as bordas da imagem
    if bola.ycor() > 290:
        bola.sety(290)
        # reverte o movimento
        bola.dy = bola.dy * -1

    # definindo as bordas da imagem
    if bola.ycor() < -290:
        bola.sety(-290)
        # reverte o movimento
        bola.dy = bola.dy * -1

    # definindo as bordas da imagem
    if bola.xcor() > 390:
        bola.goto(0, 0)
        # reverte o movimento
        bola.dx = bola.dx * -1
        pontuacao_A = pontuacao_A + 1
        placar.clear()
        placar.write(f"Player 1: {pontuacao_A} \nPlayer 2: {pontuacao_B}", align='center',
                     font=('Fixedsys', 16, 'normal'))

    # definindo as bordas da imagem
    if bola.xcor() < -390:
        bola.goto(0, 0)
        # reverte o movimento
        bola.dx = bola.dx * -1
        pontuacao_B = pontuacao_B + 1
        placar.clear()
        placar.write(f"Player 1: {pontuacao_A} \nPlayer 2: {pontuacao_B}", align='center',
                     font=('Fixedsys', 16, 'normal'))

    if (360 < bola.xcor() < 370) and (barra_B.ycor() + 80 > bola.ycor() > barra_B.ycor() - 80):
        bola.setx(360)
        bola.dx = bola.dx * -1

    if (-360 > bola.xcor() > -370) and (barra_A.ycor() + 80 > bola.ycor() > barra_A.ycor() - 80):
        bola.setx(-360)
        bola.dx = bola.dx * -1
