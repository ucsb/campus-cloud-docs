---
title: AWS Overview
description: Overview of the UCSB Campus Cloud AWS environment — accounts, regions, default configuration, and how to access it.
permalink: /docs/aws/
last_reviewed: 2026-03-30
---

## AWS at UCSB

The UCSB Campus Cloud AWS platform is built on **AWS Control Tower** with a
multi-account structure managed by Service Control Policies (SCPs). Every
account is pre-provisioned with a consistent set of guardrails, networking
configuration, auditing, and default roles so teams can start building
quickly without setting up security infrastructure from scratch.

---

## Key Facts

| Item | Value |
|---|---|
| Sign-in URL | [aws.cloud.ucsb.edu](https://aws.cloud.ucsb.edu) |
| Identity Provider | Shibboleth (UCSB NetID) |
| Supported Regions | us-east-1 (N. Virginia), us-west-2 (Oregon) |
| New Account Turnaround | ~2 business days after PO is approved |

---

## Account Structure

Accounts live inside an **AWS Organization** managed by the Cloud Team. They
are organized into Organizational Units (OUs):

| OU | Purpose | Notes |
|---|---|---|
| Research | Regulated and sensitive research workloads | NIST 800-171 controls available |
| Academic | Coursework, labs, student projects | |
| Administrative | Business operations (HR, Finance, etc.) | |
| Sandbox | Exploration and development | No production data |
| UCSB Core | Cloud Team–managed shared services | Not for direct PI use |

New accounts are placed in the OU that matches the request type. Accounts can
be moved between OUs on request if your project's needs change.

---

## What Is Pre-configured

When your account is provisioned, the Cloud Team will:

* **Attach your account** to the AWS Organization and apply SCPs
* **Enable AWS Security Hub** and configure NIST 800-171 standards
* **Enable AWS Config** to track configuration changes
* **Enable AWS CloudTrail** (organization-level, cannot be disabled)
* **Pre-wire networking** — your account receives a VPC connected to the
  Transit Gateway for campus campus network access (if requested)
* **Create four default IAM roles** for your team (see [Identity & Access](/docs/general/identity))
* **Set a billing alarm** at the threshold you specify during account request

---

## Regions

All workloads must run in **us-east-1 or us-west-2**. Other regions are
blocked by SCP. Attempting to launch resources in any other region will
produce an `Access Denied` error from the SCP.

The region restriction does not apply to AWS global services such as IAM,
Route 53, and STS.

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

See the [Identity & Access](/docs/general/identity) page for instructions on
adding and removing users.

---

## Service Catalog

The AWS [Service Catalog](/docs/aws/service-catalog) provides pre-approved,
pre-configured product templates for common infrastructure patterns. Using a
Service Catalog product is the recommended way to provision new infrastructure
because the templates are already configured for UCSB compliance requirements.

---

## Next Steps

* [Request an Account](/docs/aws/account-request)
* [First Steps](/docs/aws/first-steps)
* [Networking](/docs/aws/networking)
* [Guardrails & SCPs](/docs/aws/guardrails)
