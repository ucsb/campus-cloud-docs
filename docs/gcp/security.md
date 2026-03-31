---
title: GCP Security
description: Security monitoring, audit logging, Security Command Center, and incident response for GCP projects.
permalink: /docs/gcp/security
last_reviewed: 2026-03-30
---

## GCP Security

Every Campus Cloud GCP project comes with security tools already turned on.
You don't need to set any of this up — it's ready when your project is
created. The main tools are **Cloud Audit Logs** (audit logging) and
**Security Command Center** (security checks and threat detection).

---

## Cloud Audit Logs

[Cloud Audit Logs](https://cloud.google.com/logging/docs/audit) record every
administrative action in your project — who did what, when, and from where.

| Log Type | What It Records | Retention |
|---|---|---|
| Admin Activity | Changes to resources and settings | 3 years (cannot be deleted or modified) |
| Data Access | Reads and writes to data (if enabled) | 30 days default (configurable) |
| System Events | Automated GCP actions | 30 days default |

**Admin Activity logs are always on** and cannot be disabled.

### Enabling Data Access Logs

Data Access logs are off by default because they can generate high volume.
To enable them for a specific service:

1. Go to **IAM & Admin → Audit Logs** in the Google Cloud console.
2. Select a service (e.g., Cloud Storage, BigQuery).
3. Check **Data Read**, **Data Write**, and/or **Admin Read**.
4. Save.

For accounts handling sensitive data, Data Access logs are recommended.

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

## Security Command Center

[Security Command Center](https://cloud.google.com/security-command-center/docs/concepts-security-command-center-overview)
is enabled at the UCSB organization level. It checks all projects for security
issues — publicly exposed storage buckets, VM vulnerabilities, IAM
misconfigurations, unusual API activity, and unsafe network settings.

### Reviewing Findings

1. Open **Security → Security Command Center → Findings** in the Google Cloud
   console.
2. Filter by your project ID.
3. Start with Critical and High severity.
4. Click a finding to see which resource is affected and how to fix it.

Address Critical and High findings promptly. The Cloud Team may follow up if
they remain unresolved.

For details, see the
[Security Command Center docs](https://cloud.google.com/security-command-center/docs).

---

## Wiz Cloud Security Posture Management

Wiz is available across all Campus Cloud platforms (AWS, Azure, GCP). See
[Security & Shared Responsibility — Wiz](/docs/general/security#wiz-cloud-security-posture-management)
for details.

---

## Identity Restrictions

**Only @ucsb.edu accounts can access Campus Cloud GCP projects.**

You cannot grant access to personal Gmail addresses or to "all users" —
attempts to do so will fail with a policy error.

If an external collaborator needs access, contact the Cloud Team to discuss
options (e.g., a sponsored UCSB account).

---

## Incident Response

Follow the general
[incident response steps](/docs/general/security#reporting-a-security-incident)
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
