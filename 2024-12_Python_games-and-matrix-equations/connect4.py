import random

def validation(input_msg: str, expected_answer_1, expected_answer_2, error_msg: str, range: bool=False):

    validation = False
    while(validation == False):
        user_input = input(f"{input_msg}").lower()
        if(range == False):
            if(user_input == str(expected_answer_1).lower() or user_input == str(expected_answer_2).lower()):
                validation = True
                return user_input
        else:
            if(user_input.isnumeric() and int(user_input) >= expected_answer_1 and int(user_input) <= expected_answer_2):
                validation = True
                return user_input
        
        print(f"{error_msg}")

def generate_playing_field(rows: int, col: int) -> list:

    field = []
    for i in range(rows):
        row = []
        for x in range(col):
            row.append("| |")
        field.append(row)
    
    return field

def pretty_output(field: list, message: str, include_field: bool=True):

    line = []
    if(len(field) > len(message)):
        for i in range(len(field)):
            line.append("=")
    else:
        for i in range(len(message)):
            line.append("=")
    print(f'{"".join(line)}')
    print(f"{message}")
    print(f'{"".join(line)}')

    if(include_field):
        for row in field:
            print("".join(row))

def add_player_move_to_field(field: list, col_choice: int, player: str):

    col_choice -= 1
    for row, col in reversed(list(enumerate(field))):
        if col[col_choice] == "| |":
            field[row][col_choice] = f"|{player}|"
            break

def check_connections_on_field(field: list):

    for col in range(len(field[0])):
        X_connection = 1
        O_connection = 1
        for value in range(len(field) - 1):
            if(field[value][col] == "|X|"):
                if(field[value + 1][col] == "|X|"):
                    X_connection += 1
                else:
                    X_connection = 1
            elif(field[value][col] == "|O|"):
                if(field[value + 1][col] == "|O|"):
                    O_connection += 1
                else:
                    O_connection = 1

            if X_connection == 4:
                return "X"
            elif O_connection == 4:
                return "O"
    
    for row in range(len(field)):
        X_connection = 1
        O_connection = 1
        for value in range(len(field[row]) - 1):
            if(field[row][value] == "|X|"):
                if(field[row][value + 1] == "|X|"):
                    X_connection += 1
                else:
                    X_connection = 1
            elif(field[row][value] == "|O|"):
                if(field[row][value + 1] == "|O|"):
                    O_connection += 1
                else:
                    O_connection = 1

            if(X_connection == 4):
                return "X"
            elif(O_connection == 4):
                return "O"
    
    check_connections_on_field_diagonally(field) #diagonali

def check_connections_on_field_diagonally(field): #https://www.geeksforgeeks.org/python-print-diagonals-of-2d-list/ + gpt
    def check_diagonal(diagonal):
        """Helper function to check a single diagonal for winning conditions."""
        X_connection = 0
        O_connection = 0
        for cell in diagonal:
            if cell == "|X|":
                X_connection += 1
                O_connection = 0
            elif cell == "|O|":
                O_connection += 1
                X_connection = 0
            else:
                X_connection = 0
                O_connection = 0

            if X_connection == 4:
                return "X"
            elif O_connection == 4:
                return "O"
        return None

    n = len(field)       # Number of rows
    m = len(field[0])    # Number of columns

    # Check diagonals in the '\' direction (top-left to bottom-right)
    for start_row in range(n):  # Start from each row in the first column
        diagonal = []
        row, col = start_row, 0
        while row < n and col < m:
            diagonal.append(field[row][col])
            row += 1
            col += 1
        result = check_diagonal(diagonal)
        if result:
            return result

    for start_col in range(1, m):  # Start from each column in the first row (excluding top-left corner)
        diagonal = []
        row, col = 0, start_col
        while row < n and col < m:
            diagonal.append(field[row][col])
            row += 1
            col += 1
        result = check_diagonal(diagonal)
        if result:
            return result

    # Check diagonals in the '/' direction (top-right to bottom-left)
    for start_row in range(n):  # Start from each row in the last column
        diagonal = []
        row, col = start_row, m - 1
        while row < n and col >= 0:
            diagonal.append(field[row][col])
            row += 1
            col -= 1
        result = check_diagonal(diagonal)
        if result:
            return result

    for start_col in range(m - 2, -1, -1):  # Start from each column in the first row (excluding top-right corner)
        diagonal = []
        row, col = 0, start_col
        while row < n and col >= 0:
            diagonal.append(field[row][col])
            row += 1
            col -= 1
        result = check_diagonal(diagonal)
        if result:
            return result

    return None
        
