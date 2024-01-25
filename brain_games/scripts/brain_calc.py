#!/usr/bin/env python3
from brain_games.games import calc
from brain_games.game_engine import game_gear


def main():
    game_gear(calc.game_call_reply, calc.game_task)


if __name__ == "__main__":
    main()
