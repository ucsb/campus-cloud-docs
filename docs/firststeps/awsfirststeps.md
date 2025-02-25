### Campus Single Sign On for AWS: [https://aws.cloud.ucsb.edu](https://aws.cloud.ucsb.edu)
   * Supported Campus Cloud Regions: 
     * **US-West-2 (Oregon)** 
     * **US-East-1 (N.Virginia)** 
   * We recommend starting in *US-West-2*

{% include alert.html type="info" title="Information" content="To ADD/REMOVE user access to these Roles, please see Step 5 below" %}

## AWS Account First Steps D

For teams or individuals that are creating an AWS account, here are some essential first steps that you should take. This guide assumes your account is a UCSB Campus Cloud account and that you have received an email from the Campus Cloud team detailing your account is now ready for use.

1. **Logging in to your AWS Account**

    The Campus Cloud team has configured new accounts to use campus single sign on for user authentication and a mapping of identity groups to [AWS Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) for authorization. Your account will come with four pre-defined roles:
    * _Administrator (ucsb-idp-administrator)_: This role has full access and can delegate permissions to every service and resource in AWS. Provides full access to AWS services and resources.
    * _PowerUser (ucsb-idp-poweruser)_: Provides full access to AWS services and resources, but does not allow management of [IAM](https://docs.aws.amazon.com/iam/index.html). This user performs application development tasks and can create and configure resources and services that support AWS aware application development.
    * _ReadOnly (ucsb-idp-readonly)_: Provides read-only access to AWS services and resources. This user can view a list of AWS resources and basic metadata in the account across all services. The user cannot read resource content or metadata that goes beyond the quota and list information for resources.
    * _Billing (ucsb-idp-billing)_: This user has access to view billing information, The user can monitor the costs accumulated for the entire AWS service.

2. **Setup Monthly Billing Alert**

    Use the Service Catalog Product, *Fixed Monthly Budget with Notification*, provided by the UCSB Campus Cloud Team to create a fixed cost monthly budget, and notification based on a forecasted threshold in your account. See [Service Catalog]({{site.url}}docs/bestpractices/servicecatalog) for more info.
    
    <!---When you created your Purchase Order through [Gateway](https://gateway.procurement.ucsb.edu), you provided a budget and duration for your account. The Campus Cloud team has configured your account for a billing alert based on your provided budget and estimated monthly spend. If your monthly bill is forecasted to go over your budget you will get a notification. Please verify that you have an email address subscribed to the configured billing alert. -->

3. **Verify [CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)**,
**[Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html), and
[GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) are enabled**.  

    The Campus Cloud team has configured your account to have CloudTrail, Securty Hub, and Guard Duty enabled. All three services will send findings to the AWS Logging Account for inspection.
    Cloud Trail logs every AWS API call, so all actions done in the AWS console will be logged. Cloud Trail is your audit log for all activities done by those whom are granted access.
    
    
    [Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) and CloudTrail are pre-requisites for a Control Tower based Landing Zone (LZ). Audit, compliance and security tools are utilized in the LZ. These tools may use one or more of these services thereby generating costs in your account.  It is important that you account for these costs in your budgeting.  For a busy account it may be a small percentage of monthly costs.
   
   
   **Security Hub** - Check regulalry for Findings. ENABLE other integrations so Secuirty Hub can be the centralized tool for Findings, Security Checks, Recomendations and Threats.
    * Enable Guard Duty Integration
    * Enable Trusted Advisor Integration  (now available with Enterprise Support)
    * Enable AWS Foundational Security Best Practices v1.0.0 and/or CIS AWS Foundations Benchmark v1.2.0
        
        _(be AWARE of potential cost for resource checks IF you have substantial resources or turnover)_

4. **Configure Account Alternate Contacts**    

    Configure your account’s [alternate contacts](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-alternate.html#manage-acct-update-contact-alternate-edit) to point to a group rather than an individual. For example, create separate email distribution lists for billing, operations, and security and configure these as Billing, Security, and Operations contacts in each active AWS account. This ensures that multiple people will receive AWS notifications and be able to respond, even if someone is on vacation, changes roles, or leaves the University. For details see the [Best Practices for Contacts]({{site.url}}/docs/bestpractices/contacts).

5. **Create Network Connectivity**

    Use the Service Catalog Product, *Simple VPC with Campus Connectivity*, provided by the UCSB Campus Cloud Team to create a VPC that will quickly provide internet and VPN (if needed) access in your account. See [Service Catalog]({{site.url}}docs/bestpractices/servicecatalog) for more info.

6. **ADD Additional User Access**

    You will use the "Manage Group Tags" tool available at [im.ucsb.edu](https://im.ucsb.edu) to add and remove members to/from the pre-defined identity groups.
   *  OWNERS have access to add/remove MEMBERS.
   *  Only MEMBERS are authorized for an Identity Group (Not OWNERS)
   *  [How To: Add User to AWS Account (Confluence)](https://ucsb-atlas.atlassian.net/wiki/spaces/CCID/pages/18265964605/How+To+Add+User+to+AWS+Account+Subscription)


        **Manage Group Tags: [https://im.ucsb.edu](https://im.ucsb.edu)**
        (Note, you must Log in first to access the tool)

## AWS Enterprise Support
    
  *  [Enterprise support](https://aws.amazon.com/premiumsupport/features/) is available to all child accounts.
  *  Plan provides web, email, chat, and phone access to support
  *  A Technical Account Manager (TAM) and Concierge Team is provided and shared across the participating UCs
  *  Single support charge billed at the EDP AWS Organization Payer account
  *  Twice per month new accounts in the Organization are automatically added to Enterprise Support (Boyd, Sep 2023)

  To create a support ticket click the support/help icon (orange circle w question mark inside) at the top right when logged in to your Landing Zone account.
