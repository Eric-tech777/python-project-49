#!/usr/bin/env python3
from brain_games.games import gcd
from brain_games.game_engine import game_gear


def main():
    game_gear(gcd.game_task, gcd.get_output)


if __name__ == "__main__":
    main()
