import argparse
import sys

from features.move_rover.move_request import MoveRequest

if __name__ == "__main__":
    args = sys.argv
    request = MoveRequest(args)
