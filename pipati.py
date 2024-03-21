"""
Piedra, Papel y Tijeras en Python

Objetivo: Implementar el juego clásico de "Piedra, Papel y Tijeras" utilizando clases 
y objetos en Python.

Requisitos:

El juego consiste en dos jugadores, cada uno selecciona uno de los tres gestos posibles: 
    piedra, papel o tijera.

El juego debe decidir el ganador basado en las reglas clásicas:

Piedra aplasta tijera.
Tijera corta papel.
Papel cubre piedra.

Si ambos jugadores eligen el mismo gesto, es un empate.
El juego se juega en rondas, y el primer jugador que gane dos rondas 
será declarado el ganador final.
Los gestos de los jugadores deben ser seleccionados al azar.

Instrucciones:

Defina una clase Gesto que represente uno de los gestos posibles. 
    Esta clase debe ser capaz de generar un gesto aleatorio y mostrarlo como una cadena de texto.
Defina una clase Jugador que represente a un jugador del juego. 
    Cada jugador tiene un nombre y un gesto actual.
Defina una clase Juego que coordine el juego entre dos jugadores. 
    Debe ser capaz de determinar el ganador de una ronda y seguir la puntuación.

Implemente una función main que inicialice y comience el juego.

Ejecute el programa y observe los resultados de cada ronda hasta que un jugador gane.
Consejos:

Utilice constantes para representar los gestos posibles, esto hará que su código sea más legible.
Descomponga el problema en partes manejables y enfoque su atención en una clase a la vez.
Pruebe cada clase individualmente para asegurarse de que funcione correctamente antes de combinarlas.
"""

import random

class Gesto:

    # Definimos constantes para los gestos

    PIEDRA = 1
    PAPEL = 2
    TIJERA = 3

    # Creamos un diccionario para mapear el número del gesto a su nombre
    GESTOS = {1:'PIEDRA', 2:'PAPEL', 3:'TIJERAS'}

    # Constructor de la clase Gesto
    def __init__(self) -> None:
        
        # Iniciamos el gesto del jugador
        self.__gesto:int = self.__gesto_random()

    
    def get_gesto(self)->int:
        # Devolvemos el gesto actual del jugador
        return self.__gesto

    def __gesto_random(self)-> int:
        # Generamos un gesto aleatorio para el jugador
        return random.randint(Gesto.PIEDRA,Gesto.TIJERA)
    
    def __str__(self) -> str:
        # Convertimos el gesto a su nombre correspondiente
        return Gesto.GESTOS[self.__gesto]
    
    def __eq__(self, __value: object) -> bool:
        # Este metodo nos sirve para comparar dos gestos y ver si son iguales
        if __value is None or not isinstance(__value,Gesto):
            return False
        return self.__gesto == __value.__gesto



class Jugador:

    # Constructor de la clase Jugador
    def __init__(self, nombre:str) -> None:

        # Asigna el nombre del jugador y un gesto inicial aleatorio
        self.__nombre:str = nombre
        self.__gesto:Gesto = Gesto()

    def get_gesto(self)->Gesto:
        # Método para obtener el gesto actual del jugador
        return self.__gesto
    
    def get_nombre(self)->str:
        # Método para obtener eñ nombre del jugador 
        return self.__nombre
    
    def __str__(self) -> str:
        # Método para obtener una representación en forma de string del jugador y su gesto actual
        return f"{self.__nombre} ==> {str(self.__gesto)}"

    # Método para que el jugador realice un nuevo gesto
    def hacer_gesto(self)->None:
        # Actualiza el gesto actual del jugador a uno nuevo generado aleatoriamente
        self.__gesto = Gesto()




class PiPaTi:

    # Constructor de la clase PiPaTi
    def __init__(self, nombre_jugador1:str, nombre_jugador2:str) -> None:
        # Crea dos jugadores con los nombres dados
        self.__jug1 = Jugador(nombre_jugador1)
        self.__jug2 = Jugador(nombre_jugador2)

    
    # Método para iniciar el juego
    def jugar(self):
        # Se juegan rondas hasta que un jugador gane dos veces
        victorias_jugador1 = 0
        victorias_jugador2 = 0

        while victorias_jugador1 < 2 and victorias_jugador2 < 2:
            # Cada jugador hace un gesto
            self.__jug1.hacer_gesto()
            print(self.__jug1)
            self.__jug2.hacer_gesto()
            print(self.__jug2)

            # Se determina el ganador de la ronda
            ganador = self.__quien_gana()

            if ganador is self.__jug1:
                print(f"Gana: {self.__jug1.get_nombre()}")
                victorias_jugador1 += 1
            elif ganador is self.__jug2:
                victorias_jugador2 += 1
                print(f"Gana: {self.__jug2.get_nombre()}")
            else:
                print("Empate!")

        # Se muestra el ganador del juego
        print(f"Ganadorrrrrrrrrrrrrrr: {ganador.get_nombre()}")


    # Método privado utilizado para determinar el ganador de la ronda
    def __quien_gana(self)->Jugador:
        gesto1 = self.__jug1.get_gesto()
        gesto2 = self.__jug2.get_gesto()

        if gesto1 == gesto2:
            return None
        else:
            gesto1 = gesto1.get_gesto()
            gesto2 = gesto2.get_gesto()
            if gesto1 == Gesto.PIEDRA and gesto2 == Gesto.TIJERA or \
                gesto1 == Gesto.PAPEL and gesto2 == Gesto.PIEDRA or \
                    gesto1 == Gesto.TIJERA and gesto2 == Gesto.PAPEL:
                return self.__jug1
        return self.__jug2

        

# Función principal que inicia el juego de Piedra, Papel o Tijeras
def main():
    
    # Crea una instancia de PiPaTi con los nombres "Juan" y "Maria"
    # Llama al método jugar() para iniciar el juego
    PiPaTi("Juan","Maria").jugar()

main()