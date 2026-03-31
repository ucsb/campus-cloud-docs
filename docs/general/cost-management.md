---
title: Costs & Billing
description: Cloud pricing, UC discounts, and how to manage your cloud spending
permalink: /docs/general/cost-management
last_reviewed: 2026-03-30
redirect_from:
  - /docs/bestpractices/costmodels
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

## Monitoring Your Costs

* **AWS:** Cost and Usage Reports, AWS Cost Explorer, and QuickSight dashboards
  provided by the Cloud Team — see [QuickSight Dashboards](docs/aws/quicksight).
* **Azure:** Azure Cost Management + Billing in the Azure portal.
  *(Azure cost tool — contact Cloud Team for details.)*
* **GCP:** GCP Billing Account console under **Billing → Reports**.

### Budget Alerts

Set up a budget alert in your account so you are notified before your spending
exceeds expectations. Instructions are in each provider's First Steps guide.

* For AWS, use the **Fixed Monthly Budget with Notification** product in the
  Service Catalog — see [AWS First Steps](docs/aws/first-steps).
* For Azure, use **Azure Cost Management** — see [Azure First Steps](docs/azure/first-steps).
* For GCP, use **Cloud Billing budgets** — see [GCP First Steps](docs/gcp/first-steps).

A budget alert does not automatically stop your account from spending — it sends
a notification. Monitor your account regularly during the first few weeks of a
new workload.

---

## Purchase Orders and Invoicing

Cloud costs are tracked against the Purchase Order you created in Gateway.
Monthly usage is invoiced approximately three weeks after the end of each month.
Keep your PO active until all invoices have been processed — see
[Close an Account](docs/general/close-account) for details on the closure timeline.

If your costs are approaching your PO limit, renew or increase your PO before
it expires. Contact your departmental financial administrator and the Cloud Team.

---

## Pricing, Discounts & Credits

### UC Enterprise Discounts

UCSB participates in system-wide enterprise agreements with all three providers.
You receive these discounts automatically — no action required.

| Provider | Program | Key Discount |
|---|---|---|
| AWS | Enterprise Discount Program (EDP) | Percentage discount across all services; additional discount on S3 storage |
| Azure | Enterprise Agreement (EA) | Negotiated rates across Azure services |
| GCP | Google Negotiated Pricing | Committed use discounts and negotiated rates |

### Pricing Calculators

Before starting a project, estimate your monthly spend using the official calculators:

* [AWS Pricing Calculator](https://calculator.aws/)
* [Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/)
* [GCP Pricing Calculator](https://cloud.google.com/products/calculator)

Note that the calculators show list prices. Your actual bill will reflect UC
enterprise discounts.

### Pricing Models

| Model | Description | Best For |
|---|---|---|
| On-demand / Pay-as-you-go | Billed by the second or hour, no commitment | Variable workloads, development, testing |
| Reserved / Committed use | Pay upfront or commit to 1–3 years for a discount | Steady, predictable production workloads |
| Spot / Preemptible / Interruptible | Deeply discounted but can be terminated with short notice | Batch jobs, fault-tolerant compute |

### Research Credits

All three providers offer programs that award cloud credits or research funds to
academic researchers. If you receive an award, use a Campus Cloud account to
redeem it — either create a new account or migrate an existing personal account.

| Provider | Program | What You Get | Link |
|----------|---------|-------------|------|
| **AWS** | [Amazon Research Awards (ARA)](https://www.amazon.science/research-awards) | Unrestricted funds + AWS Promotional Credits | [Apply / Learn more](https://www.amazon.science/research-awards) |
| **GCP** | [Google Cloud Research Credits](https://edu.google.com/programs/credits/research/) | Up to $5,000 in GCP credits (faculty, PhD students, postdocs) | [Apply](https://edu.google.com/programs/credits/research/) |
| **GCP** | [Google Academic Research Awards (GARA)](https://research.google/programs-and-events/google-academic-research-awards/) | Unrestricted gifts for computing & technology research (professors) | [Learn more](https://research.google/programs-and-events/google-academic-research-awards/) |
| **Azure** | [Microsoft Research Fellowship](https://www.microsoft.com/en-us/research/academic-program/microsoft-research-fellowship/) | Azure compute access for collaborative research (faculty, PhD students, postdocs) | [Learn more](https://www.microsoft.com/en-us/research/academic-program/microsoft-research-fellowship/) |
| **Azure** | [Accelerating Foundation Models Research (AFMR)](https://www.microsoft.com/en-us/research/collaboration/accelerating-foundation-models-research/) | Azure AI services grants for foundation-model research | [Learn more](https://www.microsoft.com/en-us/research/collaboration/accelerating-foundation-models-research/) |

### Teaching & Classroom Credits

Faculty can apply for cloud credits to give students hands-on experience in
coursework. These programs provide credits to the instructor for distribution to
the class — they are not self-service student accounts.

| Provider | Program | What You Get | Link |
|----------|---------|-------------|------|
| **GCP** | [Google Cloud Teaching Credits](https://edu.google.com/programs/credits/teaching/) | Faculty apply per-course; GCP credits for students to use in coursework | [Apply](https://edu.google.com/programs/credits/teaching/) |
| **Azure** | [Azure Education Hub](https://learn.microsoft.com/en-us/azure/education-hub/) | Faculty-managed Azure credits and lab environments for classroom use | [Learn more](https://learn.microsoft.com/en-us/azure/education-hub/) |

AWS does not offer a direct credits-to-faculty program;
[AWS Academy](https://aws.amazon.com/training/awsacademy/) provides free
curriculum with a Learner Lab sandbox but requires institutional membership and
uses pre-built courses.

Programs change frequently — check each provider's site for current eligibility,
deadlines, and award amounts.

---

## Cost Optimization Tips

* **Reserved Instances / Committed Use Discounts:** If you have stable,
  predictable workloads (e.g., a long-running research cluster), committing to
  1–3 years can reduce compute costs significantly.
* **Spot / Preemptible VMs:** For fault-tolerant batch workloads, Spot VMs are
  60–80% cheaper than on-demand.
* **Rightsizing:** Review provider recommendations (AWS Compute Optimizer,
  Azure Advisor, GCP VM Manager) to downsize over-provisioned resources.
* **Storage lifecycle policies:** Move infrequently accessed data to cheaper
  storage tiers (S3 Glacier, Azure Cool/Archive, GCS Nearline/Coldline).
