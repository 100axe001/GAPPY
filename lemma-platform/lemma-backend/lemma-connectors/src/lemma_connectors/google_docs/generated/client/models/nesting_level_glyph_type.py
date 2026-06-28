from enum import Enum

class NestingLevelGlyphType(str, Enum):
    ALPHA = "ALPHA"
    DECIMAL = "DECIMAL"
    GLYPH_TYPE_UNSPECIFIED = "GLYPH_TYPE_UNSPECIFIED"
    NONE = "NONE"
    ROMAN = "ROMAN"
    UPPER_ALPHA = "UPPER_ALPHA"
    UPPER_ROMAN = "UPPER_ROMAN"
    ZERO_DECIMAL = "ZERO_DECIMAL"

    def __str__(self) -> str:
        return str(self.value)
