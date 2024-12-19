#!/bin/bash

# Enabling Azure Monitor for Microsoft Fabric Resources
# Replace <resource_id> with your Azure resource ID.
az monitor diagnostic-settings create --name "DiagnosticSetting" --resource <resource_id> --logs '[{"category": "AuditLogs", "enabled": true}]' --metrics '[{"category": "AllMetrics", "enabled": true}]'

# Creating a Log Analytics Workspace in Azure
# Replace <resource_group> and <workspace_name> with your values.
az monitor log-analytics workspace create --resource-group <resource_group> --workspace-name <workspace_name>
