# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkrds.v3.model.allow_db_privilege_request import AllowDbPrivilegeRequest
from huaweicloudsdkrds.v3.model.allow_db_privilege_response import AllowDbPrivilegeResponse
from huaweicloudsdkrds.v3.model.allow_db_user_privilege_request import AllowDbUserPrivilegeRequest
from huaweicloudsdkrds.v3.model.allow_db_user_privilege_response import AllowDbUserPrivilegeResponse
from huaweicloudsdkrds.v3.model.allow_sqlserver_db_user_privilege_request import AllowSqlserverDbUserPrivilegeRequest
from huaweicloudsdkrds.v3.model.allow_sqlserver_db_user_privilege_response import AllowSqlserverDbUserPrivilegeResponse
from huaweicloudsdkrds.v3.model.apply_configuration_request import ApplyConfigurationRequest
from huaweicloudsdkrds.v3.model.apply_configuration_response_apply_results import ApplyConfigurationResponseApplyResults
from huaweicloudsdkrds.v3.model.attach_eip_request import AttachEipRequest
from huaweicloudsdkrds.v3.model.attach_eip_response import AttachEipResponse
from huaweicloudsdkrds.v3.model.auditlog import Auditlog
from huaweicloudsdkrds.v3.model.backup_database import BackupDatabase
from huaweicloudsdkrds.v3.model.backup_for_list import BackupForList
from huaweicloudsdkrds.v3.model.backup_info import BackupInfo
from huaweicloudsdkrds.v3.model.backup_policy import BackupPolicy
from huaweicloudsdkrds.v3.model.backup_strategy import BackupStrategy
from huaweicloudsdkrds.v3.model.backup_strategy_for_response import BackupStrategyForResponse
from huaweicloudsdkrds.v3.model.batch_tag_action_add_request_body import BatchTagActionAddRequestBody
from huaweicloudsdkrds.v3.model.batch_tag_action_del_request_body import BatchTagActionDelRequestBody
from huaweicloudsdkrds.v3.model.batch_tag_add_action_request import BatchTagAddActionRequest
from huaweicloudsdkrds.v3.model.batch_tag_add_action_response import BatchTagAddActionResponse
from huaweicloudsdkrds.v3.model.batch_tag_del_action_request import BatchTagDelActionRequest
from huaweicloudsdkrds.v3.model.batch_tag_del_action_response import BatchTagDelActionResponse
from huaweicloudsdkrds.v3.model.bind_eip_request import BindEipRequest
from huaweicloudsdkrds.v3.model.change_failover_mode_request import ChangeFailoverModeRequest
from huaweicloudsdkrds.v3.model.change_failover_mode_response import ChangeFailoverModeResponse
from huaweicloudsdkrds.v3.model.change_failover_strategy_request import ChangeFailoverStrategyRequest
from huaweicloudsdkrds.v3.model.change_failover_strategy_response import ChangeFailoverStrategyResponse
from huaweicloudsdkrds.v3.model.change_ops_window_request import ChangeOpsWindowRequest
from huaweicloudsdkrds.v3.model.change_ops_window_response import ChangeOpsWindowResponse
from huaweicloudsdkrds.v3.model.charge_info import ChargeInfo
from huaweicloudsdkrds.v3.model.charge_info_response import ChargeInfoResponse
from huaweicloudsdkrds.v3.model.configuration_for_creation import ConfigurationForCreation
from huaweicloudsdkrds.v3.model.configuration_for_update import ConfigurationForUpdate
from huaweicloudsdkrds.v3.model.configuration_parameter import ConfigurationParameter
from huaweicloudsdkrds.v3.model.configuration_summary import ConfigurationSummary
from huaweicloudsdkrds.v3.model.configuration_summary_for_create import ConfigurationSummaryForCreate
from huaweicloudsdkrds.v3.model.create_configuration_request import CreateConfigurationRequest
from huaweicloudsdkrds.v3.model.create_configuration_response import CreateConfigurationResponse
from huaweicloudsdkrds.v3.model.create_database_request import CreateDatabaseRequest
from huaweicloudsdkrds.v3.model.create_database_response import CreateDatabaseResponse
from huaweicloudsdkrds.v3.model.create_db_user_request import CreateDbUserRequest
from huaweicloudsdkrds.v3.model.create_db_user_response import CreateDbUserResponse
from huaweicloudsdkrds.v3.model.create_dns_name_request import CreateDnsNameRequest
from huaweicloudsdkrds.v3.model.create_dns_name_request_body import CreateDnsNameRequestBody
from huaweicloudsdkrds.v3.model.create_dns_name_response import CreateDnsNameResponse
from huaweicloudsdkrds.v3.model.create_instance_request import CreateInstanceRequest
from huaweicloudsdkrds.v3.model.create_instance_resp_item import CreateInstanceRespItem
from huaweicloudsdkrds.v3.model.create_instance_response import CreateInstanceResponse
from huaweicloudsdkrds.v3.model.create_manual_backup_request import CreateManualBackupRequest
from huaweicloudsdkrds.v3.model.create_manual_backup_request_body import CreateManualBackupRequestBody
from huaweicloudsdkrds.v3.model.create_manual_backup_response import CreateManualBackupResponse
from huaweicloudsdkrds.v3.model.create_postgresql_database_request import CreatePostgresqlDatabaseRequest
from huaweicloudsdkrds.v3.model.create_postgresql_database_response import CreatePostgresqlDatabaseResponse
from huaweicloudsdkrds.v3.model.create_postgresql_database_schema_request import CreatePostgresqlDatabaseSchemaRequest
from huaweicloudsdkrds.v3.model.create_postgresql_database_schema_response import CreatePostgresqlDatabaseSchemaResponse
from huaweicloudsdkrds.v3.model.create_postgresql_db_user_request import CreatePostgresqlDbUserRequest
from huaweicloudsdkrds.v3.model.create_postgresql_db_user_response import CreatePostgresqlDbUserResponse
from huaweicloudsdkrds.v3.model.create_restore_instance_request import CreateRestoreInstanceRequest
from huaweicloudsdkrds.v3.model.create_restore_instance_response import CreateRestoreInstanceResponse
from huaweicloudsdkrds.v3.model.create_sqlserver_database_request import CreateSqlserverDatabaseRequest
from huaweicloudsdkrds.v3.model.create_sqlserver_database_response import CreateSqlserverDatabaseResponse
from huaweicloudsdkrds.v3.model.create_sqlserver_db_user_request import CreateSqlserverDbUserRequest
from huaweicloudsdkrds.v3.model.create_sqlserver_db_user_response import CreateSqlserverDbUserResponse
from huaweicloudsdkrds.v3.model.data_ip_request import DataIpRequest
from huaweicloudsdkrds.v3.model.database_for_creation import DatabaseForCreation
from huaweicloudsdkrds.v3.model.database_for_list_schema import DatabaseForListSchema
from huaweicloudsdkrds.v3.model.database_with_privilege import DatabaseWithPrivilege
from huaweicloudsdkrds.v3.model.datastore import Datastore
from huaweicloudsdkrds.v3.model.db_schema_req import DbSchemaReq
from huaweicloudsdkrds.v3.model.db_user_pwd_request import DbUserPwdRequest
from huaweicloudsdkrds.v3.model.delete_configuration_request import DeleteConfigurationRequest
from huaweicloudsdkrds.v3.model.delete_configuration_response import DeleteConfigurationResponse
from huaweicloudsdkrds.v3.model.delete_database_request import DeleteDatabaseRequest
from huaweicloudsdkrds.v3.model.delete_database_response import DeleteDatabaseResponse
from huaweicloudsdkrds.v3.model.delete_db_user_request import DeleteDbUserRequest
from huaweicloudsdkrds.v3.model.delete_db_user_response import DeleteDbUserResponse
from huaweicloudsdkrds.v3.model.delete_instance_request import DeleteInstanceRequest
from huaweicloudsdkrds.v3.model.delete_instance_response import DeleteInstanceResponse
from huaweicloudsdkrds.v3.model.delete_manual_backup_request import DeleteManualBackupRequest
from huaweicloudsdkrds.v3.model.delete_manual_backup_response import DeleteManualBackupResponse
from huaweicloudsdkrds.v3.model.delete_sqlserver_database_request import DeleteSqlserverDatabaseRequest
from huaweicloudsdkrds.v3.model.delete_sqlserver_database_response import DeleteSqlserverDatabaseResponse
from huaweicloudsdkrds.v3.model.delete_sqlserver_db_user_request import DeleteSqlserverDbUserRequest
from huaweicloudsdkrds.v3.model.delete_sqlserver_db_user_response import DeleteSqlserverDbUserResponse
from huaweicloudsdkrds.v3.model.download_slowlog_request import DownloadSlowlogRequest
from huaweicloudsdkrds.v3.model.download_slowlog_response import DownloadSlowlogResponse
from huaweicloudsdkrds.v3.model.dss_pool_info import DssPoolInfo
from huaweicloudsdkrds.v3.model.enable_configuration_request import EnableConfigurationRequest
from huaweicloudsdkrds.v3.model.enable_configuration_response import EnableConfigurationResponse
from huaweicloudsdkrds.v3.model.enlarge_volume import EnlargeVolume
from huaweicloudsdkrds.v3.model.error_log import ErrorLog
from huaweicloudsdkrds.v3.model.error_response import ErrorResponse
from huaweicloudsdkrds.v3.model.failover_mode_request import FailoverModeRequest
from huaweicloudsdkrds.v3.model.failover_strategy_request import FailoverStrategyRequest
from huaweicloudsdkrds.v3.model.flavor import Flavor
from huaweicloudsdkrds.v3.model.follower_migrate_request import FollowerMigrateRequest
from huaweicloudsdkrds.v3.model.generate_auditlog_download_link_request import GenerateAuditlogDownloadLinkRequest
from huaweicloudsdkrds.v3.model.get_backup_download_link_files import GetBackupDownloadLinkFiles
from huaweicloudsdkrds.v3.model.get_job_info_response_body_job import GetJobInfoResponseBodyJob
from huaweicloudsdkrds.v3.model.get_restore_time_response_restore_time import GetRestoreTimeResponseRestoreTime
from huaweicloudsdkrds.v3.model.get_task_detail_list_rsp_instance import GetTaskDetailListRspInstance
from huaweicloudsdkrds.v3.model.get_task_detail_list_rsp_jobs import GetTaskDetailListRspJobs
from huaweicloudsdkrds.v3.model.grant_request import GrantRequest
from huaweicloudsdkrds.v3.model.ha import Ha
from huaweicloudsdkrds.v3.model.ha_response import HaResponse
from huaweicloudsdkrds.v3.model.instance_request import InstanceRequest
from huaweicloudsdkrds.v3.model.instance_response import InstanceResponse
from huaweicloudsdkrds.v3.model.instance_restart_requset_body import InstanceRestartRequsetBody
from huaweicloudsdkrds.v3.model.l_datastore import LDatastore
from huaweicloudsdkrds.v3.model.list_auditlogs_request import ListAuditlogsRequest
from huaweicloudsdkrds.v3.model.list_auditlogs_response import ListAuditlogsResponse
from huaweicloudsdkrds.v3.model.list_authorized_databases_request import ListAuthorizedDatabasesRequest
from huaweicloudsdkrds.v3.model.list_authorized_databases_response import ListAuthorizedDatabasesResponse
from huaweicloudsdkrds.v3.model.list_authorized_db_users_request import ListAuthorizedDbUsersRequest
from huaweicloudsdkrds.v3.model.list_authorized_db_users_response import ListAuthorizedDbUsersResponse
from huaweicloudsdkrds.v3.model.list_authorized_sqlserver_db_users_request import ListAuthorizedSqlserverDbUsersRequest
from huaweicloudsdkrds.v3.model.list_authorized_sqlserver_db_users_response import ListAuthorizedSqlserverDbUsersResponse
from huaweicloudsdkrds.v3.model.list_backups_request import ListBackupsRequest
from huaweicloudsdkrds.v3.model.list_backups_response import ListBackupsResponse
from huaweicloudsdkrds.v3.model.list_collations_request import ListCollationsRequest
from huaweicloudsdkrds.v3.model.list_collations_response import ListCollationsResponse
from huaweicloudsdkrds.v3.model.list_configurations_request import ListConfigurationsRequest
from huaweicloudsdkrds.v3.model.list_configurations_response import ListConfigurationsResponse
from huaweicloudsdkrds.v3.model.list_databases_request import ListDatabasesRequest
from huaweicloudsdkrds.v3.model.list_databases_response import ListDatabasesResponse
from huaweicloudsdkrds.v3.model.list_datastores_request import ListDatastoresRequest
from huaweicloudsdkrds.v3.model.list_datastores_response import ListDatastoresResponse
from huaweicloudsdkrds.v3.model.list_db_users_request import ListDbUsersRequest
from huaweicloudsdkrds.v3.model.list_db_users_response import ListDbUsersResponse
from huaweicloudsdkrds.v3.model.list_error_logs_request import ListErrorLogsRequest
from huaweicloudsdkrds.v3.model.list_error_logs_response import ListErrorLogsResponse
from huaweicloudsdkrds.v3.model.list_flavors_request import ListFlavorsRequest
from huaweicloudsdkrds.v3.model.list_flavors_response import ListFlavorsResponse
from huaweicloudsdkrds.v3.model.list_instances_request import ListInstancesRequest
from huaweicloudsdkrds.v3.model.list_instances_response import ListInstancesResponse
from huaweicloudsdkrds.v3.model.list_job_info_detail_request import ListJobInfoDetailRequest
from huaweicloudsdkrds.v3.model.list_job_info_detail_response import ListJobInfoDetailResponse
from huaweicloudsdkrds.v3.model.list_job_info_request import ListJobInfoRequest
from huaweicloudsdkrds.v3.model.list_job_info_response import ListJobInfoResponse
from huaweicloudsdkrds.v3.model.list_off_site_backups_request import ListOffSiteBackupsRequest
from huaweicloudsdkrds.v3.model.list_off_site_backups_response import ListOffSiteBackupsResponse
from huaweicloudsdkrds.v3.model.list_off_site_instances_request import ListOffSiteInstancesRequest
from huaweicloudsdkrds.v3.model.list_off_site_instances_response import ListOffSiteInstancesResponse
from huaweicloudsdkrds.v3.model.list_off_site_restore_times_request import ListOffSiteRestoreTimesRequest
from huaweicloudsdkrds.v3.model.list_off_site_restore_times_response import ListOffSiteRestoreTimesResponse
from huaweicloudsdkrds.v3.model.list_postgresql_database_schemas_request import ListPostgresqlDatabaseSchemasRequest
from huaweicloudsdkrds.v3.model.list_postgresql_database_schemas_response import ListPostgresqlDatabaseSchemasResponse
from huaweicloudsdkrds.v3.model.list_postgresql_databases_request import ListPostgresqlDatabasesRequest
from huaweicloudsdkrds.v3.model.list_postgresql_databases_response import ListPostgresqlDatabasesResponse
from huaweicloudsdkrds.v3.model.list_postgresql_db_user_paginated_request import ListPostgresqlDbUserPaginatedRequest
from huaweicloudsdkrds.v3.model.list_postgresql_db_user_paginated_response import ListPostgresqlDbUserPaginatedResponse
from huaweicloudsdkrds.v3.model.list_project_tags_request import ListProjectTagsRequest
from huaweicloudsdkrds.v3.model.list_project_tags_response import ListProjectTagsResponse
from huaweicloudsdkrds.v3.model.list_restore_times_request import ListRestoreTimesRequest
from huaweicloudsdkrds.v3.model.list_restore_times_response import ListRestoreTimesResponse
from huaweicloudsdkrds.v3.model.list_slow_logs_request import ListSlowLogsRequest
from huaweicloudsdkrds.v3.model.list_slow_logs_response import ListSlowLogsResponse
from huaweicloudsdkrds.v3.model.list_slowlog_statistics_request import ListSlowlogStatisticsRequest
from huaweicloudsdkrds.v3.model.list_slowlog_statistics_response import ListSlowlogStatisticsResponse
from huaweicloudsdkrds.v3.model.list_sqlserver_databases_request import ListSqlserverDatabasesRequest
from huaweicloudsdkrds.v3.model.list_sqlserver_databases_response import ListSqlserverDatabasesResponse
from huaweicloudsdkrds.v3.model.list_sqlserver_db_users_request import ListSqlserverDbUsersRequest
from huaweicloudsdkrds.v3.model.list_sqlserver_db_users_response import ListSqlserverDbUsersResponse
from huaweicloudsdkrds.v3.model.list_storage_types_request import ListStorageTypesRequest
from huaweicloudsdkrds.v3.model.list_storage_types_response import ListStorageTypesResponse
from huaweicloudsdkrds.v3.model.migrate_follower_request import MigrateFollowerRequest
from huaweicloudsdkrds.v3.model.migrate_follower_response import MigrateFollowerResponse
from huaweicloudsdkrds.v3.model.modifiy_instance_name_request import ModifiyInstanceNameRequest
from huaweicloudsdkrds.v3.model.modify_dns_name_request_body import ModifyDnsNameRequestBody
from huaweicloudsdkrds.v3.model.node_response import NodeResponse
from huaweicloudsdkrds.v3.model.off_site_backup_for_list import OffSiteBackupForList
from huaweicloudsdkrds.v3.model.off_site_backup_policy import OffSiteBackupPolicy
from huaweicloudsdkrds.v3.model.offsite_backup_instance import OffsiteBackupInstance
from huaweicloudsdkrds.v3.model.ops_window_request import OpsWindowRequest
from huaweicloudsdkrds.v3.model.pg_grant_request import PgGrantRequest
from huaweicloudsdkrds.v3.model.pg_list_database import PgListDatabase
from huaweicloudsdkrds.v3.model.pg_user_for_list import PgUserForList
from huaweicloudsdkrds.v3.model.pg_user_with_privilege import PgUserWithPrivilege
from huaweicloudsdkrds.v3.model.postgresql_database_for_creation import PostgresqlDatabaseForCreation
from huaweicloudsdkrds.v3.model.postgresql_user_for_creation import PostgresqlUserForCreation
from huaweicloudsdkrds.v3.model.project_tag_info_response import ProjectTagInfoResponse
from huaweicloudsdkrds.v3.model.pwd_reset_request import PwdResetRequest
from huaweicloudsdkrds.v3.model.recycle_policy_request_body import RecyclePolicyRequestBody
from huaweicloudsdkrds.v3.model.related_instance import RelatedInstance
from huaweicloudsdkrds.v3.model.reset_pwd_request import ResetPwdRequest
from huaweicloudsdkrds.v3.model.reset_pwd_response import ResetPwdResponse
from huaweicloudsdkrds.v3.model.resize_flavor_request import ResizeFlavorRequest
from huaweicloudsdkrds.v3.model.restore_databases_info import RestoreDatabasesInfo
from huaweicloudsdkrds.v3.model.restore_point import RestorePoint
from huaweicloudsdkrds.v3.model.restore_table_info import RestoreTableInfo
from huaweicloudsdkrds.v3.model.restore_tables_request import RestoreTablesRequest
from huaweicloudsdkrds.v3.model.restore_tables_request_body import RestoreTablesRequestBody
from huaweicloudsdkrds.v3.model.restore_tables_response import RestoreTablesResponse
from huaweicloudsdkrds.v3.model.restore_to_existing_instance_request import RestoreToExistingInstanceRequest
from huaweicloudsdkrds.v3.model.restore_to_existing_instance_request_body import RestoreToExistingInstanceRequestBody
from huaweicloudsdkrds.v3.model.restore_to_existing_instance_request_body_source import RestoreToExistingInstanceRequestBodySource
from huaweicloudsdkrds.v3.model.restore_to_existing_instance_request_body_target import RestoreToExistingInstanceRequestBodyTarget
from huaweicloudsdkrds.v3.model.restore_to_existing_instance_response import RestoreToExistingInstanceResponse
from huaweicloudsdkrds.v3.model.revoke_request import RevokeRequest
from huaweicloudsdkrds.v3.model.revoke_request_body import RevokeRequestBody
from huaweicloudsdkrds.v3.model.revoke_request_body_users import RevokeRequestBodyUsers
from huaweicloudsdkrds.v3.model.revoke_response import RevokeResponse
from huaweicloudsdkrds.v3.model.revoke_sqlserver_db_user_privilege_request import RevokeSqlserverDbUserPrivilegeRequest
from huaweicloudsdkrds.v3.model.revoke_sqlserver_db_user_privilege_response import RevokeSqlserverDbUserPrivilegeResponse
from huaweicloudsdkrds.v3.model.schema_req import SchemaReq
from huaweicloudsdkrds.v3.model.security_group_request import SecurityGroupRequest
from huaweicloudsdkrds.v3.model.set_auditlog_policy_request import SetAuditlogPolicyRequest
from huaweicloudsdkrds.v3.model.set_auditlog_policy_request_body import SetAuditlogPolicyRequestBody
from huaweicloudsdkrds.v3.model.set_auditlog_policy_response import SetAuditlogPolicyResponse
from huaweicloudsdkrds.v3.model.set_backup_policy_request import SetBackupPolicyRequest
from huaweicloudsdkrds.v3.model.set_backup_policy_request_body import SetBackupPolicyRequestBody
from huaweicloudsdkrds.v3.model.set_backup_policy_response import SetBackupPolicyResponse
from huaweicloudsdkrds.v3.model.set_db_user_pwd_request import SetDbUserPwdRequest
from huaweicloudsdkrds.v3.model.set_db_user_pwd_response import SetDbUserPwdResponse
from huaweicloudsdkrds.v3.model.set_off_site_backup_policy_request import SetOffSiteBackupPolicyRequest
from huaweicloudsdkrds.v3.model.set_off_site_backup_policy_request_body import SetOffSiteBackupPolicyRequestBody
from huaweicloudsdkrds.v3.model.set_off_site_backup_policy_response import SetOffSiteBackupPolicyResponse
from huaweicloudsdkrds.v3.model.set_postgresql_db_user_pwd_request import SetPostgresqlDbUserPwdRequest
from huaweicloudsdkrds.v3.model.set_postgresql_db_user_pwd_response import SetPostgresqlDbUserPwdResponse
from huaweicloudsdkrds.v3.model.set_security_group_request import SetSecurityGroupRequest
from huaweicloudsdkrds.v3.model.set_security_group_response import SetSecurityGroupResponse
from huaweicloudsdkrds.v3.model.show_auditlog_download_link_request import ShowAuditlogDownloadLinkRequest
from huaweicloudsdkrds.v3.model.show_auditlog_download_link_response import ShowAuditlogDownloadLinkResponse
from huaweicloudsdkrds.v3.model.show_auditlog_policy_request import ShowAuditlogPolicyRequest
from huaweicloudsdkrds.v3.model.show_auditlog_policy_response import ShowAuditlogPolicyResponse
from huaweicloudsdkrds.v3.model.show_backup_download_link_request import ShowBackupDownloadLinkRequest
from huaweicloudsdkrds.v3.model.show_backup_download_link_response import ShowBackupDownloadLinkResponse
from huaweicloudsdkrds.v3.model.show_backup_policy_request import ShowBackupPolicyRequest
from huaweicloudsdkrds.v3.model.show_backup_policy_response import ShowBackupPolicyResponse
from huaweicloudsdkrds.v3.model.show_configuration_request import ShowConfigurationRequest
from huaweicloudsdkrds.v3.model.show_configuration_response import ShowConfigurationResponse
from huaweicloudsdkrds.v3.model.show_instance_configuration_request import ShowInstanceConfigurationRequest
from huaweicloudsdkrds.v3.model.show_instance_configuration_response import ShowInstanceConfigurationResponse
from huaweicloudsdkrds.v3.model.show_off_site_backup_policy_request import ShowOffSiteBackupPolicyRequest
from huaweicloudsdkrds.v3.model.show_off_site_backup_policy_response import ShowOffSiteBackupPolicyResponse
from huaweicloudsdkrds.v3.model.single2_ha import Single2Ha
from huaweicloudsdkrds.v3.model.slow_log import SlowLog
from huaweicloudsdkrds.v3.model.slow_log_statistics import SlowLogStatistics
from huaweicloudsdkrds.v3.model.slowlog_download_info import SlowlogDownloadInfo
from huaweicloudsdkrds.v3.model.slowlog_download_request import SlowlogDownloadRequest
from huaweicloudsdkrds.v3.model.sqlserver_database_for_creation import SqlserverDatabaseForCreation
from huaweicloudsdkrds.v3.model.sqlserver_database_for_detail import SqlserverDatabaseForDetail
from huaweicloudsdkrds.v3.model.sqlserver_grant_request import SqlserverGrantRequest
from huaweicloudsdkrds.v3.model.sqlserver_revoke_request import SqlserverRevokeRequest
from huaweicloudsdkrds.v3.model.sqlserver_user_for_creation import SqlserverUserForCreation
from huaweicloudsdkrds.v3.model.sqlserver_user_with_privilege import SqlserverUserWithPrivilege
from huaweicloudsdkrds.v3.model.ssl_option_request import SslOptionRequest
from huaweicloudsdkrds.v3.model.start_failover_request import StartFailoverRequest
from huaweicloudsdkrds.v3.model.start_failover_response import StartFailoverResponse
from huaweicloudsdkrds.v3.model.start_instance_enlarge_volume_action_request import StartInstanceEnlargeVolumeActionRequest
from huaweicloudsdkrds.v3.model.start_instance_enlarge_volume_action_response import StartInstanceEnlargeVolumeActionResponse
from huaweicloudsdkrds.v3.model.start_instance_restart_action_request import StartInstanceRestartActionRequest
from huaweicloudsdkrds.v3.model.start_instance_restart_action_response import StartInstanceRestartActionResponse
from huaweicloudsdkrds.v3.model.start_instance_single_to_ha_action_request import StartInstanceSingleToHaActionRequest
from huaweicloudsdkrds.v3.model.start_instance_single_to_ha_action_response import StartInstanceSingleToHaActionResponse
from huaweicloudsdkrds.v3.model.start_recycle_policy_request import StartRecyclePolicyRequest
from huaweicloudsdkrds.v3.model.start_recycle_policy_response import StartRecyclePolicyResponse
from huaweicloudsdkrds.v3.model.start_resize_flavor_action_request import StartResizeFlavorActionRequest
from huaweicloudsdkrds.v3.model.start_resize_flavor_action_response import StartResizeFlavorActionResponse
from huaweicloudsdkrds.v3.model.storage import Storage
from huaweicloudsdkrds.v3.model.switch_ssl_request import SwitchSslRequest
from huaweicloudsdkrds.v3.model.switch_ssl_response import SwitchSslResponse
from huaweicloudsdkrds.v3.model.tag_del_with_key_value import TagDelWithKeyValue
from huaweicloudsdkrds.v3.model.tag_response import TagResponse
from huaweicloudsdkrds.v3.model.tag_with_key_value import TagWithKeyValue
from huaweicloudsdkrds.v3.model.update_configuration_request import UpdateConfigurationRequest
from huaweicloudsdkrds.v3.model.update_configuration_response import UpdateConfigurationResponse
from huaweicloudsdkrds.v3.model.update_data_ip_request import UpdateDataIpRequest
from huaweicloudsdkrds.v3.model.update_data_ip_response import UpdateDataIpResponse
from huaweicloudsdkrds.v3.model.update_db_port_request import UpdateDbPortRequest
from huaweicloudsdkrds.v3.model.update_dns_name_request import UpdateDnsNameRequest
from huaweicloudsdkrds.v3.model.update_dns_name_response import UpdateDnsNameResponse
from huaweicloudsdkrds.v3.model.update_instance_configuration_request import UpdateInstanceConfigurationRequest
from huaweicloudsdkrds.v3.model.update_instance_configuration_request_body import UpdateInstanceConfigurationRequestBody
from huaweicloudsdkrds.v3.model.update_instance_configuration_response import UpdateInstanceConfigurationResponse
from huaweicloudsdkrds.v3.model.update_instance_name_request import UpdateInstanceNameRequest
from huaweicloudsdkrds.v3.model.update_instance_name_response import UpdateInstanceNameResponse
from huaweicloudsdkrds.v3.model.update_port_request import UpdatePortRequest
from huaweicloudsdkrds.v3.model.update_port_response import UpdatePortResponse
from huaweicloudsdkrds.v3.model.update_postgresql_instance_alias_request import UpdatePostgresqlInstanceAliasRequest
from huaweicloudsdkrds.v3.model.update_postgresql_instance_alias_response import UpdatePostgresqlInstanceAliasResponse
from huaweicloudsdkrds.v3.model.update_rds_instance_alias_request import UpdateRdsInstanceAliasRequest
from huaweicloudsdkrds.v3.model.user_for_creation import UserForCreation
from huaweicloudsdkrds.v3.model.user_for_list import UserForList
from huaweicloudsdkrds.v3.model.user_with_privilege import UserWithPrivilege
from huaweicloudsdkrds.v3.model.volume import Volume
