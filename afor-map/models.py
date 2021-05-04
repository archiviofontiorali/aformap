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
