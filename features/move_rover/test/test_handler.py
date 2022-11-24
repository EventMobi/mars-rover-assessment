import pytest

from features.move_rover.move_handler import MoveHandler


class TestMoveHandler:
    def test_success_process_request(self):
        handler = MoveHandler()
        result = handler.process_request("input.txt")

        assert len(handler.rover_position) == 2
        assert result is None

    def test_failed_process_request(self):
        handler = MoveHandler()
        result = handler.process_request("test.txt")

        assert result is not None

