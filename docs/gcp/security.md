---
title: GCP Security
description: Security monitoring, audit logging, Security Command Center, and incident response for GCP projects.
permalink: /docs/gcp/security
last_reviewed: 2026-07-08
---

# GCP Security

Every Campus Cloud GCP project comes with security tools already turned on.
You don't need to set any of this up — it's ready when your project is
created. The main tools are **Cloud Audit Logs** (audit logging) and
**Security Command Center** (security checks and threat detection).

---

## Security Command Center

[Security Command Center](https://cloud.google.com/security-command-center/docs/concepts-security-command-center-overview)
is enabled at the UCSB organization level. It checks all projects for security
issues — publicly exposed storage buckets, VM vulnerabilities, IAM
misconfigurations, unusual API activity, and unsafe network settings.

### Reviewing Findings

Project owners can view Security Command Center findings for their own project —
this access comes automatically with membership in the project's owners group.
(The Owner role on its own does not grant access to findings, so use the owners
group rather than a direct IAM grant.) This access is scoped to your project, so
you automatically see findings for your own project only — there's nothing to
restrict manually.

1. Open **Security → Security Command Center → Findings** in the Google Cloud
   console.
2. Start with Critical and High severity.
3. Click a finding to see which resource is affected and how to fix it.

For a simpler overview, [Cloud Hub](https://console.cloud.google.com/cloud-hub/)
has a **Security & compliance** panel (in preview) that shows findings by
severity alongside your compliance scores. To see how your project scores
against a compliance standard such as NIST, open **Security Command Center →
Compliance Manager**.

Address Critical and High findings promptly. The Cloud Team monitors
organization-wide findings and may follow up if they remain unresolved.

For details, see the
[Security Command Center docs](https://cloud.google.com/security-command-center/docs).

---

## Incident Response

Follow the general
[incident response steps]({{ "/docs/general/security#reporting-a-security-incident" | relative_url }})
for all suspected security events. The section below covers GCP-specific
emergency actions.

### Emergency Isolation

If a GCP resource is actively being exploited:
* Remove the compromised user or service account's access to the project.
* Add a deny-all firewall rule (priority 1) to isolate a compromised VM.
* **Do not delete the VM** — preserve it for forensics.

---

## Project Quarantine

Projects that violate policies or are suspected of compromise may be
quarantined by the Cloud Team. When a project is quarantined:

* Most actions in the project are restricted.
* The Cloud Team will contact the project owner to investigate.
* The project is restored after the issue is resolved.

---

## Cloud Audit Logs

[Cloud Audit Logs](https://cloud.google.com/logging/docs/audit) record every
administrative action in your project — who did what, when, and from where.

| Log Type | What It Records | Retention |
|---|---|---|
| Admin Activity | Changes to resources and settings | 3 years (cannot be deleted or modified) |
| Data Access | Reads and writes to data | 30 days default (configurable) |
| System Events | Automated GCP actions | 30 days default |

**Admin Activity logs are always on** and cannot be disabled. **Data Access
logs are enabled for all services by default** as a Campus Cloud guardrail —
older projects that predate this guardrail may not have it. If you don't see
Data Access entries for a service you expect, check **IAM & Admin → Audit
Logs** in the Google Cloud console and contact the Cloud Team if it looks
disabled.

For details, see the
[Cloud Audit Logs docs](https://cloud.google.com/logging/docs/audit).

---

## Centralized Log Management

In addition to the per-project log retention above, the Cloud Team collects
audit logs from all projects into a central archive:

| Destination | Purpose | Retention |
|---|---|---|
| Cloud Storage | Long-term archive (locked, cannot be deleted early) | 3 years |
| BigQuery | Searchable access for investigation | Retained in dataset |

You don't need to configure this — it's managed by the Cloud Team.

---

## Wiz Cloud Security Posture Management

Wiz is available across all Campus Cloud platforms (AWS, Azure, GCP). See
[Security & Shared Responsibility — Wiz]({{ "/docs/general/security#wiz-cloud-security-posture-management" | relative_url }})
for details.

---

## Identity & Access

**Only @ucsb.edu accounts can access Campus Cloud GCP projects.**

You cannot grant access to personal Gmail addresses or to "all users" —
attempts to do so will fail with a policy error.

Grant access through your project's **per-project access groups** (owners,
editors, viewers, billing) rather than adding people directly under IAM — the
groups also carry billing-data and Shared VPC access. See
[GCP First Steps — Adding and Removing Users]({{ "/docs/gcp/first-steps#step-2--verify-your-access" | relative_url }})
and [Identity & Access]({{ "/docs/general/identity" | relative_url }}).

If an external collaborator needs access, contact the Cloud Team to discuss
options (e.g., a sponsored UCSB account).
