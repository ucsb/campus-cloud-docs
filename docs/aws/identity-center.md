---
title: AWS Identity Center
description: How to sign in to AWS accounts and supported AWS applications with AWS IAM Identity Center
permalink: /docs/aws/identity-center
last_reviewed: 2026-10-21
redirect_from:
  - /docs/firststeps/awsidentitycenter
---

# AWS Identity Center (IdC) Overview

**AWS IAM Identity Center (IdC)** lets you sign in to your AWS accounts with
your UCSB netID. It also lets you sign in to AWS applications such as Kiro,
AWS Transform, and Amazon Quick. The Cloud Team connects Identity Center
to the campus identity system, so you don't need a separate AWS username or
password.

This page is for account administrators. It covers signing in, command-line
access, and connecting AWS applications to UCSB's shared Identity Center.

To sign in, go to the
[UCSB AWS Identity Center sign-in page](https://ucsb-identity-center.awsapps.com/start)
and sign in with your UCSB netID and password.

* TOC
{:toc}

---

## Signing In to an Account

After you sign in, you see the AWS accounts you can use. Your access level in
each account (for example, Administrator or ReadOnly) depends on which account
groups you belong to. Account owners manage those groups — see
[AWS First Steps — Adding and Removing Users]({{ "/docs/aws/first-steps#adding-and-removing-users" | relative_url }}).

If you add someone and the account doesn't appear for them, wait 10–15 minutes
for the change to take effect.

Console sessions last up to 8 hours. After that, sign in again.

### Command-Line Access

To use the AWS Command Line Interface (CLI), open the menu on an account and
select **Access keys**. AWS offers three options. We recommend
**AWS IAM Identity Center credentials** on every platform (macOS and Linux,
Windows, or PowerShell). When the CLI asks for them, use:

* **Start URL:** `https://ucsb-identity-center.awsapps.com/start`
* **Region:** `us-west-2`

For the full steps, see the AWS guide to
[configuring the AWS CLI with IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html#sso-configure-profile-token-auto-sso).

---

## Kiro

Kiro is an AI coding tool from AWS. Account owners, or users with console
access, can turn it on for their team:

1. In the AWS Console, open Kiro / Amazon Q Developer.
2. Select **Setup as Admin**.
3. Choose Identity Center as the identity provider.
4. Search for users by netID and assign them subscriptions.

Then each user signs in to Kiro:

1. Go to the [Kiro sign-in page](https://app.kiro.dev/signin) and choose
   **Your Organization**.
2. Enter the start URL: `https://ucsb-identity-center.awsapps.com/start`.
3. Choose the **us-west-2** region. That's where UCSB's Identity Center is
   hosted.

You're responsible for Kiro's settings and guardrails in your account. Review
them in the Kiro management console. Subscription costs appear on your monthly
invoice and are charged to your account's Purchase Order.

---

## AWS Transform

To set up AWS Transform, open the service and start the
**Enable web application** wizard. Choose **Manual setup**, then choose
**AWS IAM Identity Center (IdC)** as the user access method.

You may then see a red error box. This is a known issue, and you can ignore
it. The green message below it confirms that Identity Center is ready:

![AWS Transform setup screen with AWS IAM Identity Center selected, showing a red error box and, below it, a green confirmation message]({{ "/assets/img/idc-bug.png" | relative_url }})

The key lines read:

> Failed to check AWS IAM Identity Center status. … is not authorized to
> perform: sso:ListInstances … with an explicit deny in a service control policy
>
> AWS IAM Identity Center enabled in Org management account. You can now enable
> the AWS Transform web application.

Select **Enable** to finish. To check that it worked, add a user in the
Transform dashboard and search for their netID. For more, see the
[AWS Transform documentation](https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html).

---

## Your Own Applications

If you run your own application in AWS that signs users in with SAML 2.0 or
OAuth 2.0 (common sign-in standards), you can connect it to Identity Center so
UCSB users can sign in with their netID. See the
[AWS guide to customer managed applications](https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps.html).
