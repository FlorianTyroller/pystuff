from typing import Tuple

class Tile:
    def __init__(self, tile_coord: Tuple[int, int],  resource: str, number: int):
        self.coord = tile_coord
        self.resource = resource
        self.number = number

    def __repr__(self):
        return f"Tile({self.resource}, {self.number})"

    def to_dict(self):
        d = {'r': self.resource}
        if self.number is not None:
            d['n'] = self.number
        d['c1'] = [self.coord[0], self.coord[1]]
        return d

    def from_dict(d):
        coords1 = tuple((int(d['c1'][0]),int(d['c1'][1])))
        number_d = d.get('n', None)
        if number_d is not None:
            number_d = int(number_d)
        return Tile(tile_coord=coords1, resource=d['r'], number=number_d)
        
    def get_coords(self):
        return self.coord

