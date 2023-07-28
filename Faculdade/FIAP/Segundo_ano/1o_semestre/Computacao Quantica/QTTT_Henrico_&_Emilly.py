"""
Nomes: Henrico Nardelli Bela & Emilly Gabrielly
RMs: 95985 & 94437
"""

from termcolor import colored, cprint
import json
import qiskit
from qiskit import *
from qiskit.tools.monitor import job_monitor

def initializeBoard():
  return {'1': [' ', 0], '2': [' ', 0], '3': [' ', 0],
          '4': [' ', 0], '5': [' ', 0], '6': [' ', 0],
          '7': [' ', 0], '8': [' ', 0], '9': [' ', 0]}

def displayBoard(board):
  print()
  color_index = 0
  for i in range(1, 10):
    if board[str(i)][1] == 0:
      cprint(board[str(i)][0], end='')
    else:
      colors = ['red', 'green', 'blue', 'yellow']
      cprint(board[str(i)][0], colors[color_index % len(colors)], end='')
      color_index += 1

    if i % 3 == 0:
      print()
      if i != 9:
        print('-+-+-')
    else:
      cprint('|', end='')

def performClassicMove(theBoard, turn, count, circuit):
  valid_moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

  while True:
    print()
    print("Qual a posição? (1-9) ", end='')
    position = input()

    if position in valid_moves:
      if theBoard[position][0] == ' ':
        theBoard[position][0] = turn
        count += 1
        theBoard[position][1] = 0
        circuit.x(int(position) - 1)
        print(circuit.draw())
        break
      else:
        print()
        print("Essa posição já está preenchida.")
    else:
      print("Por favor, escolha uma posição de 1 a 9")

  return theBoard, turn, count, circuit

def performQuantumMove(theBoard, count, circuit, turn):
  valid_moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

  while True:
    print()
    print("Escolha a primeira posição? (1-9) ")
    position1 = input()
    print("Escolha a segunda posição? (1-9) ")
    position2 = input()

    if (theBoard[position1][0] == ' ' and theBoard[position2][0] == ' '
            and position1 != position2):
      theBoard[position1][0] = turn
      theBoard[position2][0] = turn
      count += 2
      theBoard[position1][1] = 1
      theBoard[position2][1] = 1

      circuit.h(int(position1) - 1)
      circuit.x(int(position2) - 1)
      circuit.cx(int(position1) - 1, int(position2) - 1)

      print(circuit.draw())
      break
    else:
      print()
      print("Você selecionou uma(s) posição(ões) inválida(s)")

  return theBoard, count, circuit, turn

def performMeasurement(circuit, theBoard, count):
  displayBoard(theBoard)
  print()
  print("Realizando a medida.")
  print()

  simulator = qiskit.Aer.get_backend('qasm_simulator')

  for i in range(9):
    circuit.measure(i, i)

  print(circuit.draw())

  job = qiskit.execute(circuit, simulator, shots=1)

  result = job.result()

  out = json.dumps(result.get_counts()) 
  string = out[2:11] 

  for i in range(9):
    if string[i] == '1':
      theBoard[str(9 - i)][1] = 0
    else:
      theBoard[str(9 - i)][1] = 0
      theBoard[str(9 - i)][0] = ' '

  count = 0
  for i in range(9):
    theBoard[str(i + 1)][1] = 0
    if theBoard[str(i + 1)][0] != ' ':
      count += 1

  for i in range(9):
    circuit.reset(i)

  for i in range(9):
    if string[8 - i] == '1':
      circuit.x(i)

  return circuit, string, theBoard, count

