#!/usr/bin/env python3
from brain_games.games import even
from brain_games.game_engine import start_game


def main():
    start_game(even.game_task, even.run_game)


if __name__ == "__main__":
    main()
