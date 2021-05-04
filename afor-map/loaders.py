import csv


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
