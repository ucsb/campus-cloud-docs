---
title: Azure First Steps
description: What to do after your Azure subscription is provisioned — sign in, verify setup, deploy your first resource.
permalink: /docs/azure/first-steps
last_reviewed: 2026-03-30
redirect_from:
  - /docs/firststeps/azurefirststeps
---

## Getting Started With Your Azure Subscription

Your subscription is ready when you receive the provisioning confirmation from
the Cloud Team. Follow the steps below to get set up.

---

## Step 1 — Sign In

1. Go to [portal.azure.com](https://portal.azure.com).
2. Sign in with your UCSB email address (`yournetid@ucsb.edu`).
   * If prompted, choose **Work or school account**.
   * Authenticate with Duo MFA if required.
3. In the top-right dropdown, verify you are in the **UC Santa Barbara** directory.
   * If you see a personal directory instead, click your name → **Switch directory**
     → select **UC Santa Barbara**.

{% include alert.html type="info" title="Always use the UCSB directory" content="Azure has both a UCSB tenant (ucsb.edu) and a personal Microsoft account option. Always confirm you are in the UC Santa Barbara directory before working to avoid creating resources in the wrong place." %}

---

## Step 2 — Find Your Subscription

1. In the portal search bar, type **Subscriptions**.
2. Locate your subscription in the list.
3. Click it to view the subscription overview — note your **Subscription ID** for
   future support tickets.

If your subscription does not appear, verify that:
* You are in the UC Santa Barbara directory (step 1).
* Your role assignment is complete (ask the Cloud Team if unsure).

---

## Step 3 — Verify Defender for Cloud

Microsoft Defender for Cloud is enabled on all Campus Cloud subscriptions.
Confirm it is active:

1. Search for **Microsoft Defender for Cloud** in the portal.
2. Under **Environment settings**, click your subscription.
3. Verify Defender plans are showing as **On** for the resource types you use
   (VMs, Storage, SQL, Key Vault, etc.).

If Defender plans are showing as Off, contact the Cloud Team.

---

## Step 4 — Set Subscription Contacts

Configure notification contacts so your team receives security, billing, and
health alerts. See [Account Contacts]({{ "/docs/general/contacts" | relative_url }}) for general best
practices.

The primary billing contact is managed by the Cloud Team. **You configure:**

**Security alerts (Defender for Cloud):**
1. Navigate to **Microsoft Defender for Cloud → Environment settings**.
2. Click your subscription → **Email notifications**.
3. Set the email to your team's functional security address.
4. Alert severity: High as a minimum (All recommended).
5. Save.

**Budget alerts:** Add your team's billing email when you create a budget
(see Step 8 below).

**Service Health alerts:**
1. Navigate to **Service Health → Health alerts → + Create service health alert**.
2. Scope to your subscription; choose the services and regions you use.
3. Create an Action Group with an Email action pointing to your team's address.
4. Save.

---

## Step 5 — Review Your Roles

Four custom RBAC roles are assigned to your team. Use the principle of
least privilege — most day-to-day work should use **Application Owner**,
not **UCSB Subscription Owner**.

See [Roles & Access]({{ "/docs/azure/roles" | relative_url }}) for details on each role and
instructions for adding team members.

---

## Step 6 — Create a Resource Group

All resources must be in a Resource Group. Azure Policy audits Resource Groups
for the five required tags — groups missing tags will be flagged as
non-compliant.

1. Navigate to **Resource Groups → + Create**.
2. Select your subscription and a region (West US 2 recommended).
3. Fill in all five required tags:
   * `ucsb:po-number`
   * `ucsb:environment`
   * `ucsb:mission`
   * `ucsb:protection-level`
   * `ucsb:availability-level`
4. Click **Review + Create**.

See [Tagging]({{ "/docs/general/tagging" | relative_url }}) for allowed values.

---

## Step 7 — Configure Networking (Optional)

If your request included hub-spoke Virtual WAN peering for campus connectivity:

1. Navigate to **Virtual Networks** in your subscription to confirm the VNet exists.
2. Check **Peerings** — it should show a peering to the Campus Cloud hub VNet.
3. If the VNet or peering is missing, open a [ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5).

---

## Step 8 — Set a Budget Alert

Create a cost budget to alert you if spend approaches your expected amount:

1. Navigate to **Cost Management → Budgets → + Add**.
2. Set the budget amount, scope (subscription), and reset period (Monthly).
3. Configure alert thresholds (e.g., 80% actual, 100% forecasted).
4. Set the alert email to your team's functional email address.

---

## Getting Help

| Issue | Where to go |
|---|---|
| Access problems (can't sign in, wrong directory) | [Identity & Access]({{ "/docs/general/identity" | relative_url }}) |
| Tag policy blocking resource group creation | [Tagging]({{ "/docs/general/tagging" | relative_url }}) |
| Missing VNet, networking issues | [Networking]({{ "/docs/azure/networking" | relative_url }}) |
| Policy violations | [Guardrails]({{ "/docs/azure/guardrails" | relative_url }}) |
| Billing questions | [Cost Management]({{ "/docs/general/cost-management" | relative_url }}) |
| Everything else | [ServiceNow](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5) |
