# Importowanie modułu i wywołanie konstruktora
import turtle
import random
import secrets

t = turtle.Turtle()

# Ustawianie prędkości poruszania się znacznika
t.speed("fastest")

# Generating a random number in between 0 and 2^24



# Definicja funkcji tworzącej fragment fraktala


class Fractals:
    def __init__(self):
        pass

    def frac_widly(self, x):
        if x <= 1:
            return
        t.left(90)
        t.forward(x)
        t.right(90)
        t.forward(x)
        self.frac_widly(x / 3)
        # cofnij się
        t.backward(x)
        t.right(90)
        t.forward(x)
        # rysuj środkową część wideł (rys. 3)
        t.left(90)
        t.forward(x)
        self.frac_widly(x / 3)
        # cofnij się
        t.backward(x)
        # rysuj prawą część wideł (rys. 4)
        t.right(90)
        t.forward(x)
        t.left(90)
        t.forward(x)
        self.frac_widly(x / 3)
        # cofnij się do punktu początkowego i obróć się w kierunku początkowym (rys. 5)
        t.backward(x)
        t.left(90)
        t.forward(x)
        t.right(90)

    def square(self, x):
        if x <= 1:
            return
        self.square(x - x * 0.1)
        t.forward(x)
        t.left(90)
        t.forward(x)
        t.left(90)
        t.forward(x)
        t.left(90)
        t.forward(x)
        t.left(90)

    def twig(self, x):
        if x <= 8:
            return
        t.forward(x)
        self.twig(x / 2)
        t.backward(x)
        t.left(60)
        t.forward(x)
        self.twig(x / 2)
        t.backward(x)
        t.right(120)
        t.forward(x)
        self.twig(x / 2)
        t.backward(x)
        t.left(60)

    def triangle(self, x):
        if x <= 8:
            return
        # pierwszy trójkąt
        self.triangle(x / 2)
        t.forward(x)
        t.left(120)
        t.forward(x)
        t.left(120)
        t.forward(x)
        t.left(120)
        # przejście
        t.forward(x)
        # drugi trójkąt
        self.triangle(x / 2)
        t.forward(x)
        t.left(120)
        t.forward(x)
        t.left(120)
        t.forward(x)
        # przejście
        t.right(120)
        t.forward(x)
        t.right(120)
        # trzeci trójkąt
        self.triangle(x / 2)
        t.forward(x)
        t.left(120)
        t.forward(x)
        t.left(120)
        t.forward(x)
        # powrót na poczatek
        t.forward(x)
        t.left(120)

    def colors(self):
        std_color = "#" + secrets.token_hex(3)
        t.color(std_color, std_color)
    def squareBOSS(self, x):
        if x <= 8:
            return


        for i in range(8):
            # pierwszy kwadrat
            self.colors()
            self.squareBOSS(x / 3)
            self.colors()
            t.forward(x)
            t.left(90)
            self.colors()
            t.forward(x)
            t.left(90)
            self.colors()
            t.forward(x)
            t.left(90)
            self.colors()
            t.forward(x)
            t.left(90)
            if i % 2 == 0:
                t.forward(x)
            else:
                t.forward(x)
                t.forward(x)
                t.left(90)


# Wywołanie funkcji frac_widly
x = 128
frac = Fractals()
frac.squareBOSS(x)
# t.forward(x)
# frac_widly(x)
#frac.twig(x)
# triangle(x)
turtle.onclick(None)

