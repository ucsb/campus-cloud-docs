---
title: Security & Shared Responsibility
description: How security responsibilities are divided between the Cloud Team, cloud providers, and you
permalink: /docs/general/security
last_reviewed: 2026-03-30
---

## Security & Shared Responsibility

Cloud security is a shared responsibility. The cloud provider secures the
underlying infrastructure. The Campus Cloud Team secures the Campus Cloud Landing Zone
configuration, policies, and platform tooling. You are responsible for how you
configure and use the resources in your account.

This model applies across all three providers.

---

### What the Cloud Provider Is Responsible For

* Physical data center security, hardware, and networking infrastructure
* The underlying compute, storage, and network systems that managed services
  run on
* Software patches and updates for managed services (RDS, Cloud SQL, Azure SQL, etc.)

### What the Campus Cloud Team Is Responsible For

* Campus Cloud Landing Zone configuration: guardrails, org policies, management group
  structure
* Centralized audit logging and security monitoring
* Campus network connectivity
* Identity federation (UCSB SSO to each provider)
* Platform-level compliance controls (NIST 800-171 baseline)

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

## Wiz Cloud Security Posture Management

UCSB Campus Cloud uses [Wiz](https://www.wiz.io/) for additional security
posture scanning across all cloud environments (AWS, Azure, GCP). Wiz performs
agentless scanning for:

* Vulnerabilities on running VMs and containers
* Identity and access risks
* Network exposure analysis
* Secrets and credentials exposed in code or disk

Wiz scanning is **opt-in** and is not enabled by default for most accounts. If
your account handles sensitive data or you would like the additional visibility,
contact the Cloud Team to request it.

---

## Reporting a Security Incident

If you suspect a security incident (unauthorized access, data exposure, unusual
account activity):

1. **Document immediately** — Note the account/project/subscription ID, resource
   name, approximate time of the suspicious activity, and what you observed.
2. **Do not delete evidence** — Do not terminate VMs, delete logs, revoke
   service accounts, or rotate secrets before the Cloud Team has been notified.
3. **Open a [ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5) marked Urgent** and describe the incident.
   Include the account or project identifier.
4. **Contact your department's ISO** (Information Security Officer) if regulated
   data may be involved.

Each provider page describes platform-specific emergency isolation steps:
[AWS Security](docs/aws/security) ·
[Azure Security](docs/azure/security) ·
[GCP Security](docs/gcp/security)
