import turtle

# QUESTÃO 1

# Instanciando o objeto
t1 = turtle.Turtle()

# Aplicando alterações
turtle.screensize(500, 500)

t1.shape("turtle")
t1.color("blue")

t1.speed(1)
t1.forward(100)

turtle.clear()

# QUESTÃO 2

# Instanciando o objeto turtle
t2 = turtle.Turtle()
t2.shape("turtle")

# Aplicando movimentos
t2.speed(1)
t2.forward(25)

for i in range(3):
    t2.left(90)
    t2.forward(50)

t2.left(90)
t2.forward(25)

turtle.clear()

# QUESTÃO 3

# Instanciando t3

t3 = turtle.Turtle()

# Aplicando as mudanças
t3.shape("turtle")
t3.color("green")
t3.forward(25)

for i in range(2):
    t3.left(90)
    t3.forward(50)

t3.left(90)
t3.forward(25)

turtle.clear()

# QUESTÃO 4

# Instanciando objeto t4
t4 = turtle.Turtle()

# Aplicando mudanças

t4.shape("turtle")
t4.left(120)

for i in range(2):
    t4.forward(50)
    t4.left(120)

t4.forward(50)
turtle.clear()

# QUESTÃO 5

# Instanciando o objeto t5

t5 = turtle.Turtle()
t5.shape("turtle")


# Aplicando mudanças
t5.circle(50)
turtle.clear()

# QUESTÃO 6

# Instanciando objeto t6

t6 = turtle.Turtle()
t6.shape("turtle")

# Aplicando mudanças
t6.up()
t6.back(250)
t6.down()
t6.color("yellow")
t6.begin_fill()
t6.circle(50)
t6.end_fill()


while True:
    option = input("Process running... Press Y to exit: ")
    if (option.upper() == "Y"):
        break