#===============================================================================

rows, col = 5, 5
field_generated = False

while(field_generated == False):

    print("Šis ir pašreizējais lauciņa izmērs: ")
    playing_field = generate_playing_field(rows, col)
    for row in playing_field:
        print("".join(row))
    rows += 1
    col += 1
    
    user_input = validation(input_msg= 'Vai vēlaties palielināt lauciņu? (y/n): ',
                            expected_answer_1= "y",
                            expected_answer_2= "n",
                            error_msg= 'Lūdzu ievadiet y vai n')
    if(user_input == "n"):
        field_generated = True
        break

user_choice = validation(input_msg= 'Vai vēlaties spēlēt pret AI? (y/n): ',
                         expected_answer_1= "y",
                         expected_answer_2= "n",
                         error_msg= 'Lūdzu ievadiet y vai n')

if(user_choice.lower() == "n"):
    AI_selected = False
    pretty_output(field= playing_field, message= "Spēle ir sākusies PC1 apzīmējums ( X ) un PC2 apzīmējums ( O )")

    while(check_connections_on_field(field= playing_field) == None):
        user_input = validation(input_msg= f'PC1 gājiens: Izvēlaties kolonu(1-{len(playing_field)}): ',
                                expected_answer_1= 1,
                                expected_answer_2= len(playing_field),
                                error_msg= f"Lūdzu ievadi skaitli no 1 līdz {len(playing_field)}",
                                range= True)
        add_player_move_to_field(field= playing_field, col_choice=int(user_input), player="X")
        pretty_output(field= playing_field, message= "PC1 izvēlējās savu gājienu")

        if(check_connections_on_field(field= playing_field) == None):
            user_input = validation(input_msg= f'PC1 gājiens: Izvēlaties kolonu(1-{len(playing_field)}): ',
                                    expected_answer_1= 1,
                                    expected_answer_2= len(playing_field),
                                    error_msg= f"Lūdzu ievadi skaitli no 1 līdz {len(playing_field)}",
                                    range= True)
            add_player_move_to_field(field= playing_field, col_choice=int(user_input), player="O")
            pretty_output(field= playing_field, message= "PC2 izvēlējās savu gājienu")
elif(user_choice.lower() == "y"):
    AI_selected = True
    pretty_output(field= playing_field, message= "Spēle ir sākusies PC1 apzīmējums ( X ) un AI apzīmējums ( O )")

    while(check_connections_on_field(field= playing_field) == None):
        user_input = validation(input_msg= f'PC1 gājiens: Izvēlaties kolonu(1-{len(playing_field)}): ',
                                expected_answer_1= 1,
                                expected_answer_2= len(playing_field),
                                error_msg= f"Lūdzu ievadi skaitli no 1 līdz {len(playing_field)}",
                                range= True)
        add_player_move_to_field(field= playing_field, col_choice=int(user_input), player="X")
        pretty_output(field= playing_field, message= "PC1 izvēlējās savu gājienu")

        if(check_connections_on_field(field= playing_field) == None):

            add_player_move_to_field(field= playing_field, col_choice=random.randint(1, len(playing_field)), player="O")
            pretty_output(field= playing_field, message= "AI izvēlējās savu gājienu")

if(check_connections_on_field(field= playing_field) == "X"):
    winner = "PC1"
elif(AI_selected and check_connections_on_field(field= playing_field) == "O"):
    winner = "AI"
else:
    winner = "PC2"

pretty_output(field= playing_field, message= f"Spēles uzvarētājs: {winner}", include_field=False)
