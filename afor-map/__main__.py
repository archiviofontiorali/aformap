import csv
import dataclasses
from pathlib import Path


@dataclasses.dataclass
class Node:
    id: str
    video_id: str
    name: str
    address: str
    description: str


class CSV:
    def __init__(self, **opts):
        self._opts = opts

    def read(self, path, model, skip_header=True) -> list:
        with open(path, "rt") as csv_fp:
            reader = csv.reader(csv_fp, **self._opts)
            if skip_header:
                next(reader)
            return [model(*row) for row in reader]


csv_loader = CSV(delimiter='\t', quotechar='"')


nodes_path = Path("data/nodes_fixed.csv")
nodes = csv_loader.read(nodes_path, Node)

for node in nodes:
    print(node)
