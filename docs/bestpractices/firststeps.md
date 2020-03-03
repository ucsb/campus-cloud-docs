---
title: First Steps
description: First Steps after you access your Cloud Account
permalink: /docs/bestpractices/firststeps
---

## AWS Account First Steps

For teams or individuals that are creating an AWS account, here are some essential first steps that you should take.  
This guide assumes your account is a UCSB Campus Cloud account and that you have recieved an email from the Campus Cloud teams
saying your account is now ready for use.

1. Verify your Billing Alert

When you created your Purchase Order through [Gateway](https://gateway.procurement.ucsb.edu), you provided a budget and duration for your account. The Campus Cloud team has configured your account for a billing alert based on your provided budget and estimated monthly spend. If your monthly bill is forecasted to go over your budget you will get a notification. Please verify that you have an email address subscribed to the configured billing alert.

2. Verify [CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html),
[Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html), and
[GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) are enabled.

The Campus Cloud team has configured your account to have CloudTrail, Securty Hub, and Guard Duty enabled. All three services will send findings to the AWS Logging Account for inspection.
Cloud Trail logs every AWS API call, so all actions done in the AWS console will be logged. Cloud Trail is your audit log for all activities done by those whom are granted access.

3. Enable MFA on the Root User

If you have been provided with root user credentials; you goal should be to enable MFA on the root user and stop using the root user for day to day tasks.

*  Create a strong root account password
*  enable physical MFA on the root account
  *  AWS hardware based MFA options are limited, please choose from a supported vendor.
  *  It is advised to purchase two physical based MFAs for the root user, one will be a backup.
*  Create a process for storing and retrieving these credentials only when absolutely necessary.  
  *  There are rare [tasks](https://docs.aws.amazon.com/general/latest/gr/aws_tasks-that-require-root.html) where using the root user is required.

4. Configure your account’s [alternate contacts](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-account-payment.html#account-contacts) to point to a group rather than an individual. For example, create separate email distribution lists for billing, operations, and security and configure these as Billing, Security, and Operations contacts in each active AWS account. This ensures that multiple people will receive AWS notifications and be able to respond, even if someone is on vacation, changes roles, or leaves the company. For details see the [Best Practices for Contacts]({{site.url}}/docs/bestpractices/contacts).

5. For critical production services, you should sign up for an [AWS support plan](https://aws.amazon.com/premiumsupport/features/) that aligns with your organization’s support expectations. Business and Enterprise support plans provide additional contact mechanisms (web, chat, and phone) that are especially useful when a customer needs an immediate response from AWS.
