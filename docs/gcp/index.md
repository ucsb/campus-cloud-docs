---
title: GCP Overview
description: Overview of the UCSB Campus Cloud GCP environment — org hierarchy, folders, projects, regions, and what is pre-configured.
permalink: /docs/gcp/
last_reviewed: 2026-03-30
---

## GCP at UCSB

The UCSB Campus Cloud GCP platform is built on a **Google Cloud Organization**
with a structured folder hierarchy managed by the Cloud Team using HCP Terraform
and Workload Identity Federation. Every project is provisioned inside a folder
with organization-level policies and guardrails, giving teams a compliant
starting point without manual security setup.

---

## Key Facts

| Item | Value |
|---|---|
| Sign-in URL | [console.cloud.google.com](https://console.cloud.google.com) |
| Identity Provider | UCSB Google Workspace (via Entra ID) — sign in with `@ucsb.edu` |
| Supported Regions | us-central1 (Iowa), us-west1 (Oregon) |
| New Project Turnaround | ~2 business days after PO is approved |

---

## Organization Hierarchy

GCP resources are organized in a tree: **Organization → Folders → Projects**.
Policies applied at a higher level are inherited by everything underneath.

```
UCSB Organization (ucsb.edu)
├── UCSB Core               (Cloud Team infrastructure — not for PI use)
├── UCSB NIST Baseline      (Regulated research workloads)
├── UCSB Legacy             (Pre-landing-zone projects)
├── UCSB Sandbox Unfunded   (Exploration — no billing attached)
└── UCSB Quarantine-Disabled (Suspended/policy-violating projects)
```

Your project will be placed in the folder that matches your funding and
compliance requirements:

| Folder | Use Case | Billing | Who Provisions |
|---|---|---|---|
| UCSB NIST Baseline | Research, sensitive data, funded workloads | Yes | Cloud Team via Gateway PO |
| UCSB Sandbox Unfunded | Exploration, learning, testing | No | Cloud Team on request |
| UCSB Core | Shared services | n/a | Cloud Team only |

{% include alert.html type="info" title="Sandbox Unfunded — no billing" content="Projects in the Sandbox Unfunded folder cannot have a billing account attached. This means most paid services (Compute Engine, Cloud SQL, GKE) cannot be enabled. Sandbox is for exploring the GCP console, IAM, and free-tier services only." %}

---

## What Is Pre-configured

When your project is provisioned, the Cloud Team will:

* **Apply organization IAM deny policies** — Block high-risk operations
  (e.g., `allUsers` public access, disabling audit logs)
* **Enable Cloud Audit Logs** — Admin Activity logs are WORM protected for 3 years
* **Enable Security Command Center (SCC)** — Central security findings
* **Require required resource labels** — Enforce your team's tags on resources
* **Restrict networking** — Add your project to the Shared VPC or configure
  a standalone VPC with org policy controls
* **Set a billing budget alert** — Notifies you when spend approaches your
  specified threshold (funded projects only)

---

## Regions

All workloads should use **us-central1** or **us-west1**. Org policies allow
other regions in some cases, but networking, compliance tooling, and support
are tested primarily in these two regions.

---

## Next Steps

* [Request a Project](/getting-started)
* [First Steps](/docs/gcp/first-steps)
* [Networking](/docs/gcp/networking)
* [Guardrails & Org Policies](/docs/gcp/guardrails)
* [Labels & Tags](/docs/gcp/tagging)
