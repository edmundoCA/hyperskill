#@title Stage 5/5
from random import randint


def split_full_domino(full_domino):
  stock_pieces = full_domino.copy()
  player_pieces = [list(stock_pieces.pop()) for i in range(7)]
  computer_pieces = [list(stock_pieces.pop()) for i in range(7)]
  stock_pieces = [list(stock_pieces.pop()) for i in range(14)]
  return stock_pieces, player_pieces, computer_pieces


def determinate_starting_piece(player_pieces, computer_pieces):
  piece = None
  i = 7
  while piece is None and i > 0:
    if [i, i] in player_pieces:
      player_pieces.remove([i, i])
      piece = [i, i]
    elif [i, i] in computer_pieces:
      computer_pieces.remove([i, i])
      piece = [i, i]
    i -= 1
  return piece


def determinate_starting_status(player_pieces, computer_pieces):
  return "player" if len(player_pieces) > len(computer_pieces) else "computer"


def draw_interface(stock_pieces, computer_pieces, domino_snake, player_pieces,
                   status):
  print("======================================================================")
  print(f"Stock pieces: {len(stock_pieces)}")
  print(f"Computer pieces: {len(computer_pieces)}\n")
  string_domino_snake = ""
  if len(domino_snake) > 6:
    for domino in domino_snake[:3]:
      string_domino_snake += f"{domino}"
    string_domino_snake += f"..."
    for domino in domino_snake[-3:]:
      string_domino_snake += f"{domino}"
  else:
    for domino in domino_snake:
      string_domino_snake += f"{domino}"
  print(string_domino_snake)
  print("\nYour pieces:")
  for i in range(len(player_pieces)):
    print(f"{i + 1}: {player_pieces[i]}")
  print("\nStatus: It's your turn to make a move. Enter your command." 
        if status == "player" 
        else "\nStatus: Computer is about to make a move. Press Enter to continue...")


def player_move(stock_pieces, computer_pieces, domino_snake, player_pieces, 
              status, prompt):
  if prompt == 0:
    if len(stock_pieces) > 0:
      player_pieces.append(stock_pieces.pop())
  else:
    piece = player_pieces.pop(abs(prompt) - 1)
    if prompt > 0:
      if piece[0] != domino_snake[-1][-1]:
        piece.reverse()
      domino_snake.insert(len(domino_snake), piece)
    else:
      if piece[1] != domino_snake[0][0]:
        piece.reverse()
      domino_snake.insert(0, piece)
  status = "computer"
  return stock_pieces, computer_pieces, domino_snake, player_pieces, status


def is_valid_move(piece, domino_snake, prompt):
  return (piece[0] == domino_snake[0][0] or piece[1] == domino_snake[0][0] 
          if prompt < 0 else piece[0] == domino_snake[-1][-1] 
          or piece[1] == domino_snake[-1][-1])


def calc_rarity(domino_list):
  rarity_dict = {}
  for domino in domino_list:
    for i in range(2):
      try:
        rarity_dict[domino[i]] += 1
      except KeyError:
        rarity_dict[domino[i]] = 1
  return rarity_dict


def computer_move(stock_pieces, computer_pieces, domino_snake, player_pieces, 
              status):
  rarity_hand = calc_rarity(computer_pieces)
  rarity_snake = calc_rarity(domino_snake)
  for key in set(rarity_hand.keys()).intersection(set(rarity_snake.keys())):
    rarity_hand[key] += rarity_snake[key]
  rarity_piece = {}
  for piece in computer_pieces:
    rarity_piece[tuple(piece)] = rarity_hand[piece[0]] + rarity_hand[piece[1]]
  rarity_piece = dict(sorted(rarity_piece.items(), key=lambda item: item[1]))
  keys = list(rarity_piece.keys())
  while len(keys) > 0:
    key = list(keys.pop(-1))
    if domino_snake[0][0] == key[1]:
      computer_pieces.remove(key)
      domino_snake.insert(0, key)
      break
    elif domino_snake[0][0] == key[0]:
      computer_pieces.remove(key)
      key.reverse()
      domino_snake.insert(0, key)
      break
    elif domino_snake[-1][-1] == key[0]:
      computer_pieces.remove(key)
      domino_snake.insert(-1, key)
      break
    elif domino_snake[-1][-1] == key[-1]:
      computer_pieces.remove(key)
      key.reverse()
      domino_snake.insert(-1, key)
      break
    elif len(keys) == 0 and len(stock_pieces) > 0:
      computer_pieces.append(stock_pieces.pop())
  status = "player"
  return stock_pieces, computer_pieces, domino_snake, player_pieces, status


