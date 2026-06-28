from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from lemma_connectors.gmail.client import GmailInfoClient
from lemma_connectors.jira.client import JiraInfoClient
from lemma_connectors.google_calendar.client import GoogleCalendarInfoClient
from lemma_connectors.google_docs.client import GoogleDocsInfoClient
from lemma_connectors.google_drive.client import GoogleDriveInfoClient
from lemma_connectors.google_sheets.client import GoogleSheetsInfoClient
from lemma_connectors.slack.client import SlackInfoClient


def test_gmail_info_client_lists_generated_tools_and_operations():
    client = GmailInfoClient()

    tool_names = {tool.name for tool in client.list_tools()}
    operation_names = {operation.name for operation in client.list_operations()}

    assert "gmail_users_messages_send" in tool_names
    assert "gmail_users_drafts_create" in tool_names
    assert "messages_send" in operation_names
    assert "messages_get" in operation_names
    assert hasattr(client.resources, "messages")


def test_google_calendar_info_client_lists_generated_tools_and_operations():
    client = GoogleCalendarInfoClient()

    tool_names = {tool.name for tool in client.list_tools()}
    operation_names = {operation.name for operation in client.list_operations()}

    assert "calendar_events_list" in tool_names
    assert "calendar_events_insert" in tool_names
    assert "events_insert" in operation_names
    assert "freebusy_query" in operation_names
    assert hasattr(client.resources, "calendar_list")


def test_google_drive_docs_and_sheets_info_clients_load_with_expected_operations():
    drive = GoogleDriveInfoClient()
    docs = GoogleDocsInfoClient()
    sheets = GoogleSheetsInfoClient()

    assert "files_list" in {operation.name for operation in drive.list_operations()}
    assert "documents_get" in {operation.name for operation in docs.list_operations()}
    assert "spreadsheets_values_get" in {
        operation.name for operation in sheets.list_operations()
    }


def test_slack_info_client_excludes_admin_operations():
    client = SlackInfoClient()
    operation_names = {operation.name for operation in client.list_operations()}
    tool_names = {tool.name for tool in client.list_tools()}

    assert "conversations_history" in operation_names
    assert "chat_post_message" in operation_names
    assert not any(name.startswith("admin_") for name in operation_names)
    assert not any(name.startswith("admin_") for name in tool_names)


def test_jira_info_client_lists_generated_tools_and_operations():
    client = JiraInfoClient()

    tool_names = {tool.name for tool in client.list_tools()}
    operation_names = {operation.name for operation in client.list_operations()}

    assert "get_attachment_content" in tool_names
    assert "get_attachment_content" in operation_names
    assert "add_comment" in operation_names
    assert hasattr(client.resources, "attachment_content")
