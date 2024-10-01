import os
class MapaIgrica:
    
    def __init__(self,mapa):
        self.mapa = mapa
        self.skor = 0
        self.hp = 100
        self.path = 'PositionCheck.txt'

    def ucrtaj_mapu(self):
        while True:
            os.system('cls')      
            for x in self.mapa:         
                if x == '9':
                    print('')
                else:
                    print(x, end='')

            print(f"skor: {self.skor}")
            print(f"Health: {self.hp}")
            print('Type in Exit to exit the game. ')
            dugme = input("Pokreni se: ")

            if dugme == 'Exit':
                for i, blok in enumerate(self.mapa):
                    if blok == 'a':
                        if os.path.exists(self.path):
                            with open(self.path, 'w') as file:
                                file.write(str(i))
                                exit()
                        else:
                            with open(self.path, 'w') as file:
                                file.write(str(i))
                                exit()
            if dugme == 'd':
                for i, blok in enumerate(self.mapa):
                    if blok == 'a':
                        if self.mapa[i+1] == '@':
                            self.mapa[i] = ' '
                            self.skor += 10
                        if self.mapa[i+1] == '%':
                            self.mapa[i] = ' '
                            self.hp -= 10
                        if self.mapa[i+1] == '#':
                            continue
                        else:
                            self.mapa[i] = ' '
                            self.mapa[i+1] = 'a'
                            break
            elif dugme == 'w':
                for i, blok in enumerate(self.mapa):
                    if blok == 'a':
                        if self.mapa[i-11] == '@':
                            self.mapa[i] = ' '
                            self.skor += 10
                        if self.mapa[i-11] == '%':
                            self.mapa[i] = ' '
                            self.hp -= 10
                        if self.mapa[i-11] == '#':
                            continue
                        else:
                            self.mapa[i] = ' '
                            self.mapa[i-11] = 'a'
                            break
            elif dugme == 's':
                for i, blok in enumerate(self.mapa):
                    if blok == 'a':
                        if self.mapa[i+11] == '@':
                            self.mapa[i] = ' '
                            self.skor += 10
                        if self.mapa[i+11] == '%':
                            self.mapa[i] = ' '
                            self.hp -= 10
                        if self.mapa[i+11] == '#':
                            continue
                        else:
                            self.mapa[i] = ' '
                            self.mapa[i+11] = 'a'
                            break
            elif dugme == 'a':
                for i, blok in enumerate(self.mapa):
                    if blok == 'a':
                        if self.mapa[i-1] == '@':
                            self.mapa[i] = ' '
                            self.skor += 10
                        if self.mapa[i-1] == '%':
                            self.mapa[i] = ' '
                            self.hp -= 10
                        if self.mapa[i-1] == '#':
                            continue
                        else:
                            self.mapa[i] = ' '
                            self.mapa[i-1] = 'a'
                            break


               
















































