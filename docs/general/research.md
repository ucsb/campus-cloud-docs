---
title: Cloud for Research
description: Using the UCSB Campus Cloud for research computing
permalink: /docs/general/research
last_reviewed: 2026-03-30
---

## Cloud for Research

Cloud computing has become a critical tool for researchers across fields — from
running large-scale simulations to storing and processing sensitive research
datasets. The UCSB Campus Cloud provides an environment that meets federal
compliance requirements, scales to research needs, and comes with UC enterprise
pricing.

---

## Why Use the Campus Cloud for Research?

* **Compliance for federal funding.** If your grant requires NIST 800-171
  compliance (common for DoD, NSF, and NIH grants involving CUI), the Campus
  Cloud provides a compliant account tier. See [Compliance](compliance).
* **Significant discounts.** UC enterprise agreements give you lower prices
  than retail cloud rates — automatically.
* **No credit card required.** Billing goes through your UCSB Purchase Order and
  FAU, not a personal credit card.
* **Support options.** AWS Business Support and Azure support plans are
  available to Campus Cloud accounts. Contact the Cloud Team to discuss the
  right support tier for your workload.
* **Cloud Team consulting.** The UCSB Cloud Team has supported research groups
  across campus and offers consulting on architecture, compliance, and cost
  optimization.

---

## Getting Started with Research Computing

1. **Estimate your needs.** What compute, storage, and services will you need?
   Use the provider pricing calculators to estimate costs (see
   [Costs & Billing](cost-management)).
2. **Choose your provider.** Most research groups use AWS. Azure and GCP are
   good choices for teams already using Microsoft or Google tools, or for
   specific services (e.g., Google BigQuery, Azure ML).
3. **Request an account.** Follow the [Getting Started](../../getting-started)
   procurement guide. Indicate on your form if you need NIST 800-171 compliance.
4. **Set up your environment.** Follow the First Steps guide for your provider.

---

## Amazon Research Awards (ARA)

Amazon Research Awards offer unrestricted research funds and AWS Promotional
Credits to academic institutions.

* UCSB researchers awarded ARA credits should use a Campus Cloud account to
  access them — either create a new account or migrate an existing personal
  account.
* [More about ARA](https://www.amazon.science/research-awards)

---

## Personal vs. Campus Cloud Accounts

A personal cloud account uses a personal credit card and is outside the Campus
Cloud Landing Zone. Personal accounts:

* Do not receive UC enterprise discounts
* May not meet compliance requirements for federal grants
* Should not use a `@ucsb.edu` email address (this triggers a restriction —
  see [AWS Account Request](../aws/account-request))
* May be subject to review to ensure UC policies are followed

If you have a personal account you want to bring into the Campus Cloud, contact
the Cloud Team. Migration is a standard process for all three providers.

---

## Cloud Team Consulting

The Cloud Team offers consulting support for research projects. This includes:

* Architecture design for cloud-native or hybrid workloads
* Cost optimization reviews
* Compliance guidance (NIST 800-171, HIPAA, FERPA)
* Support for migrating on-premises HPC to the cloud

Contact: [info@cloud.ucsb.edu](mailto:info@cloud.ucsb.edu) or open a
[ServiceNow ticket](https://ucsb.service-now.com/).

---

## Data Management Plans (DMPs)

If your grant requires a Data Management Plan, see [Data Management Plans](data-management).

---

## FAQ

**Can I use the Campus Cloud for a class or student project?**
Yes, with faculty sponsorship and a Purchase Order. Student projects under
faculty supervision qualify. For short-term or no-budget use, GCP's Sandbox
Unfunded folder allows project creation without billing — contact the Cloud Team.

**How do I get GPU access?**
Request a standard account and provision GPU-enabled instance types (e.g., AWS
p3/p4, Azure NC/ND series, GCP A2). Check availability in the allowed regions
for each provider.

**Can I share data with external collaborators?**
Yes, with appropriate access controls. For P3/P4 data involving CUI or regulated
data, consult the Cloud Team before sharing externally. GCP and Azure by default
only allow `@ucsb.edu` accounts — external collaborators may need a UCSB
affiliate account or guest access.
