import pytest

from features.move_rover.move_request import MoveRequest


class TestMoveRequest:
    def test_success_validate_request(self):
        move_request = MoveRequest(['app.py', 'input.txt'])
        assert move_request is not None

    def test_failed_validate_request(self):
        move_request = MoveRequest()

        assert move_request is not None
