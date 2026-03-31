---
title: GCP First Steps
description: What to do after your GCP project is provisioned — sign in, verify setup, deploy your first resource.
permalink: /docs/gcp/first-steps
last_reviewed: 2026-03-30
---

## Getting Started With Your GCP Project

Your project is ready when you receive the provisioning confirmation from the
Cloud Team. Follow the steps below to get set up.

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

## Step 2 — Verify Your IAM Role

1. Navigate to **IAM & Admin → IAM** in the left menu.
2. Confirm your `@ucsb.edu` account is listed with the appropriate role:
   * **Editor** — create and manage most resources
   * **Viewer** — read-only
   * **Project IAM Admin** — manage IAM for the project (if needed)

If you are not listed or your role is incorrect, contact the Cloud Team.

---

## Step 3 — Set Project Contacts

GCP uses **Essential Contacts** to route notifications to your team. The Cloud
Team has configured org-level contacts; you need to add project-level contacts.
See [Account Contacts](/docs/general/contacts) for general best practices.

1. Navigate to [Essential Contacts](https://console.cloud.google.com/iam-admin/essentialcontacts)
   with your project selected.
2. Click **+ Add contact**.
3. Enter a functional email address and select:
   * **Security** — Security Command Center findings
   * **Technical** — Maintenance and service disruption notices
   * **Billing** — Budget alerts and billing notifications
4. Confirm by clicking the verification link emailed to that address.
5. Repeat for each category that needs a different address.

---

## Step 4 — Review Org Policy Constraints

Organization policies are applied at the folder level and inherited by your
project. Before creating resources, review the key constraints on the
[Guardrails](/docs/gcp/guardrails) page to understand what is allowed and
what will be blocked.

Key constraints to know:
* **No external IP addresses** — VMs cannot have public IPs by default
* **Custom-mode VPCs only** — Auto-mode VPC networks are blocked
* **Allowed regions:** us-central1 and us-west1 (other regions may be blocked)

---

## Step 5 — Networking

GCP Campus Cloud does not currently have a centrally-managed Shared VPC or
campus connectivity (VPN/Interconnect) in place. Org policy blocks you from
creating VPCs yourself — only the Cloud Team's automation account can create
network resources.

If your project requires network connectivity:

* **Internet egress via Cloud NAT** — open a [ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5) and the Cloud
  Team will provision it for your project.
* **Access to UCSB campus resources** — not currently available for GCP.
  Contact the Cloud Team to discuss options.
* **No VPN to campus is available at this time.**

If your workload does not need private networking, you can proceed without a VPC.
Services like Cloud Storage, BigQuery, Pub/Sub, and Cloud Functions work without
one.

---

## Step 6 — Enable Required APIs

GCP services must be enabled via the API before you can use them. Most
common APIs are pre-enabled, but check:

1. Navigate to **APIs & Services → Enabled APIs and Services**.
2. Confirm the APIs you need are enabled.
3. To enable a new API: **+ Enable APIs and Services** → search and enable.

Note: Some APIs require billing to be enabled. Org policies may block specific
APIs — if you get an org policy error, see [Guardrails](/docs/gcp/guardrails).

---

## Step 7 — Verify Required Tags

Your project should already have the required Resource Manager Tags set by the
Cloud Team at provisioning. Verify them by navigating to **IAM & Admin → Tags**.

The owner-settable tags (`environment`, `mission`, `protection-level`,
`availability-level`, `recovery-level`, `dept`) can be updated by you if they
need to change.

See [Labels & Tags](/docs/gcp/tagging) for allowed values and how to update them.

---

## Step 8 — Verify Budget Alert (Funded Projects)

1. Navigate to **Billing → Budgets & alerts**.
2. Confirm a billing budget exists for your project.
3. The budget notifies you at 50%, 90%, and 100% of the budget by default.
4. To change thresholds or recipients, edit the budget.

See [Billing](/docs/gcp/billing) for more information.

---

## Getting Help

| Issue | Where to go |
|---|---|
| Access problems | [Identity & Access](/docs/general/identity) |
| Networking issues | [Networking](/docs/gcp/networking) |
| Org policy violations | [Guardrails](/docs/gcp/guardrails) |
| Billing questions | [Billing](/docs/gcp/billing) |
| Everything else | [ServiceNow](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5) |
