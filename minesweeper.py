"""Attempting to Create Minesweeper!"""

__author__ = "Lucas Siegel"

from random import random


class Cell:
    data: str
    tapped: bool
    flagged: bool

    def __init__(self) -> None:
        """Construct a new Cell."""
        self.data = " "
        self.tapped = False
        self.flagged = False

    def __str__(self) -> str:
        """String representation of a cell."""
        return self.data

    def get_data(self) -> str:
        return self.data
    
    def get_tapped(self) -> bool:
        return self.tapped
    
    def get_flagged(self) -> bool:
        return self.flagged
    
    def set_data(self, new_data: str) -> None:
        self.data = new_data

    def set_tapped(self, tap: bool) -> None:
        self.tapped = tap

    def set_flagged(self, flag: bool) -> None:
        self.flagged = flag


chars: list[str] = [" ", "B", "F"]
player_board: list[list[Cell]] = [
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()], 
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()]
]
master_board: list[list[Cell]] = [
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()], 
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()]
]
bombs: int = 20


def main() -> None:
    count: int = 0
    playing: bool = True
    set_bombs(bombs)
    print("Welcome to Minesweeper! Your objective is to flag all the bombs and clear the area, but if you tap on a bomb, you lose! There are three actions you can take: Tapping, Setting a Flag, and Removing a flag.")
    while playing:
        display_player()
        action: str = input("Which action would you like to take? Type 0 to quit, 1 to tap, 2 to set a flag, and 3 to remove a flag: ")
        if action == "0":
            print("Thanks for playing!")
            exit()
        if action == "1":
            tap()
        if action == "2":
            if set_flag():
                count += 1
        if action == "3":
            remove_flag()
        if count == bombs:
            playing = False
    print("Congratulations! You cleared all the bombs!")


def display_player() -> None:
    """Display the player's board."""
    i: int = 0
    while i < 10:
        print(f"| {player_board[i][0]} | {player_board[i][1]} | {player_board[i][2]} | {player_board[i][3]} | {player_board[i][4]} | {player_board[i][5]} | {player_board[i][6]} | {player_board[i][7]} | {player_board[i][8]} | {player_board[i][9]} |") 
        i += 1


def display_master() -> None:
    """Display the master board."""
    i: int = 0
    while i < 10:
        print(f"| {master_board[i][0]} | {master_board[i][1]} | {master_board[i][2]} | {master_board[i][3]} | {master_board[i][4]} | {master_board[i][5]} | {master_board[i][6]} | {master_board[i][7]} | {master_board[i][8]} | {master_board[i][9]} |") 
        i += 1


def set_bombs(bombs: int) -> None:
    """Sets the bombs up."""
    i: int = 0
    j: int = 0
    setting: bool = True
    count: int = 0
    while setting:
        i = 0
        while i < 10:
            j = 0
            while j < 10:
                if random() < 0.01 and master_board[i][j].get_data() != "B":
                    master_board[i][j].set_data("B")
                    count += 1
                    if count == bombs:
                        setting = False
                j += 1
                if setting is False:
                    break
            i += 1  
            if setting is False:
                break


def set_flag() -> bool:
    location: str = input("Where would you like to flag? Please type your answer as a two-digit integer with the first digit representing the row and the second digit representing the column. For example, if you wanted to place a flag in the top right corner, you would type 09: ")
    locationy: int = int(location[0])
    locationx: int = int(location[1])
    player_board[locationy][locationx].set_data(chars[2])
    player_board[locationy][locationx].set_flagged(True)
    if master_board[locationy][locationx].get_data() == chars[1]:
        return True
    else:
        return False


def remove_flag() -> None:
    location: str = input("Where would you like to remove a flag? Please type your answer as a two-digit integer with the first digit representing the row and the second digit representing the column. For example, if you wanted to remove a flag in the top right corner, you would type 09: ")
    locationy: int = int(location[0])
    locationx: int = int(location[1])
    player_board[locationy][locationx].set_data(chars[0])
    player_board[locationy][locationx].set_flagged(False)


