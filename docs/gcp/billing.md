---
title: GCP Billing
description: How billing is set up in Campus Cloud GCP, how to monitor costs, and how to manage billing budgets.
permalink: /docs/gcp/billing
last_reviewed: 2026-03-30
---

## GCP Billing in Campus Cloud

GCP billing in Campus Cloud is managed through **GCP Billing Accounts** at the
organization level. Each funded project is linked to a **billing sub-account**
that rolls up charges to the UCSB master billing account. Multiple projects may
share the same sub-account (sub-accounts are organized per department or cost
center, not per project). You do not manage the billing account directly —
costs are invoiced to you through the same Gateway/PO process used for account
provisioning.

{% include alert.html type="info" title="Sandbox Unfunded has no billing" content="Projects in the Sandbox Unfunded folder cannot have a billing account attached. Most paid services (Compute Engine, Cloud SQL, GKE) are not available in Sandbox. Sandbox is for exploring free-tier services and GCP configuration only." %}

---

## Key Facts

| Item | Value |
|---|---|
| Billing account type | GCP Billing Sub-Account (per project) |
| Invoice cycle | Monthly, invoiced through UCSB Gateway |
| Cost visibility | GCP Billing Console (project-level and org-level view) |
| UC negotiated discount | Applied automatically; confirmed in your billing data |
| Budget alerts | Set by Cloud Team during provisioning; configurable by owner |

---

## Viewing Your Costs

### GCP Cloud Billing Console

1. Navigate to **Billing** in the GCP Console (left sidebar, or search "Billing").
2. Select your project's billing account (or the organization-level view if
   you have access).
3. Use **Reports** to view spend by service, SKU, or label.
4. Use **Cost Table** for a tabular breakdown.
5. Use **Budget & alerts** to view the current budget for your project.

For historical cost analysis, use **BigQuery Export** (ask the Cloud Team if
you need access to the org-level BQ export).

---

## Budget Alerts

A billing budget is configured for each funded project during provisioning.
The budget sends email alerts at defined spend thresholds.

### Default Alert Thresholds

| Threshold | Alert Type |
|---|---|
| 50% of budget | Forecasted spend |
| 90% of budget | Actual spend |
| 100% of budget | Actual spend |

### Viewing or Updating Your Budget

1. Navigate to **Billing → Budgets & alerts**.
2. Select the budget for your project.
3. Click **Edit** to change the alert thresholds or notification recipients.
4. Add your team's functional email to the **Manage notifications** section.

---

## Billing Limit Tag

The `ucsb:billing-limit` platform tag on your project reflects the maximum
spend limit set by the Cloud Team during provisioning. This is informational —
it does not automatically stop billing at that threshold. You are responsible
for monitoring costs and staying within your budget.

If you expect your project to exceed the initial budget, contact the Cloud Team
to discuss options before costs accumulate.

---

## Cost Attribution with Labels

GCP billing data is exportable to BigQuery, and labels flow through to billing
data. Apply the required labels to your resources to enable cost attribution
by mission, environment, department, and protection level.

Resources without labels will show as unattributed in cost reports, making it
difficult to identify what generated specific charges.

---

## Cost Optimization Tips

* **Committed Use Discounts (CUDs):** If you have stable, predictable VM usage
  (e.g., a long-running research workload), CUDs can reduce compute costs by
  up to 57%. Contact the Cloud Team to discuss.
* **Preemptible / Spot VMs:** For fault-tolerant batch workloads, Spot VMs are
  60–80% cheaper than on-demand.
* **Rightsizing:** Use VM Manager recommendations to right-size VMs that are
  over-provisioned.
* **Storage lifecycle policies:** For GCS, configure Object Lifecycle Management
  to move infrequently accessed data to Nearline or Coldline storage classes.

---

## Invoicing

After month-end, the Cloud Team reconciles GCP billing sub-accounts and invoices
each project owner through UCSB Gateway. Keep your PO funded with sufficient
balance to avoid delays. Do not close your PO until the final invoice for the
month is submitted (see [Close an Account](/docs/general/close-account)).
