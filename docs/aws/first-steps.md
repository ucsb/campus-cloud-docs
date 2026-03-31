---
title: AWS First Steps
description: What to do after your AWS account is provisioned — sign in, set up billing, deploy your first resource.
permalink: /docs/aws/first-steps
last_reviewed: 2026-03-30
---

## Getting Started With Your AWS Account

Your account is ready when you receive the provisioning confirmation email from
the Cloud Team. Follow the steps below to get set up.

---

## Step 1 — Sign In

1. Go to [aws.cloud.ucsb.edu](https://aws.cloud.ucsb.edu).
2. Sign in with your UCSB NetID and password (Shibboleth SSO).
3. On the AWS access portal, select your account name from the list.
4. Choose a permission set:
   * **PowerUser** for day-to-day work
   * **Administrator** for IAM or billing tasks (use sparingly)
5. Click **Management Console** to open the AWS Console.

{% include alert.html type="info" title="Bookmark the SSO portal" content="Always start at aws.cloud.ucsb.edu — do not use the standard AWS Console login page. Direct console logins using an IAM user password are not permitted." %}

---

## Step 2 — Verify Your Budget Alarm

A billing alarm was configured during account provisioning at the threshold you
specified in your account request. Confirm it is in place:

1. In the Console, navigate to **CloudWatch → Alarms → All alarms**.
2. Verify a billing alarm exists and the threshold is correct.
3. Confirm the SNS subscription is set to email you or your team.

If no alarm is present, open a [ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5) to request one.

---

## Step 3 — Set Account Contacts

Set your Alternate contacts so your team receives security findings, service
health events, and billing alerts. See [Account Contacts](/docs/general/contacts)
for general best practices.

The Cloud Team manages the Primary contact. **You set the Alternate contacts:**

1. In the top-right dropdown, click your account name → **Account**.
2. Scroll to **Alternate contacts**.
3. Set the Security, Operations, and Billing contacts to your team's functional
   email addresses (e.g., `mylab-cloud@ucsb.edu`).
4. Save changes.

---

## Step 4 — Review Your Default Roles

Four IAM roles are pre-created in every account. Add your team members via
**im.ucsb.edu** (see [Identity & Access](/docs/general/identity)).

You do not need to create IAM users or local passwords. All access is
federated through UCSB Shibboleth.

---

## Step 5 — Review Guardrails

Policy controls (SCPs) are applied at the organization level and cannot be
modified at the account level. Before building, familiarize yourself with the
key restrictions on the [Guardrails](/docs/aws/guardrails) page so you do not
encounter unexpected `Access Denied` errors.

---

## Step 6 — Configure Networking

If your request included campus network connectivity:

1. Navigate to **VPC → Your VPCs** to confirm your VPC exists.
2. Check **VPC → Transit Gateway Attachments** to confirm it is attached.
3. Contact the Cloud Team ([ServiceNow](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5)) if the VPC or attachment is missing.

If you only need internet access and no campus connectivity, a standalone VPC
can be deployed via the [Service Catalog](/docs/aws/service-catalog).

---

## Step 7 — Deploy Your First Resource

Use the [Service Catalog](/docs/aws/service-catalog) to deploy
pre-approved infrastructure templates. This is the fastest way to get
compliant resources up and running.

For custom infrastructure, the AWS Console and CLI are both available.
CLI access requires configuring the AWS SSO credential helper:

```bash
aws configure sso --profile my-ucsb-account
# SSO start URL: https://aws.cloud.ucsb.edu
# SSO region: us-east-1
# Choose your account and role when prompted
aws s3 ls --profile my-ucsb-account
```

---

## Step 8 — Tag Your Resources

All resources must be tagged with the required tags. Missing tags will
eventually trigger compliance alerts or resource removal.

See the [Tagging](/docs/general/tagging) page for required tags and allowed values.

---

## Getting Help

| Issue | Where to go |
|---|---|
| Access problems (can't sign in, missing role) | [Identity & Access](/docs/general/identity) |
| Missing VPC, networking issues | [Networking](/docs/aws/networking) |
| Policy violations / Access Denied | [Guardrails](/docs/aws/guardrails) |
| Billing questions | [Cost Management](/docs/general/cost-management) |
| Everything else | [ServiceNow](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5) |
