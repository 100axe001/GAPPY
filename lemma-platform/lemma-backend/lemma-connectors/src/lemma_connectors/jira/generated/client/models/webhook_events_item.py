from enum import Enum

class WebhookEventsItem(str, Enum):
    COMMENT_CREATED = "comment_created"
    COMMENT_DELETED = "comment_deleted"
    COMMENT_UPDATED = "comment_updated"
    ISSUE_PROPERTY_DELETED = "issue_property_deleted"
    ISSUE_PROPERTY_SET = "issue_property_set"
    JIRAISSUE_CREATED = "jira:issue_created"
    JIRAISSUE_DELETED = "jira:issue_deleted"
    JIRAISSUE_UPDATED = "jira:issue_updated"

    def __str__(self) -> str:
        return str(self.value)
