#!/usr/bin/env python3
from brain_games.games import calc
from brain_games.game_engine import game_gear


def main():
    game_gear(calc.game_task, calc.get_output)


if __name__ == "__main__":
    main()
