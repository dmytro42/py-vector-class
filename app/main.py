from __future__ import annotations
from typing import Union

import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x_coord = round(x_coord, 2)
        self.y_coord = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x_coord + other.x_coord, self.y_coord + other.y_coord
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x_coord - other.x_coord, self.y_coord - other.y_coord
        )

    def __mul__(self, other: Union[float, Vector]) -> Union[float, Vector]:
        if isinstance(other, Vector):
            return self.x_coord * other.x_coord + self.y_coord * other.y_coord
        else:
            return Vector(
                round(self.x_coord * other, 2), round(self.y_coord * other, 2)
            )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls.__sub__(Vector(*end_point), Vector(*start_point))

    def get_length(self) -> float:
        return (self.x_coord ** 2 + self.y_coord ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        lenght = self.get_length()
        self.x_coord = round(self.x_coord / lenght, 2)
        self.y_coord = round(self.y_coord / lenght, 2)
        return self

    def angle_between(self, other: Vector) -> int:
        some_angle = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(some_angle)))

    def get_angle(self) -> int:
        vc = Vector(0, 1)
        some_angle = (self * vc) / (self.get_length() * vc.get_length())
        return round(math.degrees(math.acos(some_angle)))

    def rotate(self, dgreeses: int) -> Vector:
        radian = math.radians(dgreeses)
        return Vector(
            math.cos(radian) * self.x_coord - math.sin(radian) * self.y_coord,
            math.sin(radian) * self.x_coord + math.cos(radian) * self.y_coord
        )
