---
title: AWS Overview
description: Overview of the UCSB Campus Cloud AWS environment — accounts, regions, default configuration, and how to access it.
permalink: /docs/aws/
last_reviewed: 2026-10-23
---

# AWS at UCSB

The UCSB Campus Cloud AWS platform uses a multi-account structure where every
account is pre-configured with guardrails, networking, audit logging, and
default roles. Your team can start building right away without setting up
security infrastructure from scratch.

---

## Key Facts

| Item | Value |
|---|---|
| Sign-in URL | [aws.cloud.ucsb.edu](https://aws.cloud.ucsb.edu) |
| Identity Provider | Shibboleth (UCSB netID) |
| Supported Regions | us-east-1 (N. Virginia), us-west-2 (Oregon) |
| New Account Turnaround | ~2 business days after PO is approved |

---

## Requesting an AWS Account

Follow the standard [procurement process]({{ "/getting-started" | relative_url }}) via
UCSB Gateway. In addition to the standard form fields, be ready to provide:

* **Region preference** — us-east-1 (N. Virginia), us-west-2 (Oregon), or both
* **Campus network connectivity** — whether you need a Transit Gateway
  attachment to reach on-premises UCSB systems
* **Estimated monthly spend**
* **Use case** — research, coursework, administrative, etc.

After your PO is approved, the Cloud Team will provision the account within
approximately 2 business days and send a confirmation email.

---

## Account Structure

Accounts live inside an **AWS Organization** managed by the Cloud Team.

New and imported accounts will have full guardrails and
[NIST 800-171]({{ "/glossary/" | relative_url }}) controls applied. These
controls provide robust security and are suitable for most use cases. If they
do not meet your needs, please contact the Cloud Team by opening a
[ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5).

---

## What Is Pre-configured

When your account is provisioned, the Cloud Team will:

* **Attach your account** to the AWS Organization and apply guardrail policies
* **Enable AWS Security Hub** with automated checks for NIST 800-171-aligned accounts
* **Enable AWS Config** to track configuration changes
* **Enable AWS CloudTrail** (organization-level, cannot be disabled)
* **Pre-wire networking** — your account receives a VPC connected to the
  campus network (if requested)
* **Create four default IAM roles** for your team (see [First Steps]({{ "/docs/aws/first-steps" | relative_url }}))

---

## Regions

All workloads must run in **us-east-1 or us-west-2** (with a limited,
programmatic-only Amazon Bedrock exception in two additional regions). See
[Guardrails & SCPs]({{ "/docs/aws/guardrails" | relative_url }}) for details and exceptions.

---

## Roles

Four roles are created in every account. Assignments are managed in [Identity Manager](https://im.ucsb.edu).

| Role | Capabilities |
|---|---|
| Administrator | Full account access (use sparingly) |
| PowerUser | Create/manage most resources; cannot modify IAM roles |
| ReadOnly | View resource configurations and security posture |
| Billing | View billing data only |

See the [First Steps]({{ "/docs/aws/first-steps" | relative_url }}) page for instructions on
adding and removing users.

---

## Service Catalog

The AWS [Service Catalog]({{ "/docs/aws/service-catalog" | relative_url }}) provides pre-approved,
pre-configured product templates for common infrastructure patterns. Using a
Service Catalog product is the recommended way to provision new infrastructure
because the templates are already configured for UCSB compliance requirements.

---

## Next Steps

* [Request an Account]({{ "/getting-started" | relative_url }})
* [First Steps]({{ "/docs/aws/first-steps" | relative_url }})
* [Networking]({{ "/docs/aws/networking" | relative_url }})
* [Guardrails & SCPs]({{ "/docs/aws/guardrails" | relative_url }})
* [Security]({{ "/docs/aws/security" | relative_url }})
* [Service Catalog]({{ "/docs/aws/service-catalog" | relative_url }})
* [Identity Center]({{ "/docs/aws/identity-center" | relative_url }})
* [Cost Management]({{ "/docs/general/cost-management" | relative_url }})
* [Support]({{ "/docs/general/support" | relative_url }})
