---
title: Security & Shared Responsibility
description: How security responsibilities are divided between the Cloud Team, cloud providers, and you
permalink: /docs/general/security
last_reviewed: 2026-03-30
---

## Security & Shared Responsibility

Cloud security is a shared responsibility. The cloud provider secures the
underlying infrastructure. The Campus Cloud Team secures the landing zone
configuration, policies, and platform tooling. You are responsible for how you
configure and use the resources in your account.

This model applies across all three providers.

---

### What the Cloud Provider Is Responsible For

* Physical data center security, hardware, and networking infrastructure
* Hypervisor and managed service security (the underlying compute, storage, and
  network fabric)
* Software patches and updates for managed services (RDS, Cloud SQL, Azure SQL, etc.)

### What the Campus Cloud Team Is Responsible For

* Landing zone configuration: guardrails, org policies, management group
  structure
* Centralized audit logging and security monitoring
* Campus network connectivity
* Identity federation (UCSB SSO to each provider)
* Platform-level compliance controls (NIST 800-53/800-171 baseline)

### What You Are Responsible For

* Classifying your data and setting appropriate tags (protection level, etc.)
* Configuring your workloads securely (storage bucket permissions, security
  groups, firewall rules)
* Managing access to your account (who has which role)
* Responding to security findings in your account
* Ensuring your use complies with UC Policy IS-3 and applicable laws

---

## Data Classification

All data stored in the Campus Cloud should be classified. Use UCSB's four-level
protection framework:

| Level | Description | Examples |
|---|---|---|
| P1 — Public | No confidentiality requirement | Published research, public websites |
| P2 — Internal | University internal use | Administrative data, internal reports |
| P3 — Sensitive | Personally identifiable or proprietary | PII, FERPA, unpublished research |
| P4 — Regulated | Federally regulated or export-controlled | HIPAA, CUI, ITAR |

Set the appropriate `protection-level` tag on your account and resources. For
P3 and P4 data, contact the Cloud Team before storing data to confirm your
account type is appropriate.

For UC Policy IS-3 details see:
[https://security.ucop.edu/policies/it-policies.html](https://security.ucop.edu/policies/it-policies.html)

---

## Availability and Recovery

Two additional classification dimensions help align your architecture with your
operational needs:

**Availability Level** — how critical is uptime for this workload?

| Level | Meaning |
|---|---|
| A1 | Best-effort, no SLO |
| A2 | Business hours — outages OK overnight and on weekends |
| A3 | Standard — 99.5% uptime target |
| A4 | High availability — 99.9%+ uptime target |

**Recovery Level** — what are your backup and recovery requirements?

| Level | Meaning |
|---|---|
| R1 | Best-effort — rebuild from scratch acceptable |
| R2 | Standard — daily backups, 24-hour RPO |
| R3 | Enhanced — frequent backups, 4-hour RPO |
| R4 | Aggressive — near-zero RPO/RTO, cross-region replication |

Use these levels to guide your architecture decisions and to communicate
requirements to the Cloud Team.

---

## Security Monitoring

Each provider has pre-configured security monitoring in your account:

| Provider | Tool | What It Does |
|---|---|---|
| AWS | Security Hub + GuardDuty | Aggregates findings, detects threats, checks config |
| Azure | Microsoft Defender for Cloud | Security posture, threat detection, policy compliance |
| GCP | Security Command Center | Misconfiguration detection, vulnerability findings |

Review findings regularly. Critical findings may require a response — the Cloud
Team may contact you for unresolved high-severity items.

---

## Reporting a Security Incident

If you suspect a security incident (unauthorized access, data exposure, unusual
account activity):

1. Open a [ServiceNow ticket](https://ucsb.service-now.com/) immediately —
   select Cloud Services under Information Technology Services.
2. Do **not** attempt to clean up or remove evidence before the Cloud Team has
   been notified.
3. Do **not** share account credentials or access to investigate; the Cloud Team
   will request access as needed.

For provider-specific security pages, see:
[AWS Security](../aws/guardrails) ·
[Azure Security](../azure/security) ·
[GCP Security](../gcp/security)
