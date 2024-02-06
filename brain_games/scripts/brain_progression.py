#!/usr/bin/env python3
from brain_games.games import progression
from brain_games.game_engine import start_game


def main():
    start_game(progression.game_task, progression.run_game)


if __name__ == "__main__":
    main()
