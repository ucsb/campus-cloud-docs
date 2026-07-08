---
title: AWS First Steps
description: What to do after your AWS account is provisioned — sign in, set up billing, deploy your first resource.
permalink: /docs/aws/first-steps
last_reviewed: 2026-07-08
redirect_from:
  - /docs/firststeps/awsfirststeps
---

# Getting Started With Your AWS Account
{:.no_toc}

Your account is ready when you receive the provisioning confirmation email from
the Cloud Team. Follow the steps below to get set up.

These steps also work as a checklist for an established account — revisit them
any time, such as after your
[annual check-in]({{ "/docs/general/support#annual-account-check-ins" | relative_url }}),
to verify your contacts, budget, and tags are still the way you want them.

* TOC
{:toc}

---

## Step 1 — Sign In

1. Go to [aws.cloud.ucsb.edu](https://aws.cloud.ucsb.edu).
2. Sign in with your UCSB NetID and password (Shibboleth SSO).
3. On the AWS access portal, select your account name from the list.
4. Choose a role:
   * **PowerUser** for day-to-day work
   * **Administrator** for IAM or billing tasks (use sparingly)
5. Click **Management Console** to open the AWS Console.

{% include alert.html type="info" title="Bookmark the SSO portal" content="Always start at aws.cloud.ucsb.edu — do not use the standard AWS Console login page. Direct console logins using an IAM user password are not permitted." %}

---

## Step 2 — Review Your Default Roles

Four IAM roles are pre-created in every account. You do not need to create IAM
users or local passwords — all access is federated through UCSB Shibboleth.

| Role | What It Can Do |
|---|---|
| Administrator (`ucsb-idp-administrator`) | Full access to all AWS services and resources, including IAM |
| PowerUser (`ucsb-idp-poweruser`) | Full access to AWS services; cannot manage IAM |
| ReadOnly (`ucsb-idp-readonly`) | View resource configurations and security posture |
| Billing (`ucsb-idp-billing`) | View billing and cost data only |

Use **PowerUser** for day-to-day work. Reserve **Administrator** for IAM
changes and initial setup.

### Adding and Removing Users

Use the "Manage Group Tags" tool at [im.ucsb.edu](https://im.ucsb.edu):

1. Log in with your UCSB NetID.
2. Go to **Admin Tools → Manage Group Tags**.
3. Find the group for your account role (e.g., `ucsb-idp-administrator-123456789012`).
4. Owners can add and remove Members. Members are authorized for the role.

Only account owners have permission to add members. Owners are not granted the
role themselves — add yourself as a member if you also want access.

---

## Step 3 — Review Account Contacts

Your account's **alternate contacts** — the Billing, Operations, and Security
addresses that receive notifications such as security findings, service health
events, and billing notices — are **set automatically when your account is
provisioned**, using the contact information you supplied on your account
request form. There is nothing you need to set up.

To see what is on file, open the account menu (top right) → **Account** and
scroll to **Alternate contacts**.

To change a contact, open a [ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5)
so the Cloud Team can update it. Use a shared functional email address rather
than a personal one, so contacts survive staff changes. See
[Account Contacts]({{ "/docs/general/contacts" | relative_url }}) for general best practices.

---

## Step 4 — Review Guardrails

Policy controls (SCPs) are applied at the organization level and cannot be
modified at the account level. Before building, familiarize yourself with the
key restrictions on the [Guardrails]({{ "/docs/aws/guardrails" | relative_url }}) page so you do not
encounter unexpected `Access Denied` errors.

---

## Step 5 — Configure Networking

If your request included campus network connectivity:

1. Navigate to **VPC → Your VPCs** to confirm your VPC exists.
2. Check **VPC → Transit Gateway Attachments** to confirm it is attached.
3. Contact the Cloud Team ([ServiceNow](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5)) if the VPC or attachment is missing.

If you only need internet access and no campus connectivity, a standalone VPC
can be deployed via the [Service Catalog]({{ "/docs/aws/service-catalog" | relative_url }}).

---

## Step 6 — Deploy Your First Resource

Use the [Service Catalog]({{ "/docs/aws/service-catalog" | relative_url }}) to deploy
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

## Step 7 — Tag Your Resources

All resources must be tagged with the required tags. Missing tags will
eventually trigger compliance alerts or resource removal.

See the [Tagging]({{ "/docs/general/tagging" | relative_url }}) page for required tags and allowed values.

---

## Step 8 — Set Up or Verify a Budget Alert

Every account should have a monthly budget that emails you before spending
exceeds expectations. The easiest way to create one is the **Fixed Monthly
Budget with Notification** product in the
[Service Catalog]({{ "/docs/aws/service-catalog" | relative_url }}), which
alerts you when your forecasted spend is on track to exceed your budget.

To verify your budget later:

1. In the Console, navigate to **Billing and Cost Management → Budgets**.
2. Confirm a monthly budget exists and the amount is correct.
3. Open the budget and check that its alert emails you or your team.

If you need a hard spending cap that restricts resource creation — not just a
notification — use the **Budget Alert and Action on Threshold** product,
also in the [Service Catalog]({{ "/docs/aws/service-catalog" | relative_url }}).

See [Costs & Billing]({{ "/docs/general/cost-management" | relative_url }}) for
more on monitoring your spending.

---

## Getting Help

For all the ways to get help, see the
[Support]({{ "/docs/general/support" | relative_url }}) page. It covers:

* **Contacting the Cloud Team** — open a
  [ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5)
  for anything that needs tracking, or email
  [info@cloud.ucsb.edu](mailto:info@cloud.ucsb.edu).
* **Community and office hours** — the Cloud Impact Hub chat space and weekly
  drop-in office hours.
* **AWS Enterprise Support** — included with every Campus Cloud account for
  service-specific technical questions; open a case from the AWS Console.
* **Annual check-ins** — schedule a check-in with the Cloud Team to review
  your account.
