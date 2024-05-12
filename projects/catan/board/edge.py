from typing import Tuple, Optional

class Edge:
    def __init__(self, tile1_coord: Tuple[int, int], tile2_coord: Tuple[int, int], owner_id: Optional[int] = None) -> None:
        self.tile1_coord: Tuple[int, int] = tile1_coord
        self.tile2_coord: Tuple[int, int] = tile2_coord
        self.owner_id: Optional[int] = owner_id

    def __repr__(self) -> str:
        owner_name: str = self.owner_id if self.owner_id else "None"
        return f"Edge(between {self.tile1_coord} and {self.tile2_coord}, owned by {owner_name})"

    def set_owner(self, player_id: int) -> None:
        """Set the owner of the edge to a player."""
        self.owner_id = player_id

    def is_available(self) -> bool:
        """Check if the edge is available to build on (no existing owner)."""
        return self.owner_id is None

    def to_dict(self):
        d = {'owner_id': self.owner_id,}
        d['coords1'] = [self.tile1_coord[0], self.tile1_coord[1]]
        d['coords2'] = [self.tile2_coord[0], self.tile2_coord[1]]
        return d

    def from_dict(d):
        coords1 = tuple((int(d['coords1'][0]),int(d['coords1'][1])))
        coords2 = tuple((int(d['coords2'][0]),int(d['coords2'][1])))
        owner_id_d = d['owner_id']
        if owner_id_d is not None:
            owner_id_d = int(owner_id_d)
        return Edge(tile1_coord=coords1, tile2_coord=coords2, owner_id=owner_id_d)