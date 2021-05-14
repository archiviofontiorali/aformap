import csv
import dataclasses
import json

import internetarchive as ia

from .models import Interview


class CSV:
    def __init__(self, **opts):
        self._opts = opts

    def read(self, path, model, skip_header=True) -> list:
        with open(path, "rt") as fp:
            reader = csv.reader(fp, **self._opts)
            if skip_header:
                next(reader)
            return [model(*row) for row in reader]

    def write(self, path, header, objs, write_header=True):
        with open(path, "wt") as fp:
            writer = csv.writer(fp, **self._opts)

            if write_header:
                writer.writerow(header)

            for obj in objs:
                row = [getattr(obj, h) for h in header]
                writer.writerow(row)


# class JSON:
#     def __init__(self, **opts):
#         self._opts = opts
# 
#     def read(self, path) -> dict:
#         with open(path, "rt") as fp:
#             return json.load(fp, **self._opts)
# 
#     def write(self, path, obj):
#         obj = [dataclasses.asdict(o) for o in obj]
#         with open(path, "wt") as fp:
#             json.dump(obj, fp, **self._opts)


class InternetArchive:
    def __init__(self, creator: str = None, media_type: str = None):
        self._creator = creator
        self._media_type = media_type

    def fetch_all(self):
        _query = f"creator:{self._creator} mediatype:{self._media_type}"
        print(_query)
        _items = ia.search_items(_query)
        return [it["identifier"] for it in _items]

    def fetch_item(self, identifier: str):
        return ia.get_item(identifier)

    def fetch_interview(self, identifier: str) -> Interview:
        item = self.fetch_item(identifier)
        return Interview(identifier=identifier, title=item.metadata["title"])
