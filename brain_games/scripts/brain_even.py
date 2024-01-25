#!/usr/bin/env python3
from brain_games.games import even
from brain_games.game_engine import game_gear


def main():
    game_gear(even.game_call_reply, even.game_task)


if __name__ == "__main__":
    main()
