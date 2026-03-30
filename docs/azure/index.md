---
title: Azure Overview
description: Overview of the UCSB Campus Cloud Azure environment — subscriptions, management groups, regions, and what is pre-configured.
permalink: /docs/azure/
last_reviewed: 2026-03-30
---

## Azure at UCSB

The UCSB Campus Cloud Azure platform is built using the **Cloud Adoption
Framework (CAF) Enterprise Scale** reference architecture with a landing zone
deployed via Terraform. Every subscription is provisioned inside a shared
management group hierarchy with pre-applied policies, networking, and security
monitoring so teams can start building quickly with a consistent security
baseline.

---

## Key Facts

| Item | Value |
|---|---|
| Sign-in URL | [portal.azure.com](https://portal.azure.com) |
| Identity Provider | UCSB Microsoft Entra ID (Azure AD) |
| Primary Region | West US 2 (Washington) |
| Secondary Region | West Central US (Wyoming) |
| New Subscription Turnaround | ~2 business days after PO is approved |

---

## Management Group Hierarchy

Azure subscriptions are organized into a management group hierarchy. Policies
applied at a higher level in the hierarchy are inherited by all subscriptions
below it.

```
UCSB Tenant (Root)
└── Campus Cloud
    ├── Research
    ├── Academic
    ├── Administrative
    └── Sandbox
```

Your subscription is placed in the management group that matches your use
case. Policies applied to the management group govern all resources in your
subscription.

---

## What Is Pre-configured

When your subscription is provisioned, the Cloud Team will:

* **Assign four custom RBAC roles** to your team (see [Roles](/docs/azure/roles))
* **Enable Microsoft Defender for Cloud** across all supported resource types
* **Deploy Log Analytics workspace** for security monitoring (90-day retention)
* **Apply Azure Policy** for NIST 800-171 audit compliance
* **Connect networking** — your subscription receives a Virtual Network
  with hub-spoke peering to the Campus Cloud Virtual WAN (if requested)
* **Require Resource Group tags** — policy prevents RG creation without
  the five required tags

---

## Resource Groups and Tags

All resources must be inside a **Resource Group** with the five required tags.
Azure Policy enforces this — resource group creation is blocked if any
required tag is missing.

See [Tagging](/docs/general/tagging) for the full list of required tags and
allowed values.

---

## Regions

All subscriptions are configured for **West US 2** as the primary region.
West Central US is available as a secondary. Other regions are not blocked
by default but should be discussed with the Cloud Team before use to ensure
that networking, compliance, and cost monitoring will work correctly.

---

## Next Steps

* [Request a Subscription](/getting-started)
* [First Steps](/docs/azure/first-steps)
* [Networking](/docs/azure/networking)
* [Roles & Access](/docs/azure/roles)
* [Guardrails & Policies](/docs/azure/guardrails)
