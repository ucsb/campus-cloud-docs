---
title: Azure Security
description: Security monitoring, Defender for Cloud, and log management in Campus Cloud Azure subscriptions.
permalink: /docs/azure/security
last_reviewed: 2026-03-30
---

## Azure Security

Every Campus Cloud Azure subscription comes with a pre-configured security
monitoring baseline. The main components are **Microsoft Defender for Cloud**
and a centralized **Log Analytics workspace**.

---

## Microsoft Defender for Cloud

Defender for Cloud is enabled on all Campus Cloud subscriptions. It provides:

* **Continuous security posture assessment** — Identifies misconfigured resources
  and suggests remediation steps (Secure Score).
* **Workload protection** — Runtime threat detection for VMs, databases,
  storage, containers, and key vaults.
* **Regulatory compliance dashboard** — Tracks your subscription against NIST
  800-171 and other frameworks.
* **Security alerts** — Generates alerts for suspicious activity and sends
  them to your Security contact.

### Reviewing Defender Recommendations

1. Navigate to **Microsoft Defender for Cloud → Recommendations**.
2. Sort by severity (High → Medium → Low).
3. Click a recommendation to see affected resources and remediation steps.

Addressing High severity recommendations should be a routine task for account
owners.

---

## Log Analytics Workspace

A centralized Log Analytics workspace is provisioned for your subscription.
It collects:

* Azure Activity Logs (changes to subscription-level resources)
* Diagnostic logs forwarded from resources you configure
* Security alerts from Defender for Cloud

**Retention:** Logs are retained for a minimum of 90 days in the workspace.

To configure a resource (e.g., a VM, SQL database, or Key Vault) to forward
diagnostic logs to the workspace:

1. Open the resource in the portal.
2. Navigate to **Diagnostic settings → + Add diagnostic setting**.
3. Select the Log Analytics workspace for your subscription.
4. Choose the log categories to send.

The Cloud Team can provide the workspace Resource ID if needed.

---

## Microsoft Sentinel (SIEM)

{% include alert.html type="info" title="Ask the Cloud Team" content="Centralized SIEM integration via Microsoft Sentinel may be available. Contact the Cloud Team to discuss whether your subscription's logs are forwarded to the campus Sentinel workspace." %}

---

## Incident Response

If you observe a suspicious event or believe a resource has been compromised:

1. **Document immediately** — Note the resource name, subscription, approximate
   time, and what you observed.
2. **Do not delete evidence** — Do not terminate VMs, delete logs, or rotate
   secrets before notifying the Cloud Team.
3. **Open a [ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5) marked Urgent** — [ServiceNow](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5) → Cloud Services →
   describe the incident. Include the Account/Subscription ID.
4. **Contact your department's ISO** (Information Security Officer) if
   regulated data may be involved.

### Emergency Isolation

If a VM is actively compromised and you need to stop the attack:

* Apply a **Network Security Group rule** that blocks all inbound/outbound
  traffic to the VM (deny all, priority 100) while preserving the VM for forensics.
* Do **not** delete or deallocate the VM — forensic images may be needed.

---

## Azure Key Vault

Use Azure Key Vault to store secrets, certificates, and encryption keys rather
than hard-coding them in application code or configuration files.

* Defender for Cloud monitors Key Vault access and alerts on anomalous access patterns.
* Key Vault soft-delete and purge protection are recommended for production vaults.

---

## Multi-Factor Authentication

All UCSB accounts enforced MFA via UCSB Duo as part of the Entra ID configuration.
This applies to all Azure portal and API access.

If a user loses MFA access or is locked out, contact UCSB IT Security or the
Help Desk — the Cloud Team does not bypass MFA requirements.
