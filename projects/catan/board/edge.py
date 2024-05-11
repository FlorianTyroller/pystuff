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
