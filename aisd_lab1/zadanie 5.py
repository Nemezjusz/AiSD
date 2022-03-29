class kik:
    matrix_plansza = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

    def wyswietlanie(self):
        for x in self.matrix_plansza:
            print(x)

    def stawianie(self, xy):
        nr = int(input(f"Gdzie chcesz stawic {xy}? "))

        if nr <= 3:
            n1 = 0
            n2 = nr - 1
        elif nr <= 6:
            n1 = 1
            n2 = nr - 4
        else:
            n1 = 2
            n2 = nr - 7

        self.matrix_plansza[n1][n2] = xy
        self.wyswietlanie()

    def sprawdzenie(self):

        def chck(cx, cy):
            if cx == 3:
                return "wygrał X"
            elif cy == 3:
                return "wygrał O"

        for x in range(3):
            cx = 0
            cy = 0
            for y in range(3):
                if self.matrix_plansza[x][y] == "x":
                    cx += 1
                elif self.matrix_plansza[x][y] == "o":
                    cy += 1

            if chck(cx, cy) is not None:
                return chck(cx, cy)

        for x in range(3):
            cx = 0
            cy = 0
            for y in range(3):
                if self.matrix_plansza[y][x] == "x":
                    cx += 1
                elif self.matrix_plansza[y][x] == "o":
                    cy += 1

            if chck(cx, cy) is not None:
                return chck(cx, cy)

        cx = 0
        cy = 0
        z = 0

        for x in range(3):
            for y in range(z, 3):
                if self.matrix_plansza[x][y] == "x":
                    cx += 1
                    z+=1
                    break
                elif self.matrix_plansza[x][y] == "o":
                    cy += 1
                    z+=1
                    break
                z+=1

            if chck(cx, cy) is not None:
                return chck(cx, cy)

        cx = 0
        cy = 0
        z = 2

        for x in range(3):
            for y in range(z, -1, -1):
                if self.matrix_plansza[x][y] == "x":
                    cx += 1
                    z -= 1
                    break
                elif self.matrix_plansza[x][y] == "o":
                    cy += 1
                    z -= 1
                    break
                z -= 1

            if chck(cx, cy) is not None:
                return chck(cx, cy)


gra = kik()
gra.wyswietlanie()
xy = ["x", "o"]
c = 0

while True:
    gra.stawianie(xy[c])
    c = (c+1)%2
    if gra.sprawdzenie() is not None:
        print(gra.sprawdzenie())
        break