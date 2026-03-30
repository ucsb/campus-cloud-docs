---
title: Azure Guardrails & Policies
description: Azure Policy assignments and compliance controls applied to all Campus Cloud Azure subscriptions.
permalink: /docs/azure/guardrails
last_reviewed: 2026-03-30
---

## Azure Guardrails

UCSB Campus Cloud enforces guardrails — automatic restrictions that keep every
Azure subscription aligned with university security policy
([UC IS-3](https://security.ucop.edu/policies/institutional-information-and-it-resource-classification.html))
and the federal
[NIST 800-171]({{ site.baseurl }}/glossary#nist-800-171) standard for
protecting sensitive research data.

Guardrails are designed to maintain a safe, compliant baseline without getting
in the way of normal cloud usage. You will only notice them if you attempt
something outside that baseline. The sections below describe what is and is not
allowed.

---

## Required Resource Group Tags

**All Resource Groups should have the five required tags.**

This is enforced with an **Audit** policy — Resource Groups created without the
required tags will be flagged as non-compliant in Azure Policy, but creation is
not blocked.

| Tag | Allowed Values |
|---|---|
| `ucsb:po-number` | Your PO number (free text) |
| `ucsb:environment` | `dev`, `test`, `prod`, `other` |
| `ucsb:mission` | `academic`, `research`, `administrative`, `mixed` |
| `ucsb:protection-level` | `p1`, `p2`, `p3`, `p4` |
| `ucsb:availability-level` | `a1`, `a2`, `a3`, `a4` |

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

**NSG Flow Logs should be enabled on all Network Security Groups.**

NSG Flow Logs are deployed automatically via a policy assignment. If you create
NSGs directly, the policy will deploy Flow Logs for them. Verify in the NSG
configuration that Flow Logs are active.

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
