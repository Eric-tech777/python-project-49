#!/usr/bin/env python3
from brain_games.games import progression
from brain_games.game_engine import game_gear


def main():
    game_gear(progression.game_call_reply, progression.game_task)


if __name__ == "__main__":
    main()
