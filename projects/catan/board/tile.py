from typing import Tuple

class Tile:
    def __init__(self, tile_coord: Tuple[int, int],  resource: str, number: int):
        self.coord = tile_coord
        self.resource = resource
        self.number = number

    def __repr__(self):
        return f"Tile({self.resource}, {self.number})"

    def to_dict(self):
        d = {'resource': self.resource, 'number': self.number}
        d['coords1'] = [self.coord[0], self.coord[1]]
        return d

    def from_dict(d):
        coords1 = tuple((int(d['coords1'][0]),int(d['coords1'][1])))
        number_d = d['number']
        if number_d is not None:
            number_d = int(number_d)
        return Tile(tile_coord=coords1, resource=d['resource'], number=number_d)
        
    def get_coords(self):
        return self.coord