def checkWin(theBoard, turn):
  win_conditions = [
    ('7', '8', '9'),
    ('4', '5', '6'),
    ('1', '2', '3'),
    ('1', '4', '7'),
    ('2', '5', '8'),
    ('3', '6', '9'),
    ('7', '5', '3'),
    ('1', '5', '9')
  ]

  for condition in win_conditions:
    if (theBoard[condition[0]][0] == theBoard[condition[1]][0] == theBoard[condition[2]][0] != ' ' and
        theBoard[condition[0]][1] == theBoard[condition[1]][1] == theBoard[condition[2]][1] == 0):
      displayBoard(theBoard)
      print("\nJogo encerrado.\n")                
      print(" **** ", end='')
      print(theBoard[condition[1]][0], end='')
      print(" Venceu ****")
      print()
      return True

  return False

def playGame():
    turn = 'X'
    count = 0
    win = False
    x_collapse = 1
    y_collapse = 1

    circuit = qiskit.QuantumCircuit(9, 9)

    while not win:
        global theBoard
        displayBoard(theBoard)
        print()
        print("Sua vez, " + turn + ". Escolha uma opção: (1) Movimento clássico, (2) Movimento quântico, (3) Colapso, (4) Desistir")

        move = input()

        if int(move) == 1:
            theBoard, turn, count, circuit = performClassicMove(theBoard, turn, count, circuit)
            madeMove = True

        elif int(move) == 2 and count > 8:
            print()
            print("Não há espaços vazios suficientes para isso!")

        elif int(move) == 2 and count < 8:
            theBoard, count, circuit, turn = performQuantumMove(theBoard, count, circuit, turn)
            madeMove = True

        elif int(move) == 3:
            if turn == 'X' and x_collapse == 1:
                circuit, string, theBoard, count = performMeasurement(circuit, theBoard, count)
                x_collapse = 0
            elif turn == 'O' and y_collapse == 1:
                circuit, string, theBoard, count = performMeasurement(circuit, theBoard, count)
                y_collapse = 0
            else:
                print("Você já usou seu colapso neste jogo!")

        elif int(move) == 4:
            break

        if count >= 5:
            win = checkWin(theBoard, turn)
            if win:
                break

        if count == 9:
            circuit, string, theBoard, count = performMeasurement(circuit, theBoard, count)
            win = checkWin(theBoard, turn)
            if count == 9:
                print("\nAcabou o jogo.\n")
                print("O jogo empatou!")
                print()
                win = True

        if madeMove:
            madeMove = False
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'

    restart = input("Jogar novamente? (s/n) ")
    if restart.lower() == "s":
        theBoard = initializeBoard()
        playGame()


def startMenu():
    start_menu = """
    Inicio:
    1. Começar o jogo
    2. regras do jogo
    3. Sair
    """

    print("""
    ---- Quantum tic tac toe ----
    """)
    print(start_menu)
    choice = 0
    while choice != '1':
        print("O que você gostaria de fazer? ", end='')
        choice = input()

        if choice == '2':
            how_to = """
No jogo Quantum Tic-Tac-Toe, cada célula do tabuleiro começa vazia, e o objetivo é formar uma linha de três de suas peças (zeros ou xis).

Existem dois tipos de movimentos que você pode fazer:

      Movimento Clássico: Você marca uma célula vazia com a sua peça de forma permanente.
      Movimento Quântico: Você cria uma sobreposição entre duas células vazias de sua escolha. Isso significa que as duas células podem conter tanto sua peça quanto a peça do seu oponente.
      O tabuleiro entrará em colapso quando todas as células estiverem preenchidas. No colapso, cada sobreposição é "observada", e apenas uma das peças da sobreposição permanece.

Além disso, há um power-up especial disponível:

      Power-up de Colapso Prematuro: Cada jogador pode decidir colapsar o tabuleiro antes que ele esteja completamente preenchido. Isso significa que as sobreposições serão resolvidas antecipadamente, e apenas uma peça de cada sobreposição permanecerá. Cada jogador só pode usar esse poder uma vez por rodada.
            """
            print(how_to)

        if choice == '3':
            print("xau")
            break

    return choice


theBoard = initializeBoard()

if startMenu() == '1':
    madeMove = False
    playGame()
