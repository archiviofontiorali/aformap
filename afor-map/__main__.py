from .constants import ARCHIVE_CREATOR
from .repos import CSV, JSON, InternetArchive

ia = InternetArchive(creator=ARCHIVE_CREATOR, media_type="movies")
csv = CSV(delimiter="\t", quotechar='"')
json = JSON()


# TODO: read data from edges.csv
# TODO: extrapolate interviews informations
# TODO: extrapolate places informations
# TODO: retrieve from internetarchive missing informations (title)
# TODO: save as json
