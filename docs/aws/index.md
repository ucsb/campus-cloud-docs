---
title: AWS Overview
description: Overview of the UCSB Campus Cloud AWS environment — accounts, regions, default configuration, and how to access it.
permalink: /docs/aws/
last_reviewed: 2026-04-03
---

## AWS at UCSB

The UCSB Campus Cloud AWS platform uses a multi-account structure where every
account is pre-configured with guardrails, networking, audit logging, and
default roles. Your team can start building right away without setting up
security infrastructure from scratch.

---

## Key Facts

| Item | Value |
|---|---|
| Sign-in URL | [aws.cloud.ucsb.edu](https://aws.cloud.ucsb.edu) |
| Identity Provider | Shibboleth (UCSB NetID) |
| Supported Regions | us-east-1 (N. Virginia), us-west-2 (Oregon) |
| New Account Turnaround | ~2 business days after PO is approved |

---

## Requesting an AWS Account

Follow the standard [procurement process]({{ "/getting-started" | relative_url }}) via
UCSB Gateway. In addition to the standard form fields, be ready to provide:

* **Region preference** — us-east-1 (N. Virginia), us-west-2 (Oregon), or both
* **Campus network connectivity** — whether you need a Transit Gateway
  attachment to reach on-premises UCSB systems
* **Estimated monthly spend** — used to set your initial billing alarm
* **Use case** — research, coursework, administrative, etc.

After your PO is approved, the Cloud Team will provision the account within
approximately 2 business days and send a confirmation email.

---

## Account Structure

Accounts live inside an **AWS Organization** managed by the Cloud Team.
They are organized into Organizational Units (OUs). Policies applied at
the OU level are inherited by every account inside it.

| OU | Purpose |
|---|---|
| UCSB Baseline V2 | Production workloads — research, academic, and administrative accounts with full guardrails and NIST 800-171 controls |
| Sandbox | Exploration and development — no production data allowed |

New accounts are placed in **UCSB Baseline V2** by default. Contact the
Cloud Team if your needs change.

---

## What Is Pre-configured

When your account is provisioned, the Cloud Team will:

* **Attach your account** to the AWS Organization and apply guardrail policies
* **Enable AWS Security Hub** and configure NIST 800-171 standards
* **Enable AWS Config** to track configuration changes
* **Enable AWS CloudTrail** (organization-level, cannot be disabled)
* **Pre-wire networking** — your account receives a VPC connected to the
  campus network (if requested)
* **Create four default IAM roles** for your team (see [First Steps]({{ "/docs/aws/first-steps" | relative_url }}))
* **Set a billing alarm** at the threshold you specify during account request

---

## Regions

All workloads must run in **us-east-1 or us-west-2** (with a limited exception
for Amazon Bedrock). See [Guardrails & SCPs]({{ "/docs/aws/guardrails" | relative_url }}) for details
and exceptions.

---

## Roles

Four roles are created in every account using the naming pattern
`ucsb-idp-<AccountName>-<RoleName>`. Assignments are managed via **im.ucsb.edu**.

| Role | Capabilities |
|---|---|
| Administrator | Full account access (use sparingly) |
| PowerUser | Create/manage most resources; cannot modify IAM roles |
| ReadOnly | View-only; useful for auditors and stakeholders |
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

## Enterprise Support

Every Campus Cloud AWS account is automatically enrolled in **AWS Enterprise
Support** at no additional cost to your account. This includes:

* **Technical Account Manager (TAM)** — a named AWS technical advisor shared
  across the UCSB organization. The TAM meets with the Cloud Team twice monthly
  and can assist with architecture reviews, service limits, and best practices.
* **AWS Concierge Team** — assists with billing and account questions.
* **Support Channels** — you can open AWS Support cases via web, email, chat,
  or phone directly from the AWS Console (Support → Create case).

Response times depend on case severity — see
[AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/) for SLA
details.

{% include alert.html type="info" title="Open a Campus Cloud ticket first for platform issues" content="For issues related to account access, networking, guardrails, or Campus Cloud configuration, <a href='https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5'>open a ServiceNow ticket with the Cloud Team</a> rather than an AWS Support case. Use AWS Support for service-specific technical questions about your workloads." %}

---

## Next Steps

* [Request an Account]({{ "/getting-started/procurement" | relative_url }})
* [First Steps]({{ "/docs/aws/first-steps" | relative_url }})
* [Networking]({{ "/docs/aws/networking" | relative_url }})
* [Guardrails & SCPs]({{ "/docs/aws/guardrails" | relative_url }})
* [Security]({{ "/docs/aws/security" | relative_url }})
* [Service Catalog]({{ "/docs/aws/service-catalog" | relative_url }})
* [Cost Management]({{ "/docs/general/cost-management" | relative_url }})
