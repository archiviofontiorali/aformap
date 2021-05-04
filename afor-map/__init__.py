import progress.bar

from .constants import DATA_PATH, OUTPUT_PATH
from .loaders import CSV
from .models import Node
from .services import GEODecoder

csv_loader = CSV(delimiter="\t", quotechar='"')
geo_locator = GEODecoder(language="it")


def set_nodes_coordinates(nodes):
    """Set coordinates on each node."""
    bar = progress.bar.IncrementalBar("Geocoding...", max=len(nodes))
    for node in nodes:
        if node.address:
            node.latitude, node.longitude = geo_locator.geocode(node.address)
        bar.next()
    else:
        bar.finish()
    return nodes


def run():
    """Main script."""
    nodes_path = DATA_PATH / "nodes_fixed.csv"
    geocoded_path = OUTPUT_PATH / "nodes_geocoded.csv"

    nodes = csv_loader.read(nodes_path, Node)

    if geocoded_path.exists():
        geocoded_nodes = csv_loader.read(geocoded_path, Node)
    else:
        nodes_header = ("id", "video_id", "name", "address", "description")
        geocoded_header = nodes_header + ("latitude", "longitude")

        set_nodes_coordinates(nodes)

        geocoded_nodes = [node for node in nodes if node.has_coordinates]
        csv_loader.write(geocoded_path, geocoded_header, geocoded_nodes)

    for node in geocoded_nodes:
        print(node.id, node.latitude, node.longitude)


