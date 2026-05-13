---
title: Security
description: Security guidance for Campus Cloud accounts — data classification, monitoring, least-privilege, and incident response
permalink: /docs/general/security/
last_reviewed: 2026-04-06
redirect_from:
  - /docs/general/security
  - /docs/guidelines/security
---

# Security

This page covers security guidance for your Campus Cloud account. For the
foundational model that explains how responsibilities are divided between the
cloud providers, the Campus Cloud Team, and you — across security, cost,
compliance, and data — see
[Shared Responsibility]({{ "/docs/general/shared-responsibility" | relative_url }}).

---

## Least-Privilege Principle

Assign the minimum role needed for each person's responsibilities:

* **AWS** — Use **ReadOnly** or **Billing** roles for stakeholders who only
  need to review costs or resources. Use **PowerUser** for day-to-day work
  and reserve **Administrator** for IAM changes.
* **Azure** — Use **Application Owner** rather than **Subscription Owner** for
  most day-to-day work.
* **GCP** — Use project-level roles (Editor, Viewer) instead of broader roles
  unless explicitly needed.

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
[AWS Security]({{ "/docs/aws/security" | relative_url }}) ·
[Azure Security]({{ "/docs/azure/security" | relative_url }}) ·
[GCP Security]({{ "/docs/gcp/security" | relative_url }})

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

For provider-specific security best practices, see:
* [AWS Security Best Practices](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)
* [Azure Security Best Practices](https://learn.microsoft.com/en-us/azure/security/fundamentals/best-practices-and-patterns)
* [GCP Security Best Practices](https://cloud.google.com/security/best-practices)

### Wiz Cloud Security Posture Management

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

## External Collaborators

All three providers require a `@ucsb.edu` identity. External collaborators
without a UCSB NetID cannot be added directly to your account's role structure.

Options for granting access to external collaborators:

* **Create a sponsored UCSB NetID** for the collaborator through UCSB IT — this
  gives them a `@ucsb.edu` identity that works with all three providers.
* **Share data without granting account access** — for example, use pre-signed
  S3 URLs, scoped SAS tokens (Azure), or signed URLs (GCP).
* **Set up cross-institution federated access** via SAML or OIDC for the
  collaborator's home identity provider (advanced — requires Cloud Team
  involvement).

---

## Data Classification

All data and workloads in the Campus Cloud should be classified along three
dimensions: protection level, availability level, and recovery level. Set all
three values using the required tags described in
[Tagging & Labels]({{ "/docs/general/tagging" | relative_url }}).

### Protection Level

How confidential is the data? Based on the
[UC Data Classification standard](https://security.ucop.edu/policies/institutional-information-and-it-resource-classification.html).


| Level | Description | Examples |
|---|---|---|
| P1 — Public | No confidentiality requirement | Published research, public websites |
| P2 — Internal | University internal use | Administrative data, internal reports |
| P3 — Sensitive | Personally identifiable or proprietary | PII, FERPA, unpublished research |
| P4 — Regulated | Federally regulated or export-controlled | HIPAA, CUI, ITAR |

For P3 and P4 data, contact the Cloud Team before storing data to confirm your account type is appropriate.

### Availability Level

How critical is uptime? Based on the
[UC Data Classification standard](https://security.ucop.edu/policies/institutional-information-and-it-resource-classification.html).

| Level | Description |
|---|---|
| A1 — Minimal | Loss of availability poses minimal impact or financial losses |
| A2 — Low | Loss of availability may cause minor losses or inefficiencies |
| A3 — Moderate | Loss of availability would result in moderate financial losses and/or reduced customer service |
| A4 — High | Loss of availability would result in major impairment to overall operations and/or essential services |

### Recovery Level

How quickly must you recover? Based on the
[UC IS-12 IT Recovery Policy (PDF)](https://security.ucop.edu/files/documents/policies/is-12-it-recovery-policy.pdf).

| Level | Description | Recovery Time |
|---|---|---|
| R1 — Deferrable | Service can be deferred | Up to 30 days |
| R2 — Necessary | Service is necessary for normal operations | Up to 5 days |
| R3 — Critical 2 | Alternatives sustainable up to 24 hours | Up to 24 hours |
| R4 — Critical 1 | Life/safety — alternatives not sustainable | Up to 6 hours |

Use these levels to guide your architecture decisions and to communicate
requirements to the Cloud Team.

