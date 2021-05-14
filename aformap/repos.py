import csv
import dataclasses
import json

import internetarchive as ia

from .models import Interview


class CSV:
    def __init__(self, **opts):
        self._opts = opts

    def read(self, path, has_header=False, converter=None) -> list:
        """Read a CSV file from disk.

        :param path: a string or path-like object
        :param has_header: set to True if first row is an header
        :param converter: a function who take a row and optionally the header
        """
        with open(path, "rt") as fp:
            reader = csv.reader(fp, **self._opts)
            header = next(reader) if has_header else None
            if converter:
                return [converter(row, header) for row in reader]
            return list(reader)

    def write(self, path, header, objs, write_header=True):
        with open(path, "wt") as fp:
            writer = csv.writer(fp, **self._opts)

            if write_header:
                writer.writerow(header)

            for obj in objs:
                row = [getattr(obj, h) for h in header]
                writer.writerow(row)


class JSON:
    def __init__(self, **opts):
        self._opts = opts

    def read(self, path) -> dict:
        with open(path, "rt") as fp:
            return json.load(fp, **self._opts)

    def write(self, path, obj):
        with open(path, "wt") as fp:
            json.dump(obj, fp, **self._opts)


class InternetArchive:
    def __init__(self, creator: str = None, media_type: str = None):
        self._creator = creator
        self._media_type = media_type

    def fetch_all(self):
        _query = f"creator:{self._creator} mediatype:{self._media_type}"
        _items = ia.search_items(_query)
        return [it["identifier"] for it in _items]

    @staticmethod
    def fetch_item(identifier: str):
        return ia.get_item(identifier)

    def fetch_interview(self, identifier: str) -> Interview:
        item = self.fetch_item(identifier)
        return Interview(identifier=identifier, title=item.metadata["title"])
