---
title: Azure Security
description: Security monitoring, Defender for Cloud, and log management in Campus Cloud Azure subscriptions.
permalink: /docs/azure/security
last_reviewed: 2026-03-30
---

## Azure Security

Every Campus Cloud Azure subscription comes with security tools already turned
on. You don't need to set any of this up — it's ready when your subscription is
provisioned. The main tools are **Azure Activity Log** (audit logging),
**Defender for Cloud** (security checks and threat detection),
**Azure Policy** (compliance rules), and a centralized
**Log Analytics workspace** (log storage).

---

## Microsoft Defender for Cloud

[Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction)
is enabled on all Campus Cloud subscriptions. It checks your resources against
security best practices, detects threats on VMs, databases, storage, and
containers, and tracks compliance against NIST 800-171.

### Reviewing Findings

1. Open **Microsoft Defender for Cloud → Recommendations** in the Azure portal.
2. Start with High severity items.
3. Click a recommendation to see which resources are affected and how to fix
   them.

Address High severity recommendations promptly. The Cloud Team may follow up
if they remain unresolved.

For details, see the
[Microsoft Defender for Cloud docs](https://learn.microsoft.com/en-us/azure/defender-for-cloud/).

---

## Incident Response

Follow the general
[incident response steps]({{ "/docs/general/security#reporting-a-security-incident" | relative_url }})
for all suspected security events. The section below covers Azure-specific
emergency actions.

### Emergency Isolation

If a VM is actively compromised and you need to stop the attack:

* Apply a **Network Security Group rule** that blocks all inbound/outbound
  traffic to the VM (deny all, priority 100) while preserving the VM for forensics.
* Do **not** delete or deallocate the VM — forensic images may be needed.

---

## Azure Activity Log

[Azure Activity Log](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/activity-log)
records every subscription-level action — who created, changed, or deleted a
resource, and when.

* **Always on** — Activity Log cannot be turned off.
* **Centralized** — Logs are forwarded to a Log Analytics workspace and
  retained for at least 90 days.

You can view your Activity Log under **Monitor → Activity Log** in the Azure
portal.

For details, see the
[Azure Activity Log docs](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/activity-log).

---

## Azure Policy

[Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/overview)
enforces organizational standards across all Campus Cloud subscriptions. The
following policies are active:

| Policy | What It Enforces |
|---|---|
| Location restriction | Resources can only be created in approved regions |
| Required tags | Resource groups and resources must carry required tags |
| NIST 800-171 audit | Checks resources against NIST 800-171 controls |
| No public blob access | Storage accounts cannot expose blobs publicly |
| NSG Flow Logs | Network traffic logging is deployed automatically |

Resources that don't meet these policies show up as findings in Defender for
Cloud.

For details, see the
[Azure Policy docs](https://learn.microsoft.com/en-us/azure/governance/policy/).

---

## Log Analytics Workspace

A centralized [Log Analytics workspace](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview)
collects logs from your subscription:

* Activity Logs (resource changes)
* Diagnostic logs from resources you configure
* Security alerts from Defender for Cloud

**Retention:** At least 90 days.

To send diagnostic logs from a specific resource (VM, database, Key Vault,
etc.) to the workspace:

1. Open the resource in the Azure portal.
2. Go to **Diagnostic settings → + Add diagnostic setting**.
3. Select the Log Analytics workspace for your subscription.
4. Choose which log categories to send.

The Cloud Team can provide the workspace Resource ID if needed.

---

## Microsoft Sentinel (SIEM)

{% include alert.html type="info" title="Ask the Cloud Team" content="Centralized SIEM integration via Microsoft Sentinel may be available. Contact the Cloud Team to discuss whether your subscription's logs are forwarded to the campus Sentinel workspace." %}

For more information, see the
[Microsoft Sentinel documentation](https://learn.microsoft.com/en-us/azure/sentinel/overview).

---

## Wiz Cloud Security Posture Management

Wiz is available across all Campus Cloud platforms (AWS, Azure, GCP). See
[Security & Shared Responsibility — Wiz]({{ "/docs/general/security#wiz-cloud-security-posture-management" | relative_url }})
for details.

---

## Azure Key Vault

Use [Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/overview)
to store secrets, certificates, and encryption keys rather than hard-coding them
in application code or configuration files.

* Defender for Cloud monitors Key Vault access and alerts on unusual access patterns.
* Enable soft-delete and purge protection for production vaults.

---

## Multi-Factor Authentication

All UCSB accounts use MFA via Duo for Azure access. This applies to the Azure
portal and all API access.

If you're locked out of MFA, contact the
[UCSB Help Desk](https://www.it.ucsb.edu/get-help) — the Cloud Team cannot
bypass MFA.
