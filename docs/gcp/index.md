---
title: GCP Overview
description: Overview of the UCSB Campus Cloud GCP environment — org hierarchy, folders, projects, regions, and what is pre-configured.
permalink: /docs/gcp/
last_reviewed: 2026-03-30
---

## GCP at UCSB

The UCSB Campus Cloud GCP platform is organized as a **Google Cloud
Organization** with a structured folder hierarchy managed by the Cloud Team.
Every project is provisioned inside a folder with organization-level policies
and guardrails, giving your team a compliant starting point without manual
security setup.

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
Policies applied at a higher level are inherited by every project underneath.

| Folder | Purpose |
|---|---|
| UCSB NIST Baseline | Production workloads — funded research, academic, and administrative projects with full org-policy enforcement |
| Sandbox Unfunded | Self-service exploration — any `@ucsb.edu` user can create a project here, but billing cannot be attached |
| UCSB Legacy | Pre-existing projects that predate the landing zone |

{% include alert.html type="info" title="Sandbox Unfunded — self-service, no billing" content="Any @ucsb.edu user can create a project in the Sandbox Unfunded folder — including projects created automatically by tools like Apps Script. Billing cannot be attached, so most paid services (Compute Engine, Cloud SQL, GKE) are unavailable. Use this folder for exploring the GCP console, IAM, and free-tier services." %}

---

## What Is Pre-configured

When your project is provisioned, the Cloud Team will:

* **Block high-risk operations** — Policies prevent actions like granting
  public access or disabling audit logs
* **Enable Cloud Audit Logs** — Admin Activity logs are stored securely for 3 years
* **Enable Security Command Center** — Central dashboard for security findings
* **Require resource labels** — Enforce your team's tags on resources
* **Restrict networking** — Only the Cloud Team can create VPC networks; request
  networking resources if your project needs them
* **Set a billing budget alert** — Notifies you when spend approaches your
  specified threshold (funded projects only)

---

## Regions

All workloads should use **us-central1** or **us-west1**. Org policies allow
other regions in some cases, but networking, compliance tooling, and support
are tested primarily in these two regions.

---

## Next Steps

* [Request a Project]({{ "/getting-started/procurement" | relative_url }})
* [First Steps]({{ "/docs/gcp/first-steps" | relative_url }})
* [Networking]({{ "/docs/gcp/networking" | relative_url }})
* [Guardrails & Org Policies]({{ "/docs/gcp/guardrails" | relative_url }})
* [Security]({{ "/docs/gcp/security" | relative_url }})

