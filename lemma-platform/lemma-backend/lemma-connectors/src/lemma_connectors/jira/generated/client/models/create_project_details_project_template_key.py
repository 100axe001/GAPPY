from enum import Enum

class CreateProjectDetailsProjectTemplateKey(str, Enum):
    COM_ATLASSIAN_JIRA_CORE_PROJECT_TEMPLATESJIRA_CORE_SIMPLIFIED_CONTENT_MANAGEMENT = "com.atlassian.jira-core-project-templates:jira-core-simplified-content-management"
    COM_ATLASSIAN_JIRA_CORE_PROJECT_TEMPLATESJIRA_CORE_SIMPLIFIED_DOCUMENT_APPROVAL = "com.atlassian.jira-core-project-templates:jira-core-simplified-document-approval"
    COM_ATLASSIAN_JIRA_CORE_PROJECT_TEMPLATESJIRA_CORE_SIMPLIFIED_LEAD_TRACKING = "com.atlassian.jira-core-project-templates:jira-core-simplified-lead-tracking"
    COM_ATLASSIAN_JIRA_CORE_PROJECT_TEMPLATESJIRA_CORE_SIMPLIFIED_PROCESS_CONTROL = "com.atlassian.jira-core-project-templates:jira-core-simplified-process-control"
    COM_ATLASSIAN_JIRA_CORE_PROJECT_TEMPLATESJIRA_CORE_SIMPLIFIED_PROCUREMENT = "com.atlassian.jira-core-project-templates:jira-core-simplified-procurement"
    COM_ATLASSIAN_JIRA_CORE_PROJECT_TEMPLATESJIRA_CORE_SIMPLIFIED_PROJECT_MANAGEMENT = "com.atlassian.jira-core-project-templates:jira-core-simplified-project-management"
    COM_ATLASSIAN_JIRA_CORE_PROJECT_TEMPLATESJIRA_CORE_SIMPLIFIED_RECRUITMENT = "com.atlassian.jira-core-project-templates:jira-core-simplified-recruitment"
    COM_ATLASSIAN_JIRA_CORE_PROJECT_TEMPLATESJIRA_CORE_SIMPLIFIED_TASK = "com.atlassian.jira-core-project-templates:jira-core-simplified-task-"
    COM_ATLASSIAN_SERVICEDESKSIMPLIFIED_ANALYTICS_SERVICE_DESK = "com.atlassian.servicedesk:simplified-analytics-service-desk"
    COM_ATLASSIAN_SERVICEDESKSIMPLIFIED_CUSTOM_PROJECT_SERVICE_DESK = "com.atlassian.servicedesk:simplified-custom-project-service-desk"
    COM_ATLASSIAN_SERVICEDESKSIMPLIFIED_EXTERNAL_SERVICE_DESK = "com.atlassian.servicedesk:simplified-external-service-desk"
    COM_ATLASSIAN_SERVICEDESKSIMPLIFIED_FACILITIES_SERVICE_DESK = "com.atlassian.servicedesk:simplified-facilities-service-desk"
    COM_ATLASSIAN_SERVICEDESKSIMPLIFIED_FINANCE_SERVICE_DESK = "com.atlassian.servicedesk:simplified-finance-service-desk"
    COM_ATLASSIAN_SERVICEDESKSIMPLIFIED_GENERAL_SERVICE_DESK = "com.atlassian.servicedesk:simplified-general-service-desk"
    COM_ATLASSIAN_SERVICEDESKSIMPLIFIED_GENERAL_SERVICE_DESK_BUSINESS = "com.atlassian.servicedesk:simplified-general-service-desk-business"
    COM_ATLASSIAN_SERVICEDESKSIMPLIFIED_GENERAL_SERVICE_DESK_IT = "com.atlassian.servicedesk:simplified-general-service-desk-it"
    COM_ATLASSIAN_SERVICEDESKSIMPLIFIED_HALP_SERVICE_DESK = "com.atlassian.servicedesk:simplified-halp-service-desk"
    COM_ATLASSIAN_SERVICEDESKSIMPLIFIED_HR_SERVICE_DESK = "com.atlassian.servicedesk:simplified-hr-service-desk"
    COM_ATLASSIAN_SERVICEDESKSIMPLIFIED_INTERNAL_SERVICE_DESK = "com.atlassian.servicedesk:simplified-internal-service-desk"
    COM_ATLASSIAN_SERVICEDESKSIMPLIFIED_IT_SERVICE_MANAGEMENT = "com.atlassian.servicedesk:simplified-it-service-management"
    COM_ATLASSIAN_SERVICEDESKSIMPLIFIED_LEGAL_SERVICE_DESK = "com.atlassian.servicedesk:simplified-legal-service-desk"
    COM_ATLASSIAN_SERVICEDESKSIMPLIFIED_MARKETING_SERVICE_DESK = "com.atlassian.servicedesk:simplified-marketing-service-desk"
    COM_PYXIS_GREENHOPPER_JIRAGH_SIMPLIFIED_AGILITY_KANBAN = "com.pyxis.greenhopper.jira:gh-simplified-agility-kanban"
    COM_PYXIS_GREENHOPPER_JIRAGH_SIMPLIFIED_AGILITY_SCRUM = "com.pyxis.greenhopper.jira:gh-simplified-agility-scrum"
    COM_PYXIS_GREENHOPPER_JIRAGH_SIMPLIFIED_BASIC = "com.pyxis.greenhopper.jira:gh-simplified-basic"
    COM_PYXIS_GREENHOPPER_JIRAGH_SIMPLIFIED_KANBAN_CLASSIC = "com.pyxis.greenhopper.jira:gh-simplified-kanban-classic"
    COM_PYXIS_GREENHOPPER_JIRAGH_SIMPLIFIED_SCRUM_CLASSIC = "com.pyxis.greenhopper.jira:gh-simplified-scrum-classic"

    def __str__(self) -> str:
        return str(self.value)
