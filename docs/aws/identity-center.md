---
title: AWS Identity Center
description: User guide to implementing Identity Center with supported AWS Services and Application 
permalink: /docs/aws/identity-center
last_reviewed: 2026-08-03
redirect_from:
  - /docs/firststeps/awsidentitycenter
---

# AWS Identity Center (IdC) Overview

**AWS Identity Center (IdC)** is a centralized service making it possible for your users to sign in with their UCSB credentials to AWS managed services such as Kiro, Transform, and Quick. The Campus Cloud Team populates a directory of users from the Campus' Identity system and manages users and groups centrally from the Organization's management account. The instructions on this page are meant to assist account administrators with integrating the Organization's Shared instance into these supported services.

https://ucsb-identity-center.awsapps.com/start

The above link can be used to allow users to sign in with their netid credentials (netid@ucsb.edu) to connected services and applications integrated with Identity Center.

If you have a need to create a local instance of Identity Center in your account for any purpose, make a request to the Cloud Team via a [ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5).

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

## Implementation with Customer Managed Applications

Account Owners with their own managed applications in AWS that make use of SAML 2.0 or OAuth 2.0 authentication methods can provision Identity Center for provisioning of your users. Refer to the [AWS IAM Identity Center Documentation](https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps.html) for more information.



