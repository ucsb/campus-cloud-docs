---
title: Cloud for Research
description: Using the UCSB Campus Cloud for research computing
permalink: /docs/general/research
last_reviewed: 2026-10-21
redirect_from:
  - /docs/bestpractices/research
---

# Cloud for Research

Cloud computing has become a critical tool for researchers across fields — from
running large-scale simulations to storing and processing sensitive research
datasets. The UCSB Campus Cloud provides an environment that meets federal
compliance requirements, scales to research needs, and comes with UC enterprise
pricing.

---

## Why Use the Campus Cloud for Research?

* **Compliance for federal funding.** If your grant requires NIST 800-171
  compliance (common for DoD, NSF, and NIH grants involving CUI), every new
  Campus Cloud account is set up to align with it — see
  [Compliance & Governance]({{ "/docs/general/compliance" | relative_url }}) for details.
* **Significant discounts.** UC enterprise agreements give you lower prices
  than retail cloud rates — automatically.
* **No credit card required.** Billing goes through your UCSB Purchase Order and
  [Common Chart of Accounts (CCOA)]({{ "/glossary/" | relative_url }}) account string, not a personal credit card.
* **Support options.** AWS Enterprise Support and Azure support plans are
  available to Campus Cloud accounts. Contact the Cloud Team to discuss the
  right support tier for your workload.
* **Cloud Team consulting.** The UCSB Cloud Team has supported research groups
  across campus and offers consulting on architecture, compliance, and cost
  optimization.

---

## Getting Started with Research Computing

1. **Estimate your needs.** What compute, storage, and services will you need?
   Use the provider pricing calculators to estimate costs (see
   [Costs & Billing]({{ "/docs/general/cost-management" | relative_url }})).
2. **Choose your provider.** Most research groups use AWS. Azure and GCP are
   good choices for teams already using Microsoft or Google tools, or for
   specific services (e.g., Google BigQuery, Azure ML).
3. **Request an account.** Follow the [procurement guide]({{ "/getting-started" | relative_url }}).
4. **Set up your environment.** Follow the First Steps guide for your provider.

---

## Cloud Provider Research Credits

All three providers offer programs that award cloud credits or research funds to
academic researchers. See
[Pricing, Discounts & Credits]({{ "/docs/general/cost-management#research-credits" | relative_url }}) for
the full list. If you receive an award, use a Campus Cloud account to redeem
it — either create a new account or migrate an existing personal account.

---

## Personal vs. Campus Cloud Accounts

If you run research in a personal cloud account (one paid with a personal
credit card), see [Migrate to Campus Cloud]({{ "/docs/general/migrate" | relative_url }})
for why and how to bring it into the Campus Cloud.

---

## Cloud Team Consulting

The Cloud Team offers consulting support for research projects. This includes:

* Architecture design for cloud-native or hybrid workloads
* Cost optimization reviews
* Compliance guidance (NIST 800-171, HIPAA, FERPA)
* Support for migrating on-premises HPC to the cloud

Email [info@cloud.ucsb.edu](mailto:info@cloud.ucsb.edu) to start a conversation, or open a
[ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5) if you have a specific request.

---

## Data Management Plans (DMPs)

If your grant requires a Data Management Plan, see [Data Management Plans]({{ "/docs/general/data-management" | relative_url }}).

---

## FAQ

**Can I use the Campus Cloud for a class or student project?**
Yes, with faculty sponsorship and a Purchase Order. Student projects under
faculty supervision qualify. For short-term or no-budget use, GCP's
[Sandbox Unfunded]({{ "/docs/gcp/#organization-hierarchy" | relative_url }}) folder allows
project creation without billing.

**How do I get GPU access?**
Request a standard account and provision GPU-enabled instance types (e.g., AWS
p3/p4, Azure NC/ND series, GCP A2). Check availability in the allowed regions
for each provider.

**Can I share data with external collaborators?**
Yes, with appropriate access controls. For P3/P4 data involving CUI or regulated
data, consult the Cloud Team before sharing externally. All three providers
require a `@ucsb.edu` identity for account access, so external collaborators
may need a sponsored UCSB account — see
[Security — External Collaborators]({{ "/docs/general/security#external-collaborators" | relative_url }}).
