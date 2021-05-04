import dataclasses


@dataclasses.dataclass
class Reference:
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


@dataclasses.dataclass
class Interview:
    id: str
    video_id: str
    fullname: str
    video_ref: str
    latitude: float = None
    longitude: float = None
