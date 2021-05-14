# import progress.bar

# from .constants import DATA_PATH, OUTPUT_PATH
# from .loaders import CSV, JSON
# from .models import Reference
# from .services import GEODecoder

# csv_loader = CSV(delimiter="\t", quotechar='"')
# json_loader = JSON()
# geo_locator = GEODecoder(language="it")


# def set_refs_coordinates(refs):
#     """Set coordinates on each ref."""
#     bar = progress.bar.IncrementalBar("Geocoding...", max=len(refs))
#     for ref in refs:
#         if ref.address:
#             ref.latitude, ref.longitude = geo_locator.geocode(ref.address)
#         bar.next()
#     else:
#         bar.finish()
#     return refs


# def run():
#     """Main script."""
#     refs_path = DATA_PATH / "refs.csv"
#     geocoded_path = OUTPUT_PATH / "refs_geocoded.csv"
# 
#     refs = csv_loader.read(refs_path, Reference)
#     json_loader.write(OUTPUT_PATH / "test.json", refs)
# 
#     if geocoded_path.exists():
#         geocoded_refs = csv_loader.read(geocoded_path, Reference)
#     else:
#         refs_header = ("id", "video_id", "name", "address", "description")
#         geocoded_header = refs_header + ("latitude", "longitude")
# 
#         set_refs_coordinates(refs)
# 
#         geocoded_refs = [ref for ref in refs if ref.has_coordinates]
#         csv_loader.write(geocoded_path, geocoded_header, geocoded_refs)
