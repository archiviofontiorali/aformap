import dataclasses


@dataclasses.dataclass
class Node:
    id: str
    video_id: str
    name: str
    address: str
    description: str

    latitude: float = None
    longitude: float = None

    @property
    def has_coordinates(self):
        return (self.latitude is not None) and (self.longitude is not None)
