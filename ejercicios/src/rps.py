#!/usr/bin/env python3
"""
TODO: Completar este programa de piedra, papel o tijera.

Instrucciones:
- El juego debe pedir al usuario "rock", "paper" o "scissors".
- Debe repetirse muchas veces.
- Si el usuario presiona ENTER sin escribir nada, termina el programa.
- La computadora debe elegir aleatoriamente entre las tres opciones.
- Debe mostrar quién ganó.
- Si el usuario gana, mostrar emojis divertidos (🎉✨🚀).
- Validar entradas incorrectas.
- Usar funciones y type hints modernos (Python 3.9+), ejemplo: tuple[str, str].
"""

import random

# TODO 1: Lista de opciones válidas
VALID_CHOICES = ["rock", "paper", "scissors"]


def determine_result(user: str, cpu: str) -> str:
    """
    TODO 2: Determinar si el usuario gana, pierde o empata.

    Debe regresar:
    - "win"
    - "lose"
    - "draw"
    """
    if user == cpu:
        return "draw"

    # reglas: rock > scissors, scissors > paper, paper > rock
    wins = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
    }

    if wins.get(user) == cpu:
        return "win"
    else:
        return "lose"


def play(user_choice: str) -> tuple[str, str]:
    """
    TODO 3: Ejecutar una ronda del juego.

    Debe regresar una tupla:
        (eleccion_cpu, resultado)

    - Validar que user_choice esté en VALID_CHOICES
    - Elegir opción aleatoria para la CPU
    - Llamar a determine_result()
    """
    # Validar entrada
    if user_choice not in VALID_CHOICES:
        raise ValueError(f"Invalid choice: {user_choice}")

    # Elección aleatoria de la CPU
    cpu_choice = random.choice(VALID_CHOICES)

    # Determinar resultado
    result = determine_result(user_choice, cpu_choice)

    return cpu_choice, result


def main() -> None:
    """
    TODO 4: Hacer que el juego se repita usando un ciclo while.

    - Pedir la elección con input()
    - Salir si el usuario presiona ENTER
    - Mostrar:
        CPU: <elección>
        Resultado: <win/lose/draw>
    - Si el usuario gana, mostrar 🎉✨🎆🎇🚀
    """
    print("🎮 Rock, Paper, Scissors Game 🎮")
    print("Escribe rock, paper o scissors.")
    print("Presiona ENTER sin escribir nada para salir.")
    print("-" * 40)

    # TODO: implementar ciclo del juego
    while True:
        try:
            user = input("Tu elección> ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print()
            break

        # salir si presiona ENTER sin escribir nada
        if user == "":
            print("Saliendo. ¡Hasta luego!")
            break

        if user not in VALID_CHOICES:
            print(f"Entrada no válida: '{user}'. Elige rock, paper o scissors.")
            continue

        cpu_choice, result = play(user)

        print(f"CPU: {cpu_choice}")
        print(f"Resultado: {result}")

        if result == "win":
            print("¡Ganaste! 🎉✨🚀")



if __name__ == "__main__":
    main()
