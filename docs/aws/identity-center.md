---
title: AWS Identity Center
description: User guide to implementing Identity Center with supported AWS Services and Application 
permalink: /docs/aws/identity-center
last_reviewed: 2026-08-03
redirect_from:
  - /docs/firststeps/awsidentitycenter
---

# AWS Identity Center (IdC) Overview

UCSB Campus Cloud uses **Identity Center (IdC)** as a centralized service for connecting workforce users to AWS managed applications such as Kiro, Transform, and Quick. The Campus Cloud Team connects Identity Center to an external identity provider (SCIM) to populate a directory of users from the Campus' Identity system.

https://ucsb-identity-center.awsapps.com/start

The above link can be used to allow users to sign in with their netid credentials (netid@ucsb.edu) to connected services and applications integrated with Identity Center.

* TOC
{:toc}

---

## Implementation with Kiro

Account Owners or users with console access can enable Kiro for use within teams:

1. Navigate to Kiro/Amazon Q Developer in the AWS Console.
2. Select 'Setup as Admin'.
3. Use Identity Center as identity provider.
4. Organization Managed Instance should allow you to search for users (netids) to select for subscriptions.

Once the subscription has been set up, the user can now navigate to https://app.kiro.dev/signin and sign in using the “Your Organization” method. Here, they can enter the ‘Start URL’ which can be found in the management console for Kiro (https://ucsb-identity-center.awsapps.com/start). Be sure to advise users to select us-west-2 for the region, as that is where the shared Organization Instance of Identity Center is hosted.

It should be clear that the configuration and oversight of the Kiro Instance’s settings/guardrails are of the responsibility of the Administrator. Please review the settings page in the Management Console to adjust Kiro and Shared Settings to your liking. Likewise, all subscription costs will be included in your monthly invoice for all resources, paid to your account's Purchase Order.

## Implementation with Transform

To set up AWS Transform simply head over to the AWS Transform service and use the ‘Enable Web Application’ setup wizard. Use the manual setup option, making sure to select AWS IAM Identity Center (IdC) as your User Access method.

A known bug during this process is receiving this message:

![AWS Console Error Message showing SCP preventing user from Listing Instances of Identity Center]({{ "/assets/img/idc-bug.png" | relative_url }})

Disregard it, and continue by Enabling the Web Application. Once in the dashboard, you can verify the Organization Instance is active by searching an active netid when adding a new user. More in depth information on using Transform as a service in [AWS Transform Documentation](https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html).



