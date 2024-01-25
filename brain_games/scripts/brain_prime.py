#!/usr/bin/env python3
from brain_games.games import prime
from brain_games.game_engine import game_gear


def main():
    game_gear(prime.game_call_reply, prime.game_task)


if __name__ == "__main__":
    main()
