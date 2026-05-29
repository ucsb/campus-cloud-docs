---
title: Identity & Access Management
description: How to grant and manage access to Campus Cloud accounts — UCSB identity, group-based access, and least privilege across AWS, Azure, and GCP.
permalink: /docs/general/identity
last_reviewed: 2026-05-29
---

# Identity & Access Management

Every Campus Cloud account uses your **UCSB identity** — you sign in with your
`@ucsb.edu` NetID, and only `@ucsb.edu` accounts can be granted access. There
are no separate cloud passwords to create or manage.

This page covers the principles that apply everywhere. For step-by-step
instructions, follow the link to each provider's First Steps page.

---

## Manage Access With Groups, Not One-Off Grants

Wherever the platform provides access **groups**, add and remove people through
the group rather than granting access to individuals directly. Group-based
access is easier to audit, survives staff turnover, and — importantly — is often
the *only* way a person receives the full set of permissions they need. A direct
grant on a single account or project can silently miss related access such as
**billing data** or the **campus Shared VPC**.

| Provider | How access is granted | Where you manage it |
|---|---|---|
| **AWS** | Four role groups per account (Administrator, PowerUser, ReadOnly, Billing) | [im.ucsb.edu](https://im.ucsb.edu) → Manage Group Tags |
| **GCP** | Four Google Groups per project (owners, editors, viewers, billing) | [groups.google.com](https://groups.google.com) (project owners are group Managers) |
| **Azure** | Custom RBAC roles assigned to users | Azure portal → Access control (IAM) |

{% include alert.html type="warning" title="GCP: use the project groups" content="On GCP, billing-data access and Shared VPC access are attached to the per-project groups — not to direct IAM grants. Add people to the project's owners/editors/viewers/billing groups so they get the access they actually need. See GCP First Steps." %}

* **AWS** — see [AWS First Steps — Adding and Removing Users]({{ "/docs/aws/first-steps#step-2--review-your-default-roles" | relative_url }}).
* **GCP** — see [GCP First Steps — Adding and Removing Users]({{ "/docs/gcp/first-steps#step-2--verify-your-access" | relative_url }}).
* **Azure** — see [Azure First Steps — Adding and Removing Users]({{ "/docs/azure/first-steps#step-3--review-your-roles" | relative_url }}).

---

## Use the Least Privilege Needed

Assign each person the **minimum role** for their responsibilities, and reserve
the most powerful roles for setup and access-management tasks. See the
[Least-Privilege Principle]({{ "/docs/general/security#least-privilege-principle" | relative_url }})
on the Security page for the recommended role for each provider.

---

## Only @ucsb.edu Accounts

All three providers require a `@ucsb.edu` identity. Personal Gmail or Microsoft
accounts cannot be granted access, and attempts to share an account publicly are
blocked by guardrails.

For collaborators outside UCSB, see
[External Collaborators]({{ "/docs/general/security#external-collaborators" | relative_url }}).

---

## Prefer Functional Emails for Ownership

Where you designate an owner or primary contact, use a shared
[functional email]({{ "/glossary/" | relative_url }}) (e.g.,
`mylab-cloud@ucsb.edu`) rather than a personal address, so access and
notifications survive staff changes.
