import pytest

from features.move_rover.move_request import MoveRequest


class TestMoveRequest:
    def test_success_validate_request(self):
        move_request = MoveRequest(inp="input.txt")
        assert move_request is True

    def test_failed_validate_request(self):
        move_request = MoveRequest()

        with pytest.raises(ValueError):
            assert move_request is True
