from typing import Tuple

from lib.constant import DIRECTION_MAPPER


class MoveHandler:
    def __init__(self):
        self.x_point = 0
        self.y_point = 0
        self.direction = "N"
        self.max_x_point = 0
        self.max_y_point = 0
        self.rover_position = {}
        self.__mapper = DIRECTION_MAPPER

    def process_request(self, inp) -> dict:
        try:
            with open(inp, "r+") as f:
                lines = f.readlines()
            self.max_x_point, self.max_y_point = self.__get_plateau(lines[0].strip())

            for i in range(1, len(lines)):
                if i % 2 == 0:
                    self.__get_instruction(lines[i].strip())
                else:
                    self.__get_initial_landing_point(lines[i])
            return {"code": 200, "data": self.rover_position}
        except FileNotFoundError as e:
            return {"code": 500, "data": str(e)}

    def __move_forward(self, direction: str) -> None:
        if direction == "N" or direction == "E":
            self.__increase_point(direction)
        elif direction == "S" or direction == "W":
            self.__decrease_point(direction)

    def __change_direction(self, direction: str, angle: str) -> None:
        new_direction = self.__mapper.get(direction+angle)
        self.direction = new_direction

    def __increase_point(self, direction: str) -> None:
        if direction == "E":
            if self.x_point > self.max_x_point:
                raise ValueError("Out of Plateau")
            self.x_point = str(int(self.x_point) + 1)
        else:
            if self.y_point > self.max_y_point:
                raise ValueError("Out of Plateau")

            self.y_point = str(int(self.y_point) + 1)

    def __decrease_point(self, direction: str) -> None:
        if direction == "W":
            self.x_point = str(int(self.x_point) - 1)
        else:
            self.y_point = str(int(self.y_point) - 1)

    def __get_plateau(self, plateau: str) -> Tuple[str, str]:
        plateau_arr = plateau.split(":")
        max_plateau = plateau_arr[1].split(" ")
        return max_plateau[0], max_plateau[1]

    def __get_initial_landing_point(self, positions: str) -> None:
        positions_detail = positions.split(":")
        rover_name = positions_detail[0].split(" ")[0]
        initial_position = positions_detail[1].strip()
        self.rover_position[rover_name] = [i for i in initial_position.split(" ")]

    def __get_instruction(self, instructions: str) -> None:
        instructions_detail = instructions.split(":")
        rover_name = instructions_detail[0].split(" ")[0].strip()
        rover_position = self.rover_position.get(rover_name)
        self.__set_rover_position(rover_position[0], rover_position[1], rover_position[2])

        rover_instruction = instructions_detail[1]
        for i in range(len(rover_instruction)):
            if rover_instruction[i] == "L" or rover_instruction[i] == "R":
                self.__change_direction(self.direction, rover_instruction[i])
            elif rover_instruction[i] == "M":
                self.__move_forward(self.direction)

        self.rover_position[rover_name] = [self.x_point, self.y_point, self.direction]

    def __set_rover_position(self, x: str, y: str, direction: str) -> None:
        self.x_point = x
        self.y_point = y
        self.direction = direction
