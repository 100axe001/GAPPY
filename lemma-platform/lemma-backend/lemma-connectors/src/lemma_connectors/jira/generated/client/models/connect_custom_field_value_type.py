from enum import Enum

class ConnectCustomFieldValueType(str, Enum):
    MULTISELECTISSUEFIELD = "MultiSelectIssueField"
    NUMBERISSUEFIELD = "NumberIssueField"
    RICHTEXTISSUEFIELD = "RichTextIssueField"
    SINGLESELECTISSUEFIELD = "SingleSelectIssueField"
    STRINGISSUEFIELD = "StringIssueField"
    TEXTISSUEFIELD = "TextIssueField"

    def __str__(self) -> str:
        return str(self.value)
