---
title: Azure Guardrails & Policies
description: Azure Policy assignments and compliance controls applied to all Campus Cloud Azure subscriptions.
permalink: /docs/azure/guardrails
last_reviewed: 2026-03-30
---

## Azure Guardrails

UCSB Campus Cloud applies guardrails via **Azure Policy** assignments at the
management group level. Policies are inherited by all subscriptions
automatically. Some policies are **Audit** (log and alert on non-compliance)
and some are **Deny** (block non-compliant resource creation entirely).

---

## Required Resource Group Tags

**Resource Groups cannot be created without all five required tags.**

This is enforced with a **Deny** policy — attempts to create a Resource Group
without the tags will be blocked with a policy violation error.

| Tag | Allowed Values |
|---|---|
| `ucsb:po-number` | Your PO number (free text) |
| `ucsb:environment` | `production`, `staging`, `development`, `sandbox` |
| `ucsb:mission` | `research`, `academic`, `administrative`, `infrastructure` |
| `ucsb:protection-level` | `P1`, `P2`, `P3`, `P4` |
| `ucsb:availability-level` | `A1`, `A2`, `A3`, `A4` |

See [Tagging](/docs/general/tagging) for definitions of protection and
availability levels.

---

## Public Storage Access

**Public blob access on Storage Accounts is blocked.**

Azure Policy denies the creation of Storage Accounts with `allowBlobPublicAccess`
set to `true`. If you need to share data publicly, use either:

* A **pre-signed Shared Access Signature (SAS) URL** with a short expiry.
* **Azure CDN** fronting a private storage account.
* A blob with a specific **public container** configuration discussed with the
  Cloud Team.

---

## NSG Flow Logs

**NSG Flow Logs must be enabled on all Network Security Groups.**

This is an Audit policy. NSG Flow Logs are enabled automatically on NSGs
created by the Cloud Team. If you create NSGs directly, the policy will flag
them as non-compliant — enable Flow Logs in the NSG configuration.

---

## NIST 800-171 Audit Initiative

A NIST 800-171 Policy Initiative is applied in Audit mode to all subscriptions.
It does not block resource creation, but it generates compliance findings in
Microsoft Defender for Cloud for controls that are not met.

Regularly review your compliance posture:
1. Navigate to **Microsoft Defender for Cloud → Regulatory compliance**.
2. Select **NIST SP 800-171** from the list.
3. Review and remediate any failing controls.

---

## What You Can and Cannot Do

### You Can
* Create any resource type in West US 2 (recommended) and West Central US
* Create custom NSG rules and route tables within your VNet
* Create additional Resource Groups (with required tags)
* Enable, configure, and disable most Azure services in your subscription

### You Cannot
* Create a Resource Group without all five required tags
* Enable public blob access on storage accounts
* Remove or modify policy assignments (management group level, read-only)
* Detach your subscription from the management group hierarchy

---

## Requesting a Policy Exception

If a policy blocks something you believe is legitimate, open a ServiceNow
ticket. Explain the use case and the specific policy assignment that is
blocking you. The Cloud Team will evaluate the request and, if appropriate,
create a policy exemption on your subscription.

Exceptions are not granted for controls required by UC IS-3 policy.
