---
title: Tagging & Labels
description: Required tags across AWS, Azure, and GCP
permalink: /docs/general/tagging
last_reviewed: 2026-03-30
redirect_from:
  - /docs/bestpractices/tagging
  - /docs/guidelines/tagging
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

| What It Tracks | AWS Tag | Azure Tag | GCP Tag |
|---|---|---|---|
| Environment type | `ucsb:environment` | `ucsb:environment` | `environment` |
| Mission area | `ucsb:mission` | `ucsb:mission` | `mission` |
| Data sensitivity | `ucsb:protection-level` | `ucsb:protection-level` | `protection-level` |
| Uptime requirement | `ucsb:availability-level` | `ucsb:availability-level` | `availability-level` |
| Backup requirement | `ucsb:recovery-level` | — | `recovery-level` |
| Department | `ucsb:dept` | — | `dept` |

---

## Allowed Values

| Tag | Allowed Values |
|---|---|
| `environment` | `dev`, `test`, `prod`, `other` |
| `mission` | `academic`, `research`, `administrative`, `mixed` |
| `protection-level` | `p1` (public), `p2` (internal), `p3` (sensitive — PII, FERPA), `p4` (regulated — HIPAA, CUI, ITAR). See [UC Data Classification](https://security.ucop.edu/policies/institutional-information-and-it-resource-classification.html). |
| `availability-level` | `a1` (minimal impact if unavailable) through `a4` (must stay up — essential service). See [UC Data Classification](https://security.ucop.edu/policies/institutional-information-and-it-resource-classification.html). |
| `recovery-level` | `r1` (deferrable — up to 30 days to recover) through `r4` (critical — recover within hours). See [UC IS-12 IT Recovery Policy (PDF)](https://security.ucop.edu/files/documents/policies/is-12-it-recovery-policy.pdf). |
| `dept` | 4-character UCSB department code (e.g., `COMS`, `PHYS`, `MCDB`) |

---

## What Happens If You Don't Tag

| Provider | Consequence |
|---|---|
| AWS | Compliance alert in Security Hub; resource may show as non-compliant |
| Azure | Resource group flagged as non-compliant (Audit policy) |
| GCP | Audit finding; platform automation skips untagged projects |

For Azure, the required tags on **resource groups** are audited by policy:
`ucsb:environment`, `ucsb:mission`,
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
