import dataclasses

from typing import List

import progress.bar

from .constants import ARCHIVE_CREATOR, DATA_PATH, OUTPUT_PATH
from .models import Interview, Place
from .repos import CSV, JSON, InternetArchive

DATA_PATH.mkdir(parents=True, exist_ok=True)
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

ia = InternetArchive(creator=ARCHIVE_CREATOR, media_type="movies")
csv = CSV(delimiter="\t", quotechar='"')
json = JSON()


# Read data from legacy edges.csv
legacy_edges_path = DATA_PATH / "edges.csv"
legacy_edges = csv.read(legacy_edges_path, has_header=True)

assert legacy_edges_path.exists(), legacy_edges_path
assert isinstance(legacy_edges, list)
assert len(legacy_edges) > 1
assert all(isinstance(edge, list) for edge in legacy_edges), legacy_edges

interviews: List[Interview] = []

_bar = progress.bar.IncrementalBar("Parsing edges.csv", max=len(legacy_edges))
for i, edge in enumerate(legacy_edges, 1):
    # When a new identifier is found add a new interview and make active
    if edge[0]:
        _interview = ia.fetch_interview(edge[0])
        _interview.latitude = float(edge[5])
        _interview.longitude = float(edge[4])
        interviews.append(_interview)

    # Get information about place
    place = Place(title=edge[1], latitude=float(edge[3]), longitude=float(edge[2]))
    interviews[-1].places.append(place)

    _bar.next()
else:
    _bar.finish()


# save as json
output_path = OUTPUT_PATH / "map-data.json"
interviews_as_dict = [dataclasses.asdict(interview) for interview in interviews]
json.write(output_path, interviews_as_dict)
