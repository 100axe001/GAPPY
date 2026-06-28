from enum import Enum

class CustomFieldDefinitionJsonBeanSearcherKey(str, Enum):
    COM_ATLASSIAN_JIRA_PLUGIN_SYSTEM_CUSTOMFIELDTYPESCASCADINGSELECTSEARCHER = "com.atlassian.jira.plugin.system.customfieldtypes:cascadingselectsearcher"
    COM_ATLASSIAN_JIRA_PLUGIN_SYSTEM_CUSTOMFIELDTYPESDATERANGE = "com.atlassian.jira.plugin.system.customfieldtypes:daterange"
    COM_ATLASSIAN_JIRA_PLUGIN_SYSTEM_CUSTOMFIELDTYPESDATETIMERANGE = "com.atlassian.jira.plugin.system.customfieldtypes:datetimerange"
    COM_ATLASSIAN_JIRA_PLUGIN_SYSTEM_CUSTOMFIELDTYPESEXACTNUMBER = "com.atlassian.jira.plugin.system.customfieldtypes:exactnumber"
    COM_ATLASSIAN_JIRA_PLUGIN_SYSTEM_CUSTOMFIELDTYPESEXACTTEXTSEARCHER = "com.atlassian.jira.plugin.system.customfieldtypes:exacttextsearcher"
    COM_ATLASSIAN_JIRA_PLUGIN_SYSTEM_CUSTOMFIELDTYPESGROUPPICKERSEARCHER = "com.atlassian.jira.plugin.system.customfieldtypes:grouppickersearcher"
    COM_ATLASSIAN_JIRA_PLUGIN_SYSTEM_CUSTOMFIELDTYPESLABELSEARCHER = "com.atlassian.jira.plugin.system.customfieldtypes:labelsearcher"
    COM_ATLASSIAN_JIRA_PLUGIN_SYSTEM_CUSTOMFIELDTYPESMULTISELECTSEARCHER = "com.atlassian.jira.plugin.system.customfieldtypes:multiselectsearcher"
    COM_ATLASSIAN_JIRA_PLUGIN_SYSTEM_CUSTOMFIELDTYPESNUMBERRANGE = "com.atlassian.jira.plugin.system.customfieldtypes:numberrange"
    COM_ATLASSIAN_JIRA_PLUGIN_SYSTEM_CUSTOMFIELDTYPESPROJECTSEARCHER = "com.atlassian.jira.plugin.system.customfieldtypes:projectsearcher"
    COM_ATLASSIAN_JIRA_PLUGIN_SYSTEM_CUSTOMFIELDTYPESTEXTSEARCHER = "com.atlassian.jira.plugin.system.customfieldtypes:textsearcher"
    COM_ATLASSIAN_JIRA_PLUGIN_SYSTEM_CUSTOMFIELDTYPESUSERPICKERGROUPSEARCHER = "com.atlassian.jira.plugin.system.customfieldtypes:userpickergroupsearcher"
    COM_ATLASSIAN_JIRA_PLUGIN_SYSTEM_CUSTOMFIELDTYPESVERSIONSEARCHER = "com.atlassian.jira.plugin.system.customfieldtypes:versionsearcher"

    def __str__(self) -> str:
        return str(self.value)
