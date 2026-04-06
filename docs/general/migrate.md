---
title: Migrate to Campus Cloud
description: How to migrate an existing personal or free cloud account to the Campus Cloud
permalink: /docs/general/migrate
last_reviewed: 2026-04-01
redirect_from:
  - /docs/guidelines/migrate
---

# Migrate to Campus Cloud

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

## How to Migrate

Follow the standard
[Gateway procurement process]({{ "/getting-started" | relative_url }}).
When completing the Campus Cloud form, mention your existing account or project
so the Cloud Team can migrate it into the Landing Zone rather than creating a
new one.

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

## If Your Account Uses a @ucsb.edu Email

AWS restricts direct account creation using `@ucsb.edu` email addresses — you
will receive an "error processing your request" message if you try. All AWS
accounts associated with UCSB email addresses must be created through or
migrated into the Campus Cloud.

See [Security — External Collaborators]({{ "/docs/general/security#external-collaborators" | relative_url }}) for details.
