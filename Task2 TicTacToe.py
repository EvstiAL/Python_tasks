board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
    ] # досочка 3х3

class tiktaktoe:

    def __init__(self, board):
        self.board = board

    def draw_pole(self): # нарисовать поле
        """
        Данная функция предназначена для начертания игрового поля в консоль
        """
        print("-------------")
        print(self.board[0][0],"|", self.board[0][1],"|",self.board[0][2],"|")
        print(self.board[1][0],"|",self.board[1][1],"|",self.board[1][2],"|")
        print(self.board[2][0],"|",self.board[2][1],"|",self.board[2][2],"|")
        print("-------------")
    
    def moves(self): # шаги
        """
        Функция логики движения
        """
        mov = []
        for r in self.board:
            for c in r:
                if c != 'X' and c != 'O':
                    mov.append(int(c))
        return mov

    def sel_space(self, move, turn): #выбор места
        r = (move-1)//3
        c = (move-1)%3
        self.board[r][c] = '{}'.format(turn)

    def won_player(self, player): # выигрыш игрока
        """
        Функция определения победителя по трем парамтрам
        """
        for r in self.board:
            if r.count(player) == 3:
                return True
        for i in range(3):
            if self.board[0][i] == player and self.board[1][i] == player and self.board[2][i] == player:
                return True
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        if self.board[0][2] == player and self.board[1][1] == player and board[2][0] == player:
            return True
        return False


    def game_over(self): # Игра окончена
        """
        Функция обработки шагов
        """
        self.moves()
        if self.won_player("X") or self.won_player("O") or len(self.moves()) == 0:
            return True
        else:
            return False
    def player_move(self, turn):
        move = int(input("Игрок {player} cделайте Ваш шаг: ".format(player=turn)))
        self.moves()
        while move not in range (1,10) or move not in self.moves():
            move = int(input("В поле такого нет, попробуйте ещё раз!"))
        return move


def game(board): # сама игра
  """
  Функция обработки логики самой игры, а также, определения победителя.
  """
  ttt = tiktaktoe(board)
  while not ttt.game_over():
    ttt.draw_pole()
    x_move = ttt.player_move("X")
    ttt.sel_space(x_move,"X")
    ttt.draw_pole()

    o_move = ttt.player_move("O")
    ttt.sel_space(o_move,"O")
  if ttt.won_player("X"):
    print("Побелил Крестик!")

  elif ttt.won_player("O"):
    print("Победил Нолик")
  else:
    print("Ничья!")    


game(board)