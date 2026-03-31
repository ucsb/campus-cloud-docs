---
title: Identity & Access
description: How to sign in and manage access to your Campus Cloud account
permalink: /docs/general/identity
last_reviewed: 2026-03-30
---

## Identity & Access

All three Campus Cloud providers use your UCSB NetID for authentication. You do
not need a separate password for any cloud provider.

---

## How Sign-In Works

| Provider | How You Sign In | Where |
|---|---|---|
| AWS | Shibboleth SAML SSO via UCSB Identity | [aws.cloud.ucsb.edu](https://aws.cloud.ucsb.edu) |
| Azure | Microsoft Entra ID, federated with UCSB NetID | [portal.azure.com](https://portal.azure.com) |
| GCP | Google Workspace, federated with UCSB Entra ID | [console.cloud.google.com](https://console.cloud.google.com) |

Sign in with your full `netid@ucsb.edu` address when prompted. You will be
redirected to the UCSB login page.

---

## Default Roles

Each provider assigns a set of pre-defined roles to your account at creation.
These roles map to UCSB Identity groups that you manage at
[im.ucsb.edu](https://im.ucsb.edu).

### AWS Roles

| Role | What It Can Do |
|---|---|
| Administrator (`ucsb-idp-administrator`) | Full access to all AWS services and resources, including IAM |
| PowerUser (`ucsb-idp-poweruser`) | Full access to AWS services; cannot manage IAM |
| ReadOnly (`ucsb-idp-readonly`) | View-only access to all AWS resources |
| Billing (`ucsb-idp-billing`) | View billing and cost data only |

### Azure Roles

Azure subscriptions use four custom RBAC roles purpose-built for the Campus
Cloud. See [Azure Roles & Access](/docs/azure/roles) for the full role table,
permission details, and instructions for adding and removing users.

### GCP Roles

GCP uses standard IAM roles at the project level. The Cloud Team assigns initial
roles at project creation. Contact the Cloud Team or your project admin to adjust
your role.

---

## Adding and Removing Users

### AWS

Use the "Manage Group Tags" tool at [im.ucsb.edu](https://im.ucsb.edu):

1. Log in with your UCSB NetID.
2. Go to **Admin Tools → Manage Group Tags**.
3. Find the group for your account role (e.g., `ucsb-idp-administrator-123456789012`).
4. Owners can add and remove Members. Members are authorized for the role.

Only account owners have permission to add members. Owners are not granted the
role themselves — add yourself as a member if you want access.

### Azure

Role assignments in Azure are managed through Microsoft Entra ID. Contact your
Subscription Owner or the Cloud Team to request a role change. Your departmental
IT admin may also be able to help.

### GCP

IAM bindings are managed at the project level in the GCP Console under
**IAM & Admin → IAM**, or via the Cloud Team for platform-level roles. Only
project Owners can grant roles. Only `@ucsb.edu` accounts can be added —
personal Gmail accounts are not permitted.

---

## Least-Privilege Principle

Assign the minimum role needed for each person's responsibilities. In particular:

* Use **ReadOnly** or **Billing** AWS roles for stakeholders who only need to
  review costs or resources.
* In Azure, use **Application Owner** rather than **Subscription Owner** for
  most day-to-day work.
* In GCP, use project-level roles (Editor, Viewer) instead of Organization-level
  roles unless explicitly needed.

---

## Root and Platform Accounts

**AWS root credentials** — access is blocked by guardrail. You cannot use the
root account in a Campus Cloud AWS account. See [AWS Guardrails](/docs/aws/guardrails).

**Azure and GCP platform admin roles** — certain platform-level permissions
are reserved for the Cloud Team and cannot be self-assigned.

---

## External Collaborators

All three providers require a `@ucsb.edu` identity. External collaborators
without a UCSB NetID cannot be added directly to your account's role structure.

Options for granting access to external collaborators:

* **Create a sponsored UCSB NetID** for the collaborator through UCSB IT — this
  gives them a `@ucsb.edu` identity that works with all three providers.
* **Share data without granting account access** — for example, use pre-signed
  S3 URLs, scoped SAS tokens (Azure), or signed URLs (GCP).
* **Set up cross-institution federated access** via SAML or OIDC for the
  collaborator's home identity provider (advanced — requires Cloud Team
  involvement).
