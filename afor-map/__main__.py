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
    @staticmethod
    def read(path, model) -> list:
        with open(path, "rt") as csv_fp:
            reader = csv.reader(csv_fp, delimiter='\t', quotechar='"')
            header = next(reader)
            return [model(*row) for row in reader]


csv_loader = CSV()


input_path = Path("data/nodes_fixed.csv")
nodes = csv_loader.read(input_path, Node)
