from enum import Enum

class DeveloperMetadataLookupLocationType(str, Enum):
    COLUMN = "COLUMN"
    DEVELOPER_METADATA_LOCATION_TYPE_UNSPECIFIED = "DEVELOPER_METADATA_LOCATION_TYPE_UNSPECIFIED"
    ROW = "ROW"
    SHEET = "SHEET"
    SPREADSHEET = "SPREADSHEET"

    def __str__(self) -> str:
        return str(self.value)
