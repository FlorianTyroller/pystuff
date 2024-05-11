from typing import Tuple

class Tile:
    def __init__(self, tile_coord: Tuple[int, int],  resource: str, number: int):
        self.coord = tile_coord
        self.resource = resource
        self.number = number

    def __repr__(self):
        return f"Tile({self.resource}, {self.number})"

    def get_coords(self):
        return self.coord

