from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, RootModel

from lemma_connectors.core.results import BinaryContentResult

from lemma_connectors.jira.generated.pydantic_models import ActorInputBean, ActorsMap, AddAttachmentResponse, AddFieldBean, AddGroupBean, AddNotificationsDetails, AddSharePermissionResponse, AnnouncementBannerConfiguration, AnnouncementBannerConfigurationUpdate, ApplicationProperty, ApplicationRole, AssociateFieldConfigurationsWithIssueTypesRequest, AttachmentArchiveImpl, AttachmentArchiveMetadataReadable, AttachmentMetadata, AttachmentSettings, AuditRecords, AutoCompleteSuggestions, AvailableDashboardGadgetsResponse, Avatar, Avatars, BulkCustomFieldOptionCreateRequest, BulkCustomFieldOptionUpdateRequest, BulkGetUsersMigrationResponse, BulkIssueIsWatching, BulkIssuePropertyUpdateRequest, BulkPermissionGrants, BulkPermissionsRequestBean, CancelTaskResponse, ChangeFilterOwner, ChangedWorklogs, Comment, ComponentIssuesCount, Configuration, ConnectCustomFieldValues, ConnectModules, ContainerForProjectFeatures, ContainerForRegisteredWebhooks, ContainerForWebhookIDs, ContainerOfWorkflowSchemeAssociations, ConvertedJQLQueries, CreateCustomFieldContext, CreateNotificationSchemeDetails, CreatePriorityDetails, CreateProjectDetails, CreateResolutionDetails, CreateStatusesResponse, CreateUiModificationDetails, CreateUpdateRoleRequestBean, CreateWorkflowDetails, CreatedIssue, CreatedIssues, CustomFieldConfigurations, CustomFieldContextDefaultValueUpdate, CustomFieldContextUpdateDetails, CustomFieldCreatedContextOptionsList, CustomFieldDefinitionJsonBean, CustomFieldOption, CustomFieldUpdatedContextOptionsList, CustomFieldValueUpdateDetails, Dashboard, DashboardDetails, DashboardGadget, DashboardGadgetResponse, DashboardGadgetSettings, DashboardGadgetUpdateRequest, DefaultShareScope, DefaultWorkflow, DeleteAndReplaceVersionBean, EntityProperty, ErrorCollection, FailedWebhooks, FieldConfiguration, FieldConfigurationDetails, FieldConfigurationItemsDetails, FieldConfigurationScheme, FieldConfigurationSchemeProjectAssociation, FieldDetails, Filter, FindAssignableUsersResponse, FindBulkAssignableUsersResponse, FindUsersResponse, FindUsersWithAllPermissionsResponse, FindUsersWithBrowsePermissionResponse, FoundGroups, FoundUsers, FoundUsersAndGroups, GetAdvancedSettingsResponse, GetAllAccessibleProjectTypesResponse, GetAllApplicationRolesResponse, GetAllProjectCategoriesResponse, GetAllProjectRolesResponse, GetAllProjectTypesResponse, GetAllProjectsResponse, GetAllScreenTabFieldsResponse, GetAllScreenTabsResponse, GetAllStatusesResponse, GetAllUsersDefaultResponse, GetAllUsersResponse, GetAllWorkflowsResponse, GetAlternativeIssueTypesResponse, GetApplicationPropertyResponse, GetAvailableScreenFieldsResponse, GetAvailableTimeTrackingImplementationsResponse, GetColumnsResponse, GetEventsResponse, GetFavouriteFiltersResponse, GetFieldsResponse, GetFiltersResponse, GetIssueAllTypesResponse, GetIssueNavigatorDefaultColumnsResponse, GetIssueTypesForProjectResponse, GetMyFiltersResponse, GetPrioritiesResponse, GetProjectComponentsResponse, GetProjectRoleDetailsResponse, GetProjectRolesResponse, GetProjectVersionsResponse, GetRecentResponse, GetResolutionsResponse, GetSharePermissionsResponse, GetStatusCategoriesResponse, GetStatusesByIdResponse, GetStatusesResponse, GetUserDefaultColumnsResponse, GetUserGroupsResponse, GetWorklogsForIdsResponse, Group, IdBean, IssueBean, IssueChangelogIds, IssueCommentListRequestBean, IssueCreateMetadata, IssueEntityProperties, IssueFieldOption, IssueFieldOptionCreateBean, IssueFilterForBulkPropertyDelete, IssueLink, IssueLinkType, IssueLinkTypes, IssueList, IssueMatches, IssuePickerSuggestions, IssueTypeCreateBean, IssueTypeDetails, IssueTypeIds, IssueTypeIdsToRemove, IssueTypeSchemeDetails, IssueTypeSchemeID, IssueTypeSchemeProjectAssociation, IssueTypeSchemeUpdateDetails, IssueTypeScreenSchemeDetails, IssueTypeScreenSchemeId, IssueTypeScreenSchemeMappingDetails, IssueTypeScreenSchemeProjectAssociation, IssueTypeScreenSchemeUpdateDetails, IssueTypeUpdateBean, IssueTypeWorkflowMapping, IssueTypesWorkflowMapping, IssueUpdateDetails, IssueUpdateMetadata, IssuesAndJQLQueries, IssuesUpdateBean, JQLPersonalDataMigrationRequest, JQLReferenceData, JiraExpressionEvalRequestBean, JiraExpressionForAnalysis, JiraExpressionResult, JiraExpressionsAnalysis, JqlFunctionPrecomputationUpdateRequestBean, JqlQueriesToParse, JqlQueriesToSanitize, License, LicenseMetric, LinkIssueRequestJsonBean, Locale, MigrationResourceUpdateEntityPropertiesValuePutRequest, MoveFieldBean, MultiIssueEntityProperties, MultipleCustomFieldValuesUpdateDetails, NewUserDetails, Notification, NotificationScheme, NotificationSchemeId, OperationMessage, OrderOfCustomFieldOptions, OrderOfIssueTypes, PageBeanChangelog, PageBeanComment, PageBeanComponentWithIssueCount, PageBeanContext, PageBeanContextForProjectAndIssueType, PageBeanContextualConfiguration, PageBeanCustomFieldContext, PageBeanCustomFieldContextDefaultValue, PageBeanCustomFieldContextOption, PageBeanCustomFieldContextProjectMapping, PageBeanDashboard, PageBeanField, PageBeanFieldConfigurationDetails, PageBeanFieldConfigurationIssueTypeItem, PageBeanFieldConfigurationItem, PageBeanFieldConfigurationScheme, PageBeanFieldConfigurationSchemeProjects, PageBeanFilterDetails, PageBeanGroupDetails, PageBeanIssueFieldOption, PageBeanIssueSecurityLevelMember, PageBeanIssueTypeScheme, PageBeanIssueTypeSchemeMapping, PageBeanIssueTypeSchemeProjects, PageBeanIssueTypeScreenScheme, PageBeanIssueTypeScreenSchemeItem, PageBeanIssueTypeScreenSchemesProjects, PageBeanIssueTypeToContextMapping, PageBeanJqlFunctionPrecomputationBean, PageBeanNotificationScheme, PageBeanNotificationSchemeAndProjectMappingJsonBean, PageBeanPriority, PageBeanProject, PageBeanProjectDetails, PageBeanResolutionJsonBean, PageBeanScreen, PageBeanScreenScheme, PageBeanScreenWithTab, PageBeanString, PageBeanUiModificationDetails, PageBeanUser, PageBeanUserDetails, PageBeanUserKey, PageBeanVersion, PageBeanWebhook, PageBeanWorkflow, PageBeanWorkflowScheme, PageBeanWorkflowTransitionRules, PageOfChangelogs, PageOfComments, PageOfDashboards, PageOfStatuses, PageOfWorklogs, ParsedJqlQueries, PermissionGrant, PermissionGrants, PermissionScheme, PermissionSchemes, Permissions, PermissionsKeysBean, PermittedProjects, Priority, PriorityId, Project, ProjectAvatars, ProjectCategory, ProjectComponent, ProjectEmailAddress, ProjectFeatureState, ProjectIdentifiers, ProjectIds, ProjectIssueSecurityLevels, ProjectIssueTypeHierarchy, ProjectIssueTypeMappings, ProjectRole, ProjectRoleActorsUpdateBean, ProjectType, PropertyKeys, PublishDraftWorkflowScheme, RemoteIssueLink, RemoteIssueLinkIdentifies, RemoteIssueLinkRequest, ReorderIssuePriorities, ReorderIssueResolutionsRequest, Resolution, ResolutionId, SanitizedJqlQueries, Screen, ScreenDetails, ScreenSchemeDetails, ScreenSchemeId, ScreenableField, ScreenableTab, SearchAutoCompleteFilter, SearchRequestBean, SearchResults, SecurityLevel, SecurityScheme, SecuritySchemes, ServerInformation, SetColumnsRequest, SetDefaultPriorityRequest, SetDefaultResolutionRequest, SetIssueNavigatorDefaultColumnsRequest, SetUserColumnsRequest, SharePermission, SharePermissionInputBean, SimpleApplicationPropertyBean, StatusCategory, StatusCreateRequest, StatusDetails, StatusUpdateRequest, SystemAvatars, TaskProgressBeanObject, TimeTrackingConfiguration, TimeTrackingProvider, Transitions, UiModificationIdentifiers, UnrestrictedUserEmail, UpdateCustomFieldDetails, UpdateDefaultScreenScheme, UpdateFieldConfigurationSchemeDetails, UpdateNotificationSchemeDetails, UpdatePriorityDetails, UpdateProjectDetails, UpdateResolutionDetails, UpdateScreenDetails, UpdateScreenSchemeDetails, UpdateUiModificationDetails, UpdateUserToGroupBean, UpdatedProjectCategory, User, Version, VersionIssueCounts, VersionMoveBean, VersionUnresolvedIssuesCount, Votes, Watchers, WebhookRegistrationDetails, WebhooksExpirationDate, WorkflowIDs, WorkflowRulesSearch, WorkflowRulesSearchDetails, WorkflowScheme, WorkflowSchemeProjectAssociation, WorkflowTransitionProperty, WorkflowTransitionRulesUpdate, WorkflowTransitionRulesUpdateErrors, WorkflowsWithTransitionRulesDetails, Worklog, WorklogIdsRequestBean

class AddActorUsersToolInput(BaseModel):
    """Input for tool `add_actor_users`."""
    project_id_or_key: str = Field(..., description='The project ID or project key (case sensitive).')
    id: int = Field(..., description='The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.')
    body: ActorsMap = Field(..., description='Request body for `add_actor_users`.')
    model_config = ConfigDict(extra='forbid')

class AddActorUsersToolOutput(ProjectRole):
    """Output for tool `add_actor_users`."""
    pass

class AddAttachmentToolInput(BaseModel):
    """Input for tool `add_attachment`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue that attachments are added to.')
    body: str | None = Field(default=None, description='Request body for `add_attachment`.')
    model_config = ConfigDict(extra='forbid')

class AddAttachmentToolOutput(AddAttachmentResponse):
    """Output for tool `add_attachment`."""
    pass

class AddCommentToolInput(BaseModel):
    """Input for tool `add_comment`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information about comments in the response. This parameter accepts `renderedBody`, which returns the comment body rendered in HTML.')
    body: Comment = Field(..., description='Request body for `add_comment`.')
    model_config = ConfigDict(extra='forbid')

class AddCommentToolOutput(Comment):
    """Output for tool `add_comment`."""
    pass

class AddFieldToDefaultScreenToolInput(BaseModel):
    """Input for tool `add_field_to_default_screen`."""
    field_id: str = Field(..., description='The ID of the field.')
    model_config = ConfigDict(extra='forbid')

class AddFieldToDefaultScreenToolOutput(RootModel[dict[str, object]]):
    """Output for tool `add_field_to_default_screen`."""
    pass

class AddGadgetToolInput(BaseModel):
    """Input for tool `add_gadget`."""
    dashboard_id: int = Field(..., description='The ID of the dashboard.')
    body: DashboardGadgetSettings = Field(..., description='Request body for `add_gadget`.')
    model_config = ConfigDict(extra='forbid')

class AddGadgetToolOutput(DashboardGadget):
    """Output for tool `add_gadget`."""
    pass

class AddIssueTypesToContextToolInput(BaseModel):
    """Input for tool `add_issue_types_to_context`."""
    field_id: str = Field(..., description='The ID of the custom field.')
    context_id: int = Field(..., description='The ID of the context.')
    body: IssueTypeIds = Field(..., description='Request body for `add_issue_types_to_context`.')
    model_config = ConfigDict(extra='forbid')

class AddIssueTypesToContextToolOutput(RootModel[dict[str, object]]):
    """Output for tool `add_issue_types_to_context`."""
    pass

class AddIssueTypesToIssueTypeSchemeToolInput(BaseModel):
    """Input for tool `add_issue_types_to_issue_type_scheme`."""
    issue_type_scheme_id: int = Field(..., description='The ID of the issue type scheme.')
    body: IssueTypeIds = Field(..., description='Request body for `add_issue_types_to_issue_type_scheme`.')
    model_config = ConfigDict(extra='forbid')

class AddIssueTypesToIssueTypeSchemeToolOutput(RootModel[dict[str, object]]):
    """Output for tool `add_issue_types_to_issue_type_scheme`."""
    pass

class AddNotificationsToolInput(BaseModel):
    """Input for tool `add_notifications`."""
    id: str = Field(..., description='The ID of the notification scheme.')
    body: AddNotificationsDetails = Field(..., description='Request body for `add_notifications`.')
    model_config = ConfigDict(extra='forbid')

class AddNotificationsToolOutput(RootModel[dict[str, object]]):
    """Output for tool `add_notifications`."""
    pass

class AddProjectRoleActorsToRoleToolInput(BaseModel):
    """Input for tool `add_project_role_actors_to_role`."""
    id: int = Field(..., description='The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.')
    body: ActorInputBean = Field(..., description='Request body for `add_project_role_actors_to_role`.')
    model_config = ConfigDict(extra='forbid')

class AddProjectRoleActorsToRoleToolOutput(ProjectRole):
    """Output for tool `add_project_role_actors_to_role`."""
    pass

class AddScreenTabToolInput(BaseModel):
    """Input for tool `add_screen_tab`."""
    screen_id: int = Field(..., description='The ID of the screen.')
    body: ScreenableTab = Field(..., description='Request body for `add_screen_tab`.')
    model_config = ConfigDict(extra='forbid')

class AddScreenTabToolOutput(ScreenableTab):
    """Output for tool `add_screen_tab`."""
    pass

class AddScreenTabFieldToolInput(BaseModel):
    """Input for tool `add_screen_tab_field`."""
    screen_id: int = Field(..., description='The ID of the screen.')
    tab_id: int = Field(..., description='The ID of the screen tab.')
    body: AddFieldBean = Field(..., description='Request body for `add_screen_tab_field`.')
    model_config = ConfigDict(extra='forbid')

class AddScreenTabFieldToolOutput(ScreenableField):
    """Output for tool `add_screen_tab_field`."""
    pass

class AddSharePermissionToolInput(BaseModel):
    """Input for tool `add_share_permission`."""
    id: int = Field(..., description='The ID of the filter.')
    body: SharePermissionInputBean = Field(..., description='Request body for `add_share_permission`.')
    model_config = ConfigDict(extra='forbid')

class AddSharePermissionToolOutput(AddSharePermissionResponse):
    """Output for tool `add_share_permission`."""
    pass

class AddUserToGroupToolInput(BaseModel):
    """Input for tool `add_user_to_group`."""
    groupname: str | None = Field(default=None, description="As a group's name can change, use of `groupId` is recommended to identify a group.  \nThe name of the group. This parameter cannot be used with the `groupId` parameter.")
    group_id: str | None = Field(default=None, description='The ID of the group. This parameter cannot be used with the `groupName` parameter.')
    body: UpdateUserToGroupBean = Field(..., description='Request body for `add_user_to_group`.')
    model_config = ConfigDict(extra='forbid')

class AddUserToGroupToolOutput(Group):
    """Output for tool `add_user_to_group`."""
    pass

class AddVoteToolInput(BaseModel):
    """Input for tool `add_vote`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    model_config = ConfigDict(extra='forbid')

class AddVoteToolOutput(RootModel[dict[str, object]]):
    """Output for tool `add_vote`."""
    pass

class AddWatcherToolInput(BaseModel):
    """Input for tool `add_watcher`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    body: str = Field(..., description='Request body for `add_watcher`.')
    model_config = ConfigDict(extra='forbid')

class AddWatcherToolOutput(RootModel[dict[str, object]]):
    """Output for tool `add_watcher`."""
    pass

class AddWorklogToolInput(BaseModel):
    """Input for tool `add_worklog`."""
    issue_id_or_key: str = Field(..., description='The ID or key the issue.')
    notify_users: bool | None = Field(default=None, description='Whether users watching the issue are notified by email.')
    adjust_estimate: Literal['new', 'leave', 'manual', 'auto'] | None = Field(default=None, description="Defines how to update the issue's time estimate, the options are:\n\n *  `new` Sets the estimate to a specific value, defined in `newEstimate`.\n *  `leave` Leaves the estimate unchanged.\n *  `manual` Reduces the estimate by amount specified in `reduceBy`.\n *  `auto` Reduces the estimate by the value of `timeSpent` in the worklog.")
    new_estimate: str | None = Field(default=None, description="The value to set as the issue's remaining time estimate, as days (\\#d), hours (\\#h), or minutes (\\#m or \\#). For example, *2d*. Required when `adjustEstimate` is `new`.")
    reduce_by: str | None = Field(default=None, description="The amount to reduce the issue's remaining estimate by, as days (\\#d), hours (\\#h), or minutes (\\#m). For example, *2d*. Required when `adjustEstimate` is `manual`.")
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information about work logs in the response. This parameter accepts `properties`, which returns worklog properties.')
    override_editable_flag: bool | None = Field(default=None, description='Whether the worklog entry should be added to the issue even if the issue is not editable, because jira.issue.editable set to false or missing. For example, the issue is closed. Connect and Forge app users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) can use this flag.')
    body: Worklog = Field(..., description='Request body for `add_worklog`.')
    model_config = ConfigDict(extra='forbid')

class AddWorklogToolOutput(Worklog):
    """Output for tool `add_worklog`."""
    pass

class AddonPropertiesResourceDeleteAddonPropertyDeleteToolInput(BaseModel):
    """Input for tool `addon_properties_resource_delete_addon_property_delete`."""
    addon_key: str = Field(..., description='The key of the app, as defined in its descriptor.')
    property_key: str = Field(..., description='The key of the property.')
    model_config = ConfigDict(extra='forbid')

class AddonPropertiesResourceDeleteAddonPropertyDeleteToolOutput(RootModel[dict[str, object]]):
    """Output for tool `addon_properties_resource_delete_addon_property_delete`."""
    pass

class AddonPropertiesResourceGetAddonPropertiesGetToolInput(BaseModel):
    """Input for tool `addon_properties_resource_get_addon_properties_get`."""
    addon_key: str = Field(..., description='The key of the app, as defined in its descriptor.')
    model_config = ConfigDict(extra='forbid')

class AddonPropertiesResourceGetAddonPropertiesGetToolOutput(PropertyKeys):
    """Output for tool `addon_properties_resource_get_addon_properties_get`."""
    pass

class AddonPropertiesResourceGetAddonPropertyGetToolInput(BaseModel):
    """Input for tool `addon_properties_resource_get_addon_property_get`."""
    addon_key: str = Field(..., description='The key of the app, as defined in its descriptor.')
    property_key: str = Field(..., description='The key of the property.')
    model_config = ConfigDict(extra='forbid')

class AddonPropertiesResourceGetAddonPropertyGetToolOutput(EntityProperty):
    """Output for tool `addon_properties_resource_get_addon_property_get`."""
    pass

class AddonPropertiesResourcePutAddonPropertyPutToolInput(BaseModel):
    """Input for tool `addon_properties_resource_put_addon_property_put`."""
    addon_key: str = Field(..., description='The key of the app, as defined in its descriptor.')
    property_key: str = Field(..., description='The key of the property.')
    body: dict[str, object] = Field(..., description='Request body for `addon_properties_resource_put_addon_property_put`.')
    model_config = ConfigDict(extra='forbid')

class AddonPropertiesResourcePutAddonPropertyPutToolOutput(OperationMessage):
    """Output for tool `addon_properties_resource_put_addon_property_put`."""
    pass

class AnalyseExpressionToolInput(BaseModel):
    """Input for tool `analyse_expression`."""
    check: Literal['syntax', 'type', 'complexity'] | None = Field(default=None, description="The check to perform:\n\n *  `syntax` Each expression's syntax is checked to ensure the expression can be parsed. Also, syntactic limits are validated. For example, the expression's length.\n *  `type` EXPERIMENTAL. Each expression is type checked and the final type of the expression inferred. Any type errors that would result in the expression failure at runtime are reported. For example, accessing properties that don't exist or passing the wrong number of arguments to functions. Also performs the syntax check.\n *  `complexity` EXPERIMENTAL. Determines the formulae for how many [expensive operations](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/#expensive-operations) each expression may execute.")
    body: JiraExpressionForAnalysis = Field(..., description='Request body for `analyse_expression`.')
    model_config = ConfigDict(extra='forbid')

class AnalyseExpressionToolOutput(JiraExpressionsAnalysis):
    """Output for tool `analyse_expression`."""
    pass

class AppIssueFieldValueUpdateResourceUpdateIssueFieldsPutToolInput(BaseModel):
    """Input for tool `app_issue_field_value_update_resource_update_issue_fields_put`."""
    atlassian_transfer_id: str = Field(..., description='The ID of the transfer.')
    body: ConnectCustomFieldValues = Field(..., description='Request body for `app_issue_field_value_update_resource_update_issue_fields_put`.')
    model_config = ConfigDict(extra='forbid')

class AppIssueFieldValueUpdateResourceUpdateIssueFieldsPutToolOutput(RootModel[dict[str, object]]):
    """Output for tool `app_issue_field_value_update_resource_update_issue_fields_put`."""
    pass

class AppendMappingsForIssueTypeScreenSchemeToolInput(BaseModel):
    """Input for tool `append_mappings_for_issue_type_screen_scheme`."""
    issue_type_screen_scheme_id: str = Field(..., description='The ID of the issue type screen scheme.')
    body: IssueTypeScreenSchemeMappingDetails = Field(..., description='Request body for `append_mappings_for_issue_type_screen_scheme`.')
    model_config = ConfigDict(extra='forbid')

class AppendMappingsForIssueTypeScreenSchemeToolOutput(RootModel[dict[str, object]]):
    """Output for tool `append_mappings_for_issue_type_screen_scheme`."""
    pass

class ArchiveProjectToolInput(BaseModel):
    """Input for tool `archive_project`."""
    project_id_or_key: str = Field(..., description='The project ID or project key (case sensitive).')
    model_config = ConfigDict(extra='forbid')

class ArchiveProjectToolOutput(RootModel[dict[str, object]]):
    """Output for tool `archive_project`."""
    pass

class AssignFieldConfigurationSchemeToProjectToolInput(BaseModel):
    """Input for tool `assign_field_configuration_scheme_to_project`."""
    body: FieldConfigurationSchemeProjectAssociation = Field(..., description='Request body for `assign_field_configuration_scheme_to_project`.')
    model_config = ConfigDict(extra='forbid')

class AssignFieldConfigurationSchemeToProjectToolOutput(RootModel[dict[str, object]]):
    """Output for tool `assign_field_configuration_scheme_to_project`."""
    pass

class AssignIssueToolInput(BaseModel):
    """Input for tool `assign_issue`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue to be assigned.')
    body: User = Field(..., description='Request body for `assign_issue`.')
    model_config = ConfigDict(extra='forbid')

class AssignIssueToolOutput(RootModel[dict[str, object]]):
    """Output for tool `assign_issue`."""
    pass

class AssignIssueTypeSchemeToProjectToolInput(BaseModel):
    """Input for tool `assign_issue_type_scheme_to_project`."""
    body: IssueTypeSchemeProjectAssociation = Field(..., description='Request body for `assign_issue_type_scheme_to_project`.')
    model_config = ConfigDict(extra='forbid')

class AssignIssueTypeSchemeToProjectToolOutput(RootModel[dict[str, object]]):
    """Output for tool `assign_issue_type_scheme_to_project`."""
    pass

class AssignIssueTypeScreenSchemeToProjectToolInput(BaseModel):
    """Input for tool `assign_issue_type_screen_scheme_to_project`."""
    body: IssueTypeScreenSchemeProjectAssociation = Field(..., description='Request body for `assign_issue_type_screen_scheme_to_project`.')
    model_config = ConfigDict(extra='forbid')

class AssignIssueTypeScreenSchemeToProjectToolOutput(RootModel[dict[str, object]]):
    """Output for tool `assign_issue_type_screen_scheme_to_project`."""
    pass

class AssignPermissionSchemeToolInput(BaseModel):
    """Input for tool `assign_permission_scheme`."""
    project_key_or_id: str = Field(..., description='The project ID or project key (case sensitive).')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are included when you specify any value. Expand options include:\n\n *  `all` Returns all expandable information.\n *  `field` Returns information about the custom field granted the permission.\n *  `group` Returns information about the group that is granted the permission.\n *  `permissions` Returns all permission grants for each permission scheme.\n *  `projectRole` Returns information about the project role granted the permission.\n *  `user` Returns information about the user who is granted the permission.')
    body: IdBean = Field(..., description='Request body for `assign_permission_scheme`.')
    model_config = ConfigDict(extra='forbid')

class AssignPermissionSchemeToolOutput(PermissionScheme):
    """Output for tool `assign_permission_scheme`."""
    pass

class AssignProjectsToCustomFieldContextToolInput(BaseModel):
    """Input for tool `assign_projects_to_custom_field_context`."""
    field_id: str = Field(..., description='The ID of the custom field.')
    context_id: int = Field(..., description='The ID of the context.')
    body: ProjectIds = Field(..., description='Request body for `assign_projects_to_custom_field_context`.')
    model_config = ConfigDict(extra='forbid')

class AssignProjectsToCustomFieldContextToolOutput(RootModel[dict[str, object]]):
    """Output for tool `assign_projects_to_custom_field_context`."""
    pass

class AssignSchemeToProjectToolInput(BaseModel):
    """Input for tool `assign_scheme_to_project`."""
    body: WorkflowSchemeProjectAssociation = Field(..., description='Request body for `assign_scheme_to_project`.')
    model_config = ConfigDict(extra='forbid')

class AssignSchemeToProjectToolOutput(RootModel[dict[str, object]]):
    """Output for tool `assign_scheme_to_project`."""
    pass

class BulkDeleteIssuePropertyToolInput(BaseModel):
    """Input for tool `bulk_delete_issue_property`."""
    property_key: str = Field(..., description='The key of the property.')
    body: IssueFilterForBulkPropertyDelete = Field(..., description='Request body for `bulk_delete_issue_property`.')
    model_config = ConfigDict(extra='forbid')

class BulkDeleteIssuePropertyToolOutput(RootModel[dict[str, object]]):
    """Output for tool `bulk_delete_issue_property`."""
    pass

class BulkGetGroupsToolInput(BaseModel):
    """Input for tool `bulk_get_groups`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    group_id: list[str] | None = Field(default=None, description='The ID of a group. To specify multiple IDs, pass multiple `groupId` parameters. For example, `groupId=5b10a2844c20165700ede21g&groupId=5b10ac8d82e05b22cc7d4ef5`.')
    group_name: list[str] | None = Field(default=None, description='The name of a group. To specify multiple names, pass multiple `groupName` parameters. For example, `groupName=administrators&groupName=jira-software-users`.')
    access_type: str | None = Field(default=None, description="The access level of a group. Valid values: 'site-admin', 'admin', 'user'.")
    application_key: str | None = Field(default=None, description="The application key of the product user groups to search for. Valid values: 'jira-servicedesk', 'jira-software', 'jira-product-discovery', 'jira-core'.")
    model_config = ConfigDict(extra='forbid')

class BulkGetGroupsToolOutput(PageBeanGroupDetails):
    """Output for tool `bulk_get_groups`."""
    pass

class BulkGetUsersToolInput(BaseModel):
    """Input for tool `bulk_get_users`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    username: list[str] | None = Field(default=None, description='This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.')
    account_id: list[str] = Field(..., description='The account ID of a user. To specify multiple users, pass multiple `accountId` parameters. For example, `accountId=5b10a2844c20165700ede21g&accountId=5b10ac8d82e05b22cc7d4ef5`.')
    model_config = ConfigDict(extra='forbid')

class BulkGetUsersToolOutput(PageBeanUser):
    """Output for tool `bulk_get_users`."""
    pass

class BulkGetUsersMigrationToolInput(BaseModel):
    """Input for tool `bulk_get_users_migration`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    username: list[str] | None = Field(default=None, description="Username of a user. To specify multiple users, pass multiple copies of this parameter. For example, `username=fred&username=barney`. Required if `key` isn't provided. Cannot be provided if `key` is present.")
    model_config = ConfigDict(extra='forbid')

class BulkGetUsersMigrationToolOutput(BulkGetUsersMigrationResponse):
    """Output for tool `bulk_get_users_migration`."""
    pass

class BulkSetIssuePropertiesByIssueToolInput(BaseModel):
    """Input for tool `bulk_set_issue_properties_by_issue`."""
    body: MultiIssueEntityProperties = Field(..., description='Request body for `bulk_set_issue_properties_by_issue`.')
    model_config = ConfigDict(extra='forbid')

class BulkSetIssuePropertiesByIssueToolOutput(RootModel[dict[str, object]]):
    """Output for tool `bulk_set_issue_properties_by_issue`."""
    pass

class BulkSetIssuePropertyToolInput(BaseModel):
    """Input for tool `bulk_set_issue_property`."""
    property_key: str = Field(..., description='The key of the property. The maximum length is 255 characters.')
    body: BulkIssuePropertyUpdateRequest = Field(..., description='Request body for `bulk_set_issue_property`.')
    model_config = ConfigDict(extra='forbid')

class BulkSetIssuePropertyToolOutput(RootModel[dict[str, object]]):
    """Output for tool `bulk_set_issue_property`."""
    pass

class BulkSetIssuesPropertiesListToolInput(BaseModel):
    """Input for tool `bulk_set_issues_properties_list`."""
    body: IssueEntityProperties = Field(..., description='Request body for `bulk_set_issues_properties_list`.')
    model_config = ConfigDict(extra='forbid')

class BulkSetIssuesPropertiesListToolOutput(RootModel[dict[str, object]]):
    """Output for tool `bulk_set_issues_properties_list`."""
    pass

class CancelTaskToolInput(BaseModel):
    """Input for tool `cancel_task`."""
    task_id: str = Field(..., description='The ID of the task.')
    model_config = ConfigDict(extra='forbid')

class CancelTaskToolOutput(CancelTaskResponse):
    """Output for tool `cancel_task`."""
    pass

class ChangeFilterOwnerToolInput(BaseModel):
    """Input for tool `change_filter_owner`."""
    id: int = Field(..., description='The ID of the filter to update.')
    body: ChangeFilterOwner = Field(..., description='Request body for `change_filter_owner`.')
    model_config = ConfigDict(extra='forbid')

class ChangeFilterOwnerToolOutput(RootModel[dict[str, object]]):
    """Output for tool `change_filter_owner`."""
    pass

class CopyDashboardToolInput(BaseModel):
    """Input for tool `copy_dashboard`."""
    id: str = Field(...)
    body: DashboardDetails = Field(..., description='Request body for `copy_dashboard`.')
    model_config = ConfigDict(extra='forbid')

class CopyDashboardToolOutput(Dashboard):
    """Output for tool `copy_dashboard`."""
    pass

class CreateComponentToolInput(BaseModel):
    """Input for tool `create_component`."""
    body: ProjectComponent = Field(..., description='Request body for `create_component`.')
    model_config = ConfigDict(extra='forbid')

class CreateComponentToolOutput(ProjectComponent):
    """Output for tool `create_component`."""
    pass

class CreateCustomFieldToolInput(BaseModel):
    """Input for tool `create_custom_field`."""
    body: CustomFieldDefinitionJsonBean = Field(..., description='Request body for `create_custom_field`.')
    model_config = ConfigDict(extra='forbid')

class CreateCustomFieldToolOutput(FieldDetails):
    """Output for tool `create_custom_field`."""
    pass

class CreateCustomFieldContextToolInput(BaseModel):
    """Input for tool `create_custom_field_context`."""
    field_id: str = Field(..., description='The ID of the custom field.')
    body: CreateCustomFieldContext = Field(..., description='Request body for `create_custom_field_context`.')
    model_config = ConfigDict(extra='forbid')

class CreateCustomFieldContextToolOutput(CreateCustomFieldContext):
    """Output for tool `create_custom_field_context`."""
    pass

class CreateCustomFieldOptionToolInput(BaseModel):
    """Input for tool `create_custom_field_option`."""
    field_id: str = Field(..., description='The ID of the custom field.')
    context_id: int = Field(..., description='The ID of the context.')
    body: BulkCustomFieldOptionCreateRequest = Field(..., description='Request body for `create_custom_field_option`.')
    model_config = ConfigDict(extra='forbid')

class CreateCustomFieldOptionToolOutput(CustomFieldCreatedContextOptionsList):
    """Output for tool `create_custom_field_option`."""
    pass

class CreateDashboardToolInput(BaseModel):
    """Input for tool `create_dashboard`."""
    body: DashboardDetails = Field(..., description='Request body for `create_dashboard`.')
    model_config = ConfigDict(extra='forbid')

class CreateDashboardToolOutput(Dashboard):
    """Output for tool `create_dashboard`."""
    pass

class CreateFieldConfigurationToolInput(BaseModel):
    """Input for tool `create_field_configuration`."""
    body: FieldConfigurationDetails = Field(..., description='Request body for `create_field_configuration`.')
    model_config = ConfigDict(extra='forbid')

class CreateFieldConfigurationToolOutput(FieldConfiguration):
    """Output for tool `create_field_configuration`."""
    pass

class CreateFieldConfigurationSchemeToolInput(BaseModel):
    """Input for tool `create_field_configuration_scheme`."""
    body: UpdateFieldConfigurationSchemeDetails = Field(..., description='Request body for `create_field_configuration_scheme`.')
    model_config = ConfigDict(extra='forbid')

class CreateFieldConfigurationSchemeToolOutput(FieldConfigurationScheme):
    """Output for tool `create_field_configuration_scheme`."""
    pass

class CreateFilterToolInput(BaseModel):
    """Input for tool `create_filter`."""
    expand: str | None = Field(default=None, description="Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `sharedUsers` Returns the users that the filter is shared with. This includes users that can browse projects that the filter is shared with. If you don't specify `sharedUsers`, then the `sharedUsers` object is returned but it doesn't list any users. The list of users returned is limited to 1000, to access additional users append `[start-index:end-index]` to the expand request. For example, to access the next 1000 users, use `?expand=sharedUsers[1001:2000]`.\n *  `subscriptions` Returns the users that are subscribed to the filter. If you don't specify `subscriptions`, the `subscriptions` object is returned but it doesn't list any subscriptions. The list of subscriptions returned is limited to 1000, to access additional subscriptions append `[start-index:end-index]` to the expand request. For example, to access the next 1000 subscriptions, use `?expand=subscriptions[1001:2000]`.")
    override_share_permissions: bool | None = Field(default=None, description='EXPERIMENTAL: Whether share permissions are overridden to enable filters with any share permissions to be created. Available to users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).')
    body: Filter = Field(..., description='Request body for `create_filter`.')
    model_config = ConfigDict(extra='forbid')

class CreateFilterToolOutput(Filter):
    """Output for tool `create_filter`."""
    pass

class CreateGroupToolInput(BaseModel):
    """Input for tool `create_group`."""
    body: AddGroupBean = Field(..., description='Request body for `create_group`.')
    model_config = ConfigDict(extra='forbid')

class CreateGroupToolOutput(Group):
    """Output for tool `create_group`."""
    pass

class CreateIssueToolInput(BaseModel):
    """Input for tool `create_issue`."""
    update_history: bool | None = Field(default=None, description="Whether the project in which the issue is created is added to the user's **Recently viewed** project list, as shown under **Projects** in Jira. When provided, the issue type and request type are added to the user's history for a project. These values are then used to provide defaults on the issue create screen.")
    body: IssueUpdateDetails = Field(..., description='Request body for `create_issue`.')
    model_config = ConfigDict(extra='forbid')

class CreateIssueToolOutput(CreatedIssue):
    """Output for tool `create_issue`."""
    pass

class CreateIssueFieldOptionToolInput(BaseModel):
    """Input for tool `create_issue_field_option`."""
    field_key: str = Field(..., description='The field key is specified in the following format: **$(app-key)\\_\\_$(field-key)**. For example, *example-add-on\\_\\_example-issue-field*. To determine the `fieldKey` value, do one of the following:\n\n *  open the app\'s plugin descriptor, then **app-key** is the key at the top and **field-key** is the key in the `jiraIssueFields` module. **app-key** can also be found in the app listing in the Atlassian Universal Plugin Manager.\n *  run [Get fields](#api-rest-api-3-field-get) and in the field details the value is returned in `key`. For example, `"key": "teams-add-on__team-issue-field"`')
    body: IssueFieldOptionCreateBean = Field(..., description='Request body for `create_issue_field_option`.')
    model_config = ConfigDict(extra='forbid')

class CreateIssueFieldOptionToolOutput(IssueFieldOption):
    """Output for tool `create_issue_field_option`."""
    pass

class CreateIssueLinkTypeToolInput(BaseModel):
    """Input for tool `create_issue_link_type`."""
    body: IssueLinkType = Field(..., description='Request body for `create_issue_link_type`.')
    model_config = ConfigDict(extra='forbid')

class CreateIssueLinkTypeToolOutput(IssueLinkType):
    """Output for tool `create_issue_link_type`."""
    pass

class CreateIssueTypeToolInput(BaseModel):
    """Input for tool `create_issue_type`."""
    body: IssueTypeCreateBean = Field(..., description='Request body for `create_issue_type`.')
    model_config = ConfigDict(extra='forbid')

class CreateIssueTypeToolOutput(IssueTypeDetails):
    """Output for tool `create_issue_type`."""
    pass

class CreateIssueTypeAvatarToolInput(BaseModel):
    """Input for tool `create_issue_type_avatar`."""
    id: str = Field(..., description='The ID of the issue type.')
    x: int | None = Field(default=None, description='The X coordinate of the top-left corner of the crop region.')
    y: int | None = Field(default=None, description='The Y coordinate of the top-left corner of the crop region.')
    size: int = Field(..., description='The length of each side of the crop region.')
    body: dict[str, object] = Field(..., description='Request body for `create_issue_type_avatar`.')
    model_config = ConfigDict(extra='forbid')

class CreateIssueTypeAvatarToolOutput(Avatar):
    """Output for tool `create_issue_type_avatar`."""
    pass

class CreateIssueTypeSchemeToolInput(BaseModel):
    """Input for tool `create_issue_type_scheme`."""
    body: IssueTypeSchemeDetails = Field(..., description='Request body for `create_issue_type_scheme`.')
    model_config = ConfigDict(extra='forbid')

class CreateIssueTypeSchemeToolOutput(IssueTypeSchemeID):
    """Output for tool `create_issue_type_scheme`."""
    pass

class CreateIssueTypeScreenSchemeToolInput(BaseModel):
    """Input for tool `create_issue_type_screen_scheme`."""
    body: IssueTypeScreenSchemeDetails = Field(..., description='Request body for `create_issue_type_screen_scheme`.')
    model_config = ConfigDict(extra='forbid')

class CreateIssueTypeScreenSchemeToolOutput(IssueTypeScreenSchemeId):
    """Output for tool `create_issue_type_screen_scheme`."""
    pass

class CreateIssuesToolInput(BaseModel):
    """Input for tool `create_issues`."""
    body: IssuesUpdateBean = Field(..., description='Request body for `create_issues`.')
    model_config = ConfigDict(extra='forbid')

class CreateIssuesToolOutput(CreatedIssues):
    """Output for tool `create_issues`."""
    pass

class CreateNotificationSchemeToolInput(BaseModel):
    """Input for tool `create_notification_scheme`."""
    body: CreateNotificationSchemeDetails = Field(..., description='Request body for `create_notification_scheme`.')
    model_config = ConfigDict(extra='forbid')

class CreateNotificationSchemeToolOutput(NotificationSchemeId):
    """Output for tool `create_notification_scheme`."""
    pass

class CreateOrUpdateRemoteIssueLinkToolInput(BaseModel):
    """Input for tool `create_or_update_remote_issue_link`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    body: RemoteIssueLinkRequest = Field(..., description='Request body for `create_or_update_remote_issue_link`.')
    model_config = ConfigDict(extra='forbid')

class CreateOrUpdateRemoteIssueLinkToolOutput(RemoteIssueLinkIdentifies):
    """Output for tool `create_or_update_remote_issue_link`."""
    pass

class CreatePermissionGrantToolInput(BaseModel):
    """Input for tool `create_permission_grant`."""
    scheme_id: int = Field(..., description='The ID of the permission scheme in which to create a new permission grant.')
    expand: str | None = Field(default=None, description='Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are always included when you specify any value. Expand options include:\n\n *  `permissions` Returns all permission grants for each permission scheme.\n *  `user` Returns information about the user who is granted the permission.\n *  `group` Returns information about the group that is granted the permission.\n *  `projectRole` Returns information about the project role granted the permission.\n *  `field` Returns information about the custom field granted the permission.\n *  `all` Returns all expandable information.')
    body: PermissionGrant = Field(..., description='Request body for `create_permission_grant`.')
    model_config = ConfigDict(extra='forbid')

class CreatePermissionGrantToolOutput(PermissionGrant):
    """Output for tool `create_permission_grant`."""
    pass

class CreatePermissionSchemeToolInput(BaseModel):
    """Input for tool `create_permission_scheme`."""
    expand: str | None = Field(default=None, description='Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are always included when you specify any value. Expand options include:\n\n *  `all` Returns all expandable information.\n *  `field` Returns information about the custom field granted the permission.\n *  `group` Returns information about the group that is granted the permission.\n *  `permissions` Returns all permission grants for each permission scheme.\n *  `projectRole` Returns information about the project role granted the permission.\n *  `user` Returns information about the user who is granted the permission.')
    body: PermissionScheme = Field(..., description='Request body for `create_permission_scheme`.')
    model_config = ConfigDict(extra='forbid')

class CreatePermissionSchemeToolOutput(PermissionScheme):
    """Output for tool `create_permission_scheme`."""
    pass

class CreatePriorityToolInput(BaseModel):
    """Input for tool `create_priority`."""
    body: CreatePriorityDetails = Field(..., description='Request body for `create_priority`.')
    model_config = ConfigDict(extra='forbid')

class CreatePriorityToolOutput(PriorityId):
    """Output for tool `create_priority`."""
    pass

class CreateProjectToolInput(BaseModel):
    """Input for tool `create_project`."""
    body: CreateProjectDetails = Field(..., description='Request body for `create_project`.')
    model_config = ConfigDict(extra='forbid')

class CreateProjectToolOutput(ProjectIdentifiers):
    """Output for tool `create_project`."""
    pass

class CreateProjectAvatarToolInput(BaseModel):
    """Input for tool `create_project_avatar`."""
    project_id_or_key: str = Field(..., description='The ID or (case-sensitive) key of the project.')
    x: int | None = Field(default=None, description='The X coordinate of the top-left corner of the crop region.')
    y: int | None = Field(default=None, description='The Y coordinate of the top-left corner of the crop region.')
    size: int | None = Field(default=None, description='The length of each side of the crop region.')
    body: dict[str, object] = Field(..., description='Request body for `create_project_avatar`.')
    model_config = ConfigDict(extra='forbid')

class CreateProjectAvatarToolOutput(Avatar):
    """Output for tool `create_project_avatar`."""
    pass

class CreateProjectCategoryToolInput(BaseModel):
    """Input for tool `create_project_category`."""
    body: ProjectCategory = Field(..., description='Request body for `create_project_category`.')
    model_config = ConfigDict(extra='forbid')

class CreateProjectCategoryToolOutput(ProjectCategory):
    """Output for tool `create_project_category`."""
    pass

class CreateProjectRoleToolInput(BaseModel):
    """Input for tool `create_project_role`."""
    body: CreateUpdateRoleRequestBean = Field(..., description='Request body for `create_project_role`.')
    model_config = ConfigDict(extra='forbid')

class CreateProjectRoleToolOutput(ProjectRole):
    """Output for tool `create_project_role`."""
    pass

class CreateResolutionToolInput(BaseModel):
    """Input for tool `create_resolution`."""
    body: CreateResolutionDetails = Field(..., description='Request body for `create_resolution`.')
    model_config = ConfigDict(extra='forbid')

class CreateResolutionToolOutput(ResolutionId):
    """Output for tool `create_resolution`."""
    pass

class CreateScreenToolInput(BaseModel):
    """Input for tool `create_screen`."""
    body: ScreenDetails = Field(..., description='Request body for `create_screen`.')
    model_config = ConfigDict(extra='forbid')

class CreateScreenToolOutput(Screen):
    """Output for tool `create_screen`."""
    pass

class CreateScreenSchemeToolInput(BaseModel):
    """Input for tool `create_screen_scheme`."""
    body: ScreenSchemeDetails = Field(..., description='Request body for `create_screen_scheme`.')
    model_config = ConfigDict(extra='forbid')

class CreateScreenSchemeToolOutput(ScreenSchemeId):
    """Output for tool `create_screen_scheme`."""
    pass

class CreateStatusesToolInput(BaseModel):
    """Input for tool `create_statuses`."""
    body: StatusCreateRequest = Field(..., description='Request body for `create_statuses`.')
    model_config = ConfigDict(extra='forbid')

class CreateStatusesToolOutput(CreateStatusesResponse):
    """Output for tool `create_statuses`."""
    pass

class CreateUiModificationToolInput(BaseModel):
    """Input for tool `create_ui_modification`."""
    body: CreateUiModificationDetails = Field(..., description='Request body for `create_ui_modification`.')
    model_config = ConfigDict(extra='forbid')

class CreateUiModificationToolOutput(UiModificationIdentifiers):
    """Output for tool `create_ui_modification`."""
    pass

class CreateUserToolInput(BaseModel):
    """Input for tool `create_user`."""
    body: NewUserDetails = Field(..., description='Request body for `create_user`.')
    model_config = ConfigDict(extra='forbid')

class CreateUserToolOutput(User):
    """Output for tool `create_user`."""
    pass

class CreateVersionToolInput(BaseModel):
    """Input for tool `create_version`."""
    body: Version = Field(..., description='Request body for `create_version`.')
    model_config = ConfigDict(extra='forbid')

class CreateVersionToolOutput(Version):
    """Output for tool `create_version`."""
    pass

class CreateWorkflowToolInput(BaseModel):
    """Input for tool `create_workflow`."""
    body: CreateWorkflowDetails = Field(..., description='Request body for `create_workflow`.')
    model_config = ConfigDict(extra='forbid')

class CreateWorkflowToolOutput(WorkflowIDs):
    """Output for tool `create_workflow`."""
    pass

class CreateWorkflowSchemeToolInput(BaseModel):
    """Input for tool `create_workflow_scheme`."""
    body: WorkflowScheme = Field(..., description='Request body for `create_workflow_scheme`.')
    model_config = ConfigDict(extra='forbid')

class CreateWorkflowSchemeToolOutput(WorkflowScheme):
    """Output for tool `create_workflow_scheme`."""
    pass

class CreateWorkflowSchemeDraftFromParentToolInput(BaseModel):
    """Input for tool `create_workflow_scheme_draft_from_parent`."""
    id: int = Field(..., description='The ID of the active workflow scheme that the draft is created from.')
    model_config = ConfigDict(extra='forbid')

class CreateWorkflowSchemeDraftFromParentToolOutput(WorkflowScheme):
    """Output for tool `create_workflow_scheme_draft_from_parent`."""
    pass

class CreateWorkflowTransitionPropertyToolInput(BaseModel):
    """Input for tool `create_workflow_transition_property`."""
    transition_id: int = Field(..., description='The ID of the transition. To get the ID, view the workflow in text mode in the Jira admin settings. The ID is shown next to the transition.')
    workflow_name: str = Field(..., description='The name of the workflow that the transition belongs to.')
    workflow_mode: Literal['live', 'draft'] | None = Field(default=None, description='The workflow status. Set to *live* for inactive workflows or *draft* for draft workflows. Active workflows cannot be edited.')
    body: WorkflowTransitionProperty = Field(..., description='Request body for `create_workflow_transition_property`.')
    model_config = ConfigDict(extra='forbid')

class CreateWorkflowTransitionPropertyToolOutput(WorkflowTransitionProperty):
    """Output for tool `create_workflow_transition_property`."""
    pass

class DeleteActorToolInput(BaseModel):
    """Input for tool `delete_actor`."""
    project_id_or_key: str = Field(..., description='The project ID or project key (case sensitive).')
    id: int = Field(..., description='The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.')
    user: str | None = Field(default=None, description='The user account ID of the user to remove from the project role.')
    group: str | None = Field(default=None, description="The name of the group to remove from the project role. This parameter cannot be used with the `groupId` parameter. As a group's name can change, use of `groupId` is recommended.")
    group_id: str | None = Field(default=None, description='The ID of the group to remove from the project role. This parameter cannot be used with the `group` parameter.')
    model_config = ConfigDict(extra='forbid')

class DeleteActorToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_actor`."""
    pass

class DeleteAndReplaceVersionToolInput(BaseModel):
    """Input for tool `delete_and_replace_version`."""
    id: str = Field(..., description='The ID of the version.')
    body: DeleteAndReplaceVersionBean = Field(..., description='Request body for `delete_and_replace_version`.')
    model_config = ConfigDict(extra='forbid')

class DeleteAndReplaceVersionToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_and_replace_version`."""
    pass

class DeleteAvatarToolInput(BaseModel):
    """Input for tool `delete_avatar`."""
    type: Literal['project', 'issuetype'] = Field(..., description='The avatar type.')
    owning_object_id: str = Field(..., description='The ID of the item the avatar is associated with.')
    id: int = Field(..., description='The ID of the avatar.')
    model_config = ConfigDict(extra='forbid')

class DeleteAvatarToolOutput(BinaryContentResult):
    """Binary output for tool `delete_avatar`."""
    pass

class DeleteCommentToolInput(BaseModel):
    """Input for tool `delete_comment`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    id: str = Field(..., description='The ID of the comment.')
    model_config = ConfigDict(extra='forbid')

class DeleteCommentToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_comment`."""
    pass

class DeleteCommentPropertyToolInput(BaseModel):
    """Input for tool `delete_comment_property`."""
    comment_id: str = Field(..., description='The ID of the comment.')
    property_key: str = Field(..., description='The key of the property.')
    model_config = ConfigDict(extra='forbid')

class DeleteCommentPropertyToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_comment_property`."""
    pass

class DeleteComponentToolInput(BaseModel):
    """Input for tool `delete_component`."""
    id: str = Field(..., description='The ID of the component.')
    move_issues_to: str | None = Field(default=None, description='The ID of the component to replace the deleted component. If this value is null no replacement is made.')
    model_config = ConfigDict(extra='forbid')

class DeleteComponentToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_component`."""
    pass

class DeleteCustomFieldToolInput(BaseModel):
    """Input for tool `delete_custom_field`."""
    id: str = Field(..., description='The ID of a custom field.')
    model_config = ConfigDict(extra='forbid')

class DeleteCustomFieldToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_custom_field`."""
    pass

class DeleteCustomFieldContextToolInput(BaseModel):
    """Input for tool `delete_custom_field_context`."""
    field_id: str = Field(..., description='The ID of the custom field.')
    context_id: int = Field(..., description='The ID of the context.')
    model_config = ConfigDict(extra='forbid')

class DeleteCustomFieldContextToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_custom_field_context`."""
    pass

class DeleteCustomFieldOptionToolInput(BaseModel):
    """Input for tool `delete_custom_field_option`."""
    field_id: str = Field(..., description='The ID of the custom field.')
    context_id: int = Field(..., description='The ID of the context from which an option should be deleted.')
    option_id: int = Field(..., description='The ID of the option to delete.')
    model_config = ConfigDict(extra='forbid')

class DeleteCustomFieldOptionToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_custom_field_option`."""
    pass

class DeleteDashboardToolInput(BaseModel):
    """Input for tool `delete_dashboard`."""
    id: str = Field(..., description='The ID of the dashboard.')
    model_config = ConfigDict(extra='forbid')

class DeleteDashboardToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_dashboard`."""
    pass

class DeleteDashboardItemPropertyToolInput(BaseModel):
    """Input for tool `delete_dashboard_item_property`."""
    dashboard_id: str = Field(..., description='The ID of the dashboard.')
    item_id: str = Field(..., description='The ID of the dashboard item.')
    property_key: str = Field(..., description='The key of the dashboard item property.')
    model_config = ConfigDict(extra='forbid')

class DeleteDashboardItemPropertyToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_dashboard_item_property`."""
    pass

class DeleteDefaultWorkflowToolInput(BaseModel):
    """Input for tool `delete_default_workflow`."""
    id: int = Field(..., description='The ID of the workflow scheme.')
    update_draft_if_needed: bool | None = Field(default=None, description='Set to true to create or update the draft of a workflow scheme and delete the mapping from the draft, when the workflow scheme cannot be edited. Defaults to `false`.')
    model_config = ConfigDict(extra='forbid')

class DeleteDefaultWorkflowToolOutput(WorkflowScheme):
    """Output for tool `delete_default_workflow`."""
    pass

class DeleteDraftDefaultWorkflowToolInput(BaseModel):
    """Input for tool `delete_draft_default_workflow`."""
    id: int = Field(..., description='The ID of the workflow scheme that the draft belongs to.')
    model_config = ConfigDict(extra='forbid')

class DeleteDraftDefaultWorkflowToolOutput(WorkflowScheme):
    """Output for tool `delete_draft_default_workflow`."""
    pass

class DeleteDraftWorkflowMappingToolInput(BaseModel):
    """Input for tool `delete_draft_workflow_mapping`."""
    id: int = Field(..., description='The ID of the workflow scheme that the draft belongs to.')
    workflow_name: str = Field(..., description='The name of the workflow.')
    model_config = ConfigDict(extra='forbid')

class DeleteDraftWorkflowMappingToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_draft_workflow_mapping`."""
    pass

class DeleteFavouriteForFilterToolInput(BaseModel):
    """Input for tool `delete_favourite_for_filter`."""
    id: int = Field(..., description='The ID of the filter.')
    expand: str | None = Field(default=None, description="Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `sharedUsers` Returns the users that the filter is shared with. This includes users that can browse projects that the filter is shared with. If you don't specify `sharedUsers`, then the `sharedUsers` object is returned but it doesn't list any users. The list of users returned is limited to 1000, to access additional users append `[start-index:end-index]` to the expand request. For example, to access the next 1000 users, use `?expand=sharedUsers[1001:2000]`.\n *  `subscriptions` Returns the users that are subscribed to the filter. If you don't specify `subscriptions`, the `subscriptions` object is returned but it doesn't list any subscriptions. The list of subscriptions returned is limited to 1000, to access additional subscriptions append `[start-index:end-index]` to the expand request. For example, to access the next 1000 subscriptions, use `?expand=subscriptions[1001:2000]`.")
    model_config = ConfigDict(extra='forbid')

class DeleteFavouriteForFilterToolOutput(Filter):
    """Output for tool `delete_favourite_for_filter`."""
    pass

class DeleteFieldConfigurationToolInput(BaseModel):
    """Input for tool `delete_field_configuration`."""
    id: int = Field(..., description='The ID of the field configuration.')
    model_config = ConfigDict(extra='forbid')

class DeleteFieldConfigurationToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_field_configuration`."""
    pass

class DeleteFieldConfigurationSchemeToolInput(BaseModel):
    """Input for tool `delete_field_configuration_scheme`."""
    id: int = Field(..., description='The ID of the field configuration scheme.')
    model_config = ConfigDict(extra='forbid')

class DeleteFieldConfigurationSchemeToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_field_configuration_scheme`."""
    pass

class DeleteFilterToolInput(BaseModel):
    """Input for tool `delete_filter`."""
    id: int = Field(..., description='The ID of the filter to delete.')
    model_config = ConfigDict(extra='forbid')

class DeleteFilterToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_filter`."""
    pass

class DeleteInactiveWorkflowToolInput(BaseModel):
    """Input for tool `delete_inactive_workflow`."""
    entity_id: str = Field(..., description='The entity ID of the workflow.')
    model_config = ConfigDict(extra='forbid')

class DeleteInactiveWorkflowToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_inactive_workflow`."""
    pass

class DeleteIssueToolInput(BaseModel):
    """Input for tool `delete_issue`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    delete_subtasks: Literal['true', 'false'] | None = Field(default=None, description="Whether the issue's subtasks are deleted when the issue is deleted.")
    model_config = ConfigDict(extra='forbid')

class DeleteIssueToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_issue`."""
    pass

class DeleteIssueFieldOptionToolInput(BaseModel):
    """Input for tool `delete_issue_field_option`."""
    field_key: str = Field(..., description='The field key is specified in the following format: **$(app-key)\\_\\_$(field-key)**. For example, *example-add-on\\_\\_example-issue-field*. To determine the `fieldKey` value, do one of the following:\n\n *  open the app\'s plugin descriptor, then **app-key** is the key at the top and **field-key** is the key in the `jiraIssueFields` module. **app-key** can also be found in the app listing in the Atlassian Universal Plugin Manager.\n *  run [Get fields](#api-rest-api-3-field-get) and in the field details the value is returned in `key`. For example, `"key": "teams-add-on__team-issue-field"`')
    option_id: int = Field(..., description='The ID of the option to be deleted.')
    model_config = ConfigDict(extra='forbid')

class DeleteIssueFieldOptionToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_issue_field_option`."""
    pass

class DeleteIssueLinkToolInput(BaseModel):
    """Input for tool `delete_issue_link`."""
    link_id: str = Field(..., description='The ID of the issue link.')
    model_config = ConfigDict(extra='forbid')

class DeleteIssueLinkToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_issue_link`."""
    pass

class DeleteIssueLinkTypeToolInput(BaseModel):
    """Input for tool `delete_issue_link_type`."""
    issue_link_type_id: str = Field(..., description='The ID of the issue link type.')
    model_config = ConfigDict(extra='forbid')

class DeleteIssueLinkTypeToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_issue_link_type`."""
    pass

class DeleteIssuePropertyToolInput(BaseModel):
    """Input for tool `delete_issue_property`."""
    issue_id_or_key: str = Field(..., description='The key or ID of the issue.')
    property_key: str = Field(..., description='The key of the property.')
    model_config = ConfigDict(extra='forbid')

class DeleteIssuePropertyToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_issue_property`."""
    pass

class DeleteIssueTypeToolInput(BaseModel):
    """Input for tool `delete_issue_type`."""
    id: str = Field(..., description='The ID of the issue type.')
    alternative_issue_type_id: str | None = Field(default=None, description='The ID of the replacement issue type.')
    model_config = ConfigDict(extra='forbid')

class DeleteIssueTypeToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_issue_type`."""
    pass

class DeleteIssueTypePropertyToolInput(BaseModel):
    """Input for tool `delete_issue_type_property`."""
    issue_type_id: str = Field(..., description='The ID of the issue type.')
    property_key: str = Field(..., description='The key of the property. Use [Get issue type property keys](#api-rest-api-3-issuetype-issueTypeId-properties-get) to get a list of all issue type property keys.')
    model_config = ConfigDict(extra='forbid')

class DeleteIssueTypePropertyToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_issue_type_property`."""
    pass

class DeleteIssueTypeSchemeToolInput(BaseModel):
    """Input for tool `delete_issue_type_scheme`."""
    issue_type_scheme_id: int = Field(..., description='The ID of the issue type scheme.')
    model_config = ConfigDict(extra='forbid')

class DeleteIssueTypeSchemeToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_issue_type_scheme`."""
    pass

class DeleteIssueTypeScreenSchemeToolInput(BaseModel):
    """Input for tool `delete_issue_type_screen_scheme`."""
    issue_type_screen_scheme_id: str = Field(..., description='The ID of the issue type screen scheme.')
    model_config = ConfigDict(extra='forbid')

class DeleteIssueTypeScreenSchemeToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_issue_type_screen_scheme`."""
    pass

class DeleteLocaleToolInput(BaseModel):
    """Input for tool `delete_locale`."""
    model_config = ConfigDict(extra='forbid')

class DeleteLocaleToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_locale`."""
    pass

class DeleteNotificationSchemeToolInput(BaseModel):
    """Input for tool `delete_notification_scheme`."""
    notification_scheme_id: str = Field(..., description='The ID of the notification scheme.')
    model_config = ConfigDict(extra='forbid')

class DeleteNotificationSchemeToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_notification_scheme`."""
    pass

class DeletePermissionSchemeToolInput(BaseModel):
    """Input for tool `delete_permission_scheme`."""
    scheme_id: int = Field(..., description='The ID of the permission scheme being deleted.')
    model_config = ConfigDict(extra='forbid')

class DeletePermissionSchemeToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_permission_scheme`."""
    pass

class DeletePermissionSchemeEntityToolInput(BaseModel):
    """Input for tool `delete_permission_scheme_entity`."""
    scheme_id: int = Field(..., description='The ID of the permission scheme to delete the permission grant from.')
    permission_id: int = Field(..., description='The ID of the permission grant to delete.')
    model_config = ConfigDict(extra='forbid')

class DeletePermissionSchemeEntityToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_permission_scheme_entity`."""
    pass

class DeletePriorityToolInput(BaseModel):
    """Input for tool `delete_priority`."""
    id: str = Field(..., description='The ID of the issue priority.')
    replace_with: str = Field(..., description='The ID of the issue priority that will replace the currently selected resolution.')
    model_config = ConfigDict(extra='forbid')

class DeletePriorityToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_priority`."""
    pass

class DeleteProjectToolInput(BaseModel):
    """Input for tool `delete_project`."""
    project_id_or_key: str = Field(..., description='The project ID or project key (case sensitive).')
    enable_undo: bool | None = Field(default=None, description='Whether this project is placed in the Jira recycle bin where it will be available for restoration.')
    model_config = ConfigDict(extra='forbid')

class DeleteProjectToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_project`."""
    pass

class DeleteProjectAsynchronouslyToolInput(BaseModel):
    """Input for tool `delete_project_asynchronously`."""
    project_id_or_key: str = Field(..., description='The project ID or project key (case sensitive).')
    model_config = ConfigDict(extra='forbid')

class DeleteProjectAsynchronouslyToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_project_asynchronously`."""
    pass

class DeleteProjectAvatarToolInput(BaseModel):
    """Input for tool `delete_project_avatar`."""
    project_id_or_key: str = Field(..., description='The project ID or (case-sensitive) key.')
    id: int = Field(..., description='The ID of the avatar.')
    model_config = ConfigDict(extra='forbid')

class DeleteProjectAvatarToolOutput(BinaryContentResult):
    """Binary output for tool `delete_project_avatar`."""
    pass

class DeleteProjectPropertyToolInput(BaseModel):
    """Input for tool `delete_project_property`."""
    project_id_or_key: str = Field(..., description='The project ID or project key (case sensitive).')
    property_key: str = Field(..., description='The project property key. Use [Get project property keys](#api-rest-api-3-project-projectIdOrKey-properties-get) to get a list of all project property keys.')
    model_config = ConfigDict(extra='forbid')

class DeleteProjectPropertyToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_project_property`."""
    pass

class DeleteProjectRoleToolInput(BaseModel):
    """Input for tool `delete_project_role`."""
    id: int = Field(..., description='The ID of the project role to delete. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.')
    swap: int | None = Field(default=None, description='The ID of the project role that will replace the one being deleted.')
    model_config = ConfigDict(extra='forbid')

class DeleteProjectRoleToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_project_role`."""
    pass

class DeleteProjectRoleActorsFromRoleToolInput(BaseModel):
    """Input for tool `delete_project_role_actors_from_role`."""
    id: int = Field(..., description='The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.')
    user: str | None = Field(default=None, description='The user account ID of the user to remove as a default actor.')
    group_id: str | None = Field(default=None, description='The group ID of the group to be removed as a default actor. This parameter cannot be used with the `group` parameter.')
    group: str | None = Field(default=None, description="The group name of the group to be removed as a default actor.This parameter cannot be used with the `groupId` parameter. As a group's name can change, use of `groupId` is recommended.")
    model_config = ConfigDict(extra='forbid')

class DeleteProjectRoleActorsFromRoleToolOutput(ProjectRole):
    """Output for tool `delete_project_role_actors_from_role`."""
    pass

class DeleteRemoteIssueLinkByGlobalIdToolInput(BaseModel):
    """Input for tool `delete_remote_issue_link_by_global_id`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    global_id: str = Field(..., description='The global ID of a remote issue link.')
    model_config = ConfigDict(extra='forbid')

class DeleteRemoteIssueLinkByGlobalIdToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_remote_issue_link_by_global_id`."""
    pass

class DeleteRemoteIssueLinkByIdToolInput(BaseModel):
    """Input for tool `delete_remote_issue_link_by_id`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    link_id: str = Field(..., description='The ID of a remote issue link.')
    model_config = ConfigDict(extra='forbid')

class DeleteRemoteIssueLinkByIdToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_remote_issue_link_by_id`."""
    pass

class DeleteResolutionToolInput(BaseModel):
    """Input for tool `delete_resolution`."""
    id: str = Field(..., description='The ID of the issue resolution.')
    replace_with: str = Field(..., description='The ID of the issue resolution that will replace the currently selected resolution.')
    model_config = ConfigDict(extra='forbid')

class DeleteResolutionToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_resolution`."""
    pass

class DeleteScreenToolInput(BaseModel):
    """Input for tool `delete_screen`."""
    screen_id: int = Field(..., description='The ID of the screen.')
    model_config = ConfigDict(extra='forbid')

class DeleteScreenToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_screen`."""
    pass

class DeleteScreenSchemeToolInput(BaseModel):
    """Input for tool `delete_screen_scheme`."""
    screen_scheme_id: str = Field(..., description='The ID of the screen scheme.')
    model_config = ConfigDict(extra='forbid')

class DeleteScreenSchemeToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_screen_scheme`."""
    pass

class DeleteScreenTabToolInput(BaseModel):
    """Input for tool `delete_screen_tab`."""
    screen_id: int = Field(..., description='The ID of the screen.')
    tab_id: int = Field(..., description='The ID of the screen tab.')
    model_config = ConfigDict(extra='forbid')

class DeleteScreenTabToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_screen_tab`."""
    pass

class DeleteSharePermissionToolInput(BaseModel):
    """Input for tool `delete_share_permission`."""
    id: int = Field(..., description='The ID of the filter.')
    permission_id: int = Field(..., description='The ID of the share permission.')
    model_config = ConfigDict(extra='forbid')

class DeleteSharePermissionToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_share_permission`."""
    pass

class DeleteStatusesByIdToolInput(BaseModel):
    """Input for tool `delete_statuses_by_id`."""
    id: list[str] | None = Field(default=None, description='The list of status IDs. To include multiple IDs, provide an ampersand-separated list. For example, id=10000&id=10001.\n\nMin items `1`, Max items `50`')
    model_config = ConfigDict(extra='forbid')

class DeleteStatusesByIdToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_statuses_by_id`."""
    pass

class DeleteUiModificationToolInput(BaseModel):
    """Input for tool `delete_ui_modification`."""
    ui_modification_id: str = Field(..., description='The ID of the UI modification.')
    model_config = ConfigDict(extra='forbid')

class DeleteUiModificationToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_ui_modification`."""
    pass

class DeleteUserPropertyToolInput(BaseModel):
    """Input for tool `delete_user_property`."""
    account_id: str | None = Field(default=None, description='The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.')
    user_key: str | None = Field(default=None, description='This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.')
    username: str | None = Field(default=None, description='This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.')
    property_key: str = Field(..., description="The key of the user's property.")
    model_config = ConfigDict(extra='forbid')

class DeleteUserPropertyToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_user_property`."""
    pass

class DeleteVersionToolInput(BaseModel):
    """Input for tool `delete_version`."""
    id: str = Field(..., description='The ID of the version.')
    move_fix_issues_to: str | None = Field(default=None, description='The ID of the version to update `fixVersion` to when the field contains the deleted version. The replacement version must be in the same project as the version being deleted and cannot be the version being deleted.')
    move_affected_issues_to: str | None = Field(default=None, description='The ID of the version to update `affectedVersion` to when the field contains the deleted version. The replacement version must be in the same project as the version being deleted and cannot be the version being deleted.')
    model_config = ConfigDict(extra='forbid')

class DeleteVersionToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_version`."""
    pass

class DeleteWebhookByIdToolInput(BaseModel):
    """Input for tool `delete_webhook_by_id`."""
    body: ContainerForWebhookIDs = Field(..., description='Request body for `delete_webhook_by_id`.')
    model_config = ConfigDict(extra='forbid')

class DeleteWebhookByIdToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_webhook_by_id`."""
    pass

class DeleteWorkflowMappingToolInput(BaseModel):
    """Input for tool `delete_workflow_mapping`."""
    id: int = Field(..., description='The ID of the workflow scheme.')
    workflow_name: str = Field(..., description='The name of the workflow.')
    update_draft_if_needed: bool | None = Field(default=None, description='Set to true to create or update the draft of a workflow scheme and delete the mapping from the draft, when the workflow scheme cannot be edited. Defaults to `false`.')
    model_config = ConfigDict(extra='forbid')

class DeleteWorkflowMappingToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_workflow_mapping`."""
    pass

class DeleteWorkflowSchemeToolInput(BaseModel):
    """Input for tool `delete_workflow_scheme`."""
    id: int = Field(..., description='The ID of the workflow scheme. Find this ID by editing the desired workflow scheme in Jira. The ID is shown in the URL as `schemeId`. For example, *schemeId=10301*.')
    model_config = ConfigDict(extra='forbid')

class DeleteWorkflowSchemeToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_workflow_scheme`."""
    pass

class DeleteWorkflowSchemeDraftToolInput(BaseModel):
    """Input for tool `delete_workflow_scheme_draft`."""
    id: int = Field(..., description='The ID of the active workflow scheme that the draft was created from.')
    model_config = ConfigDict(extra='forbid')

class DeleteWorkflowSchemeDraftToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_workflow_scheme_draft`."""
    pass

class DeleteWorkflowSchemeDraftIssueTypeToolInput(BaseModel):
    """Input for tool `delete_workflow_scheme_draft_issue_type`."""
    id: int = Field(..., description='The ID of the workflow scheme that the draft belongs to.')
    issue_type: str = Field(..., description='The ID of the issue type.')
    model_config = ConfigDict(extra='forbid')

class DeleteWorkflowSchemeDraftIssueTypeToolOutput(WorkflowScheme):
    """Output for tool `delete_workflow_scheme_draft_issue_type`."""
    pass

class DeleteWorkflowSchemeIssueTypeToolInput(BaseModel):
    """Input for tool `delete_workflow_scheme_issue_type`."""
    id: int = Field(..., description='The ID of the workflow scheme.')
    issue_type: str = Field(..., description='The ID of the issue type.')
    update_draft_if_needed: bool | None = Field(default=None, description='Set to true to create or update the draft of a workflow scheme and update the mapping in the draft, when the workflow scheme cannot be edited. Defaults to `false`.')
    model_config = ConfigDict(extra='forbid')

class DeleteWorkflowSchemeIssueTypeToolOutput(WorkflowScheme):
    """Output for tool `delete_workflow_scheme_issue_type`."""
    pass

class DeleteWorkflowTransitionPropertyToolInput(BaseModel):
    """Input for tool `delete_workflow_transition_property`."""
    transition_id: int = Field(..., description='The ID of the transition. To get the ID, view the workflow in text mode in the Jira admin settings. The ID is shown next to the transition.')
    workflow_name: str = Field(..., description='The name of the workflow that the transition belongs to.')
    workflow_mode: Literal['live', 'draft'] | None = Field(default=None, description='The workflow status. Set to `live` for inactive workflows or `draft` for draft workflows. Active workflows cannot be edited.')
    model_config = ConfigDict(extra='forbid')

class DeleteWorkflowTransitionPropertyToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_workflow_transition_property`."""
    pass

class DeleteWorkflowTransitionRuleConfigurationsToolInput(BaseModel):
    """Input for tool `delete_workflow_transition_rule_configurations`."""
    body: WorkflowsWithTransitionRulesDetails = Field(..., description='Request body for `delete_workflow_transition_rule_configurations`.')
    model_config = ConfigDict(extra='forbid')

class DeleteWorkflowTransitionRuleConfigurationsToolOutput(WorkflowTransitionRulesUpdateErrors):
    """Output for tool `delete_workflow_transition_rule_configurations`."""
    pass

class DeleteWorklogToolInput(BaseModel):
    """Input for tool `delete_worklog`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    id: str = Field(..., description='The ID of the worklog.')
    notify_users: bool | None = Field(default=None, description='Whether users watching the issue are notified by email.')
    adjust_estimate: Literal['new', 'leave', 'manual', 'auto'] | None = Field(default=None, description="Defines how to update the issue's time estimate, the options are:\n\n *  `new` Sets the estimate to a specific value, defined in `newEstimate`.\n *  `leave` Leaves the estimate unchanged.\n *  `manual` Increases the estimate by amount specified in `increaseBy`.\n *  `auto` Reduces the estimate by the value of `timeSpent` in the worklog.")
    new_estimate: str | None = Field(default=None, description="The value to set as the issue's remaining time estimate, as days (\\#d), hours (\\#h), or minutes (\\#m or \\#). For example, *2d*. Required when `adjustEstimate` is `new`.")
    increase_by: str | None = Field(default=None, description="The amount to increase the issue's remaining estimate by, as days (\\#d), hours (\\#h), or minutes (\\#m or \\#). For example, *2d*. Required when `adjustEstimate` is `manual`.")
    override_editable_flag: bool | None = Field(default=None, description='Whether the work log entry should be added to the issue even if the issue is not editable, because jira.issue.editable set to false or missing. For example, the issue is closed. Connect and Forge app users with admin permission can use this flag.')
    model_config = ConfigDict(extra='forbid')

class DeleteWorklogToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_worklog`."""
    pass

class DeleteWorklogPropertyToolInput(BaseModel):
    """Input for tool `delete_worklog_property`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    worklog_id: str = Field(..., description='The ID of the worklog.')
    property_key: str = Field(..., description='The key of the property.')
    model_config = ConfigDict(extra='forbid')

class DeleteWorklogPropertyToolOutput(RootModel[dict[str, object]]):
    """Output for tool `delete_worklog_property`."""
    pass

class DoTransitionToolInput(BaseModel):
    """Input for tool `do_transition`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    body: IssueUpdateDetails = Field(..., description='Request body for `do_transition`.')
    model_config = ConfigDict(extra='forbid')

class DoTransitionToolOutput(RootModel[dict[str, object]]):
    """Output for tool `do_transition`."""
    pass

class DynamicModulesResourceGetModulesGetToolInput(BaseModel):
    """Input for tool `dynamic_modules_resource_get_modules_get`."""
    model_config = ConfigDict(extra='forbid')

class DynamicModulesResourceGetModulesGetToolOutput(ConnectModules):
    """Output for tool `dynamic_modules_resource_get_modules_get`."""
    pass

class DynamicModulesResourceRegisterModulesPostToolInput(BaseModel):
    """Input for tool `dynamic_modules_resource_register_modules_post`."""
    body: ConnectModules = Field(..., description='Request body for `dynamic_modules_resource_register_modules_post`.')
    model_config = ConfigDict(extra='forbid')

class DynamicModulesResourceRegisterModulesPostToolOutput(RootModel[dict[str, object]]):
    """Output for tool `dynamic_modules_resource_register_modules_post`."""
    pass

class DynamicModulesResourceRemoveModulesDeleteToolInput(BaseModel):
    """Input for tool `dynamic_modules_resource_remove_modules_delete`."""
    module_key: list[str] | None = Field(default=None, description='The key of the module to remove. To include multiple module keys, provide multiple copies of this parameter.\nFor example, `moduleKey=dynamic-attachment-entity-property&moduleKey=dynamic-select-field`.\nNonexistent keys are ignored.')
    model_config = ConfigDict(extra='forbid')

class DynamicModulesResourceRemoveModulesDeleteToolOutput(RootModel[dict[str, object]]):
    """Output for tool `dynamic_modules_resource_remove_modules_delete`."""
    pass

class EditIssueToolInput(BaseModel):
    """Input for tool `edit_issue`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    notify_users: bool | None = Field(default=None, description="Whether a notification email about the issue update is sent to all watchers. To disable the notification, administer Jira or administer project permissions are required. If the user doesn't have the necessary permission the request is ignored.")
    override_screen_security: bool | None = Field(default=None, description='Whether screen security is overridden to enable hidden fields to be edited. Available to Connect app users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) and Forge apps acting on behalf of users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).')
    override_editable_flag: bool | None = Field(default=None, description='Whether screen security is overridden to enable uneditable fields to be edited. Available to Connect app users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) and Forge apps acting on behalf of users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).')
    body: IssueUpdateDetails = Field(..., description='Request body for `edit_issue`.')
    model_config = ConfigDict(extra='forbid')

class EditIssueToolOutput(RootModel[dict[str, object]]):
    """Output for tool `edit_issue`."""
    pass

class EvaluateJiraExpressionToolInput(BaseModel):
    """Input for tool `evaluate_jira_expression`."""
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information in the response. This parameter accepts `meta.complexity` that returns information about the expression complexity. For example, the number of expensive operations used by the expression and how close the expression is to reaching the [complexity limit](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/#restrictions). Useful when designing and debugging your expressions.')
    body: JiraExpressionEvalRequestBean = Field(..., description='Request body for `evaluate_jira_expression`.')
    model_config = ConfigDict(extra='forbid')

class EvaluateJiraExpressionToolOutput(JiraExpressionResult):
    """Output for tool `evaluate_jira_expression`."""
    pass

class ExpandAttachmentForHumansToolInput(BaseModel):
    """Input for tool `expand_attachment_for_humans`."""
    id: str = Field(..., description='The ID of the attachment.')
    model_config = ConfigDict(extra='forbid')

class ExpandAttachmentForHumansToolOutput(AttachmentArchiveMetadataReadable):
    """Output for tool `expand_attachment_for_humans`."""
    pass

class ExpandAttachmentForMachinesToolInput(BaseModel):
    """Input for tool `expand_attachment_for_machines`."""
    id: str = Field(..., description='The ID of the attachment.')
    model_config = ConfigDict(extra='forbid')

class ExpandAttachmentForMachinesToolOutput(AttachmentArchiveImpl):
    """Output for tool `expand_attachment_for_machines`."""
    pass

class FindAssignableUsersToolInput(BaseModel):
    """Input for tool `find_assignable_users`."""
    query: str | None = Field(default=None, description="A query string that is matched against user attributes, such as `displayName`, and `emailAddress`, to find relevant users. The string can match the prefix of the attribute's value. For example, *query=john* matches a user with a `displayName` of *John Smith* and a user with an `emailAddress` of *johnson@example.com*. Required, unless `username` or `accountId` is specified.")
    session_id: str | None = Field(default=None, description='The sessionId of this request. SessionId is the same until the assignee is set.')
    username: str | None = Field(default=None, description='This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.')
    account_id: str | None = Field(default=None, description='A query string that is matched exactly against user `accountId`. Required, unless `query` is specified.')
    project: str | None = Field(default=None, description='The project ID or project key (case sensitive). Required, unless `issueKey` is specified.')
    issue_key: str | None = Field(default=None, description='The key of the issue. Required, unless `project` is specified.')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return. This operation may return less than the maximum number of items even if more are available. The operation fetches users up to the maximum and then, from the fetched users, returns only the users that can be assigned to the issue.')
    action_descriptor_id: int | None = Field(default=None, description='The ID of the transition.')
    recommend: bool | None = None
    model_config = ConfigDict(extra='forbid')

class FindAssignableUsersToolOutput(FindAssignableUsersResponse):
    """Output for tool `find_assignable_users`."""
    pass

class FindBulkAssignableUsersToolInput(BaseModel):
    """Input for tool `find_bulk_assignable_users`."""
    query: str | None = Field(default=None, description="A query string that is matched against user attributes, such as `displayName` and `emailAddress`, to find relevant users. The string can match the prefix of the attribute's value. For example, *query=john* matches a user with a `displayName` of *John Smith* and a user with an `emailAddress` of *johnson@example.com*. Required, unless `accountId` is specified.")
    username: str | None = Field(default=None, description='This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.')
    account_id: str | None = Field(default=None, description='A query string that is matched exactly against user `accountId`. Required, unless `query` is specified.')
    project_keys: str = Field(..., description='A list of project keys (case sensitive). This parameter accepts a comma-separated list.')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    model_config = ConfigDict(extra='forbid')

class FindBulkAssignableUsersToolOutput(FindBulkAssignableUsersResponse):
    """Output for tool `find_bulk_assignable_users`."""
    pass

class FindGroupsToolInput(BaseModel):
    """Input for tool `find_groups`."""
    account_id: str | None = Field(default=None, description='This parameter is deprecated, setting it does not affect the results. To find groups containing a particular user, use [Get user groups](#api-rest-api-3-user-groups-get).')
    query: str | None = Field(default=None, description='The string to find in group names.')
    exclude: list[str] | None = Field(default=None, description="As a group's name can change, use of `excludeGroupIds` is recommended to identify a group.  \nA group to exclude from the result. To exclude multiple groups, provide an ampersand-separated list. For example, `exclude=group1&exclude=group2`. This parameter cannot be used with the `excludeGroupIds` parameter.")
    exclude_id: list[str] | None = Field(default=None, description='A group ID to exclude from the result. To exclude multiple groups, provide an ampersand-separated list. For example, `excludeId=group1-id&excludeId=group2-id`. This parameter cannot be used with the `excludeGroups` parameter.')
    max_results: int | None = Field(default=None, description='The maximum number of groups to return. The maximum number of groups that can be returned is limited by the system property `jira.ajax.autocomplete.limit`.')
    case_insensitive: bool | None = Field(default=None, description='Whether the search for groups should be case insensitive.')
    user_name: str | None = Field(default=None, description='This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.')
    model_config = ConfigDict(extra='forbid')

class FindGroupsToolOutput(FoundGroups):
    """Output for tool `find_groups`."""
    pass

class FindUserKeysByQueryToolInput(BaseModel):
    """Input for tool `find_user_keys_by_query`."""
    query: str = Field(..., description='The search query.')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    model_config = ConfigDict(extra='forbid')

class FindUserKeysByQueryToolOutput(PageBeanUserKey):
    """Output for tool `find_user_keys_by_query`."""
    pass

class FindUsersToolInput(BaseModel):
    """Input for tool `find_users`."""
    query: str | None = Field(default=None, description="A query string that is matched against user attributes ( `displayName`, and `emailAddress`) to find relevant users. The string can match the prefix of the attribute's value. For example, *query=john* matches a user with a `displayName` of *John Smith* and a user with an `emailAddress` of *johnson@example.com*. Required, unless `accountId` or `property` is specified.")
    username: str | None = None
    account_id: str | None = Field(default=None, description='A query string that is matched exactly against a user `accountId`. Required, unless `query` or `property` is specified.')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of filtered results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    property: str | None = Field(default=None, description='A query string used to search properties. Property keys are specified by path, so property keys containing dot (.) or equals (=) characters cannot be used. The query string cannot be specified using a JSON object. Example: To search for the value of `nested` from `{"something":{"nested":1,"other":2}}` use `thepropertykey.something.nested=1`. Required, unless `accountId` or `query` is specified.')
    model_config = ConfigDict(extra='forbid')

class FindUsersToolOutput(FindUsersResponse):
    """Output for tool `find_users`."""
    pass

class FindUsersAndGroupsToolInput(BaseModel):
    """Input for tool `find_users_and_groups`."""
    query: str = Field(..., description='The search string.')
    max_results: int | None = Field(default=None, description='The maximum number of items to return in each list.')
    show_avatar: bool | None = Field(default=None, description='Whether the user avatar should be returned. If an invalid value is provided, the default value is used.')
    field_id: str | None = Field(default=None, description='The custom field ID of the field this request is for.')
    project_id: list[str] | None = Field(default=None, description='The ID of a project that returned users and groups must have permission to view. To include multiple projects, provide an ampersand-separated list. For example, `projectId=10000&projectId=10001`. This parameter is only used when `fieldId` is present.')
    issue_type_id: list[str] | None = Field(default=None, description='The ID of an issue type that returned users and groups must have permission to view. To include multiple issue types, provide an ampersand-separated list. For example, `issueTypeId=10000&issueTypeId=10001`. Special values, such as `-1` (all standard issue types) and `-2` (all subtask issue types), are supported. This parameter is only used when `fieldId` is present.')
    avatar_size: Literal['xsmall', 'xsmall@2x', 'xsmall@3x', 'small', 'small@2x', 'small@3x', 'medium', 'medium@2x', 'medium@3x', 'large', 'large@2x', 'large@3x', 'xlarge', 'xlarge@2x', 'xlarge@3x', 'xxlarge', 'xxlarge@2x', 'xxlarge@3x', 'xxxlarge', 'xxxlarge@2x', 'xxxlarge@3x'] | None = Field(default=None, description='The size of the avatar to return. If an invalid value is provided, the default value is used.')
    case_insensitive: bool | None = Field(default=None, description='Whether the search for groups should be case insensitive.')
    exclude_connect_addons: bool | None = Field(default=None, description='Whether Connect app users and groups should be excluded from the search results. If an invalid value is provided, the default value is used.')
    model_config = ConfigDict(extra='forbid')

class FindUsersAndGroupsToolOutput(FoundUsersAndGroups):
    """Output for tool `find_users_and_groups`."""
    pass

class FindUsersByQueryToolInput(BaseModel):
    """Input for tool `find_users_by_query`."""
    query: str = Field(..., description='The search query.')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    model_config = ConfigDict(extra='forbid')

class FindUsersByQueryToolOutput(PageBeanUser):
    """Output for tool `find_users_by_query`."""
    pass

class FindUsersForPickerToolInput(BaseModel):
    """Input for tool `find_users_for_picker`."""
    query: str = Field(..., description="A query string that is matched against user attributes, such as `displayName`, and `emailAddress`, to find relevant users. The string can match the prefix of the attribute's value. For example, *query=john* matches a user with a `displayName` of *John Smith* and a user with an `emailAddress` of *johnson@example.com*.")
    max_results: int | None = Field(default=None, description='The maximum number of items to return. The total number of matched users is returned in `total`.')
    show_avatar: bool | None = Field(default=None, description="Include the URI to the user's avatar.")
    exclude: list[str] | None = Field(default=None, description='This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.')
    exclude_account_ids: list[str] | None = Field(default=None, description='A list of account IDs to exclude from the search results. This parameter accepts a comma-separated list. Multiple account IDs can also be provided using an ampersand-separated list. For example, `excludeAccountIds=5b10a2844c20165700ede21g,5b10a0effa615349cb016cd8&excludeAccountIds=5b10ac8d82e05b22cc7d4ef5`. Cannot be provided with `exclude`.')
    avatar_size: str | None = None
    exclude_connect_users: bool | None = None
    model_config = ConfigDict(extra='forbid')

class FindUsersForPickerToolOutput(FoundUsers):
    """Output for tool `find_users_for_picker`."""
    pass

class FindUsersWithAllPermissionsToolInput(BaseModel):
    """Input for tool `find_users_with_all_permissions`."""
    query: str | None = Field(default=None, description="A query string that is matched against user attributes, such as `displayName` and `emailAddress`, to find relevant users. The string can match the prefix of the attribute's value. For example, *query=john* matches a user with a `displayName` of *John Smith* and a user with an `emailAddress` of *johnson@example.com*. Required, unless `accountId` is specified.")
    username: str | None = Field(default=None, description='This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.')
    account_id: str | None = Field(default=None, description='A query string that is matched exactly against user `accountId`. Required, unless `query` is specified.')
    permissions: str = Field(..., description='A comma separated list of permissions. Permissions can be specified as any:\n\n *  permission returned by [Get all permissions](#api-rest-api-3-permissions-get).\n *  custom project permission added by Connect apps.\n *  (deprecated) one of the following:\n    \n     *  ASSIGNABLE\\_USER\n     *  ASSIGN\\_ISSUE\n     *  ATTACHMENT\\_DELETE\\_ALL\n     *  ATTACHMENT\\_DELETE\\_OWN\n     *  BROWSE\n     *  CLOSE\\_ISSUE\n     *  COMMENT\\_DELETE\\_ALL\n     *  COMMENT\\_DELETE\\_OWN\n     *  COMMENT\\_EDIT\\_ALL\n     *  COMMENT\\_EDIT\\_OWN\n     *  COMMENT\\_ISSUE\n     *  CREATE\\_ATTACHMENT\n     *  CREATE\\_ISSUE\n     *  DELETE\\_ISSUE\n     *  EDIT\\_ISSUE\n     *  LINK\\_ISSUE\n     *  MANAGE\\_WATCHER\\_LIST\n     *  MODIFY\\_REPORTER\n     *  MOVE\\_ISSUE\n     *  PROJECT\\_ADMIN\n     *  RESOLVE\\_ISSUE\n     *  SCHEDULE\\_ISSUE\n     *  SET\\_ISSUE\\_SECURITY\n     *  TRANSITION\\_ISSUE\n     *  VIEW\\_VERSION\\_CONTROL\n     *  VIEW\\_VOTERS\\_AND\\_WATCHERS\n     *  VIEW\\_WORKFLOW\\_READONLY\n     *  WORKLOG\\_DELETE\\_ALL\n     *  WORKLOG\\_DELETE\\_OWN\n     *  WORKLOG\\_EDIT\\_ALL\n     *  WORKLOG\\_EDIT\\_OWN\n     *  WORK\\_ISSUE')
    issue_key: str | None = Field(default=None, description='The issue key for the issue.')
    project_key: str | None = Field(default=None, description='The project key for the project (case sensitive).')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    model_config = ConfigDict(extra='forbid')

class FindUsersWithAllPermissionsToolOutput(FindUsersWithAllPermissionsResponse):
    """Output for tool `find_users_with_all_permissions`."""
    pass

class FindUsersWithBrowsePermissionToolInput(BaseModel):
    """Input for tool `find_users_with_browse_permission`."""
    query: str | None = Field(default=None, description="A query string that is matched against user attributes, such as `displayName` and `emailAddress`, to find relevant users. The string can match the prefix of the attribute's value. For example, *query=john* matches a user with a `displayName` of *John Smith* and a user with an `emailAddress` of *johnson@example.com*. Required, unless `accountId` is specified.")
    username: str | None = Field(default=None, description='This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.')
    account_id: str | None = Field(default=None, description='A query string that is matched exactly against user `accountId`. Required, unless `query` is specified.')
    issue_key: str | None = Field(default=None, description='The issue key for the issue. Required, unless `projectKey` is specified.')
    project_key: str | None = Field(default=None, description='The project key for the project (case sensitive). Required, unless `issueKey` is specified.')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    model_config = ConfigDict(extra='forbid')

class FindUsersWithBrowsePermissionToolOutput(FindUsersWithBrowsePermissionResponse):
    """Output for tool `find_users_with_browse_permission`."""
    pass

class FullyUpdateProjectRoleToolInput(BaseModel):
    """Input for tool `fully_update_project_role`."""
    id: int = Field(..., description='The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.')
    body: CreateUpdateRoleRequestBean = Field(..., description='Request body for `fully_update_project_role`.')
    model_config = ConfigDict(extra='forbid')

class FullyUpdateProjectRoleToolOutput(ProjectRole):
    """Output for tool `fully_update_project_role`."""
    pass

class GetAccessibleProjectTypeByKeyToolInput(BaseModel):
    """Input for tool `get_accessible_project_type_by_key`."""
    project_type_key: Literal['software', 'service_desk', 'business', 'product_discovery'] = Field(..., description='The key of the project type.')
    model_config = ConfigDict(extra='forbid')

class GetAccessibleProjectTypeByKeyToolOutput(ProjectType):
    """Output for tool `get_accessible_project_type_by_key`."""
    pass

class GetAdvancedSettingsToolInput(BaseModel):
    """Input for tool `get_advanced_settings`."""
    model_config = ConfigDict(extra='forbid')

class GetAdvancedSettingsToolOutput(GetAdvancedSettingsResponse):
    """Output for tool `get_advanced_settings`."""
    pass

class GetAllAccessibleProjectTypesToolInput(BaseModel):
    """Input for tool `get_all_accessible_project_types`."""
    model_config = ConfigDict(extra='forbid')

class GetAllAccessibleProjectTypesToolOutput(GetAllAccessibleProjectTypesResponse):
    """Output for tool `get_all_accessible_project_types`."""
    pass

class GetAllApplicationRolesToolInput(BaseModel):
    """Input for tool `get_all_application_roles`."""
    model_config = ConfigDict(extra='forbid')

class GetAllApplicationRolesToolOutput(GetAllApplicationRolesResponse):
    """Output for tool `get_all_application_roles`."""
    pass

class GetAllAvailableDashboardGadgetsToolInput(BaseModel):
    """Input for tool `get_all_available_dashboard_gadgets`."""
    model_config = ConfigDict(extra='forbid')

class GetAllAvailableDashboardGadgetsToolOutput(AvailableDashboardGadgetsResponse):
    """Output for tool `get_all_available_dashboard_gadgets`."""
    pass

class GetAllDashboardsToolInput(BaseModel):
    """Input for tool `get_all_dashboards`."""
    filter: Literal['my', 'favourite'] | None = Field(default=None, description='The filter applied to the list of dashboards. Valid values are:\n\n *  `favourite` Returns dashboards the user has marked as favorite.\n *  `my` Returns dashboards owned by the user.')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    model_config = ConfigDict(extra='forbid')

class GetAllDashboardsToolOutput(PageOfDashboards):
    """Output for tool `get_all_dashboards`."""
    pass

class GetAllFieldConfigurationSchemesToolInput(BaseModel):
    """Input for tool `get_all_field_configuration_schemes`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    id: list[int] | None = Field(default=None, description='The list of field configuration scheme IDs. To include multiple IDs, provide an ampersand-separated list. For example, `id=10000&id=10001`.')
    model_config = ConfigDict(extra='forbid')

class GetAllFieldConfigurationSchemesToolOutput(PageBeanFieldConfigurationScheme):
    """Output for tool `get_all_field_configuration_schemes`."""
    pass

class GetAllFieldConfigurationsToolInput(BaseModel):
    """Input for tool `get_all_field_configurations`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    id: list[int] | None = Field(default=None, description='The list of field configuration IDs. To include multiple IDs, provide an ampersand-separated list. For example, `id=10000&id=10001`.')
    is_default: bool | None = Field(default=None, description='If *true* returns default field configurations only.')
    query: str | None = Field(default=None, description='The query string used to match against field configuration names and descriptions.')
    model_config = ConfigDict(extra='forbid')

class GetAllFieldConfigurationsToolOutput(PageBeanFieldConfigurationDetails):
    """Output for tool `get_all_field_configurations`."""
    pass

class GetAllGadgetsToolInput(BaseModel):
    """Input for tool `get_all_gadgets`."""
    dashboard_id: int = Field(..., description='The ID of the dashboard.')
    module_key: list[str] | None = Field(default=None, description='The list of gadgets module keys. To include multiple module keys, separate module keys with ampersand: `moduleKey=key:one&moduleKey=key:two`.')
    uri: list[str] | None = Field(default=None, description='The list of gadgets URIs. To include multiple URIs, separate URIs with ampersand: `uri=/rest/example/uri/1&uri=/rest/example/uri/2`.')
    gadget_id: list[int] | None = Field(default=None, description='The list of gadgets IDs. To include multiple IDs, separate IDs with ampersand: `gadgetId=10000&gadgetId=10001`.')
    model_config = ConfigDict(extra='forbid')

class GetAllGadgetsToolOutput(DashboardGadgetResponse):
    """Output for tool `get_all_gadgets`."""
    pass

class GetAllIssueFieldOptionsToolInput(BaseModel):
    """Input for tool `get_all_issue_field_options`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    field_key: str = Field(..., description='The field key is specified in the following format: **$(app-key)\\_\\_$(field-key)**. For example, *example-add-on\\_\\_example-issue-field*. To determine the `fieldKey` value, do one of the following:\n\n *  open the app\'s plugin descriptor, then **app-key** is the key at the top and **field-key** is the key in the `jiraIssueFields` module. **app-key** can also be found in the app listing in the Atlassian Universal Plugin Manager.\n *  run [Get fields](#api-rest-api-3-field-get) and in the field details the value is returned in `key`. For example, `"key": "teams-add-on__team-issue-field"`')
    model_config = ConfigDict(extra='forbid')

class GetAllIssueFieldOptionsToolOutput(PageBeanIssueFieldOption):
    """Output for tool `get_all_issue_field_options`."""
    pass

class GetAllIssueTypeSchemesToolInput(BaseModel):
    """Input for tool `get_all_issue_type_schemes`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    id: list[int] | None = Field(default=None, description='The list of issue type schemes IDs. To include multiple IDs, provide an ampersand-separated list. For example, `id=10000&id=10001`.')
    order_by: Literal['name', '-name', '+name', 'id', '-id', '+id'] | None = Field(default=None, description='[Order](#ordering) the results by a field:\n\n *  `name` Sorts by issue type scheme name.\n *  `id` Sorts by issue type scheme ID.')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `projects` For each issue type schemes, returns information about the projects the issue type scheme is assigned to.\n *  `issueTypes` For each issue type schemes, returns information about the issueTypes the issue type scheme have.')
    query_string: str | None = Field(default=None, description='String used to perform a case-insensitive partial match with issue type scheme name.')
    model_config = ConfigDict(extra='forbid')

class GetAllIssueTypeSchemesToolOutput(PageBeanIssueTypeScheme):
    """Output for tool `get_all_issue_type_schemes`."""
    pass

class GetAllLabelsToolInput(BaseModel):
    """Input for tool `get_all_labels`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    model_config = ConfigDict(extra='forbid')

class GetAllLabelsToolOutput(PageBeanString):
    """Output for tool `get_all_labels`."""
    pass

class GetAllPermissionSchemesToolInput(BaseModel):
    """Input for tool `get_all_permission_schemes`."""
    expand: str | None = Field(default=None, description='Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are included when you specify any value. Expand options include:\n\n *  `all` Returns all expandable information.\n *  `field` Returns information about the custom field granted the permission.\n *  `group` Returns information about the group that is granted the permission.\n *  `permissions` Returns all permission grants for each permission scheme.\n *  `projectRole` Returns information about the project role granted the permission.\n *  `user` Returns information about the user who is granted the permission.')
    model_config = ConfigDict(extra='forbid')

class GetAllPermissionSchemesToolOutput(PermissionSchemes):
    """Output for tool `get_all_permission_schemes`."""
    pass

class GetAllPermissionsToolInput(BaseModel):
    """Input for tool `get_all_permissions`."""
    model_config = ConfigDict(extra='forbid')

class GetAllPermissionsToolOutput(Permissions):
    """Output for tool `get_all_permissions`."""
    pass

class GetAllProjectAvatarsToolInput(BaseModel):
    """Input for tool `get_all_project_avatars`."""
    project_id_or_key: str = Field(..., description='The ID or (case-sensitive) key of the project.')
    model_config = ConfigDict(extra='forbid')

class GetAllProjectAvatarsToolOutput(ProjectAvatars):
    """Output for tool `get_all_project_avatars`."""
    pass

class GetAllProjectCategoriesToolInput(BaseModel):
    """Input for tool `get_all_project_categories`."""
    model_config = ConfigDict(extra='forbid')

class GetAllProjectCategoriesToolOutput(GetAllProjectCategoriesResponse):
    """Output for tool `get_all_project_categories`."""
    pass

class GetAllProjectRolesToolInput(BaseModel):
    """Input for tool `get_all_project_roles`."""
    model_config = ConfigDict(extra='forbid')

class GetAllProjectRolesToolOutput(GetAllProjectRolesResponse):
    """Output for tool `get_all_project_roles`."""
    pass

class GetAllProjectTypesToolInput(BaseModel):
    """Input for tool `get_all_project_types`."""
    model_config = ConfigDict(extra='forbid')

class GetAllProjectTypesToolOutput(GetAllProjectTypesResponse):
    """Output for tool `get_all_project_types`."""
    pass

class GetAllProjectsToolInput(BaseModel):
    """Input for tool `get_all_projects`."""
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expanded options include:\n\n *  `description` Returns the project description.\n *  `issueTypes` Returns all issue types associated with the project.\n *  `lead` Returns information about the project lead.\n *  `projectKeys` Returns all project keys associated with the project.')
    recent: int | None = Field(default=None, description="Returns the user's most recently accessed projects. You may specify the number of results to return up to a maximum of 20. If access is anonymous, then the recently accessed projects are based on the current HTTP session.")
    properties: list[str] | None = Field(default=None, description='A list of project properties to return for the project. This parameter accepts a comma-separated list.')
    model_config = ConfigDict(extra='forbid')

class GetAllProjectsToolOutput(GetAllProjectsResponse):
    """Output for tool `get_all_projects`."""
    pass

class GetAllScreenTabFieldsToolInput(BaseModel):
    """Input for tool `get_all_screen_tab_fields`."""
    screen_id: int = Field(..., description='The ID of the screen.')
    tab_id: int = Field(..., description='The ID of the screen tab.')
    project_key: str | None = Field(default=None, description='The key of the project.')
    model_config = ConfigDict(extra='forbid')

class GetAllScreenTabFieldsToolOutput(GetAllScreenTabFieldsResponse):
    """Output for tool `get_all_screen_tab_fields`."""
    pass

class GetAllScreenTabsToolInput(BaseModel):
    """Input for tool `get_all_screen_tabs`."""
    screen_id: int = Field(..., description='The ID of the screen.')
    project_key: str | None = Field(default=None, description='The key of the project.')
    model_config = ConfigDict(extra='forbid')

class GetAllScreenTabsToolOutput(GetAllScreenTabsResponse):
    """Output for tool `get_all_screen_tabs`."""
    pass

class GetAllStatusesToolInput(BaseModel):
    """Input for tool `get_all_statuses`."""
    project_id_or_key: str = Field(..., description='The project ID or project key (case sensitive).')
    model_config = ConfigDict(extra='forbid')

class GetAllStatusesToolOutput(GetAllStatusesResponse):
    """Output for tool `get_all_statuses`."""
    pass

class GetAllSystemAvatarsToolInput(BaseModel):
    """Input for tool `get_all_system_avatars`."""
    type: Literal['issuetype', 'project', 'user'] = Field(..., description='The avatar type.')
    model_config = ConfigDict(extra='forbid')

class GetAllSystemAvatarsToolOutput(SystemAvatars):
    """Output for tool `get_all_system_avatars`."""
    pass

class GetAllUsersToolInput(BaseModel):
    """Input for tool `get_all_users`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return.')
    max_results: int | None = Field(default=None, description='The maximum number of items to return.')
    model_config = ConfigDict(extra='forbid')

class GetAllUsersToolOutput(GetAllUsersResponse):
    """Output for tool `get_all_users`."""
    pass

class GetAllUsersDefaultToolInput(BaseModel):
    """Input for tool `get_all_users_default`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return.')
    max_results: int | None = Field(default=None, description='The maximum number of items to return.')
    model_config = ConfigDict(extra='forbid')

class GetAllUsersDefaultToolOutput(GetAllUsersDefaultResponse):
    """Output for tool `get_all_users_default`."""
    pass

class GetAllWorkflowSchemesToolInput(BaseModel):
    """Input for tool `get_all_workflow_schemes`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    model_config = ConfigDict(extra='forbid')

class GetAllWorkflowSchemesToolOutput(PageBeanWorkflowScheme):
    """Output for tool `get_all_workflow_schemes`."""
    pass

class GetAllWorkflowsToolInput(BaseModel):
    """Input for tool `get_all_workflows`."""
    workflow_name: str | None = Field(default=None, description='The name of the workflow to be returned. Only one workflow can be specified.')
    model_config = ConfigDict(extra='forbid')

class GetAllWorkflowsToolOutput(GetAllWorkflowsResponse):
    """Output for tool `get_all_workflows`."""
    pass

class GetAlternativeIssueTypesToolInput(BaseModel):
    """Input for tool `get_alternative_issue_types`."""
    id: str = Field(..., description='The ID of the issue type.')
    model_config = ConfigDict(extra='forbid')

class GetAlternativeIssueTypesToolOutput(GetAlternativeIssueTypesResponse):
    """Output for tool `get_alternative_issue_types`."""
    pass

class GetApplicationPropertyToolInput(BaseModel):
    """Input for tool `get_application_property`."""
    permission_level: str | None = Field(default=None, description='The permission level of all items being returned in the list.')
    key_filter: str | None = Field(default=None, description="When a `key` isn't provided, this filters the list of results by the application property `key` using a regular expression. For example, using `jira.lf.*` will return all application properties with keys that start with *jira.lf.*.")
    model_config = ConfigDict(extra='forbid')

class GetApplicationPropertyToolOutput(GetApplicationPropertyResponse):
    """Output for tool `get_application_property`."""
    pass

class GetApplicationRoleToolInput(BaseModel):
    """Input for tool `get_application_role`."""
    model_config = ConfigDict(extra='forbid')

class GetApplicationRoleToolOutput(ApplicationRole):
    """Output for tool `get_application_role`."""
    pass

class GetApproximateApplicationLicenseCountToolInput(BaseModel):
    """Input for tool `get_approximate_application_license_count`."""
    application_key: str = Field(...)
    model_config = ConfigDict(extra='forbid')

class GetApproximateApplicationLicenseCountToolOutput(LicenseMetric):
    """Output for tool `get_approximate_application_license_count`."""
    pass

class GetApproximateLicenseCountToolInput(BaseModel):
    """Input for tool `get_approximate_license_count`."""
    model_config = ConfigDict(extra='forbid')

class GetApproximateLicenseCountToolOutput(LicenseMetric):
    """Output for tool `get_approximate_license_count`."""
    pass

class GetAssignedPermissionSchemeToolInput(BaseModel):
    """Input for tool `get_assigned_permission_scheme`."""
    project_key_or_id: str = Field(..., description='The project ID or project key (case sensitive).')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are included when you specify any value. Expand options include:\n\n *  `all` Returns all expandable information.\n *  `field` Returns information about the custom field granted the permission.\n *  `group` Returns information about the group that is granted the permission.\n *  `permissions` Returns all permission grants for each permission scheme.\n *  `projectRole` Returns information about the project role granted the permission.\n *  `user` Returns information about the user who is granted the permission.')
    model_config = ConfigDict(extra='forbid')

class GetAssignedPermissionSchemeToolOutput(PermissionScheme):
    """Output for tool `get_assigned_permission_scheme`."""
    pass

class GetAttachmentToolInput(BaseModel):
    """Input for tool `get_attachment`."""
    id: str = Field(..., description='The ID of the attachment.')
    model_config = ConfigDict(extra='forbid')

class GetAttachmentToolOutput(AttachmentMetadata):
    """Output for tool `get_attachment`."""
    pass

class GetAttachmentContentToolInput(BaseModel):
    """Input for tool `get_attachment_content`."""
    id: str = Field(..., description='The ID of the attachment.')
    redirect: bool | None = Field(default=None, description='Whether a redirect is provided for the attachment download. Clients that do not automatically follow redirects can set this to `false` to avoid making multiple requests to download the attachment.')
    model_config = ConfigDict(extra='forbid')

class GetAttachmentContentToolOutput(BinaryContentResult):
    """Binary output for tool `get_attachment_content`."""
    pass

class GetAttachmentMetaToolInput(BaseModel):
    """Input for tool `get_attachment_meta`."""
    model_config = ConfigDict(extra='forbid')

class GetAttachmentMetaToolOutput(AttachmentSettings):
    """Output for tool `get_attachment_meta`."""
    pass

class GetAttachmentThumbnailToolInput(BaseModel):
    """Input for tool `get_attachment_thumbnail`."""
    id: str = Field(..., description='The ID of the attachment.')
    redirect: bool | None = Field(default=None, description='Whether a redirect is provided for the attachment download. Clients that do not automatically follow redirects can set this to `false` to avoid making multiple requests to download the attachment.')
    fallback_to_default: bool | None = Field(default=None, description='Whether a default thumbnail is returned when the requested thumbnail is not found.')
    width: int | None = Field(default=None, description='The maximum width to scale the thumbnail to.')
    height: int | None = Field(default=None, description='The maximum height to scale the thumbnail to.')
    model_config = ConfigDict(extra='forbid')

class GetAttachmentThumbnailToolOutput(BinaryContentResult):
    """Binary output for tool `get_attachment_thumbnail`."""
    pass

class GetAuditRecordsToolInput(BaseModel):
    """Input for tool `get_audit_records`."""
    offset: int | None = Field(default=None, description='The number of records to skip before returning the first result.')
    limit: int | None = Field(default=None, description='The maximum number of results to return.')
    filter: str | None = Field(default=None, description='The strings to match with audit field content, space separated.')
    from_: str | None = Field(default=None, description='The date and time on or after which returned audit records must have been created. If `to` is provided `from` must be before `to` or no audit records are returned.')
    to: str | None = Field(default=None, description='The date and time on or before which returned audit results must have been created. If `from` is provided `to` must be after `from` or no audit records are returned.')
    model_config = ConfigDict(extra='forbid')

class GetAuditRecordsToolOutput(AuditRecords):
    """Output for tool `get_audit_records`."""
    pass

class GetAutoCompleteToolInput(BaseModel):
    """Input for tool `get_auto_complete`."""
    model_config = ConfigDict(extra='forbid')

class GetAutoCompleteToolOutput(JQLReferenceData):
    """Output for tool `get_auto_complete`."""
    pass

class GetAutoCompletePostToolInput(BaseModel):
    """Input for tool `get_auto_complete_post`."""
    body: SearchAutoCompleteFilter = Field(..., description='Request body for `get_auto_complete_post`.')
    model_config = ConfigDict(extra='forbid')

class GetAutoCompletePostToolOutput(JQLReferenceData):
    """Output for tool `get_auto_complete_post`."""
    pass

class GetAvailableScreenFieldsToolInput(BaseModel):
    """Input for tool `get_available_screen_fields`."""
    screen_id: int = Field(..., description='The ID of the screen.')
    model_config = ConfigDict(extra='forbid')

class GetAvailableScreenFieldsToolOutput(GetAvailableScreenFieldsResponse):
    """Output for tool `get_available_screen_fields`."""
    pass

class GetAvailableTimeTrackingImplementationsToolInput(BaseModel):
    """Input for tool `get_available_time_tracking_implementations`."""
    model_config = ConfigDict(extra='forbid')

class GetAvailableTimeTrackingImplementationsToolOutput(GetAvailableTimeTrackingImplementationsResponse):
    """Output for tool `get_available_time_tracking_implementations`."""
    pass

class GetAvatarImageByIdToolInput(BaseModel):
    """Input for tool `get_avatar_image_by_id`."""
    type: Literal['issuetype', 'project'] = Field(..., description='The icon type of the avatar.')
    id: int = Field(..., description='The ID of the avatar.')
    size: Literal['xsmall', 'small', 'medium', 'large', 'xlarge'] | None = Field(default=None, description='The size of the avatar image. If not provided the default size is returned.')
    format: Literal['png', 'svg'] | None = Field(default=None, description='The format to return the avatar image in. If not provided the original content format is returned.')
    model_config = ConfigDict(extra='forbid')

class GetAvatarImageByIdToolOutput(BinaryContentResult):
    """Binary output for tool `get_avatar_image_by_id`."""
    pass

class GetAvatarImageByOwnerToolInput(BaseModel):
    """Input for tool `get_avatar_image_by_owner`."""
    type: Literal['issuetype', 'project'] = Field(..., description='The icon type of the avatar.')
    entity_id: str = Field(..., description='The ID of the project or issue type the avatar belongs to.')
    size: Literal['xsmall', 'small', 'medium', 'large', 'xlarge'] | None = Field(default=None, description='The size of the avatar image. If not provided the default size is returned.')
    format: Literal['png', 'svg'] | None = Field(default=None, description='The format to return the avatar image in. If not provided the original content format is returned.')
    model_config = ConfigDict(extra='forbid')

class GetAvatarImageByOwnerToolOutput(BinaryContentResult):
    """Binary output for tool `get_avatar_image_by_owner`."""
    pass

class GetAvatarImageByTypeToolInput(BaseModel):
    """Input for tool `get_avatar_image_by_type`."""
    type: Literal['issuetype', 'project'] = Field(..., description='The icon type of the avatar.')
    size: Literal['xsmall', 'small', 'medium', 'large', 'xlarge'] | None = Field(default=None, description='The size of the avatar image. If not provided the default size is returned.')
    format: Literal['png', 'svg'] | None = Field(default=None, description='The format to return the avatar image in. If not provided the original content format is returned.')
    model_config = ConfigDict(extra='forbid')

class GetAvatarImageByTypeToolOutput(BinaryContentResult):
    """Binary output for tool `get_avatar_image_by_type`."""
    pass

class GetAvatarsToolInput(BaseModel):
    """Input for tool `get_avatars`."""
    type: Literal['project', 'issuetype'] = Field(..., description='The avatar type.')
    entity_id: str = Field(..., description='The ID of the item the avatar is associated with.')
    model_config = ConfigDict(extra='forbid')

class GetAvatarsToolOutput(Avatars):
    """Output for tool `get_avatars`."""
    pass

class GetBannerToolInput(BaseModel):
    """Input for tool `get_banner`."""
    model_config = ConfigDict(extra='forbid')

class GetBannerToolOutput(AnnouncementBannerConfiguration):
    """Output for tool `get_banner`."""
    pass

class GetBulkPermissionsToolInput(BaseModel):
    """Input for tool `get_bulk_permissions`."""
    body: BulkPermissionsRequestBean = Field(..., description='Request body for `get_bulk_permissions`.')
    model_config = ConfigDict(extra='forbid')

class GetBulkPermissionsToolOutput(BulkPermissionGrants):
    """Output for tool `get_bulk_permissions`."""
    pass

class GetChangeLogsToolInput(BaseModel):
    """Input for tool `get_change_logs`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    model_config = ConfigDict(extra='forbid')

class GetChangeLogsToolOutput(PageBeanChangelog):
    """Output for tool `get_change_logs`."""
    pass

class GetChangeLogsByIdsToolInput(BaseModel):
    """Input for tool `get_change_logs_by_ids`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    body: IssueChangelogIds = Field(..., description='Request body for `get_change_logs_by_ids`.')
    model_config = ConfigDict(extra='forbid')

class GetChangeLogsByIdsToolOutput(PageOfChangelogs):
    """Output for tool `get_change_logs_by_ids`."""
    pass

class GetColumnsToolInput(BaseModel):
    """Input for tool `get_columns`."""
    id: int = Field(..., description='The ID of the filter.')
    model_config = ConfigDict(extra='forbid')

class GetColumnsToolOutput(GetColumnsResponse):
    """Output for tool `get_columns`."""
    pass

class GetCommentToolInput(BaseModel):
    """Input for tool `get_comment`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    id: str = Field(..., description='The ID of the comment.')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information about comments in the response. This parameter accepts `renderedBody`, which returns the comment body rendered in HTML.')
    model_config = ConfigDict(extra='forbid')

class GetCommentToolOutput(Comment):
    """Output for tool `get_comment`."""
    pass

class GetCommentPropertyToolInput(BaseModel):
    """Input for tool `get_comment_property`."""
    comment_id: str = Field(..., description='The ID of the comment.')
    property_key: str = Field(..., description='The key of the property.')
    model_config = ConfigDict(extra='forbid')

class GetCommentPropertyToolOutput(EntityProperty):
    """Output for tool `get_comment_property`."""
    pass

class GetCommentPropertyKeysToolInput(BaseModel):
    """Input for tool `get_comment_property_keys`."""
    comment_id: str = Field(..., description='The ID of the comment.')
    model_config = ConfigDict(extra='forbid')

class GetCommentPropertyKeysToolOutput(PropertyKeys):
    """Output for tool `get_comment_property_keys`."""
    pass

class GetCommentsToolInput(BaseModel):
    """Input for tool `get_comments`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    order_by: Literal['created', '-created', '+created'] | None = Field(default=None, description='[Order](#ordering) the results by a field. Accepts *created* to sort comments by their created date.')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information about comments in the response. This parameter accepts `renderedBody`, which returns the comment body rendered in HTML.')
    model_config = ConfigDict(extra='forbid')

class GetCommentsToolOutput(PageOfComments):
    """Output for tool `get_comments`."""
    pass

class GetCommentsByIdsToolInput(BaseModel):
    """Input for tool `get_comments_by_ids`."""
    expand: str | None = Field(default=None, description="Use [expand](#expansion) to include additional information about comments in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `renderedBody` Returns the comment body rendered in HTML.\n *  `properties` Returns the comment's properties.")
    body: IssueCommentListRequestBean = Field(..., description='Request body for `get_comments_by_ids`.')
    model_config = ConfigDict(extra='forbid')

class GetCommentsByIdsToolOutput(PageBeanComment):
    """Output for tool `get_comments_by_ids`."""
    pass

class GetComponentToolInput(BaseModel):
    """Input for tool `get_component`."""
    id: str = Field(..., description='The ID of the component.')
    model_config = ConfigDict(extra='forbid')

class GetComponentToolOutput(ProjectComponent):
    """Output for tool `get_component`."""
    pass

class GetComponentRelatedIssuesToolInput(BaseModel):
    """Input for tool `get_component_related_issues`."""
    id: str = Field(..., description='The ID of the component.')
    model_config = ConfigDict(extra='forbid')

class GetComponentRelatedIssuesToolOutput(ComponentIssuesCount):
    """Output for tool `get_component_related_issues`."""
    pass

class GetConfigurationToolInput(BaseModel):
    """Input for tool `get_configuration`."""
    model_config = ConfigDict(extra='forbid')

class GetConfigurationToolOutput(Configuration):
    """Output for tool `get_configuration`."""
    pass

class GetContextsForFieldToolInput(BaseModel):
    """Input for tool `get_contexts_for_field`."""
    field_id: str = Field(..., description='The ID of the custom field.')
    is_any_issue_type: bool | None = Field(default=None, description='Whether to return contexts that apply to all issue types.')
    is_global_context: bool | None = Field(default=None, description='Whether to return contexts that apply to all projects.')
    context_id: list[int] | None = Field(default=None, description='The list of context IDs. To include multiple contexts, separate IDs with ampersand: `contextId=10000&contextId=10001`.')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    model_config = ConfigDict(extra='forbid')

class GetContextsForFieldToolOutput(PageBeanCustomFieldContext):
    """Output for tool `get_contexts_for_field`."""
    pass

class GetContextsForFieldDeprecatedToolInput(BaseModel):
    """Input for tool `get_contexts_for_field_deprecated`."""
    field_id: str = Field(..., description='The ID of the field to return contexts for.')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    model_config = ConfigDict(extra='forbid')

class GetContextsForFieldDeprecatedToolOutput(PageBeanContext):
    """Output for tool `get_contexts_for_field_deprecated`."""
    pass

class GetCreateIssueMetaToolInput(BaseModel):
    """Input for tool `get_create_issue_meta`."""
    project_ids: list[str] | None = Field(default=None, description='List of project IDs. This parameter accepts a comma-separated list. Multiple project IDs can also be provided using an ampersand-separated list. For example, `projectIds=10000,10001&projectIds=10020,10021`. This parameter may be provided with `projectKeys`.')
    project_keys: list[str] | None = Field(default=None, description='List of project keys. This parameter accepts a comma-separated list. Multiple project keys can also be provided using an ampersand-separated list. For example, `projectKeys=proj1,proj2&projectKeys=proj3`. This parameter may be provided with `projectIds`.')
    issuetype_ids: list[str] | None = Field(default=None, description='List of issue type IDs. This parameter accepts a comma-separated list. Multiple issue type IDs can also be provided using an ampersand-separated list. For example, `issuetypeIds=10000,10001&issuetypeIds=10020,10021`. This parameter may be provided with `issuetypeNames`.')
    issuetype_names: list[str] | None = Field(default=None, description='List of issue type names. This parameter accepts a comma-separated list. Multiple issue type names can also be provided using an ampersand-separated list. For example, `issuetypeNames=name1,name2&issuetypeNames=name3`. This parameter may be provided with `issuetypeIds`.')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information about issue metadata in the response. This parameter accepts `projects.issuetypes.fields`, which returns information about the fields in the issue creation screen for each issue type. Fields hidden from the screen are not returned. Use the information to populate the `fields` and `update` fields in [Create issue](#api-rest-api-3-issue-post) and [Create issues](#api-rest-api-3-issue-bulk-post).')
    model_config = ConfigDict(extra='forbid')

class GetCreateIssueMetaToolOutput(IssueCreateMetadata):
    """Output for tool `get_create_issue_meta`."""
    pass

class GetCurrentUserToolInput(BaseModel):
    """Input for tool `get_current_user`."""
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information about user in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `groups` Returns all groups, including nested groups, the user belongs to.\n *  `applicationRoles` Returns the application roles the user is assigned to.')
    model_config = ConfigDict(extra='forbid')

class GetCurrentUserToolOutput(User):
    """Output for tool `get_current_user`."""
    pass

class GetCustomFieldConfigurationToolInput(BaseModel):
    """Input for tool `get_custom_field_configuration`."""
    field_id_or_key: str = Field(..., description='The ID or key of the custom field, for example `customfield_10000`.')
    id: list[int] | None = Field(default=None, description="The list of configuration IDs. To include multiple configurations, separate IDs with an ampersand: `id=10000&id=10001`. Can't be provided with `fieldContextId`, `issueId`, `projectKeyOrId`, or `issueTypeId`.")
    field_context_id: list[int] | None = Field(default=None, description="The list of field context IDs. To include multiple field contexts, separate IDs with an ampersand: `fieldContextId=10000&fieldContextId=10001`. Can't be provided with `id`, `issueId`, `projectKeyOrId`, or `issueTypeId`.")
    issue_id: int | None = Field(default=None, description="The ID of the issue to filter results by. If the issue doesn't exist, an empty list is returned. Can't be provided with `projectKeyOrId`, or `issueTypeId`.")
    project_key_or_id: str | None = Field(default=None, description="The ID or key of the project to filter results by. Must be provided with `issueTypeId`. Can't be provided with `issueId`.")
    issue_type_id: str | None = Field(default=None, description="The ID of the issue type to filter results by. Must be provided with `projectKeyOrId`. Can't be provided with `issueId`.")
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    model_config = ConfigDict(extra='forbid')

class GetCustomFieldConfigurationToolOutput(PageBeanContextualConfiguration):
    """Output for tool `get_custom_field_configuration`."""
    pass

class GetCustomFieldContextsForProjectsAndIssueTypesToolInput(BaseModel):
    """Input for tool `get_custom_field_contexts_for_projects_and_issue_types`."""
    field_id: str = Field(..., description='The ID of the custom field.')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    body: ProjectIssueTypeMappings = Field(..., description='Request body for `get_custom_field_contexts_for_projects_and_issue_types`.')
    model_config = ConfigDict(extra='forbid')

class GetCustomFieldContextsForProjectsAndIssueTypesToolOutput(PageBeanContextForProjectAndIssueType):
    """Output for tool `get_custom_field_contexts_for_projects_and_issue_types`."""
    pass

class GetCustomFieldOptionToolInput(BaseModel):
    """Input for tool `get_custom_field_option`."""
    id: str = Field(..., description='The ID of the custom field option.')
    model_config = ConfigDict(extra='forbid')

class GetCustomFieldOptionToolOutput(CustomFieldOption):
    """Output for tool `get_custom_field_option`."""
    pass

class GetDashboardToolInput(BaseModel):
    """Input for tool `get_dashboard`."""
    id: str = Field(..., description='The ID of the dashboard.')
    model_config = ConfigDict(extra='forbid')

class GetDashboardToolOutput(Dashboard):
    """Output for tool `get_dashboard`."""
    pass

class GetDashboardItemPropertyToolInput(BaseModel):
    """Input for tool `get_dashboard_item_property`."""
    dashboard_id: str = Field(..., description='The ID of the dashboard.')
    item_id: str = Field(..., description='The ID of the dashboard item.')
    property_key: str = Field(..., description='The key of the dashboard item property.')
    model_config = ConfigDict(extra='forbid')

class GetDashboardItemPropertyToolOutput(EntityProperty):
    """Output for tool `get_dashboard_item_property`."""
    pass

class GetDashboardItemPropertyKeysToolInput(BaseModel):
    """Input for tool `get_dashboard_item_property_keys`."""
    dashboard_id: str = Field(..., description='The ID of the dashboard.')
    item_id: str = Field(..., description='The ID of the dashboard item.')
    model_config = ConfigDict(extra='forbid')

class GetDashboardItemPropertyKeysToolOutput(PropertyKeys):
    """Output for tool `get_dashboard_item_property_keys`."""
    pass

class GetDashboardsPaginatedToolInput(BaseModel):
    """Input for tool `get_dashboards_paginated`."""
    dashboard_name: str | None = Field(default=None, description='String used to perform a case-insensitive partial match with `name`.')
    account_id: str | None = Field(default=None, description='User account ID used to return dashboards with the matching `owner.accountId`. This parameter cannot be used with the `owner` parameter.')
    owner: str | None = Field(default=None, description='This parameter is deprecated because of privacy changes. Use `accountId` instead. See the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details. User name used to return dashboards with the matching `owner.name`. This parameter cannot be used with the `accountId` parameter.')
    groupname: str | None = Field(default=None, description="As a group's name can change, use of `groupId` is recommended. Group name used to return dashboards that are shared with a group that matches `sharePermissions.group.name`. This parameter cannot be used with the `groupId` parameter.")
    group_id: str | None = Field(default=None, description='Group ID used to return dashboards that are shared with a group that matches `sharePermissions.group.groupId`. This parameter cannot be used with the `groupname` parameter.')
    project_id: int | None = Field(default=None, description='Project ID used to returns dashboards that are shared with a project that matches `sharePermissions.project.id`.')
    order_by: Literal['description', '-description', '+description', 'favorite_count', '-favorite_count', '+favorite_count', 'id', '-id', '+id', 'is_favorite', '-is_favorite', '+is_favorite', 'name', '-name', '+name', 'owner', '-owner', '+owner'] | None = Field(default=None, description='[Order](#ordering) the results by a field:\n\n *  `description` Sorts by dashboard description. Note that this sort works independently of whether the expand to display the description field is in use.\n *  `favourite_count` Sorts by dashboard popularity.\n *  `id` Sorts by dashboard ID.\n *  `is_favourite` Sorts by whether the dashboard is marked as a favorite.\n *  `name` Sorts by dashboard name.\n *  `owner` Sorts by dashboard owner name.')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    status: Literal['active', 'archived', 'deleted'] | None = Field(default=None, description='The status to filter by. It may be active, archived or deleted.')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information about dashboard in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `description` Returns the description of the dashboard.\n *  `owner` Returns the owner of the dashboard.\n *  `viewUrl` Returns the URL that is used to view the dashboard.\n *  `favourite` Returns `isFavourite`, an indicator of whether the user has set the dashboard as a favorite.\n *  `favouritedCount` Returns `popularity`, a count of how many users have set this dashboard as a favorite.\n *  `sharePermissions` Returns details of the share permissions defined for the dashboard.\n *  `editPermissions` Returns details of the edit permissions defined for the dashboard.\n *  `isWritable` Returns whether the current user has permission to edit the dashboard.')
    model_config = ConfigDict(extra='forbid')

class GetDashboardsPaginatedToolOutput(PageBeanDashboard):
    """Output for tool `get_dashboards_paginated`."""
    pass

class GetDefaultShareScopeToolInput(BaseModel):
    """Input for tool `get_default_share_scope`."""
    model_config = ConfigDict(extra='forbid')

class GetDefaultShareScopeToolOutput(DefaultShareScope):
    """Output for tool `get_default_share_scope`."""
    pass

class GetDefaultValuesToolInput(BaseModel):
    """Input for tool `get_default_values`."""
    field_id: str = Field(..., description='The ID of the custom field, for example `customfield\\_10000`.')
    context_id: list[int] | None = Field(default=None, description='The IDs of the contexts.')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    model_config = ConfigDict(extra='forbid')

class GetDefaultValuesToolOutput(PageBeanCustomFieldContextDefaultValue):
    """Output for tool `get_default_values`."""
    pass

class GetDefaultWorkflowToolInput(BaseModel):
    """Input for tool `get_default_workflow`."""
    id: int = Field(..., description='The ID of the workflow scheme.')
    return_draft_if_exists: bool | None = Field(default=None, description="Set to `true` to return the default workflow for the workflow scheme's draft rather than scheme itself. If the workflow scheme does not have a draft, then the default workflow for the workflow scheme is returned.")
    model_config = ConfigDict(extra='forbid')

class GetDefaultWorkflowToolOutput(DefaultWorkflow):
    """Output for tool `get_default_workflow`."""
    pass

class GetDraftDefaultWorkflowToolInput(BaseModel):
    """Input for tool `get_draft_default_workflow`."""
    id: int = Field(..., description='The ID of the workflow scheme that the draft belongs to.')
    model_config = ConfigDict(extra='forbid')

class GetDraftDefaultWorkflowToolOutput(DefaultWorkflow):
    """Output for tool `get_draft_default_workflow`."""
    pass

class GetDraftWorkflowToolInput(BaseModel):
    """Input for tool `get_draft_workflow`."""
    id: int = Field(..., description='The ID of the workflow scheme that the draft belongs to.')
    workflow_name: str | None = Field(default=None, description='The name of a workflow in the scheme. Limits the results to the workflow-issue type mapping for the specified workflow.')
    model_config = ConfigDict(extra='forbid')

class GetDraftWorkflowToolOutput(IssueTypesWorkflowMapping):
    """Output for tool `get_draft_workflow`."""
    pass

class GetDynamicWebhooksForAppToolInput(BaseModel):
    """Input for tool `get_dynamic_webhooks_for_app`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    model_config = ConfigDict(extra='forbid')

class GetDynamicWebhooksForAppToolOutput(PageBeanWebhook):
    """Output for tool `get_dynamic_webhooks_for_app`."""
    pass

class GetEditIssueMetaToolInput(BaseModel):
    """Input for tool `get_edit_issue_meta`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    override_screen_security: bool | None = Field(default=None, description='Whether hidden fields are returned. Available to Connect app users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) and Forge apps acting on behalf of users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).')
    override_editable_flag: bool | None = Field(default=None, description='Whether non-editable fields are returned. Available to Connect app users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) and Forge apps acting on behalf of users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).')
    model_config = ConfigDict(extra='forbid')

class GetEditIssueMetaToolOutput(IssueUpdateMetadata):
    """Output for tool `get_edit_issue_meta`."""
    pass

class GetEventsToolInput(BaseModel):
    """Input for tool `get_events`."""
    model_config = ConfigDict(extra='forbid')

class GetEventsToolOutput(GetEventsResponse):
    """Output for tool `get_events`."""
    pass

class GetFailedWebhooksToolInput(BaseModel):
    """Input for tool `get_failed_webhooks`."""
    max_results: int | None = Field(default=None, description='The maximum number of webhooks to return per page. If obeying the maxResults directive would result in records with the same failure time being split across pages, the directive is ignored and all records with the same failure time included on the page.')
    after: int | None = Field(default=None, description='The time after which any webhook failure must have occurred for the record to be returned, expressed as milliseconds since the UNIX epoch.')
    model_config = ConfigDict(extra='forbid')

class GetFailedWebhooksToolOutput(FailedWebhooks):
    """Output for tool `get_failed_webhooks`."""
    pass

class GetFavouriteFiltersToolInput(BaseModel):
    """Input for tool `get_favourite_filters`."""
    expand: str | None = Field(default=None, description="Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `sharedUsers` Returns the users that the filter is shared with. This includes users that can browse projects that the filter is shared with. If you don't specify `sharedUsers`, then the `sharedUsers` object is returned but it doesn't list any users. The list of users returned is limited to 1000, to access additional users append `[start-index:end-index]` to the expand request. For example, to access the next 1000 users, use `?expand=sharedUsers[1001:2000]`.\n *  `subscriptions` Returns the users that are subscribed to the filter. If you don't specify `subscriptions`, the `subscriptions` object is returned but it doesn't list any subscriptions. The list of subscriptions returned is limited to 1000, to access additional subscriptions append `[start-index:end-index]` to the expand request. For example, to access the next 1000 subscriptions, use `?expand=subscriptions[1001:2000]`.")
    model_config = ConfigDict(extra='forbid')

class GetFavouriteFiltersToolOutput(GetFavouriteFiltersResponse):
    """Output for tool `get_favourite_filters`."""
    pass

class GetFeaturesForProjectToolInput(BaseModel):
    """Input for tool `get_features_for_project`."""
    project_id_or_key: str = Field(..., description='The ID or (case-sensitive) key of the project.')
    model_config = ConfigDict(extra='forbid')

class GetFeaturesForProjectToolOutput(ContainerForProjectFeatures):
    """Output for tool `get_features_for_project`."""
    pass

class GetFieldAutoCompleteForQueryStringToolInput(BaseModel):
    """Input for tool `get_field_auto_complete_for_query_string`."""
    field_name: str | None = Field(default=None, description='The name of the field.')
    field_value: str | None = Field(default=None, description='The partial field item name entered by the user.')
    predicate_name: str | None = Field(default=None, description='The name of the [ CHANGED operator predicate](https://confluence.atlassian.com/x/hQORLQ#Advancedsearching-operatorsreference-CHANGEDCHANGED) for which the suggestions are generated. The valid predicate operators are *by*, *from*, and *to*.')
    predicate_value: str | None = Field(default=None, description='The partial predicate item name entered by the user.')
    model_config = ConfigDict(extra='forbid')

class GetFieldAutoCompleteForQueryStringToolOutput(AutoCompleteSuggestions):
    """Output for tool `get_field_auto_complete_for_query_string`."""
    pass

class GetFieldConfigurationItemsToolInput(BaseModel):
    """Input for tool `get_field_configuration_items`."""
    id: int = Field(..., description='The ID of the field configuration.')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    model_config = ConfigDict(extra='forbid')

class GetFieldConfigurationItemsToolOutput(PageBeanFieldConfigurationItem):
    """Output for tool `get_field_configuration_items`."""
    pass

class GetFieldConfigurationSchemeMappingsToolInput(BaseModel):
    """Input for tool `get_field_configuration_scheme_mappings`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    field_configuration_scheme_id: list[int] | None = Field(default=None, description='The list of field configuration scheme IDs. To include multiple field configuration schemes separate IDs with ampersand: `fieldConfigurationSchemeId=10000&fieldConfigurationSchemeId=10001`.')
    model_config = ConfigDict(extra='forbid')

class GetFieldConfigurationSchemeMappingsToolOutput(PageBeanFieldConfigurationIssueTypeItem):
    """Output for tool `get_field_configuration_scheme_mappings`."""
    pass

class GetFieldConfigurationSchemeProjectMappingToolInput(BaseModel):
    """Input for tool `get_field_configuration_scheme_project_mapping`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    project_id: list[int] = Field(..., description='The list of project IDs. To include multiple projects, separate IDs with ampersand: `projectId=10000&projectId=10001`.')
    model_config = ConfigDict(extra='forbid')

class GetFieldConfigurationSchemeProjectMappingToolOutput(PageBeanFieldConfigurationSchemeProjects):
    """Output for tool `get_field_configuration_scheme_project_mapping`."""
    pass

class GetFieldsToolInput(BaseModel):
    """Input for tool `get_fields`."""
    model_config = ConfigDict(extra='forbid')

class GetFieldsToolOutput(GetFieldsResponse):
    """Output for tool `get_fields`."""
    pass

class GetFieldsPaginatedToolInput(BaseModel):
    """Input for tool `get_fields_paginated`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    type: list[Literal['custom', 'system']] | None = Field(default=None, description='The type of fields to search.')
    id: list[str] | None = Field(default=None, description='The IDs of the custom fields to return or, where `query` is specified, filter.')
    query: str | None = Field(default=None, description='String used to perform a case-insensitive partial match with field names or descriptions.')
    order_by: Literal['contextsCount', '-contextsCount', '+contextsCount', 'lastUsed', '-lastUsed', '+lastUsed', 'name', '-name', '+name', 'screensCount', '-screensCount', '+screensCount', 'projectsCount', '-projectsCount', '+projectsCount'] | None = Field(default=None, description='[Order](#ordering) the results by a field:\n\n *  `contextsCount` sorts by the number of contexts related to a field\n *  `lastUsed` sorts by the date when the value of the field last changed\n *  `name` sorts by the field name\n *  `screensCount` sorts by the number of screens related to a field')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `key` returns the key for each field\n *  `lastUsed` returns the date when the value of the field last changed\n *  `screensCount` returns the number of screens related to a field\n *  `contextsCount` returns the number of contexts related to a field\n *  `isLocked` returns information about whether the field is [locked](https://confluence.atlassian.com/x/ZSN7Og)\n *  `searcherKey` returns the searcher key for each custom field')
    model_config = ConfigDict(extra='forbid')

class GetFieldsPaginatedToolOutput(PageBeanField):
    """Output for tool `get_fields_paginated`."""
    pass

class GetFilterToolInput(BaseModel):
    """Input for tool `get_filter`."""
    id: int = Field(..., description='The ID of the filter to return.')
    expand: str | None = Field(default=None, description="Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `sharedUsers` Returns the users that the filter is shared with. This includes users that can browse projects that the filter is shared with. If you don't specify `sharedUsers`, then the `sharedUsers` object is returned but it doesn't list any users. The list of users returned is limited to 1000, to access additional users append `[start-index:end-index]` to the expand request. For example, to access the next 1000 users, use `?expand=sharedUsers[1001:2000]`.\n *  `subscriptions` Returns the users that are subscribed to the filter. If you don't specify `subscriptions`, the `subscriptions` object is returned but it doesn't list any subscriptions. The list of subscriptions returned is limited to 1000, to access additional subscriptions append `[start-index:end-index]` to the expand request. For example, to access the next 1000 subscriptions, use `?expand=subscriptions[1001:2000]`.")
    override_share_permissions: bool | None = Field(default=None, description='EXPERIMENTAL: Whether share permissions are overridden to enable filters with any share permissions to be returned. Available to users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).')
    model_config = ConfigDict(extra='forbid')

class GetFilterToolOutput(Filter):
    """Output for tool `get_filter`."""
    pass

class GetFiltersToolInput(BaseModel):
    """Input for tool `get_filters`."""
    expand: str | None = Field(default=None, description="Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `sharedUsers` Returns the users that the filter is shared with. This includes users that can browse projects that the filter is shared with. If you don't specify `sharedUsers`, then the `sharedUsers` object is returned but it doesn't list any users. The list of users returned is limited to 1000, to access additional users append `[start-index:end-index]` to the expand request. For example, to access the next 1000 users, use `?expand=sharedUsers[1001:2000]`.\n *  `subscriptions` Returns the users that are subscribed to the filter. If you don't specify `subscriptions`, the `subscriptions` object is returned but it doesn't list any subscriptions. The list of subscriptions returned is limited to 1000, to access additional subscriptions append `[start-index:end-index]` to the expand request. For example, to access the next 1000 subscriptions, use `?expand=subscriptions[1001:2000]`.")
    model_config = ConfigDict(extra='forbid')

class GetFiltersToolOutput(GetFiltersResponse):
    """Output for tool `get_filters`."""
    pass

class GetFiltersPaginatedToolInput(BaseModel):
    """Input for tool `get_filters_paginated`."""
    filter_name: str | None = Field(default=None, description='String used to perform a case-insensitive partial match with `name`.')
    account_id: str | None = Field(default=None, description='User account ID used to return filters with the matching `owner.accountId`. This parameter cannot be used with `owner`.')
    owner: str | None = Field(default=None, description='This parameter is deprecated because of privacy changes. Use `accountId` instead. See the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details. User name used to return filters with the matching `owner.name`. This parameter cannot be used with `accountId`.')
    groupname: str | None = Field(default=None, description="As a group's name can change, use of `groupId` is recommended to identify a group. Group name used to returns filters that are shared with a group that matches `sharePermissions.group.groupname`. This parameter cannot be used with the `groupId` parameter.")
    group_id: str | None = Field(default=None, description='Group ID used to returns filters that are shared with a group that matches `sharePermissions.group.groupId`. This parameter cannot be used with the `groupname` parameter.')
    project_id: int | None = Field(default=None, description='Project ID used to returns filters that are shared with a project that matches `sharePermissions.project.id`.')
    id: list[int] | None = Field(default=None, description='The list of filter IDs. To include multiple IDs, provide an ampersand-separated list. For example, `id=10000&id=10001`. Do not exceed 200 filter IDs.')
    order_by: Literal['description', '-description', '+description', 'favourite_count', '-favourite_count', '+favourite_count', 'id', '-id', '+id', 'is_favourite', '-is_favourite', '+is_favourite', 'name', '-name', '+name', 'owner', '-owner', '+owner', 'is_shared', '-is_shared', '+is_shared'] | None = Field(default=None, description='[Order](#ordering) the results by a field:\n\n *  `description` Sorts by filter description. Note that this sorting works independently of whether the expand to display the description field is in use.\n *  `favourite_count` Sorts by the count of how many users have this filter as a favorite.\n *  `is_favourite` Sorts by whether the filter is marked as a favorite.\n *  `id` Sorts by filter ID.\n *  `name` Sorts by filter name.\n *  `owner` Sorts by the ID of the filter owner.\n *  `is_shared` Sorts by whether the filter is shared.')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    expand: str | None = Field(default=None, description="Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `description` Returns the description of the filter.\n *  `favourite` Returns an indicator of whether the user has set the filter as a favorite.\n *  `favouritedCount` Returns a count of how many users have set this filter as a favorite.\n *  `jql` Returns the JQL query that the filter uses.\n *  `owner` Returns the owner of the filter.\n *  `searchUrl` Returns a URL to perform the filter's JQL query.\n *  `sharePermissions` Returns the share permissions defined for the filter.\n *  `editPermissions` Returns the edit permissions defined for the filter.\n *  `isWritable` Returns whether the current user has permission to edit the filter.\n *  `subscriptions` Returns the users that are subscribed to the filter.\n *  `viewUrl` Returns a URL to view the filter.")
    override_share_permissions: bool | None = Field(default=None, description='EXPERIMENTAL: Whether share permissions are overridden to enable filters with any share permissions to be returned. Available to users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).')
    model_config = ConfigDict(extra='forbid')

class GetFiltersPaginatedToolOutput(PageBeanFilterDetails):
    """Output for tool `get_filters_paginated`."""
    pass

class GetGroupToolInput(BaseModel):
    """Input for tool `get_group`."""
    groupname: str | None = Field(default=None, description="As a group's name can change, use of `groupId` is recommended to identify a group.  \nThe name of the group. This parameter cannot be used with the `groupId` parameter.")
    group_id: str | None = Field(default=None, description='The ID of the group. This parameter cannot be used with the `groupName` parameter.')
    expand: str | None = Field(default=None, description='List of fields to expand.')
    model_config = ConfigDict(extra='forbid')

class GetGroupToolOutput(Group):
    """Output for tool `get_group`."""
    pass

class GetHierarchyToolInput(BaseModel):
    """Input for tool `get_hierarchy`."""
    project_id: int = Field(..., description='The ID of the project.')
    model_config = ConfigDict(extra='forbid')

class GetHierarchyToolOutput(ProjectIssueTypeHierarchy):
    """Output for tool `get_hierarchy`."""
    pass

class GetIdsOfWorklogsDeletedSinceToolInput(BaseModel):
    """Input for tool `get_ids_of_worklogs_deleted_since`."""
    since: int | None = Field(default=None, description='The date and time, as a UNIX timestamp in milliseconds, after which deleted worklogs are returned.')
    model_config = ConfigDict(extra='forbid')

class GetIdsOfWorklogsDeletedSinceToolOutput(ChangedWorklogs):
    """Output for tool `get_ids_of_worklogs_deleted_since`."""
    pass

class GetIdsOfWorklogsModifiedSinceToolInput(BaseModel):
    """Input for tool `get_ids_of_worklogs_modified_since`."""
    since: int | None = Field(default=None, description='The date and time, as a UNIX timestamp in milliseconds, after which updated worklogs are returned.')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information about worklogs in the response. This parameter accepts `properties` that returns the properties of each worklog.')
    model_config = ConfigDict(extra='forbid')

class GetIdsOfWorklogsModifiedSinceToolOutput(ChangedWorklogs):
    """Output for tool `get_ids_of_worklogs_modified_since`."""
    pass

class GetIsWatchingIssueBulkToolInput(BaseModel):
    """Input for tool `get_is_watching_issue_bulk`."""
    body: IssueList = Field(..., description='Request body for `get_is_watching_issue_bulk`.')
    model_config = ConfigDict(extra='forbid')

class GetIsWatchingIssueBulkToolOutput(BulkIssueIsWatching):
    """Output for tool `get_is_watching_issue_bulk`."""
    pass

class GetIssueToolInput(BaseModel):
    """Input for tool `get_issue`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    fields: list[str] | None = Field(default=None, description='A list of fields to return for the issue. This parameter accepts a comma-separated list. Use it to retrieve a subset of fields. Allowed values:\n\n *  `*all` Returns all fields.\n *  `*navigable` Returns navigable fields.\n *  Any issue field, prefixed with a minus to exclude.\n\nExamples:\n\n *  `summary,comment` Returns only the summary and comments fields.\n *  `-description` Returns all (default) fields except description.\n *  `*navigable,-comment` Returns all navigable fields except comment.\n\nThis parameter may be specified multiple times. For example, `fields=field1,field2& fields=field3`.\n\nNote: All fields are returned by default. This differs from [Search for issues using JQL (GET)](#api-rest-api-3-search-get) and [Search for issues using JQL (POST)](#api-rest-api-3-search-post) where the default is all navigable fields.')
    fields_by_keys: bool | None = Field(default=None, description="Whether fields in `fields` are referenced by keys rather than IDs. This parameter is useful where fields have been added by a connect app and a field's key may differ from its ID.")
    expand: str | None = Field(default=None, description="Use [expand](#expansion) to include additional information about the issues in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `renderedFields` Returns field values rendered in HTML format.\n *  `names` Returns the display name of each field.\n *  `schema` Returns the schema describing a field type.\n *  `transitions` Returns all possible transitions for the issue.\n *  `editmeta` Returns information about how each field can be edited.\n *  `changelog` Returns a list of recent updates to an issue, sorted by date, starting from the most recent.\n *  `versionedRepresentations` Returns a JSON array for each version of a field's value, with the highest number representing the most recent version. Note: When included in the request, the `fields` parameter is ignored.")
    properties: list[str] | None = Field(default=None, description='A list of issue properties to return for the issue. This parameter accepts a comma-separated list. Allowed values:\n\n *  `*all` Returns all issue properties.\n *  Any issue property key, prefixed with a minus to exclude.\n\nExamples:\n\n *  `*all` Returns all properties.\n *  `*all,-prop1` Returns all properties except `prop1`.\n *  `prop1,prop2` Returns `prop1` and `prop2` properties.\n\nThis parameter may be specified multiple times. For example, `properties=prop1,prop2& properties=prop3`.')
    update_history: bool | None = Field(default=None, description="Whether the project in which the issue is created is added to the user's **Recently viewed** project list, as shown under **Projects** in Jira. This also populates the [JQL issues search](#api-rest-api-3-search-get) `lastViewed` field.")
    model_config = ConfigDict(extra='forbid')

class GetIssueToolOutput(IssueBean):
    """Output for tool `get_issue`."""
    pass

class GetIssueAllTypesToolInput(BaseModel):
    """Input for tool `get_issue_all_types`."""
    model_config = ConfigDict(extra='forbid')

class GetIssueAllTypesToolOutput(GetIssueAllTypesResponse):
    """Output for tool `get_issue_all_types`."""
    pass

class GetIssueFieldOptionToolInput(BaseModel):
    """Input for tool `get_issue_field_option`."""
    field_key: str = Field(..., description='The field key is specified in the following format: **$(app-key)\\_\\_$(field-key)**. For example, *example-add-on\\_\\_example-issue-field*. To determine the `fieldKey` value, do one of the following:\n\n *  open the app\'s plugin descriptor, then **app-key** is the key at the top and **field-key** is the key in the `jiraIssueFields` module. **app-key** can also be found in the app listing in the Atlassian Universal Plugin Manager.\n *  run [Get fields](#api-rest-api-3-field-get) and in the field details the value is returned in `key`. For example, `"key": "teams-add-on__team-issue-field"`')
    option_id: int = Field(..., description='The ID of the option to be returned.')
    model_config = ConfigDict(extra='forbid')

class GetIssueFieldOptionToolOutput(IssueFieldOption):
    """Output for tool `get_issue_field_option`."""
    pass

class GetIssueLinkToolInput(BaseModel):
    """Input for tool `get_issue_link`."""
    link_id: str = Field(..., description='The ID of the issue link.')
    model_config = ConfigDict(extra='forbid')

class GetIssueLinkToolOutput(IssueLink):
    """Output for tool `get_issue_link`."""
    pass

class GetIssueLinkTypeToolInput(BaseModel):
    """Input for tool `get_issue_link_type`."""
    issue_link_type_id: str = Field(..., description='The ID of the issue link type.')
    model_config = ConfigDict(extra='forbid')

class GetIssueLinkTypeToolOutput(IssueLinkType):
    """Output for tool `get_issue_link_type`."""
    pass

class GetIssueLinkTypesToolInput(BaseModel):
    """Input for tool `get_issue_link_types`."""
    model_config = ConfigDict(extra='forbid')

class GetIssueLinkTypesToolOutput(IssueLinkTypes):
    """Output for tool `get_issue_link_types`."""
    pass

class GetIssueNavigatorDefaultColumnsToolInput(BaseModel):
    """Input for tool `get_issue_navigator_default_columns`."""
    model_config = ConfigDict(extra='forbid')

class GetIssueNavigatorDefaultColumnsToolOutput(GetIssueNavigatorDefaultColumnsResponse):
    """Output for tool `get_issue_navigator_default_columns`."""
    pass

class GetIssuePickerResourceToolInput(BaseModel):
    """Input for tool `get_issue_picker_resource`."""
    query: str | None = Field(default=None, description='A string to match against text fields in the issue such as title, description, or comments.')
    current_jql: str | None = Field(default=None, description='A JQL query defining a list of issues to search for the query term. Note that `username` and `userkey` cannot be used as search terms for this parameter, due to privacy reasons. Use `accountId` instead.')
    current_issue_key: str | None = Field(default=None, description='The key of an issue to exclude from search results. For example, the issue the user is viewing when they perform this query.')
    current_project_id: str | None = Field(default=None, description='The ID of a project that suggested issues must belong to.')
    show_sub_tasks: bool | None = Field(default=None, description='Indicate whether to include subtasks in the suggestions list.')
    show_sub_task_parent: bool | None = Field(default=None, description='When `currentIssueKey` is a subtask, whether to include the parent issue in the suggestions if it matches the query.')
    model_config = ConfigDict(extra='forbid')

class GetIssuePickerResourceToolOutput(IssuePickerSuggestions):
    """Output for tool `get_issue_picker_resource`."""
    pass

class GetIssuePropertyToolInput(BaseModel):
    """Input for tool `get_issue_property`."""
    issue_id_or_key: str = Field(..., description='The key or ID of the issue.')
    property_key: str = Field(..., description='The key of the property.')
    model_config = ConfigDict(extra='forbid')

class GetIssuePropertyToolOutput(EntityProperty):
    """Output for tool `get_issue_property`."""
    pass

class GetIssuePropertyKeysToolInput(BaseModel):
    """Input for tool `get_issue_property_keys`."""
    issue_id_or_key: str = Field(..., description='The key or ID of the issue.')
    model_config = ConfigDict(extra='forbid')

class GetIssuePropertyKeysToolOutput(PropertyKeys):
    """Output for tool `get_issue_property_keys`."""
    pass

class GetIssueSecurityLevelToolInput(BaseModel):
    """Input for tool `get_issue_security_level`."""
    id: str = Field(..., description='The ID of the issue security level.')
    model_config = ConfigDict(extra='forbid')

class GetIssueSecurityLevelToolOutput(SecurityLevel):
    """Output for tool `get_issue_security_level`."""
    pass

class GetIssueSecurityLevelMembersToolInput(BaseModel):
    """Input for tool `get_issue_security_level_members`."""
    issue_security_scheme_id: int = Field(..., description='The ID of the issue security scheme. Use the [Get issue security schemes](#api-rest-api-3-issuesecurityschemes-get) operation to get a list of issue security scheme IDs.')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    issue_security_level_id: list[int] | None = Field(default=None, description='The list of issue security level IDs. To include multiple issue security levels separate IDs with ampersand: `issueSecurityLevelId=10000&issueSecurityLevelId=10001`.')
    expand: str | None = Field(default=None, description='Use expand to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `all` Returns all expandable information.\n *  `field` Returns information about the custom field granted the permission.\n *  `group` Returns information about the group that is granted the permission.\n *  `projectRole` Returns information about the project role granted the permission.\n *  `user` Returns information about the user who is granted the permission.')
    model_config = ConfigDict(extra='forbid')

class GetIssueSecurityLevelMembersToolOutput(PageBeanIssueSecurityLevelMember):
    """Output for tool `get_issue_security_level_members`."""
    pass

class GetIssueSecuritySchemeToolInput(BaseModel):
    """Input for tool `get_issue_security_scheme`."""
    id: int = Field(..., description='The ID of the issue security scheme. Use the [Get issue security schemes](#api-rest-api-3-issuesecurityschemes-get) operation to get a list of issue security scheme IDs.')
    model_config = ConfigDict(extra='forbid')

class GetIssueSecuritySchemeToolOutput(SecurityScheme):
    """Output for tool `get_issue_security_scheme`."""
    pass

class GetIssueSecuritySchemesToolInput(BaseModel):
    """Input for tool `get_issue_security_schemes`."""
    model_config = ConfigDict(extra='forbid')

class GetIssueSecuritySchemesToolOutput(SecuritySchemes):
    """Output for tool `get_issue_security_schemes`."""
    pass

class GetIssueTypeToolInput(BaseModel):
    """Input for tool `get_issue_type`."""
    id: str = Field(..., description='The ID of the issue type.')
    model_config = ConfigDict(extra='forbid')

class GetIssueTypeToolOutput(IssueTypeDetails):
    """Output for tool `get_issue_type`."""
    pass

class GetIssueTypeMappingsForContextsToolInput(BaseModel):
    """Input for tool `get_issue_type_mappings_for_contexts`."""
    field_id: str = Field(..., description='The ID of the custom field.')
    context_id: list[int] | None = Field(default=None, description='The ID of the context. To include multiple contexts, provide an ampersand-separated list. For example, `contextId=10001&contextId=10002`.')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    model_config = ConfigDict(extra='forbid')

class GetIssueTypeMappingsForContextsToolOutput(PageBeanIssueTypeToContextMapping):
    """Output for tool `get_issue_type_mappings_for_contexts`."""
    pass

class GetIssueTypePropertyToolInput(BaseModel):
    """Input for tool `get_issue_type_property`."""
    issue_type_id: str = Field(..., description='The ID of the issue type.')
    property_key: str = Field(..., description='The key of the property. Use [Get issue type property keys](#api-rest-api-3-issuetype-issueTypeId-properties-get) to get a list of all issue type property keys.')
    model_config = ConfigDict(extra='forbid')

class GetIssueTypePropertyToolOutput(EntityProperty):
    """Output for tool `get_issue_type_property`."""
    pass

class GetIssueTypePropertyKeysToolInput(BaseModel):
    """Input for tool `get_issue_type_property_keys`."""
    issue_type_id: str = Field(..., description='The ID of the issue type.')
    model_config = ConfigDict(extra='forbid')

class GetIssueTypePropertyKeysToolOutput(PropertyKeys):
    """Output for tool `get_issue_type_property_keys`."""
    pass

class GetIssueTypeSchemeForProjectsToolInput(BaseModel):
    """Input for tool `get_issue_type_scheme_for_projects`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    project_id: list[int] = Field(..., description='The list of project IDs. To include multiple project IDs, provide an ampersand-separated list. For example, `projectId=10000&projectId=10001`.')
    model_config = ConfigDict(extra='forbid')

class GetIssueTypeSchemeForProjectsToolOutput(PageBeanIssueTypeSchemeProjects):
    """Output for tool `get_issue_type_scheme_for_projects`."""
    pass

class GetIssueTypeSchemesMappingToolInput(BaseModel):
    """Input for tool `get_issue_type_schemes_mapping`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    issue_type_scheme_id: list[int] | None = Field(default=None, description='The list of issue type scheme IDs. To include multiple IDs, provide an ampersand-separated list. For example, `issueTypeSchemeId=10000&issueTypeSchemeId=10001`.')
    model_config = ConfigDict(extra='forbid')

class GetIssueTypeSchemesMappingToolOutput(PageBeanIssueTypeSchemeMapping):
    """Output for tool `get_issue_type_schemes_mapping`."""
    pass

class GetIssueTypeScreenSchemeMappingsToolInput(BaseModel):
    """Input for tool `get_issue_type_screen_scheme_mappings`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    issue_type_screen_scheme_id: list[int] | None = Field(default=None, description='The list of issue type screen scheme IDs. To include multiple issue type screen schemes, separate IDs with ampersand: `issueTypeScreenSchemeId=10000&issueTypeScreenSchemeId=10001`.')
    model_config = ConfigDict(extra='forbid')

class GetIssueTypeScreenSchemeMappingsToolOutput(PageBeanIssueTypeScreenSchemeItem):
    """Output for tool `get_issue_type_screen_scheme_mappings`."""
    pass

class GetIssueTypeScreenSchemeProjectAssociationsToolInput(BaseModel):
    """Input for tool `get_issue_type_screen_scheme_project_associations`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    project_id: list[int] = Field(..., description='The list of project IDs. To include multiple projects, separate IDs with ampersand: `projectId=10000&projectId=10001`.')
    model_config = ConfigDict(extra='forbid')

class GetIssueTypeScreenSchemeProjectAssociationsToolOutput(PageBeanIssueTypeScreenSchemesProjects):
    """Output for tool `get_issue_type_screen_scheme_project_associations`."""
    pass

class GetIssueTypeScreenSchemesToolInput(BaseModel):
    """Input for tool `get_issue_type_screen_schemes`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    id: list[int] | None = Field(default=None, description='The list of issue type screen scheme IDs. To include multiple IDs, provide an ampersand-separated list. For example, `id=10000&id=10001`.')
    query_string: str | None = Field(default=None, description='String used to perform a case-insensitive partial match with issue type screen scheme name.')
    order_by: Literal['name', '-name', '+name', 'id', '-id', '+id'] | None = Field(default=None, description='[Order](#ordering) the results by a field:\n\n *  `name` Sorts by issue type screen scheme name.\n *  `id` Sorts by issue type screen scheme ID.')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information in the response. This parameter accepts `projects` that, for each issue type screen schemes, returns information about the projects the issue type screen scheme is assigned to.')
    model_config = ConfigDict(extra='forbid')

class GetIssueTypeScreenSchemesToolOutput(PageBeanIssueTypeScreenScheme):
    """Output for tool `get_issue_type_screen_schemes`."""
    pass

class GetIssueTypesForProjectToolInput(BaseModel):
    """Input for tool `get_issue_types_for_project`."""
    project_id: int = Field(..., description='The ID of the project.')
    level: int | None = Field(default=None, description='The level of the issue type to filter by. Use:\n\n *  `-1` for Subtask.\n *  `0` for Base.\n *  `1` for Epic.')
    model_config = ConfigDict(extra='forbid')

class GetIssueTypesForProjectToolOutput(GetIssueTypesForProjectResponse):
    """Output for tool `get_issue_types_for_project`."""
    pass

class GetIssueWatchersToolInput(BaseModel):
    """Input for tool `get_issue_watchers`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    model_config = ConfigDict(extra='forbid')

class GetIssueWatchersToolOutput(Watchers):
    """Output for tool `get_issue_watchers`."""
    pass

class GetIssueWorklogToolInput(BaseModel):
    """Input for tool `get_issue_worklog`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    started_after: int | None = Field(default=None, description='The worklog start date and time, as a UNIX timestamp in milliseconds, after which worklogs are returned.')
    started_before: int | None = Field(default=None, description='The worklog start date and time, as a UNIX timestamp in milliseconds, before which worklogs are returned.')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information about worklogs in the response. This parameter accepts`properties`, which returns worklog properties.')
    model_config = ConfigDict(extra='forbid')

class GetIssueWorklogToolOutput(PageOfWorklogs):
    """Output for tool `get_issue_worklog`."""
    pass

class GetLicenseToolInput(BaseModel):
    """Input for tool `get_license`."""
    model_config = ConfigDict(extra='forbid')

class GetLicenseToolOutput(License):
    """Output for tool `get_license`."""
    pass

class GetLocaleToolInput(BaseModel):
    """Input for tool `get_locale`."""
    model_config = ConfigDict(extra='forbid')

class GetLocaleToolOutput(Locale):
    """Output for tool `get_locale`."""
    pass

class GetMyFiltersToolInput(BaseModel):
    """Input for tool `get_my_filters`."""
    expand: str | None = Field(default=None, description="Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `sharedUsers` Returns the users that the filter is shared with. This includes users that can browse projects that the filter is shared with. If you don't specify `sharedUsers`, then the `sharedUsers` object is returned but it doesn't list any users. The list of users returned is limited to 1000, to access additional users append `[start-index:end-index]` to the expand request. For example, to access the next 1000 users, use `?expand=sharedUsers[1001:2000]`.\n *  `subscriptions` Returns the users that are subscribed to the filter. If you don't specify `subscriptions`, the `subscriptions` object is returned but it doesn't list any subscriptions. The list of subscriptions returned is limited to 1000, to access additional subscriptions append `[start-index:end-index]` to the expand request. For example, to access the next 1000 subscriptions, use `?expand=subscriptions[1001:2000]`.")
    include_favourites: bool | None = Field(default=None, description="Include the user's favorite filters in the response.")
    model_config = ConfigDict(extra='forbid')

class GetMyFiltersToolOutput(GetMyFiltersResponse):
    """Output for tool `get_my_filters`."""
    pass

class GetMyPermissionsToolInput(BaseModel):
    """Input for tool `get_my_permissions`."""
    project_key: str | None = Field(default=None, description='The key of project. Ignored if `projectId` is provided.')
    project_id: str | None = Field(default=None, description='The ID of project.')
    issue_key: str | None = Field(default=None, description='The key of the issue. Ignored if `issueId` is provided.')
    issue_id: str | None = Field(default=None, description='The ID of the issue.')
    permissions: str | None = Field(default=None, description='A list of permission keys. (Required) This parameter accepts a comma-separated list. To get the list of available permissions, use [Get all permissions](#api-rest-api-3-permissions-get).')
    project_uuid: str | None = None
    project_configuration_uuid: str | None = None
    comment_id: str | None = Field(default=None, description='The ID of the comment.')
    model_config = ConfigDict(extra='forbid')

class GetMyPermissionsToolOutput(Permissions):
    """Output for tool `get_my_permissions`."""
    pass

class GetNotificationSchemeToolInput(BaseModel):
    """Input for tool `get_notification_scheme`."""
    id: int = Field(..., description='The ID of the notification scheme. Use [Get notification schemes paginated](#api-rest-api-3-notificationscheme-get) to get a list of notification scheme IDs.')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `all` Returns all expandable information\n *  `field` Returns information about any custom fields assigned to receive an event\n *  `group` Returns information about any groups assigned to receive an event\n *  `notificationSchemeEvents` Returns a list of event associations. This list is returned for all expandable information\n *  `projectRole` Returns information about any project roles assigned to receive an event\n *  `user` Returns information about any users assigned to receive an event')
    model_config = ConfigDict(extra='forbid')

class GetNotificationSchemeToolOutput(NotificationScheme):
    """Output for tool `get_notification_scheme`."""
    pass

class GetNotificationSchemeForProjectToolInput(BaseModel):
    """Input for tool `get_notification_scheme_for_project`."""
    project_key_or_id: str = Field(..., description='The project ID or project key (case sensitive).')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `all` Returns all expandable information\n *  `field` Returns information about any custom fields assigned to receive an event\n *  `group` Returns information about any groups assigned to receive an event\n *  `notificationSchemeEvents` Returns a list of event associations. This list is returned for all expandable information\n *  `projectRole` Returns information about any project roles assigned to receive an event\n *  `user` Returns information about any users assigned to receive an event')
    model_config = ConfigDict(extra='forbid')

class GetNotificationSchemeForProjectToolOutput(NotificationScheme):
    """Output for tool `get_notification_scheme_for_project`."""
    pass

class GetNotificationSchemeToProjectMappingsToolInput(BaseModel):
    """Input for tool `get_notification_scheme_to_project_mappings`."""
    start_at: str | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: str | None = Field(default=None, description='The maximum number of items to return per page.')
    notification_scheme_id: list[str] | None = Field(default=None, description='The list of notifications scheme IDs to be filtered out')
    project_id: list[str] | None = Field(default=None, description='The list of project IDs to be filtered out')
    model_config = ConfigDict(extra='forbid')

class GetNotificationSchemeToProjectMappingsToolOutput(PageBeanNotificationSchemeAndProjectMappingJsonBean):
    """Output for tool `get_notification_scheme_to_project_mappings`."""
    pass

class GetNotificationSchemesToolInput(BaseModel):
    """Input for tool `get_notification_schemes`."""
    start_at: str | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: str | None = Field(default=None, description='The maximum number of items to return per page.')
    id: list[str] | None = Field(default=None, description='The list of notification schemes IDs to be filtered by')
    project_id: list[str] | None = Field(default=None, description='The list of projects IDs to be filtered by')
    only_default: bool | None = Field(default=None, description='When set to true, returns only the default notification scheme. If you provide project IDs not associated with the default, returns an empty page. The default value is false.')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `all` Returns all expandable information\n *  `field` Returns information about any custom fields assigned to receive an event\n *  `group` Returns information about any groups assigned to receive an event\n *  `notificationSchemeEvents` Returns a list of event associations. This list is returned for all expandable information\n *  `projectRole` Returns information about any project roles assigned to receive an event\n *  `user` Returns information about any users assigned to receive an event')
    model_config = ConfigDict(extra='forbid')

class GetNotificationSchemesToolOutput(PageBeanNotificationScheme):
    """Output for tool `get_notification_schemes`."""
    pass

class GetOptionsForContextToolInput(BaseModel):
    """Input for tool `get_options_for_context`."""
    field_id: str = Field(..., description='The ID of the custom field.')
    context_id: int = Field(..., description='The ID of the context.')
    option_id: int | None = Field(default=None, description='The ID of the option.')
    only_options: bool | None = Field(default=None, description='Whether only options are returned.')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    model_config = ConfigDict(extra='forbid')

class GetOptionsForContextToolOutput(PageBeanCustomFieldContextOption):
    """Output for tool `get_options_for_context`."""
    pass

class GetPermissionSchemeToolInput(BaseModel):
    """Input for tool `get_permission_scheme`."""
    scheme_id: int = Field(..., description='The ID of the permission scheme to return.')
    expand: str | None = Field(default=None, description='Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are included when you specify any value. Expand options include:\n\n *  `all` Returns all expandable information.\n *  `field` Returns information about the custom field granted the permission.\n *  `group` Returns information about the group that is granted the permission.\n *  `permissions` Returns all permission grants for each permission scheme.\n *  `projectRole` Returns information about the project role granted the permission.\n *  `user` Returns information about the user who is granted the permission.')
    model_config = ConfigDict(extra='forbid')

class GetPermissionSchemeToolOutput(PermissionScheme):
    """Output for tool `get_permission_scheme`."""
    pass

class GetPermissionSchemeGrantToolInput(BaseModel):
    """Input for tool `get_permission_scheme_grant`."""
    scheme_id: int = Field(..., description='The ID of the permission scheme.')
    permission_id: int = Field(..., description='The ID of the permission grant.')
    expand: str | None = Field(default=None, description='Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are always included when you specify any value. Expand options include:\n\n *  `all` Returns all expandable information.\n *  `field` Returns information about the custom field granted the permission.\n *  `group` Returns information about the group that is granted the permission.\n *  `permissions` Returns all permission grants for each permission scheme.\n *  `projectRole` Returns information about the project role granted the permission.\n *  `user` Returns information about the user who is granted the permission.')
    model_config = ConfigDict(extra='forbid')

class GetPermissionSchemeGrantToolOutput(PermissionGrant):
    """Output for tool `get_permission_scheme_grant`."""
    pass

class GetPermissionSchemeGrantsToolInput(BaseModel):
    """Input for tool `get_permission_scheme_grants`."""
    scheme_id: int = Field(..., description='The ID of the permission scheme.')
    expand: str | None = Field(default=None, description='Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are always included when you specify any value. Expand options include:\n\n *  `permissions` Returns all permission grants for each permission scheme.\n *  `user` Returns information about the user who is granted the permission.\n *  `group` Returns information about the group that is granted the permission.\n *  `projectRole` Returns information about the project role granted the permission.\n *  `field` Returns information about the custom field granted the permission.\n *  `all` Returns all expandable information.')
    model_config = ConfigDict(extra='forbid')

class GetPermissionSchemeGrantsToolOutput(PermissionGrants):
    """Output for tool `get_permission_scheme_grants`."""
    pass

class GetPermittedProjectsToolInput(BaseModel):
    """Input for tool `get_permitted_projects`."""
    body: PermissionsKeysBean = Field(..., description='Request body for `get_permitted_projects`.')
    model_config = ConfigDict(extra='forbid')

class GetPermittedProjectsToolOutput(PermittedProjects):
    """Output for tool `get_permitted_projects`."""
    pass

class GetPrecomputationsToolInput(BaseModel):
    """Input for tool `get_precomputations`."""
    function_key: list[str] | None = None
    start_at: int | None = None
    max_results: int | None = None
    order_by: str | None = None
    filter: str | None = None
    model_config = ConfigDict(extra='forbid')

class GetPrecomputationsToolOutput(PageBeanJqlFunctionPrecomputationBean):
    """Output for tool `get_precomputations`."""
    pass

class GetPreferenceToolInput(BaseModel):
    """Input for tool `get_preference`."""
    model_config = ConfigDict(extra='forbid')

class GetPreferenceToolOutput(RootModel[str]):
    """Output for tool `get_preference`."""
    pass

class GetPrioritiesToolInput(BaseModel):
    """Input for tool `get_priorities`."""
    model_config = ConfigDict(extra='forbid')

class GetPrioritiesToolOutput(GetPrioritiesResponse):
    """Output for tool `get_priorities`."""
    pass

class GetPriorityToolInput(BaseModel):
    """Input for tool `get_priority`."""
    id: str = Field(..., description='The ID of the issue priority.')
    model_config = ConfigDict(extra='forbid')

class GetPriorityToolOutput(Priority):
    """Output for tool `get_priority`."""
    pass

class GetProjectToolInput(BaseModel):
    """Input for tool `get_project`."""
    project_id_or_key: str = Field(..., description='The project ID or project key (case sensitive).')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Note that the project description, issue types, and project lead are included in all responses by default. Expand options include:\n\n *  `description` The project description.\n *  `issueTypes` The issue types associated with the project.\n *  `lead` The project lead.\n *  `projectKeys` All project keys associated with the project.\n *  `issueTypeHierarchy` The project issue type hierarchy.')
    properties: list[str] | None = Field(default=None, description='A list of project properties to return for the project. This parameter accepts a comma-separated list.')
    model_config = ConfigDict(extra='forbid')

class GetProjectToolOutput(Project):
    """Output for tool `get_project`."""
    pass

class GetProjectCategoryByIdToolInput(BaseModel):
    """Input for tool `get_project_category_by_id`."""
    id: int = Field(..., description='The ID of the project category.')
    model_config = ConfigDict(extra='forbid')

class GetProjectCategoryByIdToolOutput(ProjectCategory):
    """Output for tool `get_project_category_by_id`."""
    pass

class GetProjectComponentsToolInput(BaseModel):
    """Input for tool `get_project_components`."""
    project_id_or_key: str = Field(..., description='The project ID or project key (case sensitive).')
    model_config = ConfigDict(extra='forbid')

class GetProjectComponentsToolOutput(GetProjectComponentsResponse):
    """Output for tool `get_project_components`."""
    pass

class GetProjectComponentsPaginatedToolInput(BaseModel):
    """Input for tool `get_project_components_paginated`."""
    project_id_or_key: str = Field(..., description='The project ID or project key (case sensitive).')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    order_by: Literal['description', '-description', '+description', 'issueCount', '-issueCount', '+issueCount', 'lead', '-lead', '+lead', 'name', '-name', '+name'] | None = Field(default=None, description="[Order](#ordering) the results by a field:\n\n *  `description` Sorts by the component description.\n *  `issueCount` Sorts by the count of issues associated with the component.\n *  `lead` Sorts by the user key of the component's project lead.\n *  `name` Sorts by component name.")
    query: str | None = Field(default=None, description='Filter the results using a literal string. Components with a matching `name` or `description` are returned (case insensitive).')
    model_config = ConfigDict(extra='forbid')

class GetProjectComponentsPaginatedToolOutput(PageBeanComponentWithIssueCount):
    """Output for tool `get_project_components_paginated`."""
    pass

class GetProjectContextMappingToolInput(BaseModel):
    """Input for tool `get_project_context_mapping`."""
    field_id: str = Field(..., description='The ID of the custom field, for example `customfield\\_10000`.')
    context_id: list[int] | None = Field(default=None, description='The list of context IDs. To include multiple context, separate IDs with ampersand: `contextId=10000&contextId=10001`.')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    model_config = ConfigDict(extra='forbid')

class GetProjectContextMappingToolOutput(PageBeanCustomFieldContextProjectMapping):
    """Output for tool `get_project_context_mapping`."""
    pass

class GetProjectEmailToolInput(BaseModel):
    """Input for tool `get_project_email`."""
    project_id: int = Field(..., description='The project ID.')
    model_config = ConfigDict(extra='forbid')

class GetProjectEmailToolOutput(ProjectEmailAddress):
    """Output for tool `get_project_email`."""
    pass

class GetProjectIssueSecuritySchemeToolInput(BaseModel):
    """Input for tool `get_project_issue_security_scheme`."""
    project_key_or_id: str = Field(..., description='The project ID or project key (case sensitive).')
    model_config = ConfigDict(extra='forbid')

class GetProjectIssueSecuritySchemeToolOutput(SecurityScheme):
    """Output for tool `get_project_issue_security_scheme`."""
    pass

class GetProjectPropertyToolInput(BaseModel):
    """Input for tool `get_project_property`."""
    project_id_or_key: str = Field(..., description='The project ID or project key (case sensitive).')
    property_key: str = Field(..., description='The project property key. Use [Get project property keys](#api-rest-api-3-project-projectIdOrKey-properties-get) to get a list of all project property keys.')
    model_config = ConfigDict(extra='forbid')

class GetProjectPropertyToolOutput(EntityProperty):
    """Output for tool `get_project_property`."""
    pass

class GetProjectPropertyKeysToolInput(BaseModel):
    """Input for tool `get_project_property_keys`."""
    project_id_or_key: str = Field(..., description='The project ID or project key (case sensitive).')
    model_config = ConfigDict(extra='forbid')

class GetProjectPropertyKeysToolOutput(PropertyKeys):
    """Output for tool `get_project_property_keys`."""
    pass

class GetProjectRoleToolInput(BaseModel):
    """Input for tool `get_project_role`."""
    project_id_or_key: str = Field(..., description='The project ID or project key (case sensitive).')
    id: int = Field(..., description='The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.')
    exclude_inactive_users: bool | None = Field(default=None, description='Exclude inactive users.')
    model_config = ConfigDict(extra='forbid')

class GetProjectRoleToolOutput(ProjectRole):
    """Output for tool `get_project_role`."""
    pass

class GetProjectRoleActorsForRoleToolInput(BaseModel):
    """Input for tool `get_project_role_actors_for_role`."""
    id: int = Field(..., description='The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.')
    model_config = ConfigDict(extra='forbid')

class GetProjectRoleActorsForRoleToolOutput(ProjectRole):
    """Output for tool `get_project_role_actors_for_role`."""
    pass

class GetProjectRoleByIdToolInput(BaseModel):
    """Input for tool `get_project_role_by_id`."""
    id: int = Field(..., description='The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.')
    model_config = ConfigDict(extra='forbid')

class GetProjectRoleByIdToolOutput(ProjectRole):
    """Output for tool `get_project_role_by_id`."""
    pass

class GetProjectRoleDetailsToolInput(BaseModel):
    """Input for tool `get_project_role_details`."""
    project_id_or_key: str = Field(..., description='The project ID or project key (case sensitive).')
    current_member: bool | None = Field(default=None, description='Whether the roles should be filtered to include only those the user is assigned to.')
    exclude_connect_addons: bool | None = None
    model_config = ConfigDict(extra='forbid')

class GetProjectRoleDetailsToolOutput(GetProjectRoleDetailsResponse):
    """Output for tool `get_project_role_details`."""
    pass

class GetProjectRolesToolInput(BaseModel):
    """Input for tool `get_project_roles`."""
    project_id_or_key: str = Field(..., description='The project ID or project key (case sensitive).')
    model_config = ConfigDict(extra='forbid')

class GetProjectRolesToolOutput(GetProjectRolesResponse):
    """Output for tool `get_project_roles`."""
    pass

class GetProjectTypeByKeyToolInput(BaseModel):
    """Input for tool `get_project_type_by_key`."""
    project_type_key: Literal['software', 'service_desk', 'business', 'product_discovery'] = Field(..., description='The key of the project type.')
    model_config = ConfigDict(extra='forbid')

class GetProjectTypeByKeyToolOutput(ProjectType):
    """Output for tool `get_project_type_by_key`."""
    pass

class GetProjectVersionsToolInput(BaseModel):
    """Input for tool `get_project_versions`."""
    project_id_or_key: str = Field(..., description='The project ID or project key (case sensitive).')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information in the response. This parameter accepts `operations`, which returns actions that can be performed on the version.')
    model_config = ConfigDict(extra='forbid')

class GetProjectVersionsToolOutput(GetProjectVersionsResponse):
    """Output for tool `get_project_versions`."""
    pass

class GetProjectVersionsPaginatedToolInput(BaseModel):
    """Input for tool `get_project_versions_paginated`."""
    project_id_or_key: str = Field(..., description='The project ID or project key (case sensitive).')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    order_by: Literal['description', '-description', '+description', 'name', '-name', '+name', 'releaseDate', '-releaseDate', '+releaseDate', 'sequence', '-sequence', '+sequence', 'startDate', '-startDate', '+startDate'] | None = Field(default=None, description='[Order](#ordering) the results by a field:\n\n *  `description` Sorts by version description.\n *  `name` Sorts by version name.\n *  `releaseDate` Sorts by release date, starting with the oldest date. Versions with no release date are listed last.\n *  `sequence` Sorts by the order of appearance in the user interface.\n *  `startDate` Sorts by start date, starting with the oldest date. Versions with no start date are listed last.')
    query: str | None = Field(default=None, description='Filter the results using a literal string. Versions with matching `name` or `description` are returned (case insensitive).')
    status: str | None = Field(default=None, description='A list of status values used to filter the results by version status. This parameter accepts a comma-separated list. The status values are `released`, `unreleased`, and `archived`.')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `issuesstatus` Returns the number of issues in each status category for each version.\n *  `operations` Returns actions that can be performed on the specified version.')
    model_config = ConfigDict(extra='forbid')

class GetProjectVersionsPaginatedToolOutput(PageBeanVersion):
    """Output for tool `get_project_versions_paginated`."""
    pass

class GetProjectsForIssueTypeScreenSchemeToolInput(BaseModel):
    """Input for tool `get_projects_for_issue_type_screen_scheme`."""
    issue_type_screen_scheme_id: int = Field(..., description='The ID of the issue type screen scheme.')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    query: str | None = None
    model_config = ConfigDict(extra='forbid')

class GetProjectsForIssueTypeScreenSchemeToolOutput(PageBeanProjectDetails):
    """Output for tool `get_projects_for_issue_type_screen_scheme`."""
    pass

class GetRecentToolInput(BaseModel):
    """Input for tool `get_recent`."""
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expanded options include:\n\n *  `description` Returns the project description.\n *  `projectKeys` Returns all project keys associated with a project.\n *  `lead` Returns information about the project lead.\n *  `issueTypes` Returns all issue types associated with the project.\n *  `url` Returns the URL associated with the project.\n *  `permissions` Returns the permissions associated with the project.\n *  `insight` EXPERIMENTAL. Returns the insight details of total issue count and last issue update time for the project.\n *  `*` Returns the project with all available expand options.')
    properties: list[dict[str, object]] | None = Field(default=None, description='EXPERIMENTAL. A list of project properties to return for the project. This parameter accepts a comma-separated list. Invalid property names are ignored.')
    model_config = ConfigDict(extra='forbid')

class GetRecentToolOutput(GetRecentResponse):
    """Output for tool `get_recent`."""
    pass

class GetRemoteIssueLinkByIdToolInput(BaseModel):
    """Input for tool `get_remote_issue_link_by_id`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    link_id: str = Field(..., description='The ID of the remote issue link.')
    model_config = ConfigDict(extra='forbid')

class GetRemoteIssueLinkByIdToolOutput(RemoteIssueLink):
    """Output for tool `get_remote_issue_link_by_id`."""
    pass

class GetRemoteIssueLinksToolInput(BaseModel):
    """Input for tool `get_remote_issue_links`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    global_id: str | None = Field(default=None, description='The global ID of the remote issue link.')
    model_config = ConfigDict(extra='forbid')

class GetRemoteIssueLinksToolOutput(RemoteIssueLink):
    """Output for tool `get_remote_issue_links`."""
    pass

class GetResolutionToolInput(BaseModel):
    """Input for tool `get_resolution`."""
    id: str = Field(..., description='The ID of the issue resolution value.')
    model_config = ConfigDict(extra='forbid')

class GetResolutionToolOutput(Resolution):
    """Output for tool `get_resolution`."""
    pass

class GetResolutionsToolInput(BaseModel):
    """Input for tool `get_resolutions`."""
    model_config = ConfigDict(extra='forbid')

class GetResolutionsToolOutput(GetResolutionsResponse):
    """Output for tool `get_resolutions`."""
    pass

class GetScreenSchemesToolInput(BaseModel):
    """Input for tool `get_screen_schemes`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    id: list[int] | None = Field(default=None, description='The list of screen scheme IDs. To include multiple IDs, provide an ampersand-separated list. For example, `id=10000&id=10001`.')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) include additional information in the response. This parameter accepts `issueTypeScreenSchemes` that, for each screen schemes, returns information about the issue type screen scheme the screen scheme is assigned to.')
    query_string: str | None = Field(default=None, description='String used to perform a case-insensitive partial match with screen scheme name.')
    order_by: Literal['name', '-name', '+name', 'id', '-id', '+id'] | None = Field(default=None, description='[Order](#ordering) the results by a field:\n\n *  `id` Sorts by screen scheme ID.\n *  `name` Sorts by screen scheme name.')
    model_config = ConfigDict(extra='forbid')

class GetScreenSchemesToolOutput(PageBeanScreenScheme):
    """Output for tool `get_screen_schemes`."""
    pass

class GetScreensToolInput(BaseModel):
    """Input for tool `get_screens`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    id: list[int] | None = Field(default=None, description='The list of screen IDs. To include multiple IDs, provide an ampersand-separated list. For example, `id=10000&id=10001`.')
    query_string: str | None = Field(default=None, description='String used to perform a case-insensitive partial match with screen name.')
    scope: list[Literal['GLOBAL', 'TEMPLATE', 'PROJECT']] | None = Field(default=None, description='The scope filter string. To filter by multiple scope, provide an ampersand-separated list. For example, `scope=GLOBAL&scope=PROJECT`.')
    order_by: Literal['name', '-name', '+name', 'id', '-id', '+id'] | None = Field(default=None, description='[Order](#ordering) the results by a field:\n\n *  `id` Sorts by screen ID.\n *  `name` Sorts by screen name.')
    model_config = ConfigDict(extra='forbid')

class GetScreensToolOutput(PageBeanScreen):
    """Output for tool `get_screens`."""
    pass

class GetScreensForFieldToolInput(BaseModel):
    """Input for tool `get_screens_for_field`."""
    field_id: str = Field(..., description='The ID of the field to return screens for.')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information about screens in the response. This parameter accepts `tab` which returns details about the screen tabs the field is used in.')
    model_config = ConfigDict(extra='forbid')

class GetScreensForFieldToolOutput(PageBeanScreenWithTab):
    """Output for tool `get_screens_for_field`."""
    pass

class GetSecurityLevelsForProjectToolInput(BaseModel):
    """Input for tool `get_security_levels_for_project`."""
    project_key_or_id: str = Field(..., description='The project ID or project key (case sensitive).')
    model_config = ConfigDict(extra='forbid')

class GetSecurityLevelsForProjectToolOutput(ProjectIssueSecurityLevels):
    """Output for tool `get_security_levels_for_project`."""
    pass

class GetSelectableIssueFieldOptionsToolInput(BaseModel):
    """Input for tool `get_selectable_issue_field_options`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    project_id: int | None = Field(default=None, description='Filters the results to options that are only available in the specified project.')
    field_key: str = Field(..., description='The field key is specified in the following format: **$(app-key)\\_\\_$(field-key)**. For example, *example-add-on\\_\\_example-issue-field*. To determine the `fieldKey` value, do one of the following:\n\n *  open the app\'s plugin descriptor, then **app-key** is the key at the top and **field-key** is the key in the `jiraIssueFields` module. **app-key** can also be found in the app listing in the Atlassian Universal Plugin Manager.\n *  run [Get fields](#api-rest-api-3-field-get) and in the field details the value is returned in `key`. For example, `"key": "teams-add-on__team-issue-field"`')
    model_config = ConfigDict(extra='forbid')

class GetSelectableIssueFieldOptionsToolOutput(PageBeanIssueFieldOption):
    """Output for tool `get_selectable_issue_field_options`."""
    pass

class GetSelectedTimeTrackingImplementationToolInput(BaseModel):
    """Input for tool `get_selected_time_tracking_implementation`."""
    model_config = ConfigDict(extra='forbid')

class GetSelectedTimeTrackingImplementationToolOutput(TimeTrackingProvider):
    """Output for tool `get_selected_time_tracking_implementation`."""
    pass

class GetServerInfoToolInput(BaseModel):
    """Input for tool `get_server_info`."""
    model_config = ConfigDict(extra='forbid')

class GetServerInfoToolOutput(ServerInformation):
    """Output for tool `get_server_info`."""
    pass

class GetSharePermissionToolInput(BaseModel):
    """Input for tool `get_share_permission`."""
    id: int = Field(..., description='The ID of the filter.')
    permission_id: int = Field(..., description='The ID of the share permission.')
    model_config = ConfigDict(extra='forbid')

class GetSharePermissionToolOutput(SharePermission):
    """Output for tool `get_share_permission`."""
    pass

class GetSharePermissionsToolInput(BaseModel):
    """Input for tool `get_share_permissions`."""
    id: int = Field(..., description='The ID of the filter.')
    model_config = ConfigDict(extra='forbid')

class GetSharePermissionsToolOutput(GetSharePermissionsResponse):
    """Output for tool `get_share_permissions`."""
    pass

class GetSharedTimeTrackingConfigurationToolInput(BaseModel):
    """Input for tool `get_shared_time_tracking_configuration`."""
    model_config = ConfigDict(extra='forbid')

class GetSharedTimeTrackingConfigurationToolOutput(TimeTrackingConfiguration):
    """Output for tool `get_shared_time_tracking_configuration`."""
    pass

class GetStatusToolInput(BaseModel):
    """Input for tool `get_status`."""
    id_or_name: str = Field(..., description='The ID or name of the status.')
    model_config = ConfigDict(extra='forbid')

class GetStatusToolOutput(StatusDetails):
    """Output for tool `get_status`."""
    pass

class GetStatusCategoriesToolInput(BaseModel):
    """Input for tool `get_status_categories`."""
    model_config = ConfigDict(extra='forbid')

class GetStatusCategoriesToolOutput(GetStatusCategoriesResponse):
    """Output for tool `get_status_categories`."""
    pass

class GetStatusCategoryToolInput(BaseModel):
    """Input for tool `get_status_category`."""
    id_or_key: str = Field(..., description='The ID or key of the status category.')
    model_config = ConfigDict(extra='forbid')

class GetStatusCategoryToolOutput(RootModel[StatusCategory]):
    """Output for tool `get_status_category`."""
    pass

class GetStatusesToolInput(BaseModel):
    """Input for tool `get_statuses`."""
    model_config = ConfigDict(extra='forbid')

class GetStatusesToolOutput(GetStatusesResponse):
    """Output for tool `get_statuses`."""
    pass

class GetStatusesByIdToolInput(BaseModel):
    """Input for tool `get_statuses_by_id`."""
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `usages` Returns the project and issue types that use the status in their workflow.')
    id: list[str] | None = Field(default=None, description='The list of status IDs. To include multiple IDs, provide an ampersand-separated list. For example, id=10000&id=10001.\n\nMin items `1`, Max items `50`')
    model_config = ConfigDict(extra='forbid')

class GetStatusesByIdToolOutput(GetStatusesByIdResponse):
    """Output for tool `get_statuses_by_id`."""
    pass

class GetTaskToolInput(BaseModel):
    """Input for tool `get_task`."""
    task_id: str = Field(..., description='The ID of the task.')
    model_config = ConfigDict(extra='forbid')

class GetTaskToolOutput(TaskProgressBeanObject):
    """Output for tool `get_task`."""
    pass

class GetTransitionsToolInput(BaseModel):
    """Input for tool `get_transitions`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information about transitions in the response. This parameter accepts `transitions.fields`, which returns information about the fields in the transition screen for each transition. Fields hidden from the screen are not returned. Use this information to populate the `fields` and `update` fields in [Transition issue](#api-rest-api-3-issue-issueIdOrKey-transitions-post).')
    transition_id: str | None = Field(default=None, description='The ID of the transition.')
    skip_remote_only_condition: bool | None = Field(default=None, description='Whether transitions with the condition *Hide From User Condition* are included in the response.')
    include_unavailable_transitions: bool | None = Field(default=None, description='Whether details of transitions that fail a condition are included in the response')
    sort_by_ops_bar_and_status: bool | None = Field(default=None, description='Whether the transitions are sorted by ops-bar sequence value first then category order (Todo, In Progress, Done) or only by ops-bar sequence value.')
    model_config = ConfigDict(extra='forbid')

class GetTransitionsToolOutput(Transitions):
    """Output for tool `get_transitions`."""
    pass

class GetTrashedFieldsPaginatedToolInput(BaseModel):
    """Input for tool `get_trashed_fields_paginated`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    id: list[str] | None = None
    query: str | None = Field(default=None, description='String used to perform a case-insensitive partial match with field names or descriptions.')
    expand: Literal['name', '-name', '+name', 'trashDate', '-trashDate', '+trashDate', 'plannedDeletionDate', '-plannedDeletionDate', '+plannedDeletionDate', 'projectsCount', '-projectsCount', '+projectsCount'] | None = None
    order_by: str | None = Field(default=None, description='[Order](#ordering) the results by a field:\n\n *  `name` sorts by the field name\n *  `trashDate` sorts by the date the field was moved to the trash\n *  `plannedDeletionDate` sorts by the planned deletion date')
    model_config = ConfigDict(extra='forbid')

class GetTrashedFieldsPaginatedToolOutput(PageBeanField):
    """Output for tool `get_trashed_fields_paginated`."""
    pass

class GetUiModificationsToolInput(BaseModel):
    """Input for tool `get_ui_modifications`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    expand: str | None = Field(default=None, description='Use expand to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `data` Returns UI modification data.\n *  `contexts` Returns UI modification contexts.')
    model_config = ConfigDict(extra='forbid')

class GetUiModificationsToolOutput(PageBeanUiModificationDetails):
    """Output for tool `get_ui_modifications`."""
    pass

class GetUserToolInput(BaseModel):
    """Input for tool `get_user`."""
    account_id: str | None = Field(default=None, description='The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*. Required.')
    username: str | None = Field(default=None, description='This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide) for details.')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information about users in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `groups` includes all groups and nested groups to which the user belongs.\n *  `applicationRoles` includes details of all the applications to which the user has access.')
    model_config = ConfigDict(extra='forbid')

class GetUserToolOutput(User):
    """Output for tool `get_user`."""
    pass

class GetUserDefaultColumnsToolInput(BaseModel):
    """Input for tool `get_user_default_columns`."""
    account_id: str | None = Field(default=None, description='The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.')
    username: str | None = Field(default=None, description='This parameter is no longer available See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.')
    model_config = ConfigDict(extra='forbid')

class GetUserDefaultColumnsToolOutput(GetUserDefaultColumnsResponse):
    """Output for tool `get_user_default_columns`."""
    pass

class GetUserEmailToolInput(BaseModel):
    """Input for tool `get_user_email`."""
    account_id: str = Field(..., description='The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, `5b10ac8d82e05b22cc7d4ef5`.')
    model_config = ConfigDict(extra='forbid')

class GetUserEmailToolOutput(UnrestrictedUserEmail):
    """Output for tool `get_user_email`."""
    pass

class GetUserEmailBulkToolInput(BaseModel):
    """Input for tool `get_user_email_bulk`."""
    account_id: list[str] = Field(..., description='The account IDs of the users for which emails are required. An `accountId` is an identifier that uniquely identifies the user across all Atlassian products. For example, `5b10ac8d82e05b22cc7d4ef5`. Note, this should be treated as an opaque identifier (that is, do not assume any structure in the value).')
    model_config = ConfigDict(extra='forbid')

class GetUserEmailBulkToolOutput(UnrestrictedUserEmail):
    """Output for tool `get_user_email_bulk`."""
    pass

class GetUserGroupsToolInput(BaseModel):
    """Input for tool `get_user_groups`."""
    account_id: str = Field(..., description='The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.')
    username: str | None = Field(default=None, description='This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.')
    model_config = ConfigDict(extra='forbid')

class GetUserGroupsToolOutput(GetUserGroupsResponse):
    """Output for tool `get_user_groups`."""
    pass

class GetUserPropertyToolInput(BaseModel):
    """Input for tool `get_user_property`."""
    account_id: str | None = Field(default=None, description='The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.')
    user_key: str | None = Field(default=None, description='This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.')
    username: str | None = Field(default=None, description='This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.')
    property_key: str = Field(..., description="The key of the user's property.")
    model_config = ConfigDict(extra='forbid')

class GetUserPropertyToolOutput(EntityProperty):
    """Output for tool `get_user_property`."""
    pass

class GetUserPropertyKeysToolInput(BaseModel):
    """Input for tool `get_user_property_keys`."""
    account_id: str | None = Field(default=None, description='The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.')
    user_key: str | None = Field(default=None, description='This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.')
    username: str | None = Field(default=None, description='This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.')
    model_config = ConfigDict(extra='forbid')

class GetUserPropertyKeysToolOutput(PropertyKeys):
    """Output for tool `get_user_property_keys`."""
    pass

class GetUsersFromGroupToolInput(BaseModel):
    """Input for tool `get_users_from_group`."""
    groupname: str | None = Field(default=None, description="As a group's name can change, use of `groupId` is recommended to identify a group.  \nThe name of the group. This parameter cannot be used with the `groupId` parameter.")
    group_id: str | None = Field(default=None, description='The ID of the group. This parameter cannot be used with the `groupName` parameter.')
    include_inactive_users: bool | None = Field(default=None, description='Include inactive users.')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    model_config = ConfigDict(extra='forbid')

class GetUsersFromGroupToolOutput(PageBeanUserDetails):
    """Output for tool `get_users_from_group`."""
    pass

class GetValidProjectKeyToolInput(BaseModel):
    """Input for tool `get_valid_project_key`."""
    model_config = ConfigDict(extra='forbid')

class GetValidProjectKeyToolOutput(RootModel[str]):
    """Output for tool `get_valid_project_key`."""
    pass

class GetValidProjectNameToolInput(BaseModel):
    """Input for tool `get_valid_project_name`."""
    name: str = Field(..., description='The project name.')
    model_config = ConfigDict(extra='forbid')

class GetValidProjectNameToolOutput(RootModel[str]):
    """Output for tool `get_valid_project_name`."""
    pass

class GetVersionToolInput(BaseModel):
    """Input for tool `get_version`."""
    id: str = Field(..., description='The ID of the version.')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information about version in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `operations` Returns the list of operations available for this version.\n *  `issuesstatus` Returns the count of issues in this version for each of the status categories *to do*, *in progress*, *done*, and *unmapped*. The *unmapped* property represents the number of issues with a status other than *to do*, *in progress*, and *done*.')
    model_config = ConfigDict(extra='forbid')

class GetVersionToolOutput(Version):
    """Output for tool `get_version`."""
    pass

class GetVersionRelatedIssuesToolInput(BaseModel):
    """Input for tool `get_version_related_issues`."""
    id: str = Field(..., description='The ID of the version.')
    model_config = ConfigDict(extra='forbid')

class GetVersionRelatedIssuesToolOutput(VersionIssueCounts):
    """Output for tool `get_version_related_issues`."""
    pass

class GetVersionUnresolvedIssuesToolInput(BaseModel):
    """Input for tool `get_version_unresolved_issues`."""
    id: str = Field(..., description='The ID of the version.')
    model_config = ConfigDict(extra='forbid')

class GetVersionUnresolvedIssuesToolOutput(VersionUnresolvedIssuesCount):
    """Output for tool `get_version_unresolved_issues`."""
    pass

class GetVisibleIssueFieldOptionsToolInput(BaseModel):
    """Input for tool `get_visible_issue_field_options`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    project_id: int | None = Field(default=None, description='Filters the results to options that are only available in the specified project.')
    field_key: str = Field(..., description='The field key is specified in the following format: **$(app-key)\\_\\_$(field-key)**. For example, *example-add-on\\_\\_example-issue-field*. To determine the `fieldKey` value, do one of the following:\n\n *  open the app\'s plugin descriptor, then **app-key** is the key at the top and **field-key** is the key in the `jiraIssueFields` module. **app-key** can also be found in the app listing in the Atlassian Universal Plugin Manager.\n *  run [Get fields](#api-rest-api-3-field-get) and in the field details the value is returned in `key`. For example, `"key": "teams-add-on__team-issue-field"`')
    model_config = ConfigDict(extra='forbid')

class GetVisibleIssueFieldOptionsToolOutput(PageBeanIssueFieldOption):
    """Output for tool `get_visible_issue_field_options`."""
    pass

class GetVotesToolInput(BaseModel):
    """Input for tool `get_votes`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    model_config = ConfigDict(extra='forbid')

class GetVotesToolOutput(Votes):
    """Output for tool `get_votes`."""
    pass

class GetWorkflowToolInput(BaseModel):
    """Input for tool `get_workflow`."""
    id: int = Field(..., description='The ID of the workflow scheme.')
    workflow_name: str | None = Field(default=None, description='The name of a workflow in the scheme. Limits the results to the workflow-issue type mapping for the specified workflow.')
    return_draft_if_exists: bool | None = Field(default=None, description="Returns the mapping from the workflow scheme's draft rather than the workflow scheme, if set to true. If no draft exists, the mapping from the workflow scheme is returned.")
    model_config = ConfigDict(extra='forbid')

class GetWorkflowToolOutput(IssueTypesWorkflowMapping):
    """Output for tool `get_workflow`."""
    pass

class GetWorkflowSchemeToolInput(BaseModel):
    """Input for tool `get_workflow_scheme`."""
    id: int = Field(..., description='The ID of the workflow scheme. Find this ID by editing the desired workflow scheme in Jira. The ID is shown in the URL as `schemeId`. For example, *schemeId=10301*.')
    return_draft_if_exists: bool | None = Field(default=None, description="Returns the workflow scheme's draft rather than scheme itself, if set to true. If the workflow scheme does not have a draft, then the workflow scheme is returned.")
    model_config = ConfigDict(extra='forbid')

class GetWorkflowSchemeToolOutput(WorkflowScheme):
    """Output for tool `get_workflow_scheme`."""
    pass

class GetWorkflowSchemeDraftToolInput(BaseModel):
    """Input for tool `get_workflow_scheme_draft`."""
    id: int = Field(..., description='The ID of the active workflow scheme that the draft was created from.')
    model_config = ConfigDict(extra='forbid')

class GetWorkflowSchemeDraftToolOutput(WorkflowScheme):
    """Output for tool `get_workflow_scheme_draft`."""
    pass

class GetWorkflowSchemeDraftIssueTypeToolInput(BaseModel):
    """Input for tool `get_workflow_scheme_draft_issue_type`."""
    id: int = Field(..., description='The ID of the workflow scheme that the draft belongs to.')
    issue_type: str = Field(..., description='The ID of the issue type.')
    model_config = ConfigDict(extra='forbid')

class GetWorkflowSchemeDraftIssueTypeToolOutput(IssueTypeWorkflowMapping):
    """Output for tool `get_workflow_scheme_draft_issue_type`."""
    pass

class GetWorkflowSchemeIssueTypeToolInput(BaseModel):
    """Input for tool `get_workflow_scheme_issue_type`."""
    id: int = Field(..., description='The ID of the workflow scheme.')
    issue_type: str = Field(..., description='The ID of the issue type.')
    return_draft_if_exists: bool | None = Field(default=None, description="Returns the mapping from the workflow scheme's draft rather than the workflow scheme, if set to true. If no draft exists, the mapping from the workflow scheme is returned.")
    model_config = ConfigDict(extra='forbid')

class GetWorkflowSchemeIssueTypeToolOutput(IssueTypeWorkflowMapping):
    """Output for tool `get_workflow_scheme_issue_type`."""
    pass

class GetWorkflowSchemeProjectAssociationsToolInput(BaseModel):
    """Input for tool `get_workflow_scheme_project_associations`."""
    project_id: list[int] = Field(..., description='The ID of a project to return the workflow schemes for. To include multiple projects, provide an ampersand-Jim: oneseparated list. For example, `projectId=10000&projectId=10001`.')
    model_config = ConfigDict(extra='forbid')

class GetWorkflowSchemeProjectAssociationsToolOutput(ContainerOfWorkflowSchemeAssociations):
    """Output for tool `get_workflow_scheme_project_associations`."""
    pass

class GetWorkflowTransitionPropertiesToolInput(BaseModel):
    """Input for tool `get_workflow_transition_properties`."""
    transition_id: int = Field(..., description='The ID of the transition. To get the ID, view the workflow in text mode in the Jira administration console. The ID is shown next to the transition.')
    include_reserved_keys: bool | None = Field(default=None, description='Some properties with keys that have the *jira.* prefix are reserved, which means they are not editable. To include these properties in the results, set this parameter to *true*.')
    workflow_name: str = Field(..., description='The name of the workflow that the transition belongs to.')
    workflow_mode: Literal['live', 'draft'] | None = Field(default=None, description='The workflow status. Set to *live* for active and inactive workflows, or *draft* for draft workflows.')
    model_config = ConfigDict(extra='forbid')

class GetWorkflowTransitionPropertiesToolOutput(WorkflowTransitionProperty):
    """Output for tool `get_workflow_transition_properties`."""
    pass

class GetWorkflowTransitionRuleConfigurationsToolInput(BaseModel):
    """Input for tool `get_workflow_transition_rule_configurations`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    types: list[Literal['postfunction', 'condition', 'validator']] = Field(..., description='The types of the transition rules to return.')
    keys: list[str] | None = Field(default=None, description='The transition rule class keys, as defined in the Connect app descriptor, of the transition rules to return.')
    workflow_names: list[str] | None = Field(default=None, description='EXPERIMENTAL: The list of workflow names to filter by.')
    with_tags: list[str] | None = Field(default=None, description='EXPERIMENTAL: The list of `tags` to filter by.')
    draft: bool | None = Field(default=None, description='EXPERIMENTAL: Whether draft or published workflows are returned. If not provided, both workflow types are returned.')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information in the response. This parameter accepts `transition`, which, for each rule, returns information about the transition the rule is assigned to.')
    model_config = ConfigDict(extra='forbid')

class GetWorkflowTransitionRuleConfigurationsToolOutput(PageBeanWorkflowTransitionRules):
    """Output for tool `get_workflow_transition_rule_configurations`."""
    pass

class GetWorkflowsPaginatedToolInput(BaseModel):
    """Input for tool `get_workflows_paginated`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    workflow_name: list[str] | None = Field(default=None, description='The name of a workflow to return. To include multiple workflows, provide an ampersand-separated list. For example, `workflowName=name1&workflowName=name2`.')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `transitions` For each workflow, returns information about the transitions inside the workflow.\n *  `transitions.rules` For each workflow transition, returns information about its rules. Transitions are included automatically if this expand is requested.\n *  `transitions.properties` For each workflow transition, returns information about its properties. Transitions are included automatically if this expand is requested.\n *  `statuses` For each workflow, returns information about the statuses inside the workflow.\n *  `statuses.properties` For each workflow status, returns information about its properties. Statuses are included automatically if this expand is requested.\n *  `default` For each workflow, returns information about whether this is the default workflow.\n *  `schemes` For each workflow, returns information about the workflow schemes the workflow is assigned to.\n *  `projects` For each workflow, returns information about the projects the workflow is assigned to, through workflow schemes.\n *  `hasDraftWorkflow` For each workflow, returns information about whether the workflow has a draft version.\n *  `operations` For each workflow, returns information about the actions that can be undertaken on the workflow.')
    query_string: str | None = Field(default=None, description='String used to perform a case-insensitive partial match with workflow name.')
    order_by: Literal['name', '-name', '+name', 'created', '-created', '+created', 'updated', '+updated', '-updated'] | None = Field(default=None, description='[Order](#ordering) the results by a field:\n\n *  `name` Sorts by workflow name.\n *  `created` Sorts by create time.\n *  `updated` Sorts by update time.')
    is_active: bool | None = Field(default=None, description='Filters active and inactive workflows.')
    model_config = ConfigDict(extra='forbid')

class GetWorkflowsPaginatedToolOutput(PageBeanWorkflow):
    """Output for tool `get_workflows_paginated`."""
    pass

class GetWorklogToolInput(BaseModel):
    """Input for tool `get_worklog`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    id: str = Field(..., description='The ID of the worklog.')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information about work logs in the response. This parameter accepts\n\n`properties`, which returns worklog properties.')
    model_config = ConfigDict(extra='forbid')

class GetWorklogToolOutput(Worklog):
    """Output for tool `get_worklog`."""
    pass

class GetWorklogPropertyToolInput(BaseModel):
    """Input for tool `get_worklog_property`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    worklog_id: str = Field(..., description='The ID of the worklog.')
    property_key: str = Field(..., description='The key of the property.')
    model_config = ConfigDict(extra='forbid')

class GetWorklogPropertyToolOutput(EntityProperty):
    """Output for tool `get_worklog_property`."""
    pass

class GetWorklogPropertyKeysToolInput(BaseModel):
    """Input for tool `get_worklog_property_keys`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    worklog_id: str = Field(..., description='The ID of the worklog.')
    model_config = ConfigDict(extra='forbid')

class GetWorklogPropertyKeysToolOutput(PropertyKeys):
    """Output for tool `get_worklog_property_keys`."""
    pass

class GetWorklogsForIdsToolInput(BaseModel):
    """Input for tool `get_worklogs_for_ids`."""
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information about worklogs in the response. This parameter accepts `properties` that returns the properties of each worklog.')
    body: WorklogIdsRequestBean = Field(..., description='Request body for `get_worklogs_for_ids`.')
    model_config = ConfigDict(extra='forbid')

class GetWorklogsForIdsToolOutput(GetWorklogsForIdsResponse):
    """Output for tool `get_worklogs_for_ids`."""
    pass

class LinkIssuesToolInput(BaseModel):
    """Input for tool `link_issues`."""
    body: LinkIssueRequestJsonBean = Field(..., description='Request body for `link_issues`.')
    model_config = ConfigDict(extra='forbid')

class LinkIssuesToolOutput(RootModel[dict[str, object]]):
    """Output for tool `link_issues`."""
    pass

class MatchIssuesToolInput(BaseModel):
    """Input for tool `match_issues`."""
    body: IssuesAndJQLQueries = Field(..., description='Request body for `match_issues`.')
    model_config = ConfigDict(extra='forbid')

class MatchIssuesToolOutput(IssueMatches):
    """Output for tool `match_issues`."""
    pass

class MergeVersionsToolInput(BaseModel):
    """Input for tool `merge_versions`."""
    id: str = Field(..., description='The ID of the version to delete.')
    move_issues_to: str = Field(..., description='The ID of the version to merge into.')
    model_config = ConfigDict(extra='forbid')

class MergeVersionsToolOutput(RootModel[dict[str, object]]):
    """Output for tool `merge_versions`."""
    pass

class MigrateQueriesToolInput(BaseModel):
    """Input for tool `migrate_queries`."""
    body: JQLPersonalDataMigrationRequest = Field(..., description='Request body for `migrate_queries`.')
    model_config = ConfigDict(extra='forbid')

class MigrateQueriesToolOutput(ConvertedJQLQueries):
    """Output for tool `migrate_queries`."""
    pass

class MigrationResourceUpdateEntityPropertiesValuePutToolInput(BaseModel):
    """Input for tool `migration_resource_update_entity_properties_value_put`."""
    atlassian_transfer_id: str = Field(..., description='The app migration transfer ID.')
    entity_type: Literal['IssueProperty', 'CommentProperty', 'DashboardItemProperty', 'IssueTypeProperty', 'ProjectProperty', 'UserProperty', 'WorklogProperty', 'BoardProperty', 'SprintProperty'] = Field(..., description='The type indicating the object that contains the entity properties.')
    body: MigrationResourceUpdateEntityPropertiesValuePutRequest = Field(..., description='Request body for `migration_resource_update_entity_properties_value_put`.')
    model_config = ConfigDict(extra='forbid')

class MigrationResourceUpdateEntityPropertiesValuePutToolOutput(RootModel[dict[str, object]]):
    """Output for tool `migration_resource_update_entity_properties_value_put`."""
    pass

class MigrationResourceWorkflowRuleSearchPostToolInput(BaseModel):
    """Input for tool `migration_resource_workflow_rule_search_post`."""
    atlassian_transfer_id: str = Field(..., description='The app migration transfer ID.')
    body: WorkflowRulesSearch = Field(..., description='Request body for `migration_resource_workflow_rule_search_post`.')
    model_config = ConfigDict(extra='forbid')

class MigrationResourceWorkflowRuleSearchPostToolOutput(WorkflowRulesSearchDetails):
    """Output for tool `migration_resource_workflow_rule_search_post`."""
    pass

class MovePrioritiesToolInput(BaseModel):
    """Input for tool `move_priorities`."""
    body: ReorderIssuePriorities = Field(..., description='Request body for `move_priorities`.')
    model_config = ConfigDict(extra='forbid')

class MovePrioritiesToolOutput(RootModel[dict[str, object]]):
    """Output for tool `move_priorities`."""
    pass

class MoveResolutionsToolInput(BaseModel):
    """Input for tool `move_resolutions`."""
    body: ReorderIssueResolutionsRequest = Field(..., description='Request body for `move_resolutions`.')
    model_config = ConfigDict(extra='forbid')

class MoveResolutionsToolOutput(RootModel[dict[str, object]]):
    """Output for tool `move_resolutions`."""
    pass

class MoveScreenTabToolInput(BaseModel):
    """Input for tool `move_screen_tab`."""
    screen_id: int = Field(..., description='The ID of the screen.')
    tab_id: int = Field(..., description='The ID of the screen tab.')
    pos: int = Field(..., description='The position of tab. The base index is 0.')
    model_config = ConfigDict(extra='forbid')

class MoveScreenTabToolOutput(RootModel[dict[str, object]]):
    """Output for tool `move_screen_tab`."""
    pass

class MoveScreenTabFieldToolInput(BaseModel):
    """Input for tool `move_screen_tab_field`."""
    screen_id: int = Field(..., description='The ID of the screen.')
    tab_id: int = Field(..., description='The ID of the screen tab.')
    id: str = Field(..., description='The ID of the field.')
    body: MoveFieldBean = Field(..., description='Request body for `move_screen_tab_field`.')
    model_config = ConfigDict(extra='forbid')

class MoveScreenTabFieldToolOutput(RootModel[dict[str, object]]):
    """Output for tool `move_screen_tab_field`."""
    pass

class MoveVersionToolInput(BaseModel):
    """Input for tool `move_version`."""
    id: str = Field(..., description='The ID of the version to be moved.')
    body: VersionMoveBean = Field(..., description='Request body for `move_version`.')
    model_config = ConfigDict(extra='forbid')

class MoveVersionToolOutput(Version):
    """Output for tool `move_version`."""
    pass

class NotifyToolInput(BaseModel):
    """Input for tool `notify`."""
    issue_id_or_key: str = Field(..., description='ID or key of the issue that the notification is sent for.')
    body: Notification = Field(..., description='Request body for `notify`.')
    model_config = ConfigDict(extra='forbid')

class NotifyToolOutput(RootModel[dict[str, object]]):
    """Output for tool `notify`."""
    pass

class ParseJqlQueriesToolInput(BaseModel):
    """Input for tool `parse_jql_queries`."""
    validation: Literal['strict', 'warn', 'none'] | None = Field(default=None, description='How to validate the JQL query and treat the validation results. Validation options include:\n\n *  `strict` Returns all errors. If validation fails, the query structure is not returned.\n *  `warn` Returns all errors. If validation fails but the JQL query is correctly formed, the query structure is returned.\n *  `none` No validation is performed. If JQL query is correctly formed, the query structure is returned.')
    body: JqlQueriesToParse = Field(..., description='Request body for `parse_jql_queries`.')
    model_config = ConfigDict(extra='forbid')

class ParseJqlQueriesToolOutput(ParsedJqlQueries):
    """Output for tool `parse_jql_queries`."""
    pass

class PartialUpdateProjectRoleToolInput(BaseModel):
    """Input for tool `partial_update_project_role`."""
    id: int = Field(..., description='The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.')
    body: CreateUpdateRoleRequestBean = Field(..., description='Request body for `partial_update_project_role`.')
    model_config = ConfigDict(extra='forbid')

class PartialUpdateProjectRoleToolOutput(ProjectRole):
    """Output for tool `partial_update_project_role`."""
    pass

class PublishDraftWorkflowSchemeToolInput(BaseModel):
    """Input for tool `publish_draft_workflow_scheme`."""
    id: int = Field(..., description='The ID of the workflow scheme that the draft belongs to.')
    validate_only: bool | None = Field(default=None, description='Whether the request only performs a validation.')
    body: PublishDraftWorkflowScheme = Field(..., description='Request body for `publish_draft_workflow_scheme`.')
    model_config = ConfigDict(extra='forbid')

class PublishDraftWorkflowSchemeToolOutput(RootModel[dict[str, object]]):
    """Output for tool `publish_draft_workflow_scheme`."""
    pass

class RefreshWebhooksToolInput(BaseModel):
    """Input for tool `refresh_webhooks`."""
    body: ContainerForWebhookIDs = Field(..., description='Request body for `refresh_webhooks`.')
    model_config = ConfigDict(extra='forbid')

class RefreshWebhooksToolOutput(WebhooksExpirationDate):
    """Output for tool `refresh_webhooks`."""
    pass

class RegisterDynamicWebhooksToolInput(BaseModel):
    """Input for tool `register_dynamic_webhooks`."""
    body: WebhookRegistrationDetails = Field(..., description='Request body for `register_dynamic_webhooks`.')
    model_config = ConfigDict(extra='forbid')

class RegisterDynamicWebhooksToolOutput(ContainerForRegisteredWebhooks):
    """Output for tool `register_dynamic_webhooks`."""
    pass

class RemoveAttachmentToolInput(BaseModel):
    """Input for tool `remove_attachment`."""
    id: str = Field(..., description='The ID of the attachment.')
    model_config = ConfigDict(extra='forbid')

class RemoveAttachmentToolOutput(RootModel[dict[str, object]]):
    """Output for tool `remove_attachment`."""
    pass

class RemoveCustomFieldContextFromProjectsToolInput(BaseModel):
    """Input for tool `remove_custom_field_context_from_projects`."""
    field_id: str = Field(..., description='The ID of the custom field.')
    context_id: int = Field(..., description='The ID of the context.')
    body: ProjectIds = Field(..., description='Request body for `remove_custom_field_context_from_projects`.')
    model_config = ConfigDict(extra='forbid')

class RemoveCustomFieldContextFromProjectsToolOutput(RootModel[dict[str, object]]):
    """Output for tool `remove_custom_field_context_from_projects`."""
    pass

class RemoveGadgetToolInput(BaseModel):
    """Input for tool `remove_gadget`."""
    dashboard_id: int = Field(..., description='The ID of the dashboard.')
    gadget_id: int = Field(..., description='The ID of the gadget.')
    model_config = ConfigDict(extra='forbid')

class RemoveGadgetToolOutput(RootModel[dict[str, object]]):
    """Output for tool `remove_gadget`."""
    pass

class RemoveGroupToolInput(BaseModel):
    """Input for tool `remove_group`."""
    groupname: str | None = None
    group_id: str | None = Field(default=None, description='The ID of the group. This parameter cannot be used with the `groupname` parameter.')
    swap_group: str | None = Field(default=None, description="As a group's name can change, use of `swapGroupId` is recommended to identify a group.  \nThe group to transfer restrictions to. Only comments and worklogs are transferred. If restrictions are not transferred, comments and worklogs are inaccessible after the deletion. This parameter cannot be used with the `swapGroupId` parameter.")
    swap_group_id: str | None = Field(default=None, description='The ID of the group to transfer restrictions to. Only comments and worklogs are transferred. If restrictions are not transferred, comments and worklogs are inaccessible after the deletion. This parameter cannot be used with the `swapGroup` parameter.')
    model_config = ConfigDict(extra='forbid')

class RemoveGroupToolOutput(RootModel[dict[str, object]]):
    """Output for tool `remove_group`."""
    pass

class RemoveIssueTypeFromIssueTypeSchemeToolInput(BaseModel):
    """Input for tool `remove_issue_type_from_issue_type_scheme`."""
    issue_type_scheme_id: int = Field(..., description='The ID of the issue type scheme.')
    issue_type_id: int = Field(..., description='The ID of the issue type.')
    model_config = ConfigDict(extra='forbid')

class RemoveIssueTypeFromIssueTypeSchemeToolOutput(RootModel[dict[str, object]]):
    """Output for tool `remove_issue_type_from_issue_type_scheme`."""
    pass

class RemoveIssueTypesFromContextToolInput(BaseModel):
    """Input for tool `remove_issue_types_from_context`."""
    field_id: str = Field(..., description='The ID of the custom field.')
    context_id: int = Field(..., description='The ID of the context.')
    body: IssueTypeIds = Field(..., description='Request body for `remove_issue_types_from_context`.')
    model_config = ConfigDict(extra='forbid')

class RemoveIssueTypesFromContextToolOutput(RootModel[dict[str, object]]):
    """Output for tool `remove_issue_types_from_context`."""
    pass

class RemoveIssueTypesFromGlobalFieldConfigurationSchemeToolInput(BaseModel):
    """Input for tool `remove_issue_types_from_global_field_configuration_scheme`."""
    id: int = Field(..., description='The ID of the field configuration scheme.')
    body: IssueTypeIdsToRemove = Field(..., description='Request body for `remove_issue_types_from_global_field_configuration_scheme`.')
    model_config = ConfigDict(extra='forbid')

class RemoveIssueTypesFromGlobalFieldConfigurationSchemeToolOutput(RootModel[dict[str, object]]):
    """Output for tool `remove_issue_types_from_global_field_configuration_scheme`."""
    pass

class RemoveMappingsFromIssueTypeScreenSchemeToolInput(BaseModel):
    """Input for tool `remove_mappings_from_issue_type_screen_scheme`."""
    issue_type_screen_scheme_id: str = Field(..., description='The ID of the issue type screen scheme.')
    body: IssueTypeIds = Field(..., description='Request body for `remove_mappings_from_issue_type_screen_scheme`.')
    model_config = ConfigDict(extra='forbid')

class RemoveMappingsFromIssueTypeScreenSchemeToolOutput(RootModel[dict[str, object]]):
    """Output for tool `remove_mappings_from_issue_type_screen_scheme`."""
    pass

class RemoveNotificationFromNotificationSchemeToolInput(BaseModel):
    """Input for tool `remove_notification_from_notification_scheme`."""
    notification_scheme_id: str = Field(..., description='The ID of the notification scheme.')
    notification_id: str = Field(..., description='The ID of the notification.')
    model_config = ConfigDict(extra='forbid')

class RemoveNotificationFromNotificationSchemeToolOutput(RootModel[dict[str, object]]):
    """Output for tool `remove_notification_from_notification_scheme`."""
    pass

class RemovePreferenceToolInput(BaseModel):
    """Input for tool `remove_preference`."""
    model_config = ConfigDict(extra='forbid')

class RemovePreferenceToolOutput(RootModel[dict[str, object]]):
    """Output for tool `remove_preference`."""
    pass

class RemoveProjectCategoryToolInput(BaseModel):
    """Input for tool `remove_project_category`."""
    id: int = Field(..., description='ID of the project category to delete.')
    model_config = ConfigDict(extra='forbid')

class RemoveProjectCategoryToolOutput(RootModel[dict[str, object]]):
    """Output for tool `remove_project_category`."""
    pass

class RemoveScreenTabFieldToolInput(BaseModel):
    """Input for tool `remove_screen_tab_field`."""
    screen_id: int = Field(..., description='The ID of the screen.')
    tab_id: int = Field(..., description='The ID of the screen tab.')
    id: str = Field(..., description='The ID of the field.')
    model_config = ConfigDict(extra='forbid')

class RemoveScreenTabFieldToolOutput(RootModel[dict[str, object]]):
    """Output for tool `remove_screen_tab_field`."""
    pass

class RemoveUserToolInput(BaseModel):
    """Input for tool `remove_user`."""
    account_id: str = Field(..., description='The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.')
    username: str | None = Field(default=None, description='This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.')
    model_config = ConfigDict(extra='forbid')

class RemoveUserToolOutput(RootModel[dict[str, object]]):
    """Output for tool `remove_user`."""
    pass

class RemoveUserFromGroupToolInput(BaseModel):
    """Input for tool `remove_user_from_group`."""
    groupname: str | None = Field(default=None, description="As a group's name can change, use of `groupId` is recommended to identify a group.  \nThe name of the group. This parameter cannot be used with the `groupId` parameter.")
    group_id: str | None = Field(default=None, description='The ID of the group. This parameter cannot be used with the `groupName` parameter.')
    username: str | None = Field(default=None, description='This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.')
    account_id: str = Field(..., description='The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.')
    model_config = ConfigDict(extra='forbid')

class RemoveUserFromGroupToolOutput(RootModel[dict[str, object]]):
    """Output for tool `remove_user_from_group`."""
    pass

class RemoveVoteToolInput(BaseModel):
    """Input for tool `remove_vote`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    model_config = ConfigDict(extra='forbid')

class RemoveVoteToolOutput(RootModel[dict[str, object]]):
    """Output for tool `remove_vote`."""
    pass

class RemoveWatcherToolInput(BaseModel):
    """Input for tool `remove_watcher`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    username: str | None = Field(default=None, description='This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.')
    account_id: str | None = Field(default=None, description='The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*. Required.')
    model_config = ConfigDict(extra='forbid')

class RemoveWatcherToolOutput(RootModel[dict[str, object]]):
    """Output for tool `remove_watcher`."""
    pass

class RenameScreenTabToolInput(BaseModel):
    """Input for tool `rename_screen_tab`."""
    screen_id: int = Field(..., description='The ID of the screen.')
    tab_id: int = Field(..., description='The ID of the screen tab.')
    body: ScreenableTab = Field(..., description='Request body for `rename_screen_tab`.')
    model_config = ConfigDict(extra='forbid')

class RenameScreenTabToolOutput(ScreenableTab):
    """Output for tool `rename_screen_tab`."""
    pass

class ReorderCustomFieldOptionsToolInput(BaseModel):
    """Input for tool `reorder_custom_field_options`."""
    field_id: str = Field(..., description='The ID of the custom field.')
    context_id: int = Field(..., description='The ID of the context.')
    body: OrderOfCustomFieldOptions = Field(..., description='Request body for `reorder_custom_field_options`.')
    model_config = ConfigDict(extra='forbid')

class ReorderCustomFieldOptionsToolOutput(RootModel[dict[str, object]]):
    """Output for tool `reorder_custom_field_options`."""
    pass

class ReorderIssueTypesInIssueTypeSchemeToolInput(BaseModel):
    """Input for tool `reorder_issue_types_in_issue_type_scheme`."""
    issue_type_scheme_id: int = Field(..., description='The ID of the issue type scheme.')
    body: OrderOfIssueTypes = Field(..., description='Request body for `reorder_issue_types_in_issue_type_scheme`.')
    model_config = ConfigDict(extra='forbid')

class ReorderIssueTypesInIssueTypeSchemeToolOutput(RootModel[dict[str, object]]):
    """Output for tool `reorder_issue_types_in_issue_type_scheme`."""
    pass

class ReplaceIssueFieldOptionToolInput(BaseModel):
    """Input for tool `replace_issue_field_option`."""
    replace_with: int | None = Field(default=None, description='The ID of the option that will replace the currently selected option.')
    jql: str | None = Field(default=None, description='A JQL query that specifies the issues to be updated. For example, *project=10000*.')
    override_screen_security: bool | None = Field(default=None, description='Whether screen security is overridden to enable hidden fields to be edited. Available to Connect and Forge app users with admin permission.')
    override_editable_flag: bool | None = Field(default=None, description='Whether screen security is overridden to enable uneditable fields to be edited. Available to Connect and Forge app users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).')
    field_key: str = Field(..., description='The field key is specified in the following format: **$(app-key)\\_\\_$(field-key)**. For example, *example-add-on\\_\\_example-issue-field*. To determine the `fieldKey` value, do one of the following:\n\n *  open the app\'s plugin descriptor, then **app-key** is the key at the top and **field-key** is the key in the `jiraIssueFields` module. **app-key** can also be found in the app listing in the Atlassian Universal Plugin Manager.\n *  run [Get fields](#api-rest-api-3-field-get) and in the field details the value is returned in `key`. For example, `"key": "teams-add-on__team-issue-field"`')
    option_id: int = Field(..., description='The ID of the option to be deselected.')
    model_config = ConfigDict(extra='forbid')

class ReplaceIssueFieldOptionToolOutput(RootModel[dict[str, object]]):
    """Output for tool `replace_issue_field_option`."""
    pass

class ResetColumnsToolInput(BaseModel):
    """Input for tool `reset_columns`."""
    id: int = Field(..., description='The ID of the filter.')
    model_config = ConfigDict(extra='forbid')

class ResetColumnsToolOutput(RootModel[dict[str, object]]):
    """Output for tool `reset_columns`."""
    pass

class ResetUserColumnsToolInput(BaseModel):
    """Input for tool `reset_user_columns`."""
    account_id: str | None = Field(default=None, description='The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.')
    username: str | None = Field(default=None, description='This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.')
    model_config = ConfigDict(extra='forbid')

class ResetUserColumnsToolOutput(RootModel[dict[str, object]]):
    """Output for tool `reset_user_columns`."""
    pass

class RestoreToolInput(BaseModel):
    """Input for tool `restore`."""
    project_id_or_key: str = Field(..., description='The project ID or project key (case sensitive).')
    model_config = ConfigDict(extra='forbid')

class RestoreToolOutput(Project):
    """Output for tool `restore`."""
    pass

class RestoreCustomFieldToolInput(BaseModel):
    """Input for tool `restore_custom_field`."""
    id: str = Field(..., description='The ID of a custom field.')
    model_config = ConfigDict(extra='forbid')

class RestoreCustomFieldToolOutput(RootModel[dict[str, object]]):
    """Output for tool `restore_custom_field`."""
    pass

class SanitiseJqlQueriesToolInput(BaseModel):
    """Input for tool `sanitise_jql_queries`."""
    body: JqlQueriesToSanitize = Field(..., description='Request body for `sanitise_jql_queries`.')
    model_config = ConfigDict(extra='forbid')

class SanitiseJqlQueriesToolOutput(SanitizedJqlQueries):
    """Output for tool `sanitise_jql_queries`."""
    pass

class SearchToolInput(BaseModel):
    """Input for tool `search`."""
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `usages` Returns the project and issue types that use the status in their workflow.')
    project_id: str | None = Field(default=None, description='The project the status is part of or null for global statuses.')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    search_string: str | None = Field(default=None, description='Term to match status names against or null to search for all statuses in the search scope.')
    status_category: str | None = Field(default=None, description='Category of the status to filter by. The supported values are: `TODO`, `IN_PROGRESS`, and `DONE`.')
    model_config = ConfigDict(extra='forbid')

class SearchToolOutput(PageOfStatuses):
    """Output for tool `search`."""
    pass

class SearchForIssuesUsingJqlToolInput(BaseModel):
    """Input for tool `search_for_issues_using_jql`."""
    jql: str | None = Field(default=None, description='The [JQL](https://confluence.atlassian.com/x/egORLQ) that defines the search. Note:\n\n *  If no JQL expression is provided, all issues are returned.\n *  `username` and `userkey` cannot be used as search terms due to privacy reasons. Use `accountId` instead.\n *  If a user has hidden their email address in their user profile, partial matches of the email address will not find the user. An exact match is required.')
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page. To manage page size, Jira may return fewer items per page where a large number of fields are requested. The greatest number of items returned per page is achieved when requesting `id` or `key` only.')
    validate_query: Literal['strict', 'warn', 'none', 'true', 'false'] | None = Field(default=None, description='Determines how to validate the JQL query and treat the validation results. Supported values are:\n\n *  `strict` Returns a 400 response code if any errors are found, along with a list of all errors (and warnings).\n *  `warn` Returns all errors as warnings.\n *  `none` No validation is performed.\n *  `true` *Deprecated* A legacy synonym for `strict`.\n *  `false` *Deprecated* A legacy synonym for `warn`.\n\nNote: If the JQL is not correctly formed a 400 response code is returned, regardless of the `validateQuery` value.')
    fields: list[str] | None = Field(default=None, description='A list of fields to return for each issue, use it to retrieve a subset of fields. This parameter accepts a comma-separated list. Expand options include:\n\n *  `*all` Returns all fields.\n *  `*navigable` Returns navigable fields.\n *  Any issue field, prefixed with a minus to exclude.\n\nExamples:\n\n *  `summary,comment` Returns only the summary and comments fields.\n *  `-description` Returns all navigable (default) fields except description.\n *  `*all,-comment` Returns all fields except comments.\n\nThis parameter may be specified multiple times. For example, `fields=field1,field2&fields=field3`.\n\nNote: All navigable fields are returned by default. This differs from [GET issue](#api-rest-api-3-issue-issueIdOrKey-get) where the default is all fields.')
    expand: str | None = Field(default=None, description="Use [expand](#expansion) to include additional information about issues in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `renderedFields` Returns field values rendered in HTML format.\n *  `names` Returns the display name of each field.\n *  `schema` Returns the schema describing a field type.\n *  `transitions` Returns all possible transitions for the issue.\n *  `operations` Returns all possible operations for the issue.\n *  `editmeta` Returns information about how each field can be edited.\n *  `changelog` Returns a list of recent updates to an issue, sorted by date, starting from the most recent.\n *  `versionedRepresentations` Instead of `fields`, returns `versionedRepresentations` a JSON array containing each version of a field's value, with the highest numbered item representing the most recent version.")
    properties: list[str] | None = Field(default=None, description='A list of issue property keys for issue properties to include in the results. This parameter accepts a comma-separated list. Multiple properties can also be provided using an ampersand separated list. For example, `properties=prop1,prop2&properties=prop3`. A maximum of 5 issue property keys can be specified.')
    fields_by_keys: bool | None = Field(default=None, description='Reference fields by their key (rather than ID).')
    model_config = ConfigDict(extra='forbid')

class SearchForIssuesUsingJqlToolOutput(SearchResults):
    """Output for tool `search_for_issues_using_jql`."""
    pass

class SearchForIssuesUsingJqlPostToolInput(BaseModel):
    """Input for tool `search_for_issues_using_jql_post`."""
    body: SearchRequestBean = Field(..., description='Request body for `search_for_issues_using_jql_post`.')
    model_config = ConfigDict(extra='forbid')

class SearchForIssuesUsingJqlPostToolOutput(SearchResults):
    """Output for tool `search_for_issues_using_jql_post`."""
    pass

class SearchPrioritiesToolInput(BaseModel):
    """Input for tool `search_priorities`."""
    start_at: str | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: str | None = Field(default=None, description='The maximum number of items to return per page.')
    id: list[str] | None = Field(default=None, description='The list of priority IDs. To include multiple IDs, provide an ampersand-separated list. For example, `id=2&id=3`.')
    only_default: bool | None = Field(default=None, description='Whether only the default priority is returned.')
    model_config = ConfigDict(extra='forbid')

class SearchPrioritiesToolOutput(PageBeanPriority):
    """Output for tool `search_priorities`."""
    pass

class SearchProjectsToolInput(BaseModel):
    """Input for tool `search_projects`."""
    start_at: int | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: int | None = Field(default=None, description='The maximum number of items to return per page.')
    order_by: Literal['category', '-category', '+category', 'key', '-key', '+key', 'name', '-name', '+name', 'owner', '-owner', '+owner', 'issueCount', '-issueCount', '+issueCount', 'lastIssueUpdatedDate', '-lastIssueUpdatedDate', '+lastIssueUpdatedDate', 'archivedDate', '+archivedDate', '-archivedDate', 'deletedDate', '+deletedDate', '-deletedDate'] | None = Field(default=None, description='[Order](#ordering) the results by a field.\n\n *  `category` Sorts by project category. A complete list of category IDs is found using [Get all project categories](#api-rest-api-3-projectCategory-get).\n *  `issueCount` Sorts by the total number of issues in each project.\n *  `key` Sorts by project key.\n *  `lastIssueUpdatedTime` Sorts by the last issue update time.\n *  `name` Sorts by project name.\n *  `owner` Sorts by project lead.\n *  `archivedDate` EXPERIMENTAL. Sorts by project archived date.\n *  `deletedDate` EXPERIMENTAL. Sorts by project deleted date.')
    id: list[int] | None = Field(default=None, description='The project IDs to filter the results by. To include multiple IDs, provide an ampersand-separated list. For example, `id=10000&id=10001`. Up to 50 project IDs can be provided.')
    keys: list[str] | None = Field(default=None, description='The project keys to filter the results by. To include multiple keys, provide an ampersand-separated list. For example, `keys=PA&keys=PB`. Up to 50 project keys can be provided.')
    query: str | None = Field(default=None, description='Filter the results using a literal string. Projects with a matching `key` or `name` are returned (case insensitive).')
    type_key: str | None = Field(default=None, description='Orders results by the [project type](https://confluence.atlassian.com/x/GwiiLQ#Jiraapplicationsoverview-Productfeaturesandprojecttypes). This parameter accepts a comma-separated list. Valid values are `business`, `service_desk`, and `software`.')
    category_id: int | None = Field(default=None, description="The ID of the project's category. A complete list of category IDs is found using the [Get all project categories](#api-rest-api-3-projectCategory-get) operation.")
    action: Literal['view', 'browse', 'edit'] | None = Field(default=None, description='Filter results by projects for which the user can:\n\n *  `view` the project, meaning that they have one of the following permissions:\n    \n     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.\n     *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.\n     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).\n *  `browse` the project, meaning that they have the *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.\n *  `edit` the project, meaning that they have one of the following permissions:\n    \n     *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.\n     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expanded options include:\n\n *  `description` Returns the project description.\n *  `projectKeys` Returns all project keys associated with a project.\n *  `lead` Returns information about the project lead.\n *  `issueTypes` Returns all issue types associated with the project.\n *  `url` Returns the URL associated with the project.\n *  `insight` EXPERIMENTAL. Returns the insight details of total issue count and last issue update time for the project.')
    status: list[Literal['live', 'archived', 'deleted']] | None = Field(default=None, description='EXPERIMENTAL. Filter results by project status:\n\n *  `live` Search live projects.\n *  `archived` Search archived projects.\n *  `deleted` Search deleted projects, those in the recycle bin.')
    properties: list[dict[str, object]] | None = Field(default=None, description='EXPERIMENTAL. A list of project properties to return for the project. This parameter accepts a comma-separated list.')
    property_query: str | None = Field(default=None, description='EXPERIMENTAL. A query string used to search properties. The query string cannot be specified using a JSON object. For example, to search for the value of `nested` from `{"something":{"nested":1,"other":2}}` use `[thepropertykey].something.nested=1`. Note that the propertyQuery key is enclosed in square brackets to enable searching where the propertyQuery key includes dot (.) or equals (=) characters. Note that `thepropertykey` is only returned when included in `properties`.')
    model_config = ConfigDict(extra='forbid')

class SearchProjectsToolOutput(PageBeanProject):
    """Output for tool `search_projects`."""
    pass

class SearchResolutionsToolInput(BaseModel):
    """Input for tool `search_resolutions`."""
    start_at: str | None = Field(default=None, description='The index of the first item to return in a page of results (page offset).')
    max_results: str | None = Field(default=None, description='The maximum number of items to return per page.')
    id: list[str] | None = Field(default=None, description='The list of resolutions IDs to be filtered out')
    only_default: bool | None = Field(default=None, description='When set to true, return default only, when IDs provided, if none of them is default, return empty page. Default value is false')
    model_config = ConfigDict(extra='forbid')

class SearchResolutionsToolOutput(PageBeanResolutionJsonBean):
    """Output for tool `search_resolutions`."""
    pass

class SelectTimeTrackingImplementationToolInput(BaseModel):
    """Input for tool `select_time_tracking_implementation`."""
    body: TimeTrackingProvider = Field(..., description='Request body for `select_time_tracking_implementation`.')
    model_config = ConfigDict(extra='forbid')

class SelectTimeTrackingImplementationToolOutput(RootModel[dict[str, object]]):
    """Output for tool `select_time_tracking_implementation`."""
    pass

class SetActorsToolInput(BaseModel):
    """Input for tool `set_actors`."""
    project_id_or_key: str = Field(..., description='The project ID or project key (case sensitive).')
    id: int = Field(..., description='The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.')
    body: ProjectRoleActorsUpdateBean = Field(..., description='Request body for `set_actors`.')
    model_config = ConfigDict(extra='forbid')

class SetActorsToolOutput(ProjectRole):
    """Output for tool `set_actors`."""
    pass

class SetApplicationPropertyToolInput(BaseModel):
    """Input for tool `set_application_property`."""
    id: str = Field(..., description='The key of the application property to update.')
    body: SimpleApplicationPropertyBean = Field(..., description='Request body for `set_application_property`.')
    model_config = ConfigDict(extra='forbid')

class SetApplicationPropertyToolOutput(ApplicationProperty):
    """Output for tool `set_application_property`."""
    pass

class SetBannerToolInput(BaseModel):
    """Input for tool `set_banner`."""
    body: AnnouncementBannerConfigurationUpdate = Field(..., description='Request body for `set_banner`.')
    model_config = ConfigDict(extra='forbid')

class SetBannerToolOutput(RootModel[dict[str, object]]):
    """Output for tool `set_banner`."""
    pass

class SetColumnsToolInput(BaseModel):
    """Input for tool `set_columns`."""
    id: int = Field(..., description='The ID of the filter.')
    body: SetColumnsRequest | None = Field(default=None, description='Request body for `set_columns`.')
    model_config = ConfigDict(extra='forbid')

class SetColumnsToolOutput(RootModel[dict[str, object]]):
    """Output for tool `set_columns`."""
    pass

class SetCommentPropertyToolInput(BaseModel):
    """Input for tool `set_comment_property`."""
    comment_id: str = Field(..., description='The ID of the comment.')
    property_key: str = Field(..., description='The key of the property. The maximum length is 255 characters.')
    body: dict[str, object] = Field(..., description='Request body for `set_comment_property`.')
    model_config = ConfigDict(extra='forbid')

class SetCommentPropertyToolOutput(RootModel[dict[str, object]]):
    """Output for tool `set_comment_property`."""
    pass

class SetDashboardItemPropertyToolInput(BaseModel):
    """Input for tool `set_dashboard_item_property`."""
    dashboard_id: str = Field(..., description='The ID of the dashboard.')
    item_id: str = Field(..., description='The ID of the dashboard item.')
    property_key: str = Field(..., description='The key of the dashboard item property. The maximum length is 255 characters. For dashboard items with a spec URI and no complete module key, if the provided propertyKey is equal to "config", the request body\'s JSON must be an object with all keys and values as strings.')
    body: dict[str, object] = Field(..., description='Request body for `set_dashboard_item_property`.')
    model_config = ConfigDict(extra='forbid')

class SetDashboardItemPropertyToolOutput(RootModel[dict[str, object]]):
    """Output for tool `set_dashboard_item_property`."""
    pass

class SetDefaultPriorityToolInput(BaseModel):
    """Input for tool `set_default_priority`."""
    body: SetDefaultPriorityRequest = Field(..., description='Request body for `set_default_priority`.')
    model_config = ConfigDict(extra='forbid')

class SetDefaultPriorityToolOutput(RootModel[dict[str, object]]):
    """Output for tool `set_default_priority`."""
    pass

class SetDefaultResolutionToolInput(BaseModel):
    """Input for tool `set_default_resolution`."""
    body: SetDefaultResolutionRequest = Field(..., description='Request body for `set_default_resolution`.')
    model_config = ConfigDict(extra='forbid')

class SetDefaultResolutionToolOutput(RootModel[dict[str, object]]):
    """Output for tool `set_default_resolution`."""
    pass

class SetDefaultShareScopeToolInput(BaseModel):
    """Input for tool `set_default_share_scope`."""
    body: DefaultShareScope = Field(..., description='Request body for `set_default_share_scope`.')
    model_config = ConfigDict(extra='forbid')

class SetDefaultShareScopeToolOutput(DefaultShareScope):
    """Output for tool `set_default_share_scope`."""
    pass

class SetDefaultValuesToolInput(BaseModel):
    """Input for tool `set_default_values`."""
    field_id: str = Field(..., description='The ID of the custom field.')
    body: CustomFieldContextDefaultValueUpdate = Field(..., description='Request body for `set_default_values`.')
    model_config = ConfigDict(extra='forbid')

class SetDefaultValuesToolOutput(RootModel[dict[str, object]]):
    """Output for tool `set_default_values`."""
    pass

class SetFavouriteForFilterToolInput(BaseModel):
    """Input for tool `set_favourite_for_filter`."""
    id: int = Field(..., description='The ID of the filter.')
    expand: str | None = Field(default=None, description="Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `sharedUsers` Returns the users that the filter is shared with. This includes users that can browse projects that the filter is shared with. If you don't specify `sharedUsers`, then the `sharedUsers` object is returned but it doesn't list any users. The list of users returned is limited to 1000, to access additional users append `[start-index:end-index]` to the expand request. For example, to access the next 1000 users, use `?expand=sharedUsers[1001:2000]`.\n *  `subscriptions` Returns the users that are subscribed to the filter. If you don't specify `subscriptions`, the `subscriptions` object is returned but it doesn't list any subscriptions. The list of subscriptions returned is limited to 1000, to access additional subscriptions append `[start-index:end-index]` to the expand request. For example, to access the next 1000 subscriptions, use `?expand=subscriptions[1001:2000]`.")
    model_config = ConfigDict(extra='forbid')

class SetFavouriteForFilterToolOutput(Filter):
    """Output for tool `set_favourite_for_filter`."""
    pass

class SetFieldConfigurationSchemeMappingToolInput(BaseModel):
    """Input for tool `set_field_configuration_scheme_mapping`."""
    id: int = Field(..., description='The ID of the field configuration scheme.')
    body: AssociateFieldConfigurationsWithIssueTypesRequest = Field(..., description='Request body for `set_field_configuration_scheme_mapping`.')
    model_config = ConfigDict(extra='forbid')

class SetFieldConfigurationSchemeMappingToolOutput(RootModel[dict[str, object]]):
    """Output for tool `set_field_configuration_scheme_mapping`."""
    pass

class SetIssueNavigatorDefaultColumnsToolInput(BaseModel):
    """Input for tool `set_issue_navigator_default_columns`."""
    body: SetIssueNavigatorDefaultColumnsRequest | None = Field(default=None, description='Request body for `set_issue_navigator_default_columns`.')
    model_config = ConfigDict(extra='forbid')

class SetIssueNavigatorDefaultColumnsToolOutput(RootModel[dict[str, object]]):
    """Output for tool `set_issue_navigator_default_columns`."""
    pass

class SetIssuePropertyToolInput(BaseModel):
    """Input for tool `set_issue_property`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    property_key: str = Field(..., description='The key of the issue property. The maximum length is 255 characters.')
    body: dict[str, object] = Field(..., description='Request body for `set_issue_property`.')
    model_config = ConfigDict(extra='forbid')

class SetIssuePropertyToolOutput(RootModel[dict[str, object]]):
    """Output for tool `set_issue_property`."""
    pass

class SetIssueTypePropertyToolInput(BaseModel):
    """Input for tool `set_issue_type_property`."""
    issue_type_id: str = Field(..., description='The ID of the issue type.')
    property_key: str = Field(..., description='The key of the issue type property. The maximum length is 255 characters.')
    body: dict[str, object] = Field(..., description='Request body for `set_issue_type_property`.')
    model_config = ConfigDict(extra='forbid')

class SetIssueTypePropertyToolOutput(RootModel[dict[str, object]]):
    """Output for tool `set_issue_type_property`."""
    pass

class SetLocaleToolInput(BaseModel):
    """Input for tool `set_locale`."""
    body: Locale = Field(..., description='Request body for `set_locale`.')
    model_config = ConfigDict(extra='forbid')

class SetLocaleToolOutput(RootModel[dict[str, object]]):
    """Output for tool `set_locale`."""
    pass

class SetPreferenceToolInput(BaseModel):
    """Input for tool `set_preference`."""
    body: str = Field(..., description='Request body for `set_preference`.')
    model_config = ConfigDict(extra='forbid')

class SetPreferenceToolOutput(RootModel[dict[str, object]]):
    """Output for tool `set_preference`."""
    pass

class SetProjectPropertyToolInput(BaseModel):
    """Input for tool `set_project_property`."""
    project_id_or_key: str = Field(..., description='The project ID or project key (case sensitive).')
    property_key: str = Field(..., description='The key of the project property. The maximum length is 255 characters.')
    body: dict[str, object] = Field(..., description='Request body for `set_project_property`.')
    model_config = ConfigDict(extra='forbid')

class SetProjectPropertyToolOutput(RootModel[dict[str, object]]):
    """Output for tool `set_project_property`."""
    pass

class SetSharedTimeTrackingConfigurationToolInput(BaseModel):
    """Input for tool `set_shared_time_tracking_configuration`."""
    body: TimeTrackingConfiguration = Field(..., description='Request body for `set_shared_time_tracking_configuration`.')
    model_config = ConfigDict(extra='forbid')

class SetSharedTimeTrackingConfigurationToolOutput(TimeTrackingConfiguration):
    """Output for tool `set_shared_time_tracking_configuration`."""
    pass

class SetUserColumnsToolInput(BaseModel):
    """Input for tool `set_user_columns`."""
    account_id: str | None = Field(default=None, description='The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.')
    body: SetUserColumnsRequest | None = Field(default=None, description='Request body for `set_user_columns`.')
    model_config = ConfigDict(extra='forbid')

class SetUserColumnsToolOutput(RootModel[dict[str, object]]):
    """Output for tool `set_user_columns`."""
    pass

class SetUserPropertyToolInput(BaseModel):
    """Input for tool `set_user_property`."""
    account_id: str | None = Field(default=None, description='The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.')
    user_key: str | None = Field(default=None, description='This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.')
    username: str | None = Field(default=None, description='This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.')
    property_key: str = Field(..., description="The key of the user's property. The maximum length is 255 characters.")
    body: dict[str, object] = Field(..., description='Request body for `set_user_property`.')
    model_config = ConfigDict(extra='forbid')

class SetUserPropertyToolOutput(RootModel[dict[str, object]]):
    """Output for tool `set_user_property`."""
    pass

class SetWorkflowSchemeDraftIssueTypeToolInput(BaseModel):
    """Input for tool `set_workflow_scheme_draft_issue_type`."""
    id: int = Field(..., description='The ID of the workflow scheme that the draft belongs to.')
    issue_type: str = Field(..., description='The ID of the issue type.')
    body: IssueTypeWorkflowMapping = Field(..., description='Request body for `set_workflow_scheme_draft_issue_type`.')
    model_config = ConfigDict(extra='forbid')

class SetWorkflowSchemeDraftIssueTypeToolOutput(WorkflowScheme):
    """Output for tool `set_workflow_scheme_draft_issue_type`."""
    pass

class SetWorkflowSchemeIssueTypeToolInput(BaseModel):
    """Input for tool `set_workflow_scheme_issue_type`."""
    id: int = Field(..., description='The ID of the workflow scheme.')
    issue_type: str = Field(..., description='The ID of the issue type.')
    body: IssueTypeWorkflowMapping = Field(..., description='Request body for `set_workflow_scheme_issue_type`.')
    model_config = ConfigDict(extra='forbid')

class SetWorkflowSchemeIssueTypeToolOutput(WorkflowScheme):
    """Output for tool `set_workflow_scheme_issue_type`."""
    pass

class SetWorklogPropertyToolInput(BaseModel):
    """Input for tool `set_worklog_property`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    worklog_id: str = Field(..., description='The ID of the worklog.')
    property_key: str = Field(..., description='The key of the issue property. The maximum length is 255 characters.')
    body: dict[str, object] = Field(..., description='Request body for `set_worklog_property`.')
    model_config = ConfigDict(extra='forbid')

class SetWorklogPropertyToolOutput(RootModel[dict[str, object]]):
    """Output for tool `set_worklog_property`."""
    pass

class StoreAvatarToolInput(BaseModel):
    """Input for tool `store_avatar`."""
    type: Literal['project', 'issuetype'] = Field(..., description='The avatar type.')
    entity_id: str = Field(..., description='The ID of the item the avatar is associated with.')
    x: int | None = Field(default=None, description='The X coordinate of the top-left corner of the crop region.')
    y: int | None = Field(default=None, description='The Y coordinate of the top-left corner of the crop region.')
    size: int = Field(..., description='The length of each side of the crop region.')
    body: dict[str, object] = Field(..., description='Request body for `store_avatar`.')
    model_config = ConfigDict(extra='forbid')

class StoreAvatarToolOutput(Avatar):
    """Output for tool `store_avatar`."""
    pass

class ToggleFeatureForProjectToolInput(BaseModel):
    """Input for tool `toggle_feature_for_project`."""
    project_id_or_key: str = Field(..., description='The ID or (case-sensitive) key of the project.')
    feature_key: str = Field(..., description='The key of the feature.')
    body: ProjectFeatureState = Field(..., description='Request body for `toggle_feature_for_project`.')
    model_config = ConfigDict(extra='forbid')

class ToggleFeatureForProjectToolOutput(ContainerForProjectFeatures):
    """Output for tool `toggle_feature_for_project`."""
    pass

class TrashCustomFieldToolInput(BaseModel):
    """Input for tool `trash_custom_field`."""
    id: str = Field(..., description='The ID of a custom field.')
    model_config = ConfigDict(extra='forbid')

class TrashCustomFieldToolOutput(RootModel[dict[str, object]]):
    """Output for tool `trash_custom_field`."""
    pass

class UpdateCommentToolInput(BaseModel):
    """Input for tool `update_comment`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    id: str = Field(..., description='The ID of the comment.')
    notify_users: bool | None = Field(default=None, description='Whether users are notified when a comment is updated.')
    override_editable_flag: bool | None = Field(default=None, description='Whether screen security is overridden to enable uneditable fields to be edited. Available to Connect app users with the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) and Forge apps acting on behalf of users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information about comments in the response. This parameter accepts `renderedBody`, which returns the comment body rendered in HTML.')
    body: Comment = Field(..., description='Request body for `update_comment`.')
    model_config = ConfigDict(extra='forbid')

class UpdateCommentToolOutput(Comment):
    """Output for tool `update_comment`."""
    pass

class UpdateComponentToolInput(BaseModel):
    """Input for tool `update_component`."""
    id: str = Field(..., description='The ID of the component.')
    body: ProjectComponent = Field(..., description='Request body for `update_component`.')
    model_config = ConfigDict(extra='forbid')

class UpdateComponentToolOutput(ProjectComponent):
    """Output for tool `update_component`."""
    pass

class UpdateCustomFieldToolInput(BaseModel):
    """Input for tool `update_custom_field`."""
    field_id: str = Field(..., description='The ID of the custom field.')
    body: UpdateCustomFieldDetails = Field(..., description='Request body for `update_custom_field`.')
    model_config = ConfigDict(extra='forbid')

class UpdateCustomFieldToolOutput(RootModel[dict[str, object]]):
    """Output for tool `update_custom_field`."""
    pass

class UpdateCustomFieldConfigurationToolInput(BaseModel):
    """Input for tool `update_custom_field_configuration`."""
    field_id_or_key: str = Field(..., description='The ID or key of the custom field, for example `customfield_10000`.')
    body: CustomFieldConfigurations = Field(..., description='Request body for `update_custom_field_configuration`.')
    model_config = ConfigDict(extra='forbid')

class UpdateCustomFieldConfigurationToolOutput(RootModel[dict[str, object]]):
    """Output for tool `update_custom_field_configuration`."""
    pass

class UpdateCustomFieldContextToolInput(BaseModel):
    """Input for tool `update_custom_field_context`."""
    field_id: str = Field(..., description='The ID of the custom field.')
    context_id: int = Field(..., description='The ID of the context.')
    body: CustomFieldContextUpdateDetails = Field(..., description='Request body for `update_custom_field_context`.')
    model_config = ConfigDict(extra='forbid')

class UpdateCustomFieldContextToolOutput(RootModel[dict[str, object]]):
    """Output for tool `update_custom_field_context`."""
    pass

class UpdateCustomFieldOptionToolInput(BaseModel):
    """Input for tool `update_custom_field_option`."""
    field_id: str = Field(..., description='The ID of the custom field.')
    context_id: int = Field(..., description='The ID of the context.')
    body: BulkCustomFieldOptionUpdateRequest = Field(..., description='Request body for `update_custom_field_option`.')
    model_config = ConfigDict(extra='forbid')

class UpdateCustomFieldOptionToolOutput(CustomFieldUpdatedContextOptionsList):
    """Output for tool `update_custom_field_option`."""
    pass

class UpdateCustomFieldValueToolInput(BaseModel):
    """Input for tool `update_custom_field_value`."""
    field_id_or_key: str = Field(..., description='The ID or key of the custom field. For example, `customfield_10010`.')
    generate_changelog: bool | None = Field(default=None, description='Whether to generate a changelog for this update.')
    body: CustomFieldValueUpdateDetails = Field(..., description='Request body for `update_custom_field_value`.')
    model_config = ConfigDict(extra='forbid')

class UpdateCustomFieldValueToolOutput(RootModel[dict[str, object]]):
    """Output for tool `update_custom_field_value`."""
    pass

class UpdateDashboardToolInput(BaseModel):
    """Input for tool `update_dashboard`."""
    id: str = Field(..., description='The ID of the dashboard to update.')
    body: DashboardDetails = Field(..., description='Request body for `update_dashboard`.')
    model_config = ConfigDict(extra='forbid')

class UpdateDashboardToolOutput(Dashboard):
    """Output for tool `update_dashboard`."""
    pass

class UpdateDefaultScreenSchemeToolInput(BaseModel):
    """Input for tool `update_default_screen_scheme`."""
    issue_type_screen_scheme_id: str = Field(..., description='The ID of the issue type screen scheme.')
    body: UpdateDefaultScreenScheme = Field(..., description='Request body for `update_default_screen_scheme`.')
    model_config = ConfigDict(extra='forbid')

class UpdateDefaultScreenSchemeToolOutput(RootModel[dict[str, object]]):
    """Output for tool `update_default_screen_scheme`."""
    pass

class UpdateDefaultWorkflowToolInput(BaseModel):
    """Input for tool `update_default_workflow`."""
    id: int = Field(..., description='The ID of the workflow scheme.')
    body: DefaultWorkflow = Field(..., description='Request body for `update_default_workflow`.')
    model_config = ConfigDict(extra='forbid')

class UpdateDefaultWorkflowToolOutput(WorkflowScheme):
    """Output for tool `update_default_workflow`."""
    pass

class UpdateDraftDefaultWorkflowToolInput(BaseModel):
    """Input for tool `update_draft_default_workflow`."""
    id: int = Field(..., description='The ID of the workflow scheme that the draft belongs to.')
    body: DefaultWorkflow = Field(..., description='Request body for `update_draft_default_workflow`.')
    model_config = ConfigDict(extra='forbid')

class UpdateDraftDefaultWorkflowToolOutput(WorkflowScheme):
    """Output for tool `update_draft_default_workflow`."""
    pass

class UpdateDraftWorkflowMappingToolInput(BaseModel):
    """Input for tool `update_draft_workflow_mapping`."""
    id: int = Field(..., description='The ID of the workflow scheme that the draft belongs to.')
    workflow_name: str = Field(..., description='The name of the workflow.')
    body: IssueTypesWorkflowMapping = Field(..., description='Request body for `update_draft_workflow_mapping`.')
    model_config = ConfigDict(extra='forbid')

class UpdateDraftWorkflowMappingToolOutput(WorkflowScheme):
    """Output for tool `update_draft_workflow_mapping`."""
    pass

class UpdateFieldConfigurationToolInput(BaseModel):
    """Input for tool `update_field_configuration`."""
    id: int = Field(..., description='The ID of the field configuration.')
    body: FieldConfigurationDetails = Field(..., description='Request body for `update_field_configuration`.')
    model_config = ConfigDict(extra='forbid')

class UpdateFieldConfigurationToolOutput(RootModel[dict[str, object]]):
    """Output for tool `update_field_configuration`."""
    pass

class UpdateFieldConfigurationItemsToolInput(BaseModel):
    """Input for tool `update_field_configuration_items`."""
    id: int = Field(..., description='The ID of the field configuration.')
    body: FieldConfigurationItemsDetails = Field(..., description='Request body for `update_field_configuration_items`.')
    model_config = ConfigDict(extra='forbid')

class UpdateFieldConfigurationItemsToolOutput(RootModel[dict[str, object]]):
    """Output for tool `update_field_configuration_items`."""
    pass

class UpdateFieldConfigurationSchemeToolInput(BaseModel):
    """Input for tool `update_field_configuration_scheme`."""
    id: int = Field(..., description='The ID of the field configuration scheme.')
    body: UpdateFieldConfigurationSchemeDetails = Field(..., description='Request body for `update_field_configuration_scheme`.')
    model_config = ConfigDict(extra='forbid')

class UpdateFieldConfigurationSchemeToolOutput(RootModel[dict[str, object]]):
    """Output for tool `update_field_configuration_scheme`."""
    pass

class UpdateFilterToolInput(BaseModel):
    """Input for tool `update_filter`."""
    id: int = Field(..., description='The ID of the filter to update.')
    expand: str | None = Field(default=None, description="Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:\n\n *  `sharedUsers` Returns the users that the filter is shared with. This includes users that can browse projects that the filter is shared with. If you don't specify `sharedUsers`, then the `sharedUsers` object is returned but it doesn't list any users. The list of users returned is limited to 1000, to access additional users append `[start-index:end-index]` to the expand request. For example, to access the next 1000 users, use `?expand=sharedUsers[1001:2000]`.\n *  `subscriptions` Returns the users that are subscribed to the filter. If you don't specify `subscriptions`, the `subscriptions` object is returned but it doesn't list any subscriptions. The list of subscriptions returned is limited to 1000, to access additional subscriptions append `[start-index:end-index]` to the expand request. For example, to access the next 1000 subscriptions, use `?expand=subscriptions[1001:2000]`.")
    override_share_permissions: bool | None = Field(default=None, description='EXPERIMENTAL: Whether share permissions are overridden to enable the addition of any share permissions to filters. Available to users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).')
    body: Filter = Field(..., description='Request body for `update_filter`.')
    model_config = ConfigDict(extra='forbid')

class UpdateFilterToolOutput(Filter):
    """Output for tool `update_filter`."""
    pass

class UpdateGadgetToolInput(BaseModel):
    """Input for tool `update_gadget`."""
    dashboard_id: int = Field(..., description='The ID of the dashboard.')
    gadget_id: int = Field(..., description='The ID of the gadget.')
    body: DashboardGadgetUpdateRequest = Field(..., description='Request body for `update_gadget`.')
    model_config = ConfigDict(extra='forbid')

class UpdateGadgetToolOutput(RootModel[dict[str, object]]):
    """Output for tool `update_gadget`."""
    pass

class UpdateIssueFieldOptionToolInput(BaseModel):
    """Input for tool `update_issue_field_option`."""
    field_key: str = Field(..., description='The field key is specified in the following format: **$(app-key)\\_\\_$(field-key)**. For example, *example-add-on\\_\\_example-issue-field*. To determine the `fieldKey` value, do one of the following:\n\n *  open the app\'s plugin descriptor, then **app-key** is the key at the top and **field-key** is the key in the `jiraIssueFields` module. **app-key** can also be found in the app listing in the Atlassian Universal Plugin Manager.\n *  run [Get fields](#api-rest-api-3-field-get) and in the field details the value is returned in `key`. For example, `"key": "teams-add-on__team-issue-field"`')
    option_id: int = Field(..., description='The ID of the option to be updated.')
    body: IssueFieldOption = Field(..., description='Request body for `update_issue_field_option`.')
    model_config = ConfigDict(extra='forbid')

class UpdateIssueFieldOptionToolOutput(IssueFieldOption):
    """Output for tool `update_issue_field_option`."""
    pass

class UpdateIssueLinkTypeToolInput(BaseModel):
    """Input for tool `update_issue_link_type`."""
    issue_link_type_id: str = Field(..., description='The ID of the issue link type.')
    body: IssueLinkType = Field(..., description='Request body for `update_issue_link_type`.')
    model_config = ConfigDict(extra='forbid')

class UpdateIssueLinkTypeToolOutput(IssueLinkType):
    """Output for tool `update_issue_link_type`."""
    pass

class UpdateIssueTypeToolInput(BaseModel):
    """Input for tool `update_issue_type`."""
    id: str = Field(..., description='The ID of the issue type.')
    body: IssueTypeUpdateBean = Field(..., description='Request body for `update_issue_type`.')
    model_config = ConfigDict(extra='forbid')

class UpdateIssueTypeToolOutput(IssueTypeDetails):
    """Output for tool `update_issue_type`."""
    pass

class UpdateIssueTypeSchemeToolInput(BaseModel):
    """Input for tool `update_issue_type_scheme`."""
    issue_type_scheme_id: int = Field(..., description='The ID of the issue type scheme.')
    body: IssueTypeSchemeUpdateDetails = Field(..., description='Request body for `update_issue_type_scheme`.')
    model_config = ConfigDict(extra='forbid')

class UpdateIssueTypeSchemeToolOutput(RootModel[dict[str, object]]):
    """Output for tool `update_issue_type_scheme`."""
    pass

class UpdateIssueTypeScreenSchemeToolInput(BaseModel):
    """Input for tool `update_issue_type_screen_scheme`."""
    issue_type_screen_scheme_id: str = Field(..., description='The ID of the issue type screen scheme.')
    body: IssueTypeScreenSchemeUpdateDetails = Field(..., description='Request body for `update_issue_type_screen_scheme`.')
    model_config = ConfigDict(extra='forbid')

class UpdateIssueTypeScreenSchemeToolOutput(RootModel[dict[str, object]]):
    """Output for tool `update_issue_type_screen_scheme`."""
    pass

class UpdateMultipleCustomFieldValuesToolInput(BaseModel):
    """Input for tool `update_multiple_custom_field_values`."""
    generate_changelog: bool | None = Field(default=None, description='Whether to generate a changelog for this update.')
    body: MultipleCustomFieldValuesUpdateDetails = Field(..., description='Request body for `update_multiple_custom_field_values`.')
    model_config = ConfigDict(extra='forbid')

class UpdateMultipleCustomFieldValuesToolOutput(RootModel[dict[str, object]]):
    """Output for tool `update_multiple_custom_field_values`."""
    pass

class UpdateNotificationSchemeToolInput(BaseModel):
    """Input for tool `update_notification_scheme`."""
    id: str = Field(..., description='The ID of the notification scheme.')
    body: UpdateNotificationSchemeDetails = Field(..., description='Request body for `update_notification_scheme`.')
    model_config = ConfigDict(extra='forbid')

class UpdateNotificationSchemeToolOutput(RootModel[dict[str, object]]):
    """Output for tool `update_notification_scheme`."""
    pass

class UpdatePermissionSchemeToolInput(BaseModel):
    """Input for tool `update_permission_scheme`."""
    scheme_id: int = Field(..., description='The ID of the permission scheme to update.')
    expand: str | None = Field(default=None, description='Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are always included when you specify any value. Expand options include:\n\n *  `all` Returns all expandable information.\n *  `field` Returns information about the custom field granted the permission.\n *  `group` Returns information about the group that is granted the permission.\n *  `permissions` Returns all permission grants for each permission scheme.\n *  `projectRole` Returns information about the project role granted the permission.\n *  `user` Returns information about the user who is granted the permission.')
    body: PermissionScheme = Field(..., description='Request body for `update_permission_scheme`.')
    model_config = ConfigDict(extra='forbid')

class UpdatePermissionSchemeToolOutput(PermissionScheme):
    """Output for tool `update_permission_scheme`."""
    pass

class UpdatePrecomputationsToolInput(BaseModel):
    """Input for tool `update_precomputations`."""
    body: JqlFunctionPrecomputationUpdateRequestBean = Field(..., description='Request body for `update_precomputations`.')
    model_config = ConfigDict(extra='forbid')

class UpdatePrecomputationsToolOutput(RootModel[dict[str, object]]):
    """Output for tool `update_precomputations`."""
    pass

class UpdatePriorityToolInput(BaseModel):
    """Input for tool `update_priority`."""
    id: str = Field(..., description='The ID of the issue priority.')
    body: UpdatePriorityDetails = Field(..., description='Request body for `update_priority`.')
    model_config = ConfigDict(extra='forbid')

class UpdatePriorityToolOutput(RootModel[dict[str, object]]):
    """Output for tool `update_priority`."""
    pass

class UpdateProjectToolInput(BaseModel):
    """Input for tool `update_project`."""
    project_id_or_key: str = Field(..., description='The project ID or project key (case sensitive).')
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Note that the project description, issue types, and project lead are included in all responses by default. Expand options include:\n\n *  `description` The project description.\n *  `issueTypes` The issue types associated with the project.\n *  `lead` The project lead.\n *  `projectKeys` All project keys associated with the project.')
    body: UpdateProjectDetails = Field(..., description='Request body for `update_project`.')
    model_config = ConfigDict(extra='forbid')

class UpdateProjectToolOutput(Project):
    """Output for tool `update_project`."""
    pass

class UpdateProjectAvatarToolInput(BaseModel):
    """Input for tool `update_project_avatar`."""
    project_id_or_key: str = Field(..., description='The ID or (case-sensitive) key of the project.')
    body: Avatar = Field(..., description='Request body for `update_project_avatar`.')
    model_config = ConfigDict(extra='forbid')

class UpdateProjectAvatarToolOutput(RootModel[dict[str, object]]):
    """Output for tool `update_project_avatar`."""
    pass

class UpdateProjectCategoryToolInput(BaseModel):
    """Input for tool `update_project_category`."""
    id: int = Field(...)
    body: ProjectCategory = Field(..., description='Request body for `update_project_category`.')
    model_config = ConfigDict(extra='forbid')

class UpdateProjectCategoryToolOutput(UpdatedProjectCategory):
    """Output for tool `update_project_category`."""
    pass

class UpdateProjectEmailToolInput(BaseModel):
    """Input for tool `update_project_email`."""
    project_id: int = Field(..., description='The project ID.')
    body: ProjectEmailAddress = Field(..., description='Request body for `update_project_email`.')
    model_config = ConfigDict(extra='forbid')

class UpdateProjectEmailToolOutput(RootModel[dict[str, object]]):
    """Output for tool `update_project_email`."""
    pass

class UpdateProjectTypeToolInput(BaseModel):
    """Input for tool `update_project_type`."""
    project_id_or_key: str = Field(..., description='The project ID or project key (case sensitive).')
    new_project_type_key: Literal['software', 'service_desk', 'business'] = Field(..., description='The key of the new project type.')
    model_config = ConfigDict(extra='forbid')

class UpdateProjectTypeToolOutput(Project):
    """Output for tool `update_project_type`."""
    pass

class UpdateRemoteIssueLinkToolInput(BaseModel):
    """Input for tool `update_remote_issue_link`."""
    issue_id_or_key: str = Field(..., description='The ID or key of the issue.')
    link_id: str = Field(..., description='The ID of the remote issue link.')
    body: RemoteIssueLinkRequest = Field(..., description='Request body for `update_remote_issue_link`.')
    model_config = ConfigDict(extra='forbid')

class UpdateRemoteIssueLinkToolOutput(RootModel[dict[str, object]]):
    """Output for tool `update_remote_issue_link`."""
    pass

class UpdateResolutionToolInput(BaseModel):
    """Input for tool `update_resolution`."""
    id: str = Field(..., description='The ID of the issue resolution.')
    body: UpdateResolutionDetails = Field(..., description='Request body for `update_resolution`.')
    model_config = ConfigDict(extra='forbid')

class UpdateResolutionToolOutput(RootModel[dict[str, object]]):
    """Output for tool `update_resolution`."""
    pass

class UpdateScreenToolInput(BaseModel):
    """Input for tool `update_screen`."""
    screen_id: int = Field(..., description='The ID of the screen.')
    body: UpdateScreenDetails = Field(..., description='Request body for `update_screen`.')
    model_config = ConfigDict(extra='forbid')

class UpdateScreenToolOutput(Screen):
    """Output for tool `update_screen`."""
    pass

class UpdateScreenSchemeToolInput(BaseModel):
    """Input for tool `update_screen_scheme`."""
    screen_scheme_id: str = Field(..., description='The ID of the screen scheme.')
    body: UpdateScreenSchemeDetails = Field(..., description='Request body for `update_screen_scheme`.')
    model_config = ConfigDict(extra='forbid')

class UpdateScreenSchemeToolOutput(RootModel[dict[str, object]]):
    """Output for tool `update_screen_scheme`."""
    pass

class UpdateStatusesToolInput(BaseModel):
    """Input for tool `update_statuses`."""
    body: StatusUpdateRequest = Field(..., description='Request body for `update_statuses`.')
    model_config = ConfigDict(extra='forbid')

class UpdateStatusesToolOutput(RootModel[dict[str, object]]):
    """Output for tool `update_statuses`."""
    pass

class UpdateUiModificationToolInput(BaseModel):
    """Input for tool `update_ui_modification`."""
    ui_modification_id: str = Field(..., description='The ID of the UI modification.')
    body: UpdateUiModificationDetails = Field(..., description='Request body for `update_ui_modification`.')
    model_config = ConfigDict(extra='forbid')

class UpdateUiModificationToolOutput(RootModel[dict[str, object]]):
    """Output for tool `update_ui_modification`."""
    pass

class UpdateVersionToolInput(BaseModel):
    """Input for tool `update_version`."""
    id: str = Field(..., description='The ID of the version.')
    body: Version = Field(..., description='Request body for `update_version`.')
    model_config = ConfigDict(extra='forbid')

class UpdateVersionToolOutput(Version):
    """Output for tool `update_version`."""
    pass

class UpdateWorkflowMappingToolInput(BaseModel):
    """Input for tool `update_workflow_mapping`."""
    id: int = Field(..., description='The ID of the workflow scheme.')
    workflow_name: str = Field(..., description='The name of the workflow.')
    body: IssueTypesWorkflowMapping = Field(..., description='Request body for `update_workflow_mapping`.')
    model_config = ConfigDict(extra='forbid')

class UpdateWorkflowMappingToolOutput(WorkflowScheme):
    """Output for tool `update_workflow_mapping`."""
    pass

class UpdateWorkflowSchemeToolInput(BaseModel):
    """Input for tool `update_workflow_scheme`."""
    id: int = Field(..., description='The ID of the workflow scheme. Find this ID by editing the desired workflow scheme in Jira. The ID is shown in the URL as `schemeId`. For example, *schemeId=10301*.')
    body: WorkflowScheme = Field(..., description='Request body for `update_workflow_scheme`.')
    model_config = ConfigDict(extra='forbid')

class UpdateWorkflowSchemeToolOutput(WorkflowScheme):
    """Output for tool `update_workflow_scheme`."""
    pass

class UpdateWorkflowSchemeDraftToolInput(BaseModel):
    """Input for tool `update_workflow_scheme_draft`."""
    id: int = Field(..., description='The ID of the active workflow scheme that the draft was created from.')
    body: WorkflowScheme = Field(..., description='Request body for `update_workflow_scheme_draft`.')
    model_config = ConfigDict(extra='forbid')

class UpdateWorkflowSchemeDraftToolOutput(WorkflowScheme):
    """Output for tool `update_workflow_scheme_draft`."""
    pass

class UpdateWorkflowTransitionPropertyToolInput(BaseModel):
    """Input for tool `update_workflow_transition_property`."""
    transition_id: int = Field(..., description='The ID of the transition. To get the ID, view the workflow in text mode in the Jira admin settings. The ID is shown next to the transition.')
    workflow_name: str = Field(..., description='The name of the workflow that the transition belongs to.')
    workflow_mode: Literal['live', 'draft'] | None = Field(default=None, description='The workflow status. Set to `live` for inactive workflows or `draft` for draft workflows. Active workflows cannot be edited.')
    body: WorkflowTransitionProperty = Field(..., description='Request body for `update_workflow_transition_property`.')
    model_config = ConfigDict(extra='forbid')

class UpdateWorkflowTransitionPropertyToolOutput(WorkflowTransitionProperty):
    """Output for tool `update_workflow_transition_property`."""
    pass

class UpdateWorkflowTransitionRuleConfigurationsToolInput(BaseModel):
    """Input for tool `update_workflow_transition_rule_configurations`."""
    body: WorkflowTransitionRulesUpdate = Field(..., description='Request body for `update_workflow_transition_rule_configurations`.')
    model_config = ConfigDict(extra='forbid')

class UpdateWorkflowTransitionRuleConfigurationsToolOutput(WorkflowTransitionRulesUpdateErrors):
    """Output for tool `update_workflow_transition_rule_configurations`."""
    pass

class UpdateWorklogToolInput(BaseModel):
    """Input for tool `update_worklog`."""
    issue_id_or_key: str = Field(..., description='The ID or key the issue.')
    id: str = Field(..., description='The ID of the worklog.')
    notify_users: bool | None = Field(default=None, description='Whether users watching the issue are notified by email.')
    adjust_estimate: Literal['new', 'leave', 'manual', 'auto'] | None = Field(default=None, description="Defines how to update the issue's time estimate, the options are:\n\n *  `new` Sets the estimate to a specific value, defined in `newEstimate`.\n *  `leave` Leaves the estimate unchanged.\n *  `auto` Updates the estimate by the difference between the original and updated value of `timeSpent` or `timeSpentSeconds`.")
    new_estimate: str | None = Field(default=None, description="The value to set as the issue's remaining time estimate, as days (\\#d), hours (\\#h), or minutes (\\#m or \\#). For example, *2d*. Required when `adjustEstimate` is `new`.")
    expand: str | None = Field(default=None, description='Use [expand](#expansion) to include additional information about worklogs in the response. This parameter accepts `properties`, which returns worklog properties.')
    override_editable_flag: bool | None = Field(default=None, description='Whether the worklog should be added to the issue even if the issue is not editable. For example, because the issue is closed. Connect and Forge app users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) can use this flag.')
    body: Worklog = Field(..., description='Request body for `update_worklog`.')
    model_config = ConfigDict(extra='forbid')

class UpdateWorklogToolOutput(Worklog):
    """Output for tool `update_worklog`."""
    pass

class ValidateProjectKeyToolInput(BaseModel):
    """Input for tool `validate_project_key`."""
    model_config = ConfigDict(extra='forbid')

class ValidateProjectKeyToolOutput(ErrorCollection):
    """Output for tool `validate_project_key`."""
    pass

INPUT_MODELS = {
    'add_actor_users': AddActorUsersToolInput,
    'add_attachment': AddAttachmentToolInput,
    'add_comment': AddCommentToolInput,
    'add_field_to_default_screen': AddFieldToDefaultScreenToolInput,
    'add_gadget': AddGadgetToolInput,
    'add_issue_types_to_context': AddIssueTypesToContextToolInput,
    'add_issue_types_to_issue_type_scheme': AddIssueTypesToIssueTypeSchemeToolInput,
    'add_notifications': AddNotificationsToolInput,
    'add_project_role_actors_to_role': AddProjectRoleActorsToRoleToolInput,
    'add_screen_tab': AddScreenTabToolInput,
    'add_screen_tab_field': AddScreenTabFieldToolInput,
    'add_share_permission': AddSharePermissionToolInput,
    'add_user_to_group': AddUserToGroupToolInput,
    'add_vote': AddVoteToolInput,
    'add_watcher': AddWatcherToolInput,
    'add_worklog': AddWorklogToolInput,
    'addon_properties_resource_delete_addon_property_delete': AddonPropertiesResourceDeleteAddonPropertyDeleteToolInput,
    'addon_properties_resource_get_addon_properties_get': AddonPropertiesResourceGetAddonPropertiesGetToolInput,
    'addon_properties_resource_get_addon_property_get': AddonPropertiesResourceGetAddonPropertyGetToolInput,
    'addon_properties_resource_put_addon_property_put': AddonPropertiesResourcePutAddonPropertyPutToolInput,
    'analyse_expression': AnalyseExpressionToolInput,
    'app_issue_field_value_update_resource_update_issue_fields_put': AppIssueFieldValueUpdateResourceUpdateIssueFieldsPutToolInput,
    'append_mappings_for_issue_type_screen_scheme': AppendMappingsForIssueTypeScreenSchemeToolInput,
    'archive_project': ArchiveProjectToolInput,
    'assign_field_configuration_scheme_to_project': AssignFieldConfigurationSchemeToProjectToolInput,
    'assign_issue': AssignIssueToolInput,
    'assign_issue_type_scheme_to_project': AssignIssueTypeSchemeToProjectToolInput,
    'assign_issue_type_screen_scheme_to_project': AssignIssueTypeScreenSchemeToProjectToolInput,
    'assign_permission_scheme': AssignPermissionSchemeToolInput,
    'assign_projects_to_custom_field_context': AssignProjectsToCustomFieldContextToolInput,
    'assign_scheme_to_project': AssignSchemeToProjectToolInput,
    'bulk_delete_issue_property': BulkDeleteIssuePropertyToolInput,
    'bulk_get_groups': BulkGetGroupsToolInput,
    'bulk_get_users': BulkGetUsersToolInput,
    'bulk_get_users_migration': BulkGetUsersMigrationToolInput,
    'bulk_set_issue_properties_by_issue': BulkSetIssuePropertiesByIssueToolInput,
    'bulk_set_issue_property': BulkSetIssuePropertyToolInput,
    'bulk_set_issues_properties_list': BulkSetIssuesPropertiesListToolInput,
    'cancel_task': CancelTaskToolInput,
    'change_filter_owner': ChangeFilterOwnerToolInput,
    'copy_dashboard': CopyDashboardToolInput,
    'create_component': CreateComponentToolInput,
    'create_custom_field': CreateCustomFieldToolInput,
    'create_custom_field_context': CreateCustomFieldContextToolInput,
    'create_custom_field_option': CreateCustomFieldOptionToolInput,
    'create_dashboard': CreateDashboardToolInput,
    'create_field_configuration': CreateFieldConfigurationToolInput,
    'create_field_configuration_scheme': CreateFieldConfigurationSchemeToolInput,
    'create_filter': CreateFilterToolInput,
    'create_group': CreateGroupToolInput,
    'create_issue': CreateIssueToolInput,
    'create_issue_field_option': CreateIssueFieldOptionToolInput,
    'create_issue_link_type': CreateIssueLinkTypeToolInput,
    'create_issue_type': CreateIssueTypeToolInput,
    'create_issue_type_avatar': CreateIssueTypeAvatarToolInput,
    'create_issue_type_scheme': CreateIssueTypeSchemeToolInput,
    'create_issue_type_screen_scheme': CreateIssueTypeScreenSchemeToolInput,
    'create_issues': CreateIssuesToolInput,
    'create_notification_scheme': CreateNotificationSchemeToolInput,
    'create_or_update_remote_issue_link': CreateOrUpdateRemoteIssueLinkToolInput,
    'create_permission_grant': CreatePermissionGrantToolInput,
    'create_permission_scheme': CreatePermissionSchemeToolInput,
    'create_priority': CreatePriorityToolInput,
    'create_project': CreateProjectToolInput,
    'create_project_avatar': CreateProjectAvatarToolInput,
    'create_project_category': CreateProjectCategoryToolInput,
    'create_project_role': CreateProjectRoleToolInput,
    'create_resolution': CreateResolutionToolInput,
    'create_screen': CreateScreenToolInput,
    'create_screen_scheme': CreateScreenSchemeToolInput,
    'create_statuses': CreateStatusesToolInput,
    'create_ui_modification': CreateUiModificationToolInput,
    'create_user': CreateUserToolInput,
    'create_version': CreateVersionToolInput,
    'create_workflow': CreateWorkflowToolInput,
    'create_workflow_scheme': CreateWorkflowSchemeToolInput,
    'create_workflow_scheme_draft_from_parent': CreateWorkflowSchemeDraftFromParentToolInput,
    'create_workflow_transition_property': CreateWorkflowTransitionPropertyToolInput,
    'delete_actor': DeleteActorToolInput,
    'delete_and_replace_version': DeleteAndReplaceVersionToolInput,
    'delete_avatar': DeleteAvatarToolInput,
    'delete_comment': DeleteCommentToolInput,
    'delete_comment_property': DeleteCommentPropertyToolInput,
    'delete_component': DeleteComponentToolInput,
    'delete_custom_field': DeleteCustomFieldToolInput,
    'delete_custom_field_context': DeleteCustomFieldContextToolInput,
    'delete_custom_field_option': DeleteCustomFieldOptionToolInput,
    'delete_dashboard': DeleteDashboardToolInput,
    'delete_dashboard_item_property': DeleteDashboardItemPropertyToolInput,
    'delete_default_workflow': DeleteDefaultWorkflowToolInput,
    'delete_draft_default_workflow': DeleteDraftDefaultWorkflowToolInput,
    'delete_draft_workflow_mapping': DeleteDraftWorkflowMappingToolInput,
    'delete_favourite_for_filter': DeleteFavouriteForFilterToolInput,
    'delete_field_configuration': DeleteFieldConfigurationToolInput,
    'delete_field_configuration_scheme': DeleteFieldConfigurationSchemeToolInput,
    'delete_filter': DeleteFilterToolInput,
    'delete_inactive_workflow': DeleteInactiveWorkflowToolInput,
    'delete_issue': DeleteIssueToolInput,
    'delete_issue_field_option': DeleteIssueFieldOptionToolInput,
    'delete_issue_link': DeleteIssueLinkToolInput,
    'delete_issue_link_type': DeleteIssueLinkTypeToolInput,
    'delete_issue_property': DeleteIssuePropertyToolInput,
    'delete_issue_type': DeleteIssueTypeToolInput,
    'delete_issue_type_property': DeleteIssueTypePropertyToolInput,
    'delete_issue_type_scheme': DeleteIssueTypeSchemeToolInput,
    'delete_issue_type_screen_scheme': DeleteIssueTypeScreenSchemeToolInput,
    'delete_locale': DeleteLocaleToolInput,
    'delete_notification_scheme': DeleteNotificationSchemeToolInput,
    'delete_permission_scheme': DeletePermissionSchemeToolInput,
    'delete_permission_scheme_entity': DeletePermissionSchemeEntityToolInput,
    'delete_priority': DeletePriorityToolInput,
    'delete_project': DeleteProjectToolInput,
    'delete_project_asynchronously': DeleteProjectAsynchronouslyToolInput,
    'delete_project_avatar': DeleteProjectAvatarToolInput,
    'delete_project_property': DeleteProjectPropertyToolInput,
    'delete_project_role': DeleteProjectRoleToolInput,
    'delete_project_role_actors_from_role': DeleteProjectRoleActorsFromRoleToolInput,
    'delete_remote_issue_link_by_global_id': DeleteRemoteIssueLinkByGlobalIdToolInput,
    'delete_remote_issue_link_by_id': DeleteRemoteIssueLinkByIdToolInput,
    'delete_resolution': DeleteResolutionToolInput,
    'delete_screen': DeleteScreenToolInput,
    'delete_screen_scheme': DeleteScreenSchemeToolInput,
    'delete_screen_tab': DeleteScreenTabToolInput,
    'delete_share_permission': DeleteSharePermissionToolInput,
    'delete_statuses_by_id': DeleteStatusesByIdToolInput,
    'delete_ui_modification': DeleteUiModificationToolInput,
    'delete_user_property': DeleteUserPropertyToolInput,
    'delete_version': DeleteVersionToolInput,
    'delete_webhook_by_id': DeleteWebhookByIdToolInput,
    'delete_workflow_mapping': DeleteWorkflowMappingToolInput,
    'delete_workflow_scheme': DeleteWorkflowSchemeToolInput,
    'delete_workflow_scheme_draft': DeleteWorkflowSchemeDraftToolInput,
    'delete_workflow_scheme_draft_issue_type': DeleteWorkflowSchemeDraftIssueTypeToolInput,
    'delete_workflow_scheme_issue_type': DeleteWorkflowSchemeIssueTypeToolInput,
    'delete_workflow_transition_property': DeleteWorkflowTransitionPropertyToolInput,
    'delete_workflow_transition_rule_configurations': DeleteWorkflowTransitionRuleConfigurationsToolInput,
    'delete_worklog': DeleteWorklogToolInput,
    'delete_worklog_property': DeleteWorklogPropertyToolInput,
    'do_transition': DoTransitionToolInput,
    'dynamic_modules_resource_get_modules_get': DynamicModulesResourceGetModulesGetToolInput,
    'dynamic_modules_resource_register_modules_post': DynamicModulesResourceRegisterModulesPostToolInput,
    'dynamic_modules_resource_remove_modules_delete': DynamicModulesResourceRemoveModulesDeleteToolInput,
    'edit_issue': EditIssueToolInput,
    'evaluate_jira_expression': EvaluateJiraExpressionToolInput,
    'expand_attachment_for_humans': ExpandAttachmentForHumansToolInput,
    'expand_attachment_for_machines': ExpandAttachmentForMachinesToolInput,
    'find_assignable_users': FindAssignableUsersToolInput,
    'find_bulk_assignable_users': FindBulkAssignableUsersToolInput,
    'find_groups': FindGroupsToolInput,
    'find_user_keys_by_query': FindUserKeysByQueryToolInput,
    'find_users': FindUsersToolInput,
    'find_users_and_groups': FindUsersAndGroupsToolInput,
    'find_users_by_query': FindUsersByQueryToolInput,
    'find_users_for_picker': FindUsersForPickerToolInput,
    'find_users_with_all_permissions': FindUsersWithAllPermissionsToolInput,
    'find_users_with_browse_permission': FindUsersWithBrowsePermissionToolInput,
    'fully_update_project_role': FullyUpdateProjectRoleToolInput,
    'get_accessible_project_type_by_key': GetAccessibleProjectTypeByKeyToolInput,
    'get_advanced_settings': GetAdvancedSettingsToolInput,
    'get_all_accessible_project_types': GetAllAccessibleProjectTypesToolInput,
    'get_all_application_roles': GetAllApplicationRolesToolInput,
    'get_all_available_dashboard_gadgets': GetAllAvailableDashboardGadgetsToolInput,
    'get_all_dashboards': GetAllDashboardsToolInput,
    'get_all_field_configuration_schemes': GetAllFieldConfigurationSchemesToolInput,
    'get_all_field_configurations': GetAllFieldConfigurationsToolInput,
    'get_all_gadgets': GetAllGadgetsToolInput,
    'get_all_issue_field_options': GetAllIssueFieldOptionsToolInput,
    'get_all_issue_type_schemes': GetAllIssueTypeSchemesToolInput,
    'get_all_labels': GetAllLabelsToolInput,
    'get_all_permission_schemes': GetAllPermissionSchemesToolInput,
    'get_all_permissions': GetAllPermissionsToolInput,
    'get_all_project_avatars': GetAllProjectAvatarsToolInput,
    'get_all_project_categories': GetAllProjectCategoriesToolInput,
    'get_all_project_roles': GetAllProjectRolesToolInput,
    'get_all_project_types': GetAllProjectTypesToolInput,
    'get_all_projects': GetAllProjectsToolInput,
    'get_all_screen_tab_fields': GetAllScreenTabFieldsToolInput,
    'get_all_screen_tabs': GetAllScreenTabsToolInput,
    'get_all_statuses': GetAllStatusesToolInput,
    'get_all_system_avatars': GetAllSystemAvatarsToolInput,
    'get_all_users': GetAllUsersToolInput,
    'get_all_users_default': GetAllUsersDefaultToolInput,
    'get_all_workflow_schemes': GetAllWorkflowSchemesToolInput,
    'get_all_workflows': GetAllWorkflowsToolInput,
    'get_alternative_issue_types': GetAlternativeIssueTypesToolInput,
    'get_application_property': GetApplicationPropertyToolInput,
    'get_application_role': GetApplicationRoleToolInput,
    'get_approximate_application_license_count': GetApproximateApplicationLicenseCountToolInput,
    'get_approximate_license_count': GetApproximateLicenseCountToolInput,
    'get_assigned_permission_scheme': GetAssignedPermissionSchemeToolInput,
    'get_attachment': GetAttachmentToolInput,
    'get_attachment_content': GetAttachmentContentToolInput,
    'get_attachment_meta': GetAttachmentMetaToolInput,
    'get_attachment_thumbnail': GetAttachmentThumbnailToolInput,
    'get_audit_records': GetAuditRecordsToolInput,
    'get_auto_complete': GetAutoCompleteToolInput,
    'get_auto_complete_post': GetAutoCompletePostToolInput,
    'get_available_screen_fields': GetAvailableScreenFieldsToolInput,
    'get_available_time_tracking_implementations': GetAvailableTimeTrackingImplementationsToolInput,
    'get_avatar_image_by_id': GetAvatarImageByIdToolInput,
    'get_avatar_image_by_owner': GetAvatarImageByOwnerToolInput,
    'get_avatar_image_by_type': GetAvatarImageByTypeToolInput,
    'get_avatars': GetAvatarsToolInput,
    'get_banner': GetBannerToolInput,
    'get_bulk_permissions': GetBulkPermissionsToolInput,
    'get_change_logs': GetChangeLogsToolInput,
    'get_change_logs_by_ids': GetChangeLogsByIdsToolInput,
    'get_columns': GetColumnsToolInput,
    'get_comment': GetCommentToolInput,
    'get_comment_property': GetCommentPropertyToolInput,
    'get_comment_property_keys': GetCommentPropertyKeysToolInput,
    'get_comments': GetCommentsToolInput,
    'get_comments_by_ids': GetCommentsByIdsToolInput,
    'get_component': GetComponentToolInput,
    'get_component_related_issues': GetComponentRelatedIssuesToolInput,
    'get_configuration': GetConfigurationToolInput,
    'get_contexts_for_field': GetContextsForFieldToolInput,
    'get_contexts_for_field_deprecated': GetContextsForFieldDeprecatedToolInput,
    'get_create_issue_meta': GetCreateIssueMetaToolInput,
    'get_current_user': GetCurrentUserToolInput,
    'get_custom_field_configuration': GetCustomFieldConfigurationToolInput,
    'get_custom_field_contexts_for_projects_and_issue_types': GetCustomFieldContextsForProjectsAndIssueTypesToolInput,
    'get_custom_field_option': GetCustomFieldOptionToolInput,
    'get_dashboard': GetDashboardToolInput,
    'get_dashboard_item_property': GetDashboardItemPropertyToolInput,
    'get_dashboard_item_property_keys': GetDashboardItemPropertyKeysToolInput,
    'get_dashboards_paginated': GetDashboardsPaginatedToolInput,
    'get_default_share_scope': GetDefaultShareScopeToolInput,
    'get_default_values': GetDefaultValuesToolInput,
    'get_default_workflow': GetDefaultWorkflowToolInput,
    'get_draft_default_workflow': GetDraftDefaultWorkflowToolInput,
    'get_draft_workflow': GetDraftWorkflowToolInput,
    'get_dynamic_webhooks_for_app': GetDynamicWebhooksForAppToolInput,
    'get_edit_issue_meta': GetEditIssueMetaToolInput,
    'get_events': GetEventsToolInput,
    'get_failed_webhooks': GetFailedWebhooksToolInput,
    'get_favourite_filters': GetFavouriteFiltersToolInput,
    'get_features_for_project': GetFeaturesForProjectToolInput,
    'get_field_auto_complete_for_query_string': GetFieldAutoCompleteForQueryStringToolInput,
    'get_field_configuration_items': GetFieldConfigurationItemsToolInput,
    'get_field_configuration_scheme_mappings': GetFieldConfigurationSchemeMappingsToolInput,
    'get_field_configuration_scheme_project_mapping': GetFieldConfigurationSchemeProjectMappingToolInput,
    'get_fields': GetFieldsToolInput,
    'get_fields_paginated': GetFieldsPaginatedToolInput,
    'get_filter': GetFilterToolInput,
    'get_filters': GetFiltersToolInput,
    'get_filters_paginated': GetFiltersPaginatedToolInput,
    'get_group': GetGroupToolInput,
    'get_hierarchy': GetHierarchyToolInput,
    'get_ids_of_worklogs_deleted_since': GetIdsOfWorklogsDeletedSinceToolInput,
    'get_ids_of_worklogs_modified_since': GetIdsOfWorklogsModifiedSinceToolInput,
    'get_is_watching_issue_bulk': GetIsWatchingIssueBulkToolInput,
    'get_issue': GetIssueToolInput,
    'get_issue_all_types': GetIssueAllTypesToolInput,
    'get_issue_field_option': GetIssueFieldOptionToolInput,
    'get_issue_link': GetIssueLinkToolInput,
    'get_issue_link_type': GetIssueLinkTypeToolInput,
    'get_issue_link_types': GetIssueLinkTypesToolInput,
    'get_issue_navigator_default_columns': GetIssueNavigatorDefaultColumnsToolInput,
    'get_issue_picker_resource': GetIssuePickerResourceToolInput,
    'get_issue_property': GetIssuePropertyToolInput,
    'get_issue_property_keys': GetIssuePropertyKeysToolInput,
    'get_issue_security_level': GetIssueSecurityLevelToolInput,
    'get_issue_security_level_members': GetIssueSecurityLevelMembersToolInput,
    'get_issue_security_scheme': GetIssueSecuritySchemeToolInput,
    'get_issue_security_schemes': GetIssueSecuritySchemesToolInput,
    'get_issue_type': GetIssueTypeToolInput,
    'get_issue_type_mappings_for_contexts': GetIssueTypeMappingsForContextsToolInput,
    'get_issue_type_property': GetIssueTypePropertyToolInput,
    'get_issue_type_property_keys': GetIssueTypePropertyKeysToolInput,
    'get_issue_type_scheme_for_projects': GetIssueTypeSchemeForProjectsToolInput,
    'get_issue_type_schemes_mapping': GetIssueTypeSchemesMappingToolInput,
    'get_issue_type_screen_scheme_mappings': GetIssueTypeScreenSchemeMappingsToolInput,
    'get_issue_type_screen_scheme_project_associations': GetIssueTypeScreenSchemeProjectAssociationsToolInput,
    'get_issue_type_screen_schemes': GetIssueTypeScreenSchemesToolInput,
    'get_issue_types_for_project': GetIssueTypesForProjectToolInput,
    'get_issue_watchers': GetIssueWatchersToolInput,
    'get_issue_worklog': GetIssueWorklogToolInput,
    'get_license': GetLicenseToolInput,
    'get_locale': GetLocaleToolInput,
    'get_my_filters': GetMyFiltersToolInput,
    'get_my_permissions': GetMyPermissionsToolInput,
    'get_notification_scheme': GetNotificationSchemeToolInput,
    'get_notification_scheme_for_project': GetNotificationSchemeForProjectToolInput,
    'get_notification_scheme_to_project_mappings': GetNotificationSchemeToProjectMappingsToolInput,
    'get_notification_schemes': GetNotificationSchemesToolInput,
    'get_options_for_context': GetOptionsForContextToolInput,
    'get_permission_scheme': GetPermissionSchemeToolInput,
    'get_permission_scheme_grant': GetPermissionSchemeGrantToolInput,
    'get_permission_scheme_grants': GetPermissionSchemeGrantsToolInput,
    'get_permitted_projects': GetPermittedProjectsToolInput,
    'get_precomputations': GetPrecomputationsToolInput,
    'get_preference': GetPreferenceToolInput,
    'get_priorities': GetPrioritiesToolInput,
    'get_priority': GetPriorityToolInput,
    'get_project': GetProjectToolInput,
    'get_project_category_by_id': GetProjectCategoryByIdToolInput,
    'get_project_components': GetProjectComponentsToolInput,
    'get_project_components_paginated': GetProjectComponentsPaginatedToolInput,
    'get_project_context_mapping': GetProjectContextMappingToolInput,
    'get_project_email': GetProjectEmailToolInput,
    'get_project_issue_security_scheme': GetProjectIssueSecuritySchemeToolInput,
    'get_project_property': GetProjectPropertyToolInput,
    'get_project_property_keys': GetProjectPropertyKeysToolInput,
    'get_project_role': GetProjectRoleToolInput,
    'get_project_role_actors_for_role': GetProjectRoleActorsForRoleToolInput,
    'get_project_role_by_id': GetProjectRoleByIdToolInput,
    'get_project_role_details': GetProjectRoleDetailsToolInput,
    'get_project_roles': GetProjectRolesToolInput,
    'get_project_type_by_key': GetProjectTypeByKeyToolInput,
    'get_project_versions': GetProjectVersionsToolInput,
    'get_project_versions_paginated': GetProjectVersionsPaginatedToolInput,
    'get_projects_for_issue_type_screen_scheme': GetProjectsForIssueTypeScreenSchemeToolInput,
    'get_recent': GetRecentToolInput,
    'get_remote_issue_link_by_id': GetRemoteIssueLinkByIdToolInput,
    'get_remote_issue_links': GetRemoteIssueLinksToolInput,
    'get_resolution': GetResolutionToolInput,
    'get_resolutions': GetResolutionsToolInput,
    'get_screen_schemes': GetScreenSchemesToolInput,
    'get_screens': GetScreensToolInput,
    'get_screens_for_field': GetScreensForFieldToolInput,
    'get_security_levels_for_project': GetSecurityLevelsForProjectToolInput,
    'get_selectable_issue_field_options': GetSelectableIssueFieldOptionsToolInput,
    'get_selected_time_tracking_implementation': GetSelectedTimeTrackingImplementationToolInput,
    'get_server_info': GetServerInfoToolInput,
    'get_share_permission': GetSharePermissionToolInput,
    'get_share_permissions': GetSharePermissionsToolInput,
    'get_shared_time_tracking_configuration': GetSharedTimeTrackingConfigurationToolInput,
    'get_status': GetStatusToolInput,
    'get_status_categories': GetStatusCategoriesToolInput,
    'get_status_category': GetStatusCategoryToolInput,
    'get_statuses': GetStatusesToolInput,
    'get_statuses_by_id': GetStatusesByIdToolInput,
    'get_task': GetTaskToolInput,
    'get_transitions': GetTransitionsToolInput,
    'get_trashed_fields_paginated': GetTrashedFieldsPaginatedToolInput,
    'get_ui_modifications': GetUiModificationsToolInput,
    'get_user': GetUserToolInput,
    'get_user_default_columns': GetUserDefaultColumnsToolInput,
    'get_user_email': GetUserEmailToolInput,
    'get_user_email_bulk': GetUserEmailBulkToolInput,
    'get_user_groups': GetUserGroupsToolInput,
    'get_user_property': GetUserPropertyToolInput,
    'get_user_property_keys': GetUserPropertyKeysToolInput,
    'get_users_from_group': GetUsersFromGroupToolInput,
    'get_valid_project_key': GetValidProjectKeyToolInput,
    'get_valid_project_name': GetValidProjectNameToolInput,
    'get_version': GetVersionToolInput,
    'get_version_related_issues': GetVersionRelatedIssuesToolInput,
    'get_version_unresolved_issues': GetVersionUnresolvedIssuesToolInput,
    'get_visible_issue_field_options': GetVisibleIssueFieldOptionsToolInput,
    'get_votes': GetVotesToolInput,
    'get_workflow': GetWorkflowToolInput,
    'get_workflow_scheme': GetWorkflowSchemeToolInput,
    'get_workflow_scheme_draft': GetWorkflowSchemeDraftToolInput,
    'get_workflow_scheme_draft_issue_type': GetWorkflowSchemeDraftIssueTypeToolInput,
    'get_workflow_scheme_issue_type': GetWorkflowSchemeIssueTypeToolInput,
    'get_workflow_scheme_project_associations': GetWorkflowSchemeProjectAssociationsToolInput,
    'get_workflow_transition_properties': GetWorkflowTransitionPropertiesToolInput,
    'get_workflow_transition_rule_configurations': GetWorkflowTransitionRuleConfigurationsToolInput,
    'get_workflows_paginated': GetWorkflowsPaginatedToolInput,
    'get_worklog': GetWorklogToolInput,
    'get_worklog_property': GetWorklogPropertyToolInput,
    'get_worklog_property_keys': GetWorklogPropertyKeysToolInput,
    'get_worklogs_for_ids': GetWorklogsForIdsToolInput,
    'link_issues': LinkIssuesToolInput,
    'match_issues': MatchIssuesToolInput,
    'merge_versions': MergeVersionsToolInput,
    'migrate_queries': MigrateQueriesToolInput,
    'migration_resource_update_entity_properties_value_put': MigrationResourceUpdateEntityPropertiesValuePutToolInput,
    'migration_resource_workflow_rule_search_post': MigrationResourceWorkflowRuleSearchPostToolInput,
    'move_priorities': MovePrioritiesToolInput,
    'move_resolutions': MoveResolutionsToolInput,
    'move_screen_tab': MoveScreenTabToolInput,
    'move_screen_tab_field': MoveScreenTabFieldToolInput,
    'move_version': MoveVersionToolInput,
    'notify': NotifyToolInput,
    'parse_jql_queries': ParseJqlQueriesToolInput,
    'partial_update_project_role': PartialUpdateProjectRoleToolInput,
    'publish_draft_workflow_scheme': PublishDraftWorkflowSchemeToolInput,
    'refresh_webhooks': RefreshWebhooksToolInput,
    'register_dynamic_webhooks': RegisterDynamicWebhooksToolInput,
    'remove_attachment': RemoveAttachmentToolInput,
    'remove_custom_field_context_from_projects': RemoveCustomFieldContextFromProjectsToolInput,
    'remove_gadget': RemoveGadgetToolInput,
    'remove_group': RemoveGroupToolInput,
    'remove_issue_type_from_issue_type_scheme': RemoveIssueTypeFromIssueTypeSchemeToolInput,
    'remove_issue_types_from_context': RemoveIssueTypesFromContextToolInput,
    'remove_issue_types_from_global_field_configuration_scheme': RemoveIssueTypesFromGlobalFieldConfigurationSchemeToolInput,
    'remove_mappings_from_issue_type_screen_scheme': RemoveMappingsFromIssueTypeScreenSchemeToolInput,
    'remove_notification_from_notification_scheme': RemoveNotificationFromNotificationSchemeToolInput,
    'remove_preference': RemovePreferenceToolInput,
    'remove_project_category': RemoveProjectCategoryToolInput,
    'remove_screen_tab_field': RemoveScreenTabFieldToolInput,
    'remove_user': RemoveUserToolInput,
    'remove_user_from_group': RemoveUserFromGroupToolInput,
    'remove_vote': RemoveVoteToolInput,
    'remove_watcher': RemoveWatcherToolInput,
    'rename_screen_tab': RenameScreenTabToolInput,
    'reorder_custom_field_options': ReorderCustomFieldOptionsToolInput,
    'reorder_issue_types_in_issue_type_scheme': ReorderIssueTypesInIssueTypeSchemeToolInput,
    'replace_issue_field_option': ReplaceIssueFieldOptionToolInput,
    'reset_columns': ResetColumnsToolInput,
    'reset_user_columns': ResetUserColumnsToolInput,
    'restore': RestoreToolInput,
    'restore_custom_field': RestoreCustomFieldToolInput,
    'sanitise_jql_queries': SanitiseJqlQueriesToolInput,
    'search': SearchToolInput,
    'search_for_issues_using_jql': SearchForIssuesUsingJqlToolInput,
    'search_for_issues_using_jql_post': SearchForIssuesUsingJqlPostToolInput,
    'search_priorities': SearchPrioritiesToolInput,
    'search_projects': SearchProjectsToolInput,
    'search_resolutions': SearchResolutionsToolInput,
    'select_time_tracking_implementation': SelectTimeTrackingImplementationToolInput,
    'set_actors': SetActorsToolInput,
    'set_application_property': SetApplicationPropertyToolInput,
    'set_banner': SetBannerToolInput,
    'set_columns': SetColumnsToolInput,
    'set_comment_property': SetCommentPropertyToolInput,
    'set_dashboard_item_property': SetDashboardItemPropertyToolInput,
    'set_default_priority': SetDefaultPriorityToolInput,
    'set_default_resolution': SetDefaultResolutionToolInput,
    'set_default_share_scope': SetDefaultShareScopeToolInput,
    'set_default_values': SetDefaultValuesToolInput,
    'set_favourite_for_filter': SetFavouriteForFilterToolInput,
    'set_field_configuration_scheme_mapping': SetFieldConfigurationSchemeMappingToolInput,
    'set_issue_navigator_default_columns': SetIssueNavigatorDefaultColumnsToolInput,
    'set_issue_property': SetIssuePropertyToolInput,
    'set_issue_type_property': SetIssueTypePropertyToolInput,
    'set_locale': SetLocaleToolInput,
    'set_preference': SetPreferenceToolInput,
    'set_project_property': SetProjectPropertyToolInput,
    'set_shared_time_tracking_configuration': SetSharedTimeTrackingConfigurationToolInput,
    'set_user_columns': SetUserColumnsToolInput,
    'set_user_property': SetUserPropertyToolInput,
    'set_workflow_scheme_draft_issue_type': SetWorkflowSchemeDraftIssueTypeToolInput,
    'set_workflow_scheme_issue_type': SetWorkflowSchemeIssueTypeToolInput,
    'set_worklog_property': SetWorklogPropertyToolInput,
    'store_avatar': StoreAvatarToolInput,
    'toggle_feature_for_project': ToggleFeatureForProjectToolInput,
    'trash_custom_field': TrashCustomFieldToolInput,
    'update_comment': UpdateCommentToolInput,
    'update_component': UpdateComponentToolInput,
    'update_custom_field': UpdateCustomFieldToolInput,
    'update_custom_field_configuration': UpdateCustomFieldConfigurationToolInput,
    'update_custom_field_context': UpdateCustomFieldContextToolInput,
    'update_custom_field_option': UpdateCustomFieldOptionToolInput,
    'update_custom_field_value': UpdateCustomFieldValueToolInput,
    'update_dashboard': UpdateDashboardToolInput,
    'update_default_screen_scheme': UpdateDefaultScreenSchemeToolInput,
    'update_default_workflow': UpdateDefaultWorkflowToolInput,
    'update_draft_default_workflow': UpdateDraftDefaultWorkflowToolInput,
    'update_draft_workflow_mapping': UpdateDraftWorkflowMappingToolInput,
    'update_field_configuration': UpdateFieldConfigurationToolInput,
    'update_field_configuration_items': UpdateFieldConfigurationItemsToolInput,
    'update_field_configuration_scheme': UpdateFieldConfigurationSchemeToolInput,
    'update_filter': UpdateFilterToolInput,
    'update_gadget': UpdateGadgetToolInput,
    'update_issue_field_option': UpdateIssueFieldOptionToolInput,
    'update_issue_link_type': UpdateIssueLinkTypeToolInput,
    'update_issue_type': UpdateIssueTypeToolInput,
    'update_issue_type_scheme': UpdateIssueTypeSchemeToolInput,
    'update_issue_type_screen_scheme': UpdateIssueTypeScreenSchemeToolInput,
    'update_multiple_custom_field_values': UpdateMultipleCustomFieldValuesToolInput,
    'update_notification_scheme': UpdateNotificationSchemeToolInput,
    'update_permission_scheme': UpdatePermissionSchemeToolInput,
    'update_precomputations': UpdatePrecomputationsToolInput,
    'update_priority': UpdatePriorityToolInput,
    'update_project': UpdateProjectToolInput,
    'update_project_avatar': UpdateProjectAvatarToolInput,
    'update_project_category': UpdateProjectCategoryToolInput,
    'update_project_email': UpdateProjectEmailToolInput,
    'update_project_type': UpdateProjectTypeToolInput,
    'update_remote_issue_link': UpdateRemoteIssueLinkToolInput,
    'update_resolution': UpdateResolutionToolInput,
    'update_screen': UpdateScreenToolInput,
    'update_screen_scheme': UpdateScreenSchemeToolInput,
    'update_statuses': UpdateStatusesToolInput,
    'update_ui_modification': UpdateUiModificationToolInput,
    'update_version': UpdateVersionToolInput,
    'update_workflow_mapping': UpdateWorkflowMappingToolInput,
    'update_workflow_scheme': UpdateWorkflowSchemeToolInput,
    'update_workflow_scheme_draft': UpdateWorkflowSchemeDraftToolInput,
    'update_workflow_transition_property': UpdateWorkflowTransitionPropertyToolInput,
    'update_workflow_transition_rule_configurations': UpdateWorkflowTransitionRuleConfigurationsToolInput,
    'update_worklog': UpdateWorklogToolInput,
    'validate_project_key': ValidateProjectKeyToolInput,
}

OUTPUT_MODELS = {
    'add_actor_users': AddActorUsersToolOutput,
    'add_attachment': AddAttachmentToolOutput,
    'add_comment': AddCommentToolOutput,
    'add_field_to_default_screen': AddFieldToDefaultScreenToolOutput,
    'add_gadget': AddGadgetToolOutput,
    'add_issue_types_to_context': AddIssueTypesToContextToolOutput,
    'add_issue_types_to_issue_type_scheme': AddIssueTypesToIssueTypeSchemeToolOutput,
    'add_notifications': AddNotificationsToolOutput,
    'add_project_role_actors_to_role': AddProjectRoleActorsToRoleToolOutput,
    'add_screen_tab': AddScreenTabToolOutput,
    'add_screen_tab_field': AddScreenTabFieldToolOutput,
    'add_share_permission': AddSharePermissionToolOutput,
    'add_user_to_group': AddUserToGroupToolOutput,
    'add_vote': AddVoteToolOutput,
    'add_watcher': AddWatcherToolOutput,
    'add_worklog': AddWorklogToolOutput,
    'addon_properties_resource_delete_addon_property_delete': AddonPropertiesResourceDeleteAddonPropertyDeleteToolOutput,
    'addon_properties_resource_get_addon_properties_get': AddonPropertiesResourceGetAddonPropertiesGetToolOutput,
    'addon_properties_resource_get_addon_property_get': AddonPropertiesResourceGetAddonPropertyGetToolOutput,
    'addon_properties_resource_put_addon_property_put': AddonPropertiesResourcePutAddonPropertyPutToolOutput,
    'analyse_expression': AnalyseExpressionToolOutput,
    'app_issue_field_value_update_resource_update_issue_fields_put': AppIssueFieldValueUpdateResourceUpdateIssueFieldsPutToolOutput,
    'append_mappings_for_issue_type_screen_scheme': AppendMappingsForIssueTypeScreenSchemeToolOutput,
    'archive_project': ArchiveProjectToolOutput,
    'assign_field_configuration_scheme_to_project': AssignFieldConfigurationSchemeToProjectToolOutput,
    'assign_issue': AssignIssueToolOutput,
    'assign_issue_type_scheme_to_project': AssignIssueTypeSchemeToProjectToolOutput,
    'assign_issue_type_screen_scheme_to_project': AssignIssueTypeScreenSchemeToProjectToolOutput,
    'assign_permission_scheme': AssignPermissionSchemeToolOutput,
    'assign_projects_to_custom_field_context': AssignProjectsToCustomFieldContextToolOutput,
    'assign_scheme_to_project': AssignSchemeToProjectToolOutput,
    'bulk_delete_issue_property': BulkDeleteIssuePropertyToolOutput,
    'bulk_get_groups': BulkGetGroupsToolOutput,
    'bulk_get_users': BulkGetUsersToolOutput,
    'bulk_get_users_migration': BulkGetUsersMigrationToolOutput,
    'bulk_set_issue_properties_by_issue': BulkSetIssuePropertiesByIssueToolOutput,
    'bulk_set_issue_property': BulkSetIssuePropertyToolOutput,
    'bulk_set_issues_properties_list': BulkSetIssuesPropertiesListToolOutput,
    'cancel_task': CancelTaskToolOutput,
    'change_filter_owner': ChangeFilterOwnerToolOutput,
    'copy_dashboard': CopyDashboardToolOutput,
    'create_component': CreateComponentToolOutput,
    'create_custom_field': CreateCustomFieldToolOutput,
    'create_custom_field_context': CreateCustomFieldContextToolOutput,
    'create_custom_field_option': CreateCustomFieldOptionToolOutput,
    'create_dashboard': CreateDashboardToolOutput,
    'create_field_configuration': CreateFieldConfigurationToolOutput,
    'create_field_configuration_scheme': CreateFieldConfigurationSchemeToolOutput,
    'create_filter': CreateFilterToolOutput,
    'create_group': CreateGroupToolOutput,
    'create_issue': CreateIssueToolOutput,
    'create_issue_field_option': CreateIssueFieldOptionToolOutput,
    'create_issue_link_type': CreateIssueLinkTypeToolOutput,
    'create_issue_type': CreateIssueTypeToolOutput,
    'create_issue_type_avatar': CreateIssueTypeAvatarToolOutput,
    'create_issue_type_scheme': CreateIssueTypeSchemeToolOutput,
    'create_issue_type_screen_scheme': CreateIssueTypeScreenSchemeToolOutput,
    'create_issues': CreateIssuesToolOutput,
    'create_notification_scheme': CreateNotificationSchemeToolOutput,
    'create_or_update_remote_issue_link': CreateOrUpdateRemoteIssueLinkToolOutput,
    'create_permission_grant': CreatePermissionGrantToolOutput,
    'create_permission_scheme': CreatePermissionSchemeToolOutput,
    'create_priority': CreatePriorityToolOutput,
    'create_project': CreateProjectToolOutput,
    'create_project_avatar': CreateProjectAvatarToolOutput,
    'create_project_category': CreateProjectCategoryToolOutput,
    'create_project_role': CreateProjectRoleToolOutput,
    'create_resolution': CreateResolutionToolOutput,
    'create_screen': CreateScreenToolOutput,
    'create_screen_scheme': CreateScreenSchemeToolOutput,
    'create_statuses': CreateStatusesToolOutput,
    'create_ui_modification': CreateUiModificationToolOutput,
    'create_user': CreateUserToolOutput,
    'create_version': CreateVersionToolOutput,
    'create_workflow': CreateWorkflowToolOutput,
    'create_workflow_scheme': CreateWorkflowSchemeToolOutput,
    'create_workflow_scheme_draft_from_parent': CreateWorkflowSchemeDraftFromParentToolOutput,
    'create_workflow_transition_property': CreateWorkflowTransitionPropertyToolOutput,
    'delete_actor': DeleteActorToolOutput,
    'delete_and_replace_version': DeleteAndReplaceVersionToolOutput,
    'delete_avatar': DeleteAvatarToolOutput,
    'delete_comment': DeleteCommentToolOutput,
    'delete_comment_property': DeleteCommentPropertyToolOutput,
    'delete_component': DeleteComponentToolOutput,
    'delete_custom_field': DeleteCustomFieldToolOutput,
    'delete_custom_field_context': DeleteCustomFieldContextToolOutput,
    'delete_custom_field_option': DeleteCustomFieldOptionToolOutput,
    'delete_dashboard': DeleteDashboardToolOutput,
    'delete_dashboard_item_property': DeleteDashboardItemPropertyToolOutput,
    'delete_default_workflow': DeleteDefaultWorkflowToolOutput,
    'delete_draft_default_workflow': DeleteDraftDefaultWorkflowToolOutput,
    'delete_draft_workflow_mapping': DeleteDraftWorkflowMappingToolOutput,
    'delete_favourite_for_filter': DeleteFavouriteForFilterToolOutput,
    'delete_field_configuration': DeleteFieldConfigurationToolOutput,
    'delete_field_configuration_scheme': DeleteFieldConfigurationSchemeToolOutput,
    'delete_filter': DeleteFilterToolOutput,
    'delete_inactive_workflow': DeleteInactiveWorkflowToolOutput,
    'delete_issue': DeleteIssueToolOutput,
    'delete_issue_field_option': DeleteIssueFieldOptionToolOutput,
    'delete_issue_link': DeleteIssueLinkToolOutput,
    'delete_issue_link_type': DeleteIssueLinkTypeToolOutput,
    'delete_issue_property': DeleteIssuePropertyToolOutput,
    'delete_issue_type': DeleteIssueTypeToolOutput,
    'delete_issue_type_property': DeleteIssueTypePropertyToolOutput,
    'delete_issue_type_scheme': DeleteIssueTypeSchemeToolOutput,
    'delete_issue_type_screen_scheme': DeleteIssueTypeScreenSchemeToolOutput,
    'delete_locale': DeleteLocaleToolOutput,
    'delete_notification_scheme': DeleteNotificationSchemeToolOutput,
    'delete_permission_scheme': DeletePermissionSchemeToolOutput,
    'delete_permission_scheme_entity': DeletePermissionSchemeEntityToolOutput,
    'delete_priority': DeletePriorityToolOutput,
    'delete_project': DeleteProjectToolOutput,
    'delete_project_asynchronously': DeleteProjectAsynchronouslyToolOutput,
    'delete_project_avatar': DeleteProjectAvatarToolOutput,
    'delete_project_property': DeleteProjectPropertyToolOutput,
    'delete_project_role': DeleteProjectRoleToolOutput,
    'delete_project_role_actors_from_role': DeleteProjectRoleActorsFromRoleToolOutput,
    'delete_remote_issue_link_by_global_id': DeleteRemoteIssueLinkByGlobalIdToolOutput,
    'delete_remote_issue_link_by_id': DeleteRemoteIssueLinkByIdToolOutput,
    'delete_resolution': DeleteResolutionToolOutput,
    'delete_screen': DeleteScreenToolOutput,
    'delete_screen_scheme': DeleteScreenSchemeToolOutput,
    'delete_screen_tab': DeleteScreenTabToolOutput,
    'delete_share_permission': DeleteSharePermissionToolOutput,
    'delete_statuses_by_id': DeleteStatusesByIdToolOutput,
    'delete_ui_modification': DeleteUiModificationToolOutput,
    'delete_user_property': DeleteUserPropertyToolOutput,
    'delete_version': DeleteVersionToolOutput,
    'delete_webhook_by_id': DeleteWebhookByIdToolOutput,
    'delete_workflow_mapping': DeleteWorkflowMappingToolOutput,
    'delete_workflow_scheme': DeleteWorkflowSchemeToolOutput,
    'delete_workflow_scheme_draft': DeleteWorkflowSchemeDraftToolOutput,
    'delete_workflow_scheme_draft_issue_type': DeleteWorkflowSchemeDraftIssueTypeToolOutput,
    'delete_workflow_scheme_issue_type': DeleteWorkflowSchemeIssueTypeToolOutput,
    'delete_workflow_transition_property': DeleteWorkflowTransitionPropertyToolOutput,
    'delete_workflow_transition_rule_configurations': DeleteWorkflowTransitionRuleConfigurationsToolOutput,
    'delete_worklog': DeleteWorklogToolOutput,
    'delete_worklog_property': DeleteWorklogPropertyToolOutput,
    'do_transition': DoTransitionToolOutput,
    'dynamic_modules_resource_get_modules_get': DynamicModulesResourceGetModulesGetToolOutput,
    'dynamic_modules_resource_register_modules_post': DynamicModulesResourceRegisterModulesPostToolOutput,
    'dynamic_modules_resource_remove_modules_delete': DynamicModulesResourceRemoveModulesDeleteToolOutput,
    'edit_issue': EditIssueToolOutput,
    'evaluate_jira_expression': EvaluateJiraExpressionToolOutput,
    'expand_attachment_for_humans': ExpandAttachmentForHumansToolOutput,
    'expand_attachment_for_machines': ExpandAttachmentForMachinesToolOutput,
    'find_assignable_users': FindAssignableUsersToolOutput,
    'find_bulk_assignable_users': FindBulkAssignableUsersToolOutput,
    'find_groups': FindGroupsToolOutput,
    'find_user_keys_by_query': FindUserKeysByQueryToolOutput,
    'find_users': FindUsersToolOutput,
    'find_users_and_groups': FindUsersAndGroupsToolOutput,
    'find_users_by_query': FindUsersByQueryToolOutput,
    'find_users_for_picker': FindUsersForPickerToolOutput,
    'find_users_with_all_permissions': FindUsersWithAllPermissionsToolOutput,
    'find_users_with_browse_permission': FindUsersWithBrowsePermissionToolOutput,
    'fully_update_project_role': FullyUpdateProjectRoleToolOutput,
    'get_accessible_project_type_by_key': GetAccessibleProjectTypeByKeyToolOutput,
    'get_advanced_settings': GetAdvancedSettingsToolOutput,
    'get_all_accessible_project_types': GetAllAccessibleProjectTypesToolOutput,
    'get_all_application_roles': GetAllApplicationRolesToolOutput,
    'get_all_available_dashboard_gadgets': GetAllAvailableDashboardGadgetsToolOutput,
    'get_all_dashboards': GetAllDashboardsToolOutput,
    'get_all_field_configuration_schemes': GetAllFieldConfigurationSchemesToolOutput,
    'get_all_field_configurations': GetAllFieldConfigurationsToolOutput,
    'get_all_gadgets': GetAllGadgetsToolOutput,
    'get_all_issue_field_options': GetAllIssueFieldOptionsToolOutput,
    'get_all_issue_type_schemes': GetAllIssueTypeSchemesToolOutput,
    'get_all_labels': GetAllLabelsToolOutput,
    'get_all_permission_schemes': GetAllPermissionSchemesToolOutput,
    'get_all_permissions': GetAllPermissionsToolOutput,
    'get_all_project_avatars': GetAllProjectAvatarsToolOutput,
    'get_all_project_categories': GetAllProjectCategoriesToolOutput,
    'get_all_project_roles': GetAllProjectRolesToolOutput,
    'get_all_project_types': GetAllProjectTypesToolOutput,
    'get_all_projects': GetAllProjectsToolOutput,
    'get_all_screen_tab_fields': GetAllScreenTabFieldsToolOutput,
    'get_all_screen_tabs': GetAllScreenTabsToolOutput,
    'get_all_statuses': GetAllStatusesToolOutput,
    'get_all_system_avatars': GetAllSystemAvatarsToolOutput,
    'get_all_users': GetAllUsersToolOutput,
    'get_all_users_default': GetAllUsersDefaultToolOutput,
    'get_all_workflow_schemes': GetAllWorkflowSchemesToolOutput,
    'get_all_workflows': GetAllWorkflowsToolOutput,
    'get_alternative_issue_types': GetAlternativeIssueTypesToolOutput,
    'get_application_property': GetApplicationPropertyToolOutput,
    'get_application_role': GetApplicationRoleToolOutput,
    'get_approximate_application_license_count': GetApproximateApplicationLicenseCountToolOutput,
    'get_approximate_license_count': GetApproximateLicenseCountToolOutput,
    'get_assigned_permission_scheme': GetAssignedPermissionSchemeToolOutput,
    'get_attachment': GetAttachmentToolOutput,
    'get_attachment_content': GetAttachmentContentToolOutput,
    'get_attachment_meta': GetAttachmentMetaToolOutput,
    'get_attachment_thumbnail': GetAttachmentThumbnailToolOutput,
    'get_audit_records': GetAuditRecordsToolOutput,
    'get_auto_complete': GetAutoCompleteToolOutput,
    'get_auto_complete_post': GetAutoCompletePostToolOutput,
    'get_available_screen_fields': GetAvailableScreenFieldsToolOutput,
    'get_available_time_tracking_implementations': GetAvailableTimeTrackingImplementationsToolOutput,
    'get_avatar_image_by_id': GetAvatarImageByIdToolOutput,
    'get_avatar_image_by_owner': GetAvatarImageByOwnerToolOutput,
    'get_avatar_image_by_type': GetAvatarImageByTypeToolOutput,
    'get_avatars': GetAvatarsToolOutput,
    'get_banner': GetBannerToolOutput,
    'get_bulk_permissions': GetBulkPermissionsToolOutput,
    'get_change_logs': GetChangeLogsToolOutput,
    'get_change_logs_by_ids': GetChangeLogsByIdsToolOutput,
    'get_columns': GetColumnsToolOutput,
    'get_comment': GetCommentToolOutput,
    'get_comment_property': GetCommentPropertyToolOutput,
    'get_comment_property_keys': GetCommentPropertyKeysToolOutput,
    'get_comments': GetCommentsToolOutput,
    'get_comments_by_ids': GetCommentsByIdsToolOutput,
    'get_component': GetComponentToolOutput,
    'get_component_related_issues': GetComponentRelatedIssuesToolOutput,
    'get_configuration': GetConfigurationToolOutput,
    'get_contexts_for_field': GetContextsForFieldToolOutput,
    'get_contexts_for_field_deprecated': GetContextsForFieldDeprecatedToolOutput,
    'get_create_issue_meta': GetCreateIssueMetaToolOutput,
    'get_current_user': GetCurrentUserToolOutput,
    'get_custom_field_configuration': GetCustomFieldConfigurationToolOutput,
    'get_custom_field_contexts_for_projects_and_issue_types': GetCustomFieldContextsForProjectsAndIssueTypesToolOutput,
    'get_custom_field_option': GetCustomFieldOptionToolOutput,
    'get_dashboard': GetDashboardToolOutput,
    'get_dashboard_item_property': GetDashboardItemPropertyToolOutput,
    'get_dashboard_item_property_keys': GetDashboardItemPropertyKeysToolOutput,
    'get_dashboards_paginated': GetDashboardsPaginatedToolOutput,
    'get_default_share_scope': GetDefaultShareScopeToolOutput,
    'get_default_values': GetDefaultValuesToolOutput,
    'get_default_workflow': GetDefaultWorkflowToolOutput,
    'get_draft_default_workflow': GetDraftDefaultWorkflowToolOutput,
    'get_draft_workflow': GetDraftWorkflowToolOutput,
    'get_dynamic_webhooks_for_app': GetDynamicWebhooksForAppToolOutput,
    'get_edit_issue_meta': GetEditIssueMetaToolOutput,
    'get_events': GetEventsToolOutput,
    'get_failed_webhooks': GetFailedWebhooksToolOutput,
    'get_favourite_filters': GetFavouriteFiltersToolOutput,
    'get_features_for_project': GetFeaturesForProjectToolOutput,
    'get_field_auto_complete_for_query_string': GetFieldAutoCompleteForQueryStringToolOutput,
    'get_field_configuration_items': GetFieldConfigurationItemsToolOutput,
    'get_field_configuration_scheme_mappings': GetFieldConfigurationSchemeMappingsToolOutput,
    'get_field_configuration_scheme_project_mapping': GetFieldConfigurationSchemeProjectMappingToolOutput,
    'get_fields': GetFieldsToolOutput,
    'get_fields_paginated': GetFieldsPaginatedToolOutput,
    'get_filter': GetFilterToolOutput,
    'get_filters': GetFiltersToolOutput,
    'get_filters_paginated': GetFiltersPaginatedToolOutput,
    'get_group': GetGroupToolOutput,
    'get_hierarchy': GetHierarchyToolOutput,
    'get_ids_of_worklogs_deleted_since': GetIdsOfWorklogsDeletedSinceToolOutput,
    'get_ids_of_worklogs_modified_since': GetIdsOfWorklogsModifiedSinceToolOutput,
    'get_is_watching_issue_bulk': GetIsWatchingIssueBulkToolOutput,
    'get_issue': GetIssueToolOutput,
    'get_issue_all_types': GetIssueAllTypesToolOutput,
    'get_issue_field_option': GetIssueFieldOptionToolOutput,
    'get_issue_link': GetIssueLinkToolOutput,
    'get_issue_link_type': GetIssueLinkTypeToolOutput,
    'get_issue_link_types': GetIssueLinkTypesToolOutput,
    'get_issue_navigator_default_columns': GetIssueNavigatorDefaultColumnsToolOutput,
    'get_issue_picker_resource': GetIssuePickerResourceToolOutput,
    'get_issue_property': GetIssuePropertyToolOutput,
    'get_issue_property_keys': GetIssuePropertyKeysToolOutput,
    'get_issue_security_level': GetIssueSecurityLevelToolOutput,
    'get_issue_security_level_members': GetIssueSecurityLevelMembersToolOutput,
    'get_issue_security_scheme': GetIssueSecuritySchemeToolOutput,
    'get_issue_security_schemes': GetIssueSecuritySchemesToolOutput,
    'get_issue_type': GetIssueTypeToolOutput,
    'get_issue_type_mappings_for_contexts': GetIssueTypeMappingsForContextsToolOutput,
    'get_issue_type_property': GetIssueTypePropertyToolOutput,
    'get_issue_type_property_keys': GetIssueTypePropertyKeysToolOutput,
    'get_issue_type_scheme_for_projects': GetIssueTypeSchemeForProjectsToolOutput,
    'get_issue_type_schemes_mapping': GetIssueTypeSchemesMappingToolOutput,
    'get_issue_type_screen_scheme_mappings': GetIssueTypeScreenSchemeMappingsToolOutput,
    'get_issue_type_screen_scheme_project_associations': GetIssueTypeScreenSchemeProjectAssociationsToolOutput,
    'get_issue_type_screen_schemes': GetIssueTypeScreenSchemesToolOutput,
    'get_issue_types_for_project': GetIssueTypesForProjectToolOutput,
    'get_issue_watchers': GetIssueWatchersToolOutput,
    'get_issue_worklog': GetIssueWorklogToolOutput,
    'get_license': GetLicenseToolOutput,
    'get_locale': GetLocaleToolOutput,
    'get_my_filters': GetMyFiltersToolOutput,
    'get_my_permissions': GetMyPermissionsToolOutput,
    'get_notification_scheme': GetNotificationSchemeToolOutput,
    'get_notification_scheme_for_project': GetNotificationSchemeForProjectToolOutput,
    'get_notification_scheme_to_project_mappings': GetNotificationSchemeToProjectMappingsToolOutput,
    'get_notification_schemes': GetNotificationSchemesToolOutput,
    'get_options_for_context': GetOptionsForContextToolOutput,
    'get_permission_scheme': GetPermissionSchemeToolOutput,
    'get_permission_scheme_grant': GetPermissionSchemeGrantToolOutput,
    'get_permission_scheme_grants': GetPermissionSchemeGrantsToolOutput,
    'get_permitted_projects': GetPermittedProjectsToolOutput,
    'get_precomputations': GetPrecomputationsToolOutput,
    'get_preference': GetPreferenceToolOutput,
    'get_priorities': GetPrioritiesToolOutput,
    'get_priority': GetPriorityToolOutput,
    'get_project': GetProjectToolOutput,
    'get_project_category_by_id': GetProjectCategoryByIdToolOutput,
    'get_project_components': GetProjectComponentsToolOutput,
    'get_project_components_paginated': GetProjectComponentsPaginatedToolOutput,
    'get_project_context_mapping': GetProjectContextMappingToolOutput,
    'get_project_email': GetProjectEmailToolOutput,
    'get_project_issue_security_scheme': GetProjectIssueSecuritySchemeToolOutput,
    'get_project_property': GetProjectPropertyToolOutput,
    'get_project_property_keys': GetProjectPropertyKeysToolOutput,
    'get_project_role': GetProjectRoleToolOutput,
    'get_project_role_actors_for_role': GetProjectRoleActorsForRoleToolOutput,
    'get_project_role_by_id': GetProjectRoleByIdToolOutput,
    'get_project_role_details': GetProjectRoleDetailsToolOutput,
    'get_project_roles': GetProjectRolesToolOutput,
    'get_project_type_by_key': GetProjectTypeByKeyToolOutput,
    'get_project_versions': GetProjectVersionsToolOutput,
    'get_project_versions_paginated': GetProjectVersionsPaginatedToolOutput,
    'get_projects_for_issue_type_screen_scheme': GetProjectsForIssueTypeScreenSchemeToolOutput,
    'get_recent': GetRecentToolOutput,
    'get_remote_issue_link_by_id': GetRemoteIssueLinkByIdToolOutput,
    'get_remote_issue_links': GetRemoteIssueLinksToolOutput,
    'get_resolution': GetResolutionToolOutput,
    'get_resolutions': GetResolutionsToolOutput,
    'get_screen_schemes': GetScreenSchemesToolOutput,
    'get_screens': GetScreensToolOutput,
    'get_screens_for_field': GetScreensForFieldToolOutput,
    'get_security_levels_for_project': GetSecurityLevelsForProjectToolOutput,
    'get_selectable_issue_field_options': GetSelectableIssueFieldOptionsToolOutput,
    'get_selected_time_tracking_implementation': GetSelectedTimeTrackingImplementationToolOutput,
    'get_server_info': GetServerInfoToolOutput,
    'get_share_permission': GetSharePermissionToolOutput,
    'get_share_permissions': GetSharePermissionsToolOutput,
    'get_shared_time_tracking_configuration': GetSharedTimeTrackingConfigurationToolOutput,
    'get_status': GetStatusToolOutput,
    'get_status_categories': GetStatusCategoriesToolOutput,
    'get_status_category': GetStatusCategoryToolOutput,
    'get_statuses': GetStatusesToolOutput,
    'get_statuses_by_id': GetStatusesByIdToolOutput,
    'get_task': GetTaskToolOutput,
    'get_transitions': GetTransitionsToolOutput,
    'get_trashed_fields_paginated': GetTrashedFieldsPaginatedToolOutput,
    'get_ui_modifications': GetUiModificationsToolOutput,
    'get_user': GetUserToolOutput,
    'get_user_default_columns': GetUserDefaultColumnsToolOutput,
    'get_user_email': GetUserEmailToolOutput,
    'get_user_email_bulk': GetUserEmailBulkToolOutput,
    'get_user_groups': GetUserGroupsToolOutput,
    'get_user_property': GetUserPropertyToolOutput,
    'get_user_property_keys': GetUserPropertyKeysToolOutput,
    'get_users_from_group': GetUsersFromGroupToolOutput,
    'get_valid_project_key': GetValidProjectKeyToolOutput,
    'get_valid_project_name': GetValidProjectNameToolOutput,
    'get_version': GetVersionToolOutput,
    'get_version_related_issues': GetVersionRelatedIssuesToolOutput,
    'get_version_unresolved_issues': GetVersionUnresolvedIssuesToolOutput,
    'get_visible_issue_field_options': GetVisibleIssueFieldOptionsToolOutput,
    'get_votes': GetVotesToolOutput,
    'get_workflow': GetWorkflowToolOutput,
    'get_workflow_scheme': GetWorkflowSchemeToolOutput,
    'get_workflow_scheme_draft': GetWorkflowSchemeDraftToolOutput,
    'get_workflow_scheme_draft_issue_type': GetWorkflowSchemeDraftIssueTypeToolOutput,
    'get_workflow_scheme_issue_type': GetWorkflowSchemeIssueTypeToolOutput,
    'get_workflow_scheme_project_associations': GetWorkflowSchemeProjectAssociationsToolOutput,
    'get_workflow_transition_properties': GetWorkflowTransitionPropertiesToolOutput,
    'get_workflow_transition_rule_configurations': GetWorkflowTransitionRuleConfigurationsToolOutput,
    'get_workflows_paginated': GetWorkflowsPaginatedToolOutput,
    'get_worklog': GetWorklogToolOutput,
    'get_worklog_property': GetWorklogPropertyToolOutput,
    'get_worklog_property_keys': GetWorklogPropertyKeysToolOutput,
    'get_worklogs_for_ids': GetWorklogsForIdsToolOutput,
    'link_issues': LinkIssuesToolOutput,
    'match_issues': MatchIssuesToolOutput,
    'merge_versions': MergeVersionsToolOutput,
    'migrate_queries': MigrateQueriesToolOutput,
    'migration_resource_update_entity_properties_value_put': MigrationResourceUpdateEntityPropertiesValuePutToolOutput,
    'migration_resource_workflow_rule_search_post': MigrationResourceWorkflowRuleSearchPostToolOutput,
    'move_priorities': MovePrioritiesToolOutput,
    'move_resolutions': MoveResolutionsToolOutput,
    'move_screen_tab': MoveScreenTabToolOutput,
    'move_screen_tab_field': MoveScreenTabFieldToolOutput,
    'move_version': MoveVersionToolOutput,
    'notify': NotifyToolOutput,
    'parse_jql_queries': ParseJqlQueriesToolOutput,
    'partial_update_project_role': PartialUpdateProjectRoleToolOutput,
    'publish_draft_workflow_scheme': PublishDraftWorkflowSchemeToolOutput,
    'refresh_webhooks': RefreshWebhooksToolOutput,
    'register_dynamic_webhooks': RegisterDynamicWebhooksToolOutput,
    'remove_attachment': RemoveAttachmentToolOutput,
    'remove_custom_field_context_from_projects': RemoveCustomFieldContextFromProjectsToolOutput,
    'remove_gadget': RemoveGadgetToolOutput,
    'remove_group': RemoveGroupToolOutput,
    'remove_issue_type_from_issue_type_scheme': RemoveIssueTypeFromIssueTypeSchemeToolOutput,
    'remove_issue_types_from_context': RemoveIssueTypesFromContextToolOutput,
    'remove_issue_types_from_global_field_configuration_scheme': RemoveIssueTypesFromGlobalFieldConfigurationSchemeToolOutput,
    'remove_mappings_from_issue_type_screen_scheme': RemoveMappingsFromIssueTypeScreenSchemeToolOutput,
    'remove_notification_from_notification_scheme': RemoveNotificationFromNotificationSchemeToolOutput,
    'remove_preference': RemovePreferenceToolOutput,
    'remove_project_category': RemoveProjectCategoryToolOutput,
    'remove_screen_tab_field': RemoveScreenTabFieldToolOutput,
    'remove_user': RemoveUserToolOutput,
    'remove_user_from_group': RemoveUserFromGroupToolOutput,
    'remove_vote': RemoveVoteToolOutput,
    'remove_watcher': RemoveWatcherToolOutput,
    'rename_screen_tab': RenameScreenTabToolOutput,
    'reorder_custom_field_options': ReorderCustomFieldOptionsToolOutput,
    'reorder_issue_types_in_issue_type_scheme': ReorderIssueTypesInIssueTypeSchemeToolOutput,
    'replace_issue_field_option': ReplaceIssueFieldOptionToolOutput,
    'reset_columns': ResetColumnsToolOutput,
    'reset_user_columns': ResetUserColumnsToolOutput,
    'restore': RestoreToolOutput,
    'restore_custom_field': RestoreCustomFieldToolOutput,
    'sanitise_jql_queries': SanitiseJqlQueriesToolOutput,
    'search': SearchToolOutput,
    'search_for_issues_using_jql': SearchForIssuesUsingJqlToolOutput,
    'search_for_issues_using_jql_post': SearchForIssuesUsingJqlPostToolOutput,
    'search_priorities': SearchPrioritiesToolOutput,
    'search_projects': SearchProjectsToolOutput,
    'search_resolutions': SearchResolutionsToolOutput,
    'select_time_tracking_implementation': SelectTimeTrackingImplementationToolOutput,
    'set_actors': SetActorsToolOutput,
    'set_application_property': SetApplicationPropertyToolOutput,
    'set_banner': SetBannerToolOutput,
    'set_columns': SetColumnsToolOutput,
    'set_comment_property': SetCommentPropertyToolOutput,
    'set_dashboard_item_property': SetDashboardItemPropertyToolOutput,
    'set_default_priority': SetDefaultPriorityToolOutput,
    'set_default_resolution': SetDefaultResolutionToolOutput,
    'set_default_share_scope': SetDefaultShareScopeToolOutput,
    'set_default_values': SetDefaultValuesToolOutput,
    'set_favourite_for_filter': SetFavouriteForFilterToolOutput,
    'set_field_configuration_scheme_mapping': SetFieldConfigurationSchemeMappingToolOutput,
    'set_issue_navigator_default_columns': SetIssueNavigatorDefaultColumnsToolOutput,
    'set_issue_property': SetIssuePropertyToolOutput,
    'set_issue_type_property': SetIssueTypePropertyToolOutput,
    'set_locale': SetLocaleToolOutput,
    'set_preference': SetPreferenceToolOutput,
    'set_project_property': SetProjectPropertyToolOutput,
    'set_shared_time_tracking_configuration': SetSharedTimeTrackingConfigurationToolOutput,
    'set_user_columns': SetUserColumnsToolOutput,
    'set_user_property': SetUserPropertyToolOutput,
    'set_workflow_scheme_draft_issue_type': SetWorkflowSchemeDraftIssueTypeToolOutput,
    'set_workflow_scheme_issue_type': SetWorkflowSchemeIssueTypeToolOutput,
    'set_worklog_property': SetWorklogPropertyToolOutput,
    'store_avatar': StoreAvatarToolOutput,
    'toggle_feature_for_project': ToggleFeatureForProjectToolOutput,
    'trash_custom_field': TrashCustomFieldToolOutput,
    'update_comment': UpdateCommentToolOutput,
    'update_component': UpdateComponentToolOutput,
    'update_custom_field': UpdateCustomFieldToolOutput,
    'update_custom_field_configuration': UpdateCustomFieldConfigurationToolOutput,
    'update_custom_field_context': UpdateCustomFieldContextToolOutput,
    'update_custom_field_option': UpdateCustomFieldOptionToolOutput,
    'update_custom_field_value': UpdateCustomFieldValueToolOutput,
    'update_dashboard': UpdateDashboardToolOutput,
    'update_default_screen_scheme': UpdateDefaultScreenSchemeToolOutput,
    'update_default_workflow': UpdateDefaultWorkflowToolOutput,
    'update_draft_default_workflow': UpdateDraftDefaultWorkflowToolOutput,
    'update_draft_workflow_mapping': UpdateDraftWorkflowMappingToolOutput,
    'update_field_configuration': UpdateFieldConfigurationToolOutput,
    'update_field_configuration_items': UpdateFieldConfigurationItemsToolOutput,
    'update_field_configuration_scheme': UpdateFieldConfigurationSchemeToolOutput,
    'update_filter': UpdateFilterToolOutput,
    'update_gadget': UpdateGadgetToolOutput,
    'update_issue_field_option': UpdateIssueFieldOptionToolOutput,
    'update_issue_link_type': UpdateIssueLinkTypeToolOutput,
    'update_issue_type': UpdateIssueTypeToolOutput,
    'update_issue_type_scheme': UpdateIssueTypeSchemeToolOutput,
    'update_issue_type_screen_scheme': UpdateIssueTypeScreenSchemeToolOutput,
    'update_multiple_custom_field_values': UpdateMultipleCustomFieldValuesToolOutput,
    'update_notification_scheme': UpdateNotificationSchemeToolOutput,
    'update_permission_scheme': UpdatePermissionSchemeToolOutput,
    'update_precomputations': UpdatePrecomputationsToolOutput,
    'update_priority': UpdatePriorityToolOutput,
    'update_project': UpdateProjectToolOutput,
    'update_project_avatar': UpdateProjectAvatarToolOutput,
    'update_project_category': UpdateProjectCategoryToolOutput,
    'update_project_email': UpdateProjectEmailToolOutput,
    'update_project_type': UpdateProjectTypeToolOutput,
    'update_remote_issue_link': UpdateRemoteIssueLinkToolOutput,
    'update_resolution': UpdateResolutionToolOutput,
    'update_screen': UpdateScreenToolOutput,
    'update_screen_scheme': UpdateScreenSchemeToolOutput,
    'update_statuses': UpdateStatusesToolOutput,
    'update_ui_modification': UpdateUiModificationToolOutput,
    'update_version': UpdateVersionToolOutput,
    'update_workflow_mapping': UpdateWorkflowMappingToolOutput,
    'update_workflow_scheme': UpdateWorkflowSchemeToolOutput,
    'update_workflow_scheme_draft': UpdateWorkflowSchemeDraftToolOutput,
    'update_workflow_transition_property': UpdateWorkflowTransitionPropertyToolOutput,
    'update_workflow_transition_rule_configurations': UpdateWorkflowTransitionRuleConfigurationsToolOutput,
    'update_worklog': UpdateWorklogToolOutput,
    'validate_project_key': ValidateProjectKeyToolOutput,
}
