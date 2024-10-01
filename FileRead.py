from Mapa import MapaIgrica
import os
class FileRead:
    
    def __init__(self):
        self.path = 'PositionCheck.txt'
        self.position = None

        if os.path.exists(self.path):
            try:
                with open(self.path, 'r') as file:
                    self.position = int(file.readline())
            except ValueError:
                os.remove(self.path)
            finally:
                print('Relog please. (Re-Loggin again)')

        else:  
            with open(self.path, 'w') as file2:
                file2.write('12')     #Default Position
                self.position = 12
 











        
