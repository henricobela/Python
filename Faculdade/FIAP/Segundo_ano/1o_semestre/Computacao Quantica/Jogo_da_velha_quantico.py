"""
Grupo:
    Henrico Nardelli Bela - RM 95985
"""


from termcolor import colored, cprint
import json, qiskit
from qiskit import *
from qiskit.tools.monitor import job_monitor


def resetBoard():
    return {
        "1": [" ", 0],
        "2": [" ", 0],
        "3": [" ", 0],
        "4": [" ", 0],
        "5": [" ", 0],
        "6": [" ", 0],
        "7": [" ", 0],
        "8": [" ", 0],
        "9": [" ", 0],
    }


def printBoard(board):
    print()
    colour = 0
    for i in range(1, 10):
        if board[str(i)][1] == 0:
            cprint(board[str(i)][0], end="")
        else:
            if colour == 0 or colour == 1:
                cprint(board[str(i)][0], "red", end="")
                colour = colour + 1
            elif colour == 2 or colour == 3:
                cprint(board[str(i)][0], "green", end="")
                colour = colour + 1
            elif colour == 4 or colour == 5:
                cprint(board[str(i)][0], "blue", end="")
                colour = colour + 1
            elif colour == 6 or colour == 7:
                cprint(board[str(i)][0], "yellow", end="")
                colour = colour + 1

        if i % 3 == 0:
            print()
            if i != 9:
                print("-+-+-")
        else:
            cprint("|", end="")


def make_classic_move(theBoard, turn, count, circuit):
    valid_move = 0
    valid_moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    while not valid_move:
        print()
        print("Qual o local? (1-9) ", end="")
        location = input()

        if location in valid_moves:
            if theBoard[location][0] == " ":
                valid_move = 1

                theBoard[location][0] = turn

                count += 1

                theBoard[location][1] = 0

                circuit.x(int(location) - 1)

                print(circuit.draw())
            else:
                print()
                print("Esse lugar já está preenchido.")
        else:
            print("Por favor escolha um quadrado de 1-9")

    return theBoard, turn, count, circuit


def make_quantum_move(theBoard, count, circuit, turn):
    valid_move = False
    valid_moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    while not valid_move:
        print()
        print("Escolha o local? (1-9) ")
        location1 = input()
        print("Escolha o local? (1-9) ")
        location2 = input()

        if (
            theBoard[location1][0] == " "
            and theBoard[location2][0] == " "
            and location1 != location2
        ):
            theBoard[location1][0] = turn
            theBoard[location2][0] = turn

            count += 2

            theBoard[location1][1] = 1
            theBoard[location2][1] = 1

            circuit.h(int(location1) - 1)

            circuit.x(int(location2) - 1)

            circuit.cx(int(location1) - 1, int(location2) - 1)

            print(circuit.draw())
            valid_move = True
        else:
            print()
            print("Você selecionou uma(s) posição(ões) inválida(s)")

    return theBoard, count, circuit, turn


def measure(circuit, theBoard, count):
    printBoard(theBoard)
    print()
    print("Acionar o colapso.")
    print()

    simulator = qiskit.Aer.get_backend("qasm_simulator")

    circuit.measure(0, 0)
    circuit.measure(1, 1)
    circuit.measure(2, 2)
    circuit.measure(3, 3)
    circuit.measure(4, 4)
    circuit.measure(5, 5)
    circuit.measure(6, 6)
    circuit.measure(7, 7)
    circuit.measure(8, 8)

    print(circuit.draw())

    job = qiskit.execute(circuit, simulator, shots=1)

    result = job.result()

    out = json.dumps(result.get_counts())
    string = out[2:11]

    for i in range(9):
        if string[i] == "1":
            theBoard[str(9 - i)][1] = 0
        else:
            theBoard[str(9 - i)][1] = 0
            theBoard[str(9 - i)][0] = " "

    count = 0
    for i in range(9):
        theBoard[str(i + 1)][1] = 0
        if theBoard[str(i + 1)][0] != " ":
            count += 1

    circuit.reset(0)
    circuit.reset(1)
    circuit.reset(2)
    circuit.reset(3)
    circuit.reset(4)
    circuit.reset(5)
    circuit.reset(6)
    circuit.reset(7)
    circuit.reset(8)

    for i in range(9):
        if string[8 - i] == "1":
            circuit.x(i)

    return circuit, string, theBoard, count


