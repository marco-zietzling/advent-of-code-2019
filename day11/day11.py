import os
from enum import Enum
import intcode.intcode_computer as comp

print("advent of code 2019 - day 11")

# day 11 - part 1
input_file = os.path.join(os.getcwd(), "input.txt")


class Direction(Enum):
    north = 1
    east = 2
    south = 3
    west = 4


class PaintingRobot:
    """Painting robot to paint the space ship hull based on intcode computer commands"""

    def __init__(self, instructions: str, canvas: dict):
        self.computer = comp.IntcodeComputer("PaintingRobotComputer", instructions)
        self.current_direction = Direction.north
        self.current_position = (0, 0)
        self.canvas = canvas

    def __calculate_next_direction(self, turn: int):
        if self.current_direction == Direction.north:
            if turn == 0:
                self.current_direction = Direction.west
            elif turn == 1:
                self.current_direction = Direction.east
        elif self.current_direction == Direction.east:
            if turn == 0:
                self.current_direction = Direction.north
            elif turn == 1:
                self.current_direction = Direction.south
        elif self.current_direction == Direction.south:
            if turn == 0:
                self.current_direction = Direction.east
            elif turn == 1:
                self.current_direction = Direction.west
        elif self.current_direction == Direction.west:
            if turn == 0:
                self.current_direction = Direction.south
            elif turn == 1:
                self.current_direction = Direction.north

    def calculate_next_position(self, turn: int):
        """turn command: 0=turn left, 1=turn right, then move one step"""
        # print(f"old status: direction = {self.current_direction}, position = {self.current_position}")

        self.__calculate_next_direction(turn)
        if self.current_direction == Direction.north:
            self.current_position = (self.current_position[0], self.current_position[1] + 1)
        elif self.current_direction == Direction.south:
            self.current_position = (self.current_position[0], self.current_position[1] - 1)
        elif self.current_direction == Direction.east:
            self.current_position = (self.current_position[0] + 1, self.current_position[1])
        elif self.current_direction == Direction.west:
            self.current_position = (self.current_position[0] - 1, self.current_position[1])

        # print(f"new status: direction = {self.current_direction}, position = {self.current_position}")

    def run_paint_job(self):
        # input for intcode computer is current paint: 0=black, 1=white
        # output is two values: new color to paint current position and next move (0 = turn left, 1 = turn right)
        self.computer.provide_arguments([0])
        exit_code = self.computer.execute()
        output = self.computer.consume_output()

        while exit_code != 99:
            pass

        print(f"current input arguments = {self.computer.arguments}")
        print(f"exit_code = {exit_code}")
        print(f"program output = {output}")
        self.calculate_next_position(output[1])

        self.computer.provide_arguments([0])
        exit_code = self.computer.execute()
        output = self.computer.consume_output()
        print(f"current input arguments = {self.computer.arguments}")
        print(f"exit_code = {exit_code}")
        print(f"program output = {output}")
        self.calculate_next_position(output[1])


canvas = dict()
robot = PaintingRobot(input_file, canvas)
robot.run_paint_job()
