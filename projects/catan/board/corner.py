from typing import Tuple, Optional

class Corner:
    def __init__(self, tile1_coord: Tuple[int, int], tile2_coord: Tuple[int, int], tile3_coord: Tuple[int, int], owner_id: Optional[int] = None, building: Optional[str] = None) -> None:
        self.tile1_coord: Tuple[int, int] = tile1_coord
        self.tile2_coord: Tuple[int, int] = tile2_coord
        self.tile3_coord: Tuple[int, int] = tile3_coord
        self.owner_id: Optional[int] = owner_id
        self.building: Optional[str] = building

    def __repr__(self) -> str:
        owner_name: str = self.owner_id if self.owner_id else "None"
        return f"Edge(between {self.tile1_coord} and {self.tile2_coord} and {self.tile3_coord}, owned by {owner_name})"

    def set_owner(self, player_id: int) -> None:
        """Set the owner of the corner to a player."""
        self.owner_id = player_id

    def set_building(self, building: str) -> None:
        self.building = building
        
    def is_available(self) -> bool:
        """Check if the corner is available to build on (no existing owner)."""
        return self.owner_id is None

    def get_coords(self) -> Tuple[float,float]:
        x = self.tile1_coord[0] + self.tile2_coord[0] + self.tile3_coord[0]
        y = self.tile1_coord[1] + self.tile2_coord[1] + self.tile3_coord[1]

        y /= 3
        x /= 3
        
        return (x,y)