def tap() -> None:
    action: bool = True
    location: str = input("Where would you like to tap? Please type your answer as a two-digit integer with the first digit representing the row and the second digit representing the column, starting with row and column 0 and ending at row and column 9. For example, if you wanted to tap in the top right corner, you would type 09: ")
    while action is True:
        y: int = int(location[0])
        x: int = int(location[1])
        if x < 0 or y < 0 or x > 9 or y > 9:
            location = input("Your response is out of bounds! Remember that the minimum and maximum values are 0 and 9 respectively: ")
        elif master_board[y][x].get_data() == chars[1]:
            print("Sorry, you landed on a bomb! Game over!")
            action = False
            display_master()
            exit()
        elif master_board[y][x].get_data() == chars[0]:
            number_mines: str = str(count_mines(y, x))
            player_board[y][x].set_data(number_mines)
            player_board[y][x].set_tapped(True)
            if number_mines == "0":
                if y == 0 and x == 0:
                    tap_r(y, x + 1)
                    tap_r(y + 1, x)
                    tap_r(y + 1, x + 1)
                elif y == 0 and x == 9:
                    tap_r(y, x - 1)
                    tap_r(y + 1, x)
                    tap_r(y + 1, x - 1)
                elif y == 9 and x == 0:
                    tap_r(y, x + 1)
                    tap_r(y - 1, x)
                    tap_r(y - 1, x + 1)
                elif y == 9 and x == 9:
                    tap_r(y - 1, x)
                    tap_r(y, x - 1)
                    tap_r(y - 1, x - 1)
                elif y == 0:
                    tap_r(y, x - 1)
                    tap_r(y, x + 1)
                    tap_r(y + 1, x)
                    tap_r(y + 1, x + 1)
                    tap_r(y + 1, x - 1)
                elif y == 9:
                    tap_r(y, x - 1)
                    tap_r(y, x + 1)
                    tap_r(y - 1, x)
                    tap_r(y - 1, x + 1)
                    tap_r(y - 1, x - 1)
                elif x == 0:
                    tap_r(y - 1, x)
                    tap_r(y + 1, x)
                    tap_r(y, x + 1)
                    tap_r(y + 1, x + 1)
                    tap_r(y - 1, x + 1)
                elif x == 9:
                    tap_r(y + 1, x)
                    tap_r(y - 1, x)
                    tap_r(y - 1, x - 1)
                    tap_r(y, x - 1)
                    tap_r(y + 1, x - 1)
                else:
                    tap_r(y, x - 1)
                    tap_r(y, x + 1)
                    tap_r(y + 1, x)
                    tap_r(y - 1, x)
                    tap_r(y + 1, x - 1)
                    tap_r(y + 1, x + 1)
                    tap_r(y - 1, x + 1)
                    tap_r(y - 1, x - 1)
            action = False
        elif player_board[y][x].get_tapped() is True:
            location = input("You have already tapped here! Please input another location: ")


def tap_r(y: int, x: int) -> None:
    if player_board[y][x].get_tapped() is False and player_board[y][x].get_flagged() is False:
        number_mines: str = str(count_mines(y, x))
        player_board[y][x].set_data(number_mines)
        player_board[y][x].set_tapped(True)
        if number_mines == "0":
            if y == 0 and x == 0:
                tap_r(y, x + 1)
                tap_r(y + 1, x)
                tap_r(y + 1, x + 1)
            elif y == 0 and x == 9:
                tap_r(y, x - 1)
                tap_r(y + 1, x)
                tap_r(y + 1, x - 1)
            elif y == 9 and x == 0:
                tap_r(y, x + 1)
                tap_r(y - 1, x)
                tap_r(y - 1, x + 1)
            elif y == 9 and x == 9:
                tap_r(y - 1, x)
                tap_r(y, x - 1)
                tap_r(y - 1, x - 1)
            elif y == 0:
                tap_r(y, x - 1)
                tap_r(y, x + 1)
                tap_r(y + 1, x)
                tap_r(y + 1, x + 1)
                tap_r(y + 1, x - 1)
            elif y == 9:
                tap_r(y, x - 1)
                tap_r(y, x + 1)
                tap_r(y - 1, x)
                tap_r(y - 1, x + 1)
                tap_r(y - 1, x - 1)
            elif x == 0:
                tap_r(y - 1, x)
                tap_r(y + 1, x)
                tap_r(y, x + 1)
                tap_r(y + 1, x + 1)
                tap_r(y - 1, x + 1)
            elif x == 9:
                tap_r(y + 1, x)
                tap_r(y - 1, x)
                tap_r(y - 1, x - 1)
                tap_r(y, x - 1)
                tap_r(y + 1, x - 1) 
            else:
                tap_r(y, x - 1)
                tap_r(y, x + 1)
                tap_r(y + 1, x)
                tap_r(y - 1, x)
                tap_r(y + 1, x - 1)
                tap_r(y + 1, x + 1)
                tap_r(y - 1, x + 1)
                tap_r(y - 1, x - 1)


