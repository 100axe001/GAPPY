from enum import Enum

class DataSourceRefreshScheduleRefreshScope(str, Enum):
    ALL_DATA_SOURCES = "ALL_DATA_SOURCES"
    DATA_SOURCE_REFRESH_SCOPE_UNSPECIFIED = "DATA_SOURCE_REFRESH_SCOPE_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