def user_prompt(stock_pieces, computer_pieces, domino_snake, player_pieces,
                status):
  prompt = input()
  if status == "player":
    try:
      prompt = int(prompt)
    except ValueError:
      print("Invalid input. Please try again.")
      return user_prompt(stock_pieces, computer_pieces, domino_snake, 
                         player_pieces, status)
    else:
      if not -len(player_pieces) - 1 < prompt < len(player_pieces) + 1:
        print("Invalid input. Please try again.")
        return user_prompt(stock_pieces, computer_pieces, domino_snake, 
                           player_pieces, status)
      elif prompt != 0 and not is_valid_move(player_pieces[abs(prompt) - 1], 
                                             domino_snake, prompt):
        print("Illegal move. Please try again.")
        return user_prompt(stock_pieces, computer_pieces, domino_snake, 
                           player_pieces, status)

  else:
    return computer_move(stock_pieces, computer_pieces, domino_snake, 
                         player_pieces, status)
  return player_move(stock_pieces, computer_pieces, domino_snake, player_pieces, 
              status, prompt)


def win_condition(computer_pieces, domino_snake, player_pieces):
  if len(computer_pieces) == 0:
    return "Status: The game is over. The computer won!"
  elif len(player_pieces) == 0:
    return "Status: The game is over. You won!"
  elif domino_snake[0][0] == domino_snake[-1][-1]:
    count = 0
    for domino in domino_snake:
      if domino_snake[0][0] in domino:
        count += 1
    if count == 7:
      return "Status: The game is over. It's a draw!"
  return None


def main():
  FULL_DOMINO = {(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
                   (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
                   (3, 3), (3, 4), (3, 5), (3, 6), (3, 7),
                   (4, 4), (4, 5), (4, 6), (4, 7),
                   (5, 5), (5, 6), (5, 7),
                   (6, 6), (6, 7),
                   (7, 7)}
  stock_pieces, player_pieces, computer_pieces = split_full_domino(FULL_DOMINO)
  starting_piece = determinate_starting_piece(player_pieces, computer_pieces)
  if starting_piece is None:
    main()
  else:
    domino_snake = [starting_piece]
    status = determinate_starting_status(player_pieces, computer_pieces)
    game_over = None
    while game_over is None:
      draw_interface(stock_pieces, computer_pieces, domino_snake, player_pieces,
                   status)
      stock_pieces, computer_pieces, domino_snake, player_pieces, status = user_prompt(stock_pieces, computer_pieces, domino_snake, player_pieces, status)
      game_over = win_condition(computer_pieces, domino_snake, player_pieces)
    print("======================================================================")
    print(f"Stock pieces: {len(stock_pieces)}")
    print(f"Computer pieces: {len(computer_pieces)}\n")
    string_domino_snake = ""
    if len(domino_snake) > 6:
      for domino in domino_snake[:3]:
        string_domino_snake += f"{domino}"
      string_domino_snake += f"..."
      for domino in domino_snake[-3:]:
        string_domino_snake += f"{domino}"
    else:
      for domino in domino_snake:
        string_domino_snake += f"{domino}"
    print(string_domino_snake)
    print("\nYour pieces:")
    for i in range(len(player_pieces)):
      print(f"{i + 1}: {player_pieces[i]}")
    print(game_over)


if __name__ == '__main__':
    main()