def count_mines(y: int, x: int) -> int:
    count: int = 0
    if y == 0 and x == 0: 
        if master_board[y + 1][x].get_data() == chars[1]:
            count += 1
        if master_board[y][x + 1].get_data() == chars[1]:
            count += 1
        if master_board[y + 1][x + 1].get_data() == chars[1]:
            count += 1
    elif y == 0 and x == 9:
        if master_board[y + 1][x].get_data() == chars[1]:
            count += 1
        if master_board[y][x - 1].get_data() == chars[1]:
            count += 1
        if master_board[y + 1][x - 1].get_data() == chars[1]:
            count += 1
    elif y == 9 and x == 0:
        if master_board[y - 1][x].get_data() == chars[1]:
            count += 1
        if master_board[y][x + 1].get_data() == chars[1]:
            count += 1
        if master_board[y - 1][x + 1].get_data() == chars[1]:
            count += 1
    elif y == 9 and x == 9:
        if master_board[y - 1][x].get_data() == chars[1]:
            count += 1
        if master_board[y][x - 1].get_data() == chars[1]:
            count += 1
        if master_board[y - 1][x - 1].get_data() == chars[1]:
            count += 1
    elif y == 0:
        if master_board[y + 1][x].get_data() == chars[1]:
            count += 1
        if master_board[y + 1][x + 1].get_data() == chars[1]:
            count += 1
        if master_board[y + 1][x - 1].get_data() == chars[1]:
            count += 1
        if master_board[y][x - 1].get_data() == chars[1]:
            count += 1
        if master_board[y][x + 1].get_data() == chars[1]:
            count += 1
    elif y == 9:
        if master_board[y - 1][x].get_data() == chars[1]:
            count += 1
        if master_board[y - 1][x + 1].get_data() == chars[1]:
            count += 1
        if master_board[y - 1][x - 1].get_data() == chars[1]:
            count += 1
        if master_board[y][x - 1].get_data() == chars[1]:
            count += 1
        if master_board[y][x + 1].get_data() == chars[1]:
            count += 1
    elif x == 0:
        if master_board[y][x + 1].get_data() == chars[1]:
            count += 1
        if master_board[y + 1][x + 1].get_data() == chars[1]:
            count += 1
        if master_board[y - 1][x + 1].get_data() == chars[1]:
            count += 1
        if master_board[y + 1][x].get_data() == chars[1]:
            count += 1
        if master_board[y - 1][x].get_data() == chars[1]:
            count += 1
    elif x == 9:
        if master_board[y][x - 1].get_data() == chars[1]:
            count += 1
        if master_board[y + 1][x - 1].get_data() == chars[1]:
            count += 1
        if master_board[y - 1][x - 1].get_data() == chars[1]:
            count += 1
        if master_board[y + 1][x].get_data() == chars[1]:
            count += 1
        if master_board[y - 1][x].get_data() == chars[1]:
            count += 1
    else:
        if master_board[y][x - 1].get_data() == chars[1]:
            count += 1
        if master_board[y][x + 1].get_data() == chars[1]:
            count += 1
        if master_board[y + 1][x - 1].get_data() == chars[1]:
            count += 1
        if master_board[y - 1][x - 1].get_data() == chars[1]:
            count += 1
        if master_board[y + 1][x + 1].get_data() == chars[1]:
            count += 1
        if master_board[y - 1][x + 1].get_data() == chars[1]:
            count += 1
        if master_board[y + 1][x].get_data() == chars[1]:
            count += 1
        if master_board[y - 1][x].get_data() == chars[1]:
            count += 1
    return count


if __name__ == "__main__":
    main()