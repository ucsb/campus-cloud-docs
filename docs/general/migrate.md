---
title: Migrate to Campus Cloud
description: How to migrate an existing personal or free cloud account to the Campus Cloud
permalink: /docs/general/migrate
last_reviewed: 2026-03-30
redirect_from:
  - /docs/guidelines/migrate
---

## Migrate to Campus Cloud

If you have an existing personal or free cloud account in AWS, Azure, or GCP,
you can migrate it into the Campus Cloud Landing Zone. Migrating gives you
UC enterprise discounts, compliance guardrails, and campus network connectivity.

---

## What Is a Personal Cloud Account?

A personal account uses a personal credit card as the payment mechanism and is
not provisioned in the Campus Cloud Landing Zone. Personal accounts:

* Do not receive UC enterprise discounts
* May not meet compliance requirements for federal grants
* Should not have a `@ucsb.edu` email address associated with them

If you are using a personal account for UCSB research or administrative purposes,
you should migrate to the Campus Cloud or take the steps below to bring it into
compliance.

---

## How to Migrate: All Providers

Contact the Cloud Team to start the migration process:
[info@cloud.ucsb.edu](mailto:info@cloud.ucsb.edu) or open a
[ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5).

Migration is a standard process the Cloud Team performs regularly. You will need
a valid Purchase Order from Gateway before migration can begin.

### What Happens During Migration

* **AWS:** Your existing account is moved into the Campus Cloud organization.
  Campus Cloud Landing Zone controls (guardrails, logging, SSO) are applied automatically.
* **Azure:** Your existing subscription is imported into the UCSB management
  group hierarchy. Policies and monitoring are applied.
* **GCP:** Your existing project is imported into the appropriate folder in the
  UCSB organization. Org policies are applied.

Existing resources in your account are generally not affected by the migration,
but resource-specific compliance findings may be generated after controls are
applied.

---

## What Is a Free Account?

A free Azure Subscription or GCP Project is created without a payment mechanism.
Free accounts are sometimes used for student coursework or personal experimentation.

### Upgrading a Free Azure Subscription to Paid
A Purchase Order must be created to cover costs. The subscription must then be
imported into the Campus Cloud Landing Zone.

### Upgrading a Free GCP Project to Paid
Contact the Cloud Team. A Purchase Order is required, and billing will be
attached through a Campus Cloud billing sub-account.

---

## If Your Account Uses a @ucsb.edu Email

AWS restricts direct account creation using `@ucsb.edu` email addresses — you
will receive an "error processing your request" message if you try. All AWS
accounts associated with UCSB email addresses must be created through or
migrated into the Campus Cloud.

See [Identity & Access]({{ "/docs/general/identity#external-collaborators" | relative_url }}) for details.
