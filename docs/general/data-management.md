---
title: Data Management Plans
description: DMP guidelines for researchers using the Campus Cloud
permalink: /docs/general/data-management
last_reviewed: 2026-03-30
redirect_from:
  - /docs/guidelines/dmp
---

## Data Management Plans

Most federal granting agencies require a Data Management Plan (DMP) that describes
how your research data will be collected, stored, protected, and shared. This
page provides a general Cloud statement and resources for building your DMP.

---

## Campus Cloud Statement for DMPs

You may use the following language to describe the UCSB Campus Cloud environment
in your DMP:

> "Research data will be stored and processed in the UCSB Campus Cloud Landing
> Zone, a managed cloud environment operated by UCSB IT (ITS-CCID) on Amazon
> Web Services / Microsoft Azure / Google Cloud Platform. The Landing Zone
> provides NIST 800-171-aligned security controls, UC Policy IS-3-compliant
> guardrails, centralized audit logging, data-at-rest and in-transit encryption,
> and campus network connectivity. The University of California has negotiated
> enterprise agreements with these providers, ensuring data governance under UC
> Terms & Conditions."

Customize this statement for your specific provider(s) and add any project-specific
controls (e.g., HIPAA Business Associate Agreement, CUI handling procedures).

---

## Shared Responsibility for Research Data

The Campus Cloud adheres to a Shared Responsibility Model:

* **The Campus Cloud Team provides:** security controls, audit infrastructure,
  compliance guardrails, and platform monitoring.
* **You are responsible for:** classifying your data, configuring your
  workloads appropriately, managing access, and ensuring your processes follow
  applicable regulations.

---

## Key Compliance Frameworks

| Framework | Who It Applies To | Next Step |
|---|---|---|
| UC Policy IS-3 | All Campus Cloud accounts | Classify your data; apply appropriate tags |
| NIST 800-171 | Research involving CUI (DoD, NSF, NIH grants) | Request a NIST-compliant account — see [Compliance]({{ "/docs/general/compliance" | relative_url }}) |
| HIPAA | Research involving protected health information | Contact the Cloud Team; a BAA may be required |
| FERPA | Work involving student education records | Classify as P3 minimum; limit access |

---

## DMP Resources

* [DMPTool](https://dmptool.org/) — build your DMP with funder-specific templates
* [DMPTool public templates](https://dmptool.org/public_templates) — browse
  templates from NSF, NIH, DoD, and other agencies
* [UC Santa Barbara Library — Data Services](https://www.library.ucsb.edu/research-data-services)
* [University of Arizona — Data Management Best Practices](https://data.library.arizona.edu/data-management/best-practices/data-sharing-archiving)

---

## Archiving and Long-Term Retention

Cloud object storage (AWS S3, Azure Blob Storage, GCP Cloud Storage) is not a
long-term archive by default. Plan for data archiving at the conclusion of your
project:

* Move data to lower-cost storage tiers (S3 Glacier, Azure Archive, GCP
  Nearline/Coldline) for infrequently accessed long-term storage.
* For public datasets required by funders, coordinate with the UCSB Library on
  deposition to an appropriate repository.
* Delete data you no longer need — storage costs continue until data is removed.

For help designing a data lifecycle strategy for your research, contact the
[Cloud Team](mailto:info@cloud.ucsb.edu).
