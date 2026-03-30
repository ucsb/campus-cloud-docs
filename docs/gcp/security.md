---
title: GCP Security
description: Security monitoring, audit logging, Security Command Center, and incident response for GCP projects.
permalink: /docs/gcp/security
last_reviewed: 2026-03-30
---

## GCP Security

Every Campus Cloud GCP project is connected to organization-wide security
tooling. The primary components are **Cloud Audit Logs** and **Security
Command Center (SCC)**.

---

## Cloud Audit Logs

GCP Cloud Audit Logs record all administrative, data-access, and system events.

| Log Type | What It Records | Retention |
|---|---|---|
| Admin Activity | Changes to resource configurations and metadata | WORM — 3 years (cannot be deleted or modified) |
| Data Access | API calls that read or write data (if enabled) | 30 days default (configurable) |
| System Events | Automated GCP actions | 30 days default |

**Admin Activity audit logs cannot be disabled** — GCP enforces this at the
API level for all projects. These logs are your tamper-resistant record of who
changed what and when.

### Enabling Data Access Logs

Data Access logs are not enabled by default because they can generate very high
log volumes. To enable them for a specific service:

1. Navigate to **IAM & Admin → Audit Logs**.
2. Select a service (e.g., Cloud Storage, BigQuery).
3. Check **Data Read**, **Data Write**, and **Admin Read** as appropriate.
4. Save.

For NIST-compliance accounts, Data Access logs are recommended (and may be
required by your compliance team).

---

## Security Command Center (SCC)

SCC is enabled at the UCSB organization level. It aggregates security findings
from all projects into a central dashboard accessible to the Cloud Team.

SCC identifies:
* Publicly exposed storage buckets
* VMs with known vulnerabilities (via Container Analysis / VM Manager)
* IAM policy misconfigurations
* Unusual API activity (via Event Threat Detection)
* Unsafe networking configurations

### Viewing Your Project's Findings

1. Navigate to **Security → Security Command Center → Findings**.
2. Filter by your project ID.
3. Sort by severity (Critical → High → Medium → Low).
4. Click a finding to see the affected resource and remediation steps.

Address Critical and High severity findings promptly. The Cloud Team may
reach out if critical findings are not addressed within a reasonable time.

---

## Wiz Cloud Security Posture Management

UCSB Campus Cloud uses **Wiz** for additional security posture scanning across
all cloud environments (AWS, Azure, GCP). Wiz performs agentless scanning for:

* Vulnerabilities on running VMs and containers
* Identity and access risks
* Network exposure analysis
* Secrets and credentials exposed in code or disk

Wiz scanning is **opt-in** and is not enabled by default for most projects. If
your project handles sensitive data or you would like the additional visibility,
contact the Cloud Team to request it.

---

## Identity Restrictions

**Only @ucsb.edu accounts can access Campus Cloud GCP projects.**

An org policy restricts domain sharing — IAM bindings cannot be granted to
Google accounts outside the `ucsb.edu` domain, `allUsers`, or
`allAuthenticatedUsers`. Attempts to grant access to a personal Gmail address
will fail with an org policy violation error.

If an external collaborator needs access, contact the Cloud Team to discuss
options (sponsored UCSB account, Workload Identity Federation for automated
workloads, etc.).

---

## Incident Response

If you suspect a security incident:

1. **Document immediately:** Note the project ID, resource name, approximate
   time of the suspicious activity, and what you observed.
2. **Do not delete evidence:** Do not delete VMs, revoke service accounts, or
   rotate keys before notifying the Cloud Team.
3. **Open a ServiceNow ticket marked Urgent:** ServiceNow → Cloud Services →
   describe the incident. Include the GCP Project ID.
4. **Contact your department ISO** if regulated data may be involved.

### Emergency Isolation

If a GCP resource is actively being exploited:
* **IAM:** Revoke the compromised service account or user's IAM binding for
  the affected project.
* **Firewall:** Add a deny-all firewall rule at priority 1 to isolate the VM.
* **Do not delete the VM** — preserve it for forensics.

---

## Project Quarantine

Projects that violate org policies or are suspected of compromise may be
quarantined by the Cloud Team. When a project is quarantined:

* Additional org policies are applied that restrict most actions.
* The Cloud Team will contact the project owner to investigate.
* Projects are restored to the normal folder after remediation.
