---
title: Costs & Billing
description: Cloud pricing, UC discounts, and how to manage your cloud spending
permalink: /docs/general/cost-management
last_reviewed: 2026-03-30
---

## Costs & Billing

Cloud resources are billed on a pay-as-you-go model — you pay for what you use,
typically by the hour or second. This section explains how billing works in the
Campus Cloud, the discounts available to UCSB, and how to keep costs under control.

---

## Baseline Costs

{% include alert.html type="warning" title="Budget for baseline costs" content="Every Campus Cloud account incurs baseline charges even when you are not running workloads. Audit logging, security monitoring, and compliance tools run continuously. For most accounts this is a small amount per month, but factor it into your budget from the start." %}

These baseline services include:
* Audit log storage
* Security Hub / Defender for Cloud / Security Command Center
* GuardDuty (AWS)
* CloudTrail (AWS)

---

## UC Enterprise Discounts

UCSB participates in system-wide enterprise agreements with all three providers.
You receive these discounts automatically — no action required.

| Provider | Program | Key Discount |
|---|---|---|
| AWS | Enterprise Discount Program (EDP) | Percentage discount across all services; additional discount on S3 storage |
| Azure | Enterprise Agreement (EA) | Negotiated rates across Azure services |
| GCP | Google Negotiated Pricing | Committed use discounts and negotiated rates |

---

## Pricing Calculators

Before starting a project, estimate your monthly spend using the official calculators:

* [AWS Pricing Calculator](https://calculator.aws/)
* [Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/)
* [GCP Pricing Calculator](https://cloud.google.com/products/calculator)

Note that the calculators show list prices. Your actual bill will reflect UC
enterprise discounts.

---

## Pricing Models

| Model | Description | Best For |
|---|---|---|
| On-demand / Pay-as-you-go | Billed by the second or hour, no commitment | Variable workloads, development, testing |
| Reserved / Committed use | Pay upfront or commit to 1–3 years for a discount | Steady, predictable production workloads |
| Spot / Preemptible / Interruptible | Deeply discounted but can be terminated with short notice | Batch jobs, fault-tolerant compute |

---

## Budget Alerts

Set up a budget alert in your account so you are notified before your spending
exceeds expectations. Instructions are in each provider's First Steps guide.

* For AWS, use the **Fixed Monthly Budget with Notification** product in the
  Service Catalog — see [AWS First Steps](../aws/first-steps).
* For Azure, use **Azure Cost Management** — see [Azure First Steps](../azure/first-steps).
* For GCP, use **Cloud Billing budgets** — see [GCP First Steps](../gcp/first-steps).

A budget alert does not automatically stop your account from spending — it sends
a notification. Monitor your account regularly during the first few weeks of a
new workload.

---

## Viewing Your Costs

* **AWS:** Cost and Usage Reports, AWS Cost Explorer, and QuickSight dashboards
  provided by the Cloud Team — see [QuickSight Dashboards](../aws/quicksight).
* **Azure:** Azure Cost Management + Billing in the Azure portal.
  *(Azure cost tool — contact Cloud Team for details.)*
* **GCP:** GCP Billing Account console under **Billing → Reports**.

---

## Purchase Orders and Invoicing

Cloud costs are tracked against the Purchase Order you created in Gateway.
Monthly usage is invoiced approximately three weeks after the end of each month.
Keep your PO active until all invoices have been processed — see
[Close an Account](close-account) for details on the closure timeline.

If your costs are approaching your PO limit, renew or increase your PO before
it expires. Contact your departmental financial administrator and the Cloud Team.
