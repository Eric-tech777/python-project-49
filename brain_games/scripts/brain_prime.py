#!/usr/bin/env python3
from brain_games.games import prime
from brain_games.game_engine import start_game


def main():
    start_game(prime.game_task, prime.run_game)


if __name__ == "__main__":
    main()
