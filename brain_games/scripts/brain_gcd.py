#!/usr/bin/env python3
from brain_games.games import gcd
from brain_games.game_engine import game_gear


def main():
    game_gear(gcd.game_call_reply, gcd.game_task)


if __name__ == "__main__":
    main()
