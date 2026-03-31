---
title: Tagging & Labels
description: Required tags across AWS, Azure, and GCP
permalink: /docs/general/tagging
last_reviewed: 2026-03-30
---

## Tagging & Labels

Tags are key-value pairs you attach to cloud resources.
The Campus Cloud uses them for billing attribution, compliance monitoring, and
operational automation.

Some tags are required — the Cloud Team enforces them. Others are set by you.

---

## Why Tags Matter

* **Billing:** Tags appear in cost reports so you can break down charges by
  project, department, or environment.
* **Compliance:** Tags like `protection-level` drive security policy scoping
  and audit requirements.

---

## Required Tags — All Providers

The following tags are required across all three providers. AWS and Azure use a
`ucsb:` namespace prefix. GCP does not (tags are already scoped to the UCSB
organization).

| What It Tracks | AWS Tag | Azure Tag | GCP Tag | Set By |
|---|---|---|---|---|
| Purchase Order number | `ucsb:po-number` | `ucsb:po-number` | — | Cloud Team |
| Environment type | `ucsb:environment` | `ucsb:environment` | `environment` | You |
| Mission area | `ucsb:mission` | `ucsb:mission` | `mission` | You |
| Data sensitivity | `ucsb:protection-level` | `ucsb:protection-level` | `protection-level` | You |
| Uptime requirement | `ucsb:availability-level` | `ucsb:availability-level` | `availability-level` | You |
| Backup requirement | `ucsb:recovery-level` | — | `recovery-level` | You |
| Department | `ucsb:dept` | — | `dept` | You |

---

## Allowed Values

### `environment`
`dev`, `test`, `prod`, `other`

### `mission`
`academic`, `research`, `administrative`, `mixed`

### `protection-level`
| Value | Meaning |
|---|---|
| `p1` | Public — no confidentiality requirement |
| `p2` | Internal — university internal data |
| `p3` | Sensitive — PII, FERPA, proprietary research |
| `p4` | Regulated — HIPAA, CUI, ITAR, export-controlled |

### `availability-level`
`a1` (best-effort) through `a4` (99.9%+ uptime)

### `recovery-level`
`r1` (rebuild acceptable) through `r4` (near-zero RPO/RTO)

### `dept`
4-character UCSB Chart of Accounts department code (e.g., `COMS`, `PHYS`, `MCDB`).

---

## What Happens If You Don't Tag

| Provider | Consequence |
|---|---|
| AWS | Compliance alert in Security Hub; resource may show as non-compliant |
| Azure | Resource group flagged as non-compliant (Audit policy) |
| GCP | Audit finding; platform automation skips untagged projects |

For Azure, the five required tags on **resource groups** are audited by policy:
`ucsb:po-number`, `ucsb:environment`, `ucsb:mission`,
`ucsb:protection-level`, and `ucsb:availability-level`. Resource groups
without these tags will be flagged as non-compliant but can still be created.

---

## Tag Namespace

AWS and Azure tags use the `ucsb:` namespace to avoid collisions with provider
reserved namespaces (`aws:`, `Microsoft:`).

Example: `ucsb:environment = prod`

GCP Resource Manager Tags are already scoped to the UCSB organization, so no
namespace prefix is needed.

---

## How to Update Your Tags

Each provider has a different interface for managing tags:

* **AWS:** [AWS resource tagging docs](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) — use Tag Editor in the AWS Console or the CLI.
* **Azure:** [Azure resource tagging docs](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources) — set tags on Resource Groups and resources in the portal or CLI.
* **GCP:** [GCP Resource Manager Tags docs](https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing) — tags are set at the **project level** (not on individual resources). Update them under **IAM & Admin → Tags** in the console or via `gcloud resource-manager tags bindings`. For project labels, see [Creating and managing labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels).

---

## GCP: Tags vs. Labels

GCP has two separate metadata systems. The Campus Cloud uses both:

* **Resource Manager Tags** — the required tags listed above. Set at the
  project level, used for governance, compliance, and automation.
* **Project Labels** — flat key-value pairs on the project that appear in
  billing exports. Set by the project owner for cost attribution. Labels do
  not drive policies or automation — they supplement tags for billing
  visibility.
