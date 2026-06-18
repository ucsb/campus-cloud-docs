---
title: GCP First Steps
description: What to do after your GCP project is provisioned — sign in, verify setup, deploy your first resource.
permalink: /docs/gcp/first-steps
last_reviewed: 2026-06-18
redirect_from:
  - /docs/firststeps/gcpfirststeps
---

# Getting Started With Your GCP Project
{:.no_toc}

Your project is ready when you receive the provisioning confirmation from the
Cloud Team. Follow the steps below to get set up.

* TOC
{:toc}

---

## Step 1 — Sign In

1. Go to [console.cloud.google.com](https://console.cloud.google.com).
2. Sign in with your UCSB email address (`yournetid@ucsb.edu`).
   * UCSB uses Google Workspace managed through Microsoft Entra ID — your
     UCSB NetID and password work here.
   * Complete Duo MFA if prompted.
3. After signing in, click the project selector at the top of the page (next to
   the Google Cloud logo) and find your project by name or ID.

{% include alert.html type="info" title="Use your @ucsb.edu account" content="Do not sign in with a personal Gmail account. All Campus Cloud resources are in the ucsb.edu Google Workspace domain. Only @ucsb.edu accounts can access Campus Cloud GCP projects." %}

---

## Step 2 — Verify Your Access

1. Go to [Cloud Hub](https://console.cloud.google.com/cloud-hub/) and confirm
   your project appears and opens.
2. If it does, your access is working — it comes from your membership in one of
   the project's access groups (described below).

If you cannot open the project, contact the Cloud Team.

If you are the project owner and need to give colleagues access, **do not add
them under IAM & Admin** — manage membership in the project's Google Groups
instead. See [Adding and Removing Users](#adding-and-removing-users) below.

### Adding and Removing Users

Every project comes with **four Google Groups** that carry the project's
access. Manage access by adding and removing people in these groups — **do not
grant roles to individuals directly** under IAM & Admin → IAM.

| Group | Access it grants |
|---|---|
| `<id>-owners@gcp.cloud.ucsb.edu` | Full project access (Owner), **view billing data**, and use of the campus **Shared VPC** |
| `<id>-editors@gcp.cloud.ucsb.edu` | Create and manage most resources (Editor), and use of the campus **Shared VPC** |
| `<id>-viewers@gcp.cloud.ucsb.edu` | Read-only access (Viewer) |
| `<id>-billing@gcp.cloud.ucsb.edu` | View billing data and read-only project access |

(`<id>` is your project ID. Find the exact group addresses under
**IAM & Admin → IAM**, where the groups are listed as members.)

{% include alert.html type="warning" title="Use the groups, not direct grants" content="Billing-data access and Shared VPC access are attached to these groups, not to direct IAM grants. If you add someone straight to project IAM, they will be missing billing visibility and the campus network — add them to the appropriate group instead." %}

**To add or remove members**, go to [groups.google.com](https://groups.google.com)
and open the group. Project owners are **Managers** of all four groups, so they
can manage membership for every access level. Only `@ucsb.edu` accounts can be
added — personal Gmail accounts or accounts from other organizations are not permitted.

After someone is added to a group, allow up to **30 minutes** for the new
access to fully propagate before they have all their permissions.

See [Identity & Access]({{ "/docs/general/identity" | relative_url }}) for the
cross-provider picture.

---

## Step 3 — Review Project Contacts

GCP uses **Essential Contacts** to route operational notifications to your team.
**These are configured automatically** when your project is created — they point
at your project's access groups, so there is nothing to set up:

| Group | Notifications it receives |
|---|---|
| `<id>-owners` | Billing, Legal, Security, Suspension, and Technical |
| `<id>-billing` | Billing only |

Because contacts are tied to the groups, you change **who** receives these
notifications by managing group membership — the same way you
[manage access](#step-2--verify-your-access). There is no need to add or verify
contacts manually.

If you also want notifications sent to an address that isn't a group member (for
example, a shared ticketing alias), you can add it under
[Essential Contacts](https://console.cloud.google.com/iam-admin/essentialcontacts)
with your project selected. See [Account Contacts]({{ "/docs/general/contacts" | relative_url }})
for general best practices.

---

## Step 4 — Review Org Policy Constraints

Organization policies are applied at the folder level and inherited by your
project. Before creating resources, review the key constraints on the
[Guardrails]({{ "/docs/gcp/guardrails" | relative_url }}) page to understand what is allowed and
what will be blocked.

Key constraints to know:
* **No external IP addresses** — VMs cannot have public IPs by default
* **Custom-mode VPCs only** — Auto-mode VPC networks are blocked
* **Allowed regions:** us-central1 and us-west1 (other regions may be blocked)

---

## Step 5 — Networking

Your project is automatically attached to the campus Shared VPC at provisioning.
Outbound internet access via Cloud NAT is included — no ticket needed.

Org policy blocks you from creating VPCs yourself — only the Cloud Team's
automation account can provision network resources.

* **Internet egress** is available immediately via Cloud NAT.
* **Access to UCSB campus resources** — not currently available for GCP.
  There is no VPN or Interconnect between GCP and the UCSB campus network at
  this time. Contact the Cloud Team to discuss options.

If your workload uses only managed services (Cloud Storage, BigQuery, Pub/Sub,
Cloud Functions, Cloud Run), you may not need to think about networking at all.

See [GCP Networking]({{ "/docs/gcp/networking" | relative_url }}) for full details.

---

## Step 6 — Enable Required APIs

GCP services must be enabled via the API before you can use them. Most
common APIs are pre-enabled, but check:

1. Navigate to **APIs & Services → Enabled APIs and Services**.
2. Confirm the APIs you need are enabled.
3. To enable a new API: **+ Enable APIs and Services** → search and enable.

Note: Some APIs require billing to be enabled. Org policies may block specific
APIs — if you get a policy error, see [Guardrails]({{ "/docs/gcp/guardrails" | relative_url }}).

---

## Step 7 — Verify Required Tags

Your project should already have the required Resource Manager Tags set by the
Cloud Team at provisioning. Verify them by navigating to **IAM & Admin →
Settings → Tags** (not IAM & Admin → Tags).

The owner-settable tags (`environment`, `mission`, `protection-level`,
`availability-level`, `recovery-level`, `dept`) can be updated by you if they
need to change.

See [Tagging & Labels]({{ "/docs/general/tagging" | relative_url }}) for allowed values and how to update them.

---

## Step 8 — Verify Budget Alert (Funded Projects)

1. Navigate to **Billing → Budgets & alerts**.
2. Confirm a billing budget exists for your project.
3. The budget notifies you at 50%, 90%, and 100% of the budget by default.
4. To change thresholds or recipients, edit the budget.

See [Costs & Billing]({{ "/docs/general/cost-management" | relative_url }}) for more information.

---

## Getting Help

| Issue | Where to go |
|---|---|
| Access problems | [ServiceNow](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5) |
| Networking issues | [Networking]({{ "/docs/gcp/networking" | relative_url }}) |
| Org policy violations | [Guardrails]({{ "/docs/gcp/guardrails" | relative_url }}) |
| Billing questions | [Costs & Billing]({{ "/docs/general/cost-management" | relative_url }}) |
| Everything else | [ServiceNow](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5) |
