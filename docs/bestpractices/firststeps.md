---
title: First Steps
description: First Steps after you access your Cloud Account
permalink: /docs/bestpractices/firststeps
---

## AWS Account First Steps

For teams or individuals that are creating an AWS account, here are some essential first steps that you should take.  
This guide assumes your account is a UCSB Campus Cloud account and that you have received an email from the Campus Cloud team saying your account is now ready for use.

1. **Log in to your AWS Account**. The Campus Cloud team has configured new accounts to use campus single sign on for user authentication and a mapping of identity groups to [AWS Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) for authorization. Your account will come with four pre-defined roles:  

    *  Administrator: This role has full access and can delegate permissions to every service and resource in AWS. Provides full access to AWS services and resources.
    *  PowerUser: Provides full access to AWS services and resources, but does not allow management of [IAM](https://docs.aws.amazon.com/iam/index.html). This user performs application development tasks and can create and configure resources and services that support AWS aware application development.
    *  ReadOnly: Provides read-only access to AWS services and resources. This user can view a list of AWS resources and basic metadata in the account across all services. The user cannot read resource content or metadata that goes beyond the quota and list information for resources.
    *  Billing: This user has access to view billing information, The user can monitor the costs accumulated for the entire AWS service.  

    You will use the "Manage Group Tags" tool available at [im.ucsb.edu](https://im.ucsb.edu) to add and remove members from the above groups. Please note, you must Log in first to access the tool.

    The Campus Single Sign On page for AWS is [aws.cloud.ucsb.edu](https://aws.cloud.ucsb.edu) 

    Be sure to select one of the supported Campus Cloud Regions, *US-West-2 (Oregon) or US-East-1 (N.Virginia). We recommend starting in US-West-2.*

2. **Verify your Billing Alert**

    When you created your Purchase Order through [Gateway](https://gateway.procurement.ucsb.edu), you provided a budget and duration for your account. The Campus Cloud team has configured your account for a billing alert based on your provided budget and estimated monthly spend. If your monthly bill is forecasted to go over your budget you will get a notification. Please verify that you have an email address subscribed to the configured billing alert.

3. **Verify [CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)**,
**[Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html), and
[GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) are enabled**.  

    The Campus Cloud team has configured your account to have CloudTrail, Securty Hub, and Guard Duty enabled. All three services will send findings to the AWS Logging Account for inspection.
    Cloud Trail logs every AWS API call, so all actions done in the AWS console will be logged. Cloud Trail is your audit log for all activities done by those whom are granted access.

4. **Enable MFA on the Root User**

    If you have been provided with root user credentials; you goal should be to enable MFA on the root user and stop using the root user for day to day tasks.

    *  Create a strong root account password
    *  enable physical MFA on the root account
        *  AWS hardware based MFA options are limited, please choose from a supported vendor.
        *  It is advised to purchase two physical based MFAs for the root user, one will be a backup.
    *  Create a process for storing and retrieving these credentials only when absolutely necessary.
        *  There are rare [tasks](https://docs.aws.amazon.com/general/latest/gr/aws_tasks-that-require-root.html) where using the root user is required.

5. **Configure your account’s [alternate contacts](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-account-payment.html#account-contacts)** to point to a group rather than an individual. For example, create separate email distribution lists for billing, operations, and security and configure these as Billing, Security, and Operations contacts in each active AWS account. This ensures that multiple people will receive AWS notifications and be able to respond, even if someone is on vacation, changes roles, or leaves the company. For details see the [Best Practices for Contacts]({{site.url}}/docs/bestpractices/contacts).

6. **AWS Enterprise Support**
   *  [Enterprise support](https://aws.amazon.com/premiumsupport/features/) is available to all child accounts. To get started use the Support drop-dwon at the top right when logged in to your Landing Zone account.
   *  Plan provides web, email, chat, and phone access to support
   *  A Technical Account Manager (TAM) and Concierge Team is provided and shared across the participating UCs
   *  Single support charge billed at the EDP AWS Organization Payer account

7. **Create Network Connectivity**
Use the Service Catalog Product, *Simple VPC with Campus Connectivity*, provided by the UCSB Campus Cloud Team to create a VPC that will quickly provide internet and VPN (if needed) access in your account. See [Service Catalog](servicecatalog) for more info.
