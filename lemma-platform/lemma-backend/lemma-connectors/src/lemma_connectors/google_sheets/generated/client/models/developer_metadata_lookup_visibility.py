from enum import Enum

class DeveloperMetadataLookupVisibility(str, Enum):
    DEVELOPER_METADATA_VISIBILITY_UNSPECIFIED = "DEVELOPER_METADATA_VISIBILITY_UNSPECIFIED"
    DOCUMENT = "DOCUMENT"
    PROJECT = "PROJECT"

    def __str__(self) -> str:
        return str(self.value)