def check_win(theBoard, turn):
    if theBoard["7"][0] == theBoard["8"][0] == theBoard["9"][0] != " ":
        if theBoard["7"][1] == theBoard["8"][1] == theBoard["9"][1] == 0:
            printBoard(theBoard)
            print("\nAcabou o jogo.\n")
            print(" **** ", end="")
            print(theBoard["8"][0], end="")
            print(" Ganhou ****")
            print()
            return True

    elif theBoard["4"][0] == theBoard["5"][0] == theBoard["6"][0] != " ":
        if theBoard["4"][1] == theBoard["5"][1] == theBoard["6"][1] == 0:
            printBoard(theBoard)
            print("\nAcabou o jogo.\n")
            print(" **** ", end="")
            print(theBoard["5"][0], end="")
            print(" Ganhou ****")
            print()
            return True

    elif theBoard["1"][0] == theBoard["2"][0] == theBoard["3"][0] != " ":
        if theBoard["1"][1] == theBoard["2"][1] == theBoard["3"][1] == 0:
            printBoard(theBoard)
            print("\nAcabou o jogo.\n")
            print(" **** ", end="")
            print(theBoard["2"][0], end="")
            print(" Ganhou ****")
            print()
            return True

    elif theBoard["1"][0] == theBoard["4"][0] == theBoard["7"][0] != " ":
        if theBoard["1"][1] == theBoard["4"][1] == theBoard["7"][1] == 0:
            printBoard(theBoard)
            print("\nAcabou o jogo.\n")
            print(" **** ", end="")
            print(theBoard["4"][0], end="")
            print(" Ganhou ****")
            print()
            return True

    elif theBoard["2"][0] == theBoard["5"][0] == theBoard["8"][0] != " ":
        if theBoard["2"][1] == theBoard["5"][1] == theBoard["8"][1] == 0:
            printBoard(theBoard)
            print("\nAcabou o jogo.\n")
            print(" **** ", end="")
            print(theBoard["5"][0], end="")
            print(" Ganhou ****")
            print()
            return True

    elif theBoard["3"][0] == theBoard["6"][0] == theBoard["9"][0] != " ":
        if theBoard["3"][1] == theBoard["6"][1] == theBoard["9"][1] == 0:
            printBoard(theBoard)
            print("\nAcabou o jogo.\n")
            print(" **** ", end="")
            print(theBoard["6"][0], end="")
            print(" Ganhou ****")
            print()
            return True

    elif theBoard["7"][0] == theBoard["5"][0] == theBoard["3"][0] != " ":
        if theBoard["7"][1] == theBoard["5"][1] == theBoard["3"][1] == 0:
            printBoard(theBoard)
            print("\nAcabou o jogo.\n")
            print(" **** ", end="")
            print(theBoard["5"][0], end="")
            print(" Ganhou ****")
            print()
            return True

    elif theBoard["1"][0] == theBoard["5"][0] == theBoard["9"][0] != " ":
        if theBoard["1"][1] == theBoard["5"][1] == theBoard["9"][1] == 0:
            printBoard(theBoard)
            print("\nAcabou o jogo.\n")
            print(" **** ", end="")
            print(theBoard["5"][0], end="")
            print(" Ganhou ****")
            print()
            return True


def game():
    turn = "X"
    count = 0
    win = False
    x_collapse = 1
    y_collapse = 1

    circuit = qiskit.QuantumCircuit(9, 9)

    while not win:
        global theBoard
        printBoard(theBoard)

        print()
        print(
            "É a sua vez "
            + turn
            + ". Você quer fazer um (1) movimento clássico, (2) movimento quântico, (3) colapso? ou (4) desistir?"
        )

        move = input()

        if int(move) == 1:
            theBoard, turn, count, circuit = make_classic_move(
                theBoard, turn, count, circuit
            )
            madeMove = True

        elif int(move) == 2 and count > 8:
            print()
            print("Não há espaços vazios suficientes para isso!")

        elif int(move) == 2 and count < 8:
            theBoard, count, circuit, turn = make_quantum_move(
                theBoard, count, circuit, turn
            )
            madeMove = True

        elif int(move) == 3:
            if turn == "X" and x_collapse == 1:
                circuit, string, theBoard, count = measure(circuit, theBoard, count)
                x_collapse = 0
            elif turn == "O" and y_collapse == 1:
                circuit, string, theBoard, count = measure(circuit, theBoard, count)
                y_collapse = 0
            else:
                print("Você já usou seu colapso neste jogo!")

        elif int(move) == 4:
            break

        if count >= 5:
            win = check_win(theBoard, turn)
            if win:
                break

        if count == 9:
            circuit, string, theBoard, count = measure(circuit, theBoard, count)
            win = check_win(theBoard, turn)
            if count == 9:
                print("\nAcabou o jogo.\n")
                print("O jogo empatou !")
                print()
                win = True

        if madeMove:
            madeMove = False
            if turn == "X":
                turn = "O"
            else:
                turn = "X"

    restart = input("Jogar denovo?(y/n) ")
    if restart == "y" or restart == "Y":
        theBoard = resetBoard()
        game()


def start_menu():
    start_menu = """
    Menu inicial:
    1. Começar o jogo
    2. Como jogar
    3. Sair
    """

    print(
        """
    ################################
    #### Jogo da velha quantico ####
    ################################
    """
    )
    print(start_menu)
    choice = 0
    while choice != "1":
        print("O que você gostaria de fazer? ", end="")
        choice = input()

        if choice == "2":
            How_To = """ 
        Em Quantum Tic-Tac-Toe, cada quadrado começa vazio e seu objetivo é criar uma linha de três de seus zeros/cruzes.
        Jogar um movimento clássico resultará na definição de um quadrado permanentemente como sua peça.
        Jogar um movimento quântico criará uma superposição entre dois quadrados de sua escolha. Você só pode completar um movimento quântico em dois quadrados vazios.
        O tabuleiro entrará em colapso quando estiver cheio. No colapso, cada superposição é visualizada e apenas 1 peça da superposição permanecerá.
        *Powerup* Cada jogador pode decidir derrubar o tabuleiro prematuramente, eles podem fazer isso uma vez por rodada cada.
        """
            print(How_To)

        if choice == "3":
            print("Tchau")
            break

    return choice


theBoard = resetBoard()

if start_menu() == "1":
    madeMove = False
    game()
