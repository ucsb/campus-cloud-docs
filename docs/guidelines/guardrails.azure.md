Guardrails for Azure are built using Azure Policy and RBAC.

Guardrail guidance refers to the recommended practice for how to apply each guardrail to your OUs. The guidance of a guardrail is independent of whether its behavior is preventive or detective.
Guardrails are categorized according to their behavior and their guidance. The behavior of each guardrail is either preventive or detective.

The CAF Enterprise Scale for Terraform includes a MVP list of guardrails

### The List of Active Guardrails as of Dec 2020

-   ES-Allowed-Resource-Locations - Enabled
    Specifies the allowed locations (regions) where resources can be deployed

-   ES-Allowed-ResourceGroup-Locations - Enabled
    Specifies the allowed locations (regions) where Resource Groups can be deployed

-   ES-Deny-AppGW-Without-WAF
    Deny creation of App Gateway without WAF

-   ES-Deny-IP-Forwarding-On-VM
    Deny IP Forwarding on Virtual Machines

-   ES-Deny-RDP-From-Internet - Enabled
    Deny RDP access from the Internet

-   ES-Deny-Resources-Types
    Specifies the Resource Types to deny deployment by policy

-   ES-Deny-Subnet-Without-Nsg
    Deny provisioning of subnet without NSG attached.

-   ES-Deploy-ASC-ContinuousExportToWorkspace
    Deploy ASC Continuous Export To Log Analytics Workspace

-   ES-Deploy-ASC-Monitoring
    Enable Monitoring in Azure Security Center

-   ES-Deploy-ASC-Standard 
    Deploy Azure Security Center Standard Tier

-   ES-Deploy-Diagnostics-ForwardActivityLogs
    Ensures that Activity Log Diagnostics settings are set to push logs into Log Analytics workspace

-   ES-Deploy-Diagnostics-ForwardDiagnosticLogs
    Ensures that Azure resources are configured to forward diagnostic logs and metrics to an Azure Log Analytics workspace

-   ES-Deploy-VM-Monitoring
    Ensures that Azure Monitor is configured for Virtual Machines

-   Deploy-Budget
    Ensures a budget exists for each sandbox subscription, with e-mail alerts enabled. The budget will be named: default-sandbox-budget in each subscription.
