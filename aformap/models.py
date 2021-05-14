"""Data Models.

This project is based on three main objects: 
- the `interviews`, containing info about the corresponding video and localisation
- the `places` quoted inside the interviews
- the `links` between an interview and his places (this is an internal structure)
"""

import dataclasses
from typing import List


@dataclasses.dataclass
class Place:
    title: str
    lat: float
    lon: float


@dataclasses.dataclass
class Interview:
    identifier: str  # internet archive `identifier`
    title: str  # internet archive `metadata.title`
    lat: float = None
    lon: float = None

    places: List[Place] = dataclasses.field(default_factory=list)

    @property
    def url(self):
        return f"https://archive.org/details/{self.identifier}"
