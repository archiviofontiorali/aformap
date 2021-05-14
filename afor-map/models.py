"""Data Models.

This project is based on three main objects: 
- the `interviews`, containing info about the corresponding video and localisation
- the `places` quoted inside the interviews
- the `links` between an interview and his places (this is an internal structure)
"""

import dataclasses


@dataclasses.dataclass
class Interview:
    identifier: str  # internet archive `identifier`
    title: str  # internet archive `metadata.title`
    latitude: float = None
    longitude: float = None

    @property
    def url(self):
        return f"https://archive.org/details/{self.identifier}"


# @dataclasses.dataclass
# class Place:
#     pass


# @dataclasses.dataclass
# class Link:
#     pass


# @dataclasses.dataclass
# class Reference:
#     id: str
#     video_id: str
#     name: str
#     address: str
#     description: str
#
#     latitude: float = None
#     longitude: float = None
#
#     @property
#     def has_coordinates(self):
#         return (self.latitude is not None) and (self.longitude is not None)
