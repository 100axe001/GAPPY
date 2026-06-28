from enum import Enum

class BatchUpdateValuesRequestResponseDateTimeRenderOption(str, Enum):
    FORMATTED_STRING = "FORMATTED_STRING"
    SERIAL_NUMBER = "SERIAL_NUMBER"

    def __str__(self) -> str:
        return str(self.value)
