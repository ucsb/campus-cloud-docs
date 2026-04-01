---
title: Azure Overview
description: Overview of the UCSB Campus Cloud Azure environment — subscriptions, management groups, regions, and what is pre-configured.
permalink: /docs/azure/
last_reviewed: 2026-03-30
---

## Azure at UCSB

The UCSB Campus Cloud Azure platform provides every subscription inside a
shared management group hierarchy with pre-applied policies, networking, and
security monitoring. Your team can start building right away with a consistent
security baseline.

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
applied at a higher level are inherited by all subscriptions below it.

```
UCSB Tenant (Root)
└── UCSB Campus Cloud
    ├── Landing Zones
    │   ├── UCSB Baseline V1
    │   ├── UCSB Learning
    │   └── UCSB Sponsorship
    ├── Platform
    │   ├── Connectivity
    │   └── Management
    ├── Sandboxes
    └── UCSB Legacy
```

Your subscription is placed in the management group that matches your use
case. Policies applied to the management group govern all resources in your
subscription.

---

## What Is Pre-configured

When your subscription is provisioned, the Cloud Team will:

* **Assign four custom RBAC roles** to your team (see [Roles]({{ "/docs/azure/roles" | relative_url }}))
* **Enable Microsoft Defender for Cloud** across all supported resource types
* **Deploy Log Analytics workspace** for security monitoring (90-day retention)
* **Apply Azure Policy** for NIST 800-171 audit compliance
* **Connect networking** — your subscription receives a Virtual Network
  with hub-spoke peering to the Campus Cloud Virtual WAN (if requested)
* **Require Resource Group tags** — policy audits RG creation for
  the five required tags

---

## Resource Groups and Tags

All resources must be inside a **Resource Group** with the five required tags.
Azure Policy enforces this — resource group creation is blocked if any
required tag is missing.

See [Tagging]({{ "/docs/general/tagging" | relative_url }}) for the full list of required tags and
allowed values.

---

## Regions

All subscriptions are configured for **West US 2** as the primary region.
West Central US is available as a secondary. East US 2 and Central US are also
allowed by policy. Other regions are blocked by a Deny policy at the management
group level — contact the Cloud Team before attempting to use a region not
listed here.

---

## Next Steps

* [Request a Subscription]({{ "/getting-started/procurement" | relative_url }})
* [First Steps]({{ "/docs/azure/first-steps" | relative_url }})
* [Networking]({{ "/docs/azure/networking" | relative_url }})
* [Guardrails & Policies]({{ "/docs/azure/guardrails" | relative_url }})
* [Security]({{ "/docs/azure/security" | relative_url }})
* [Roles & Access]({{ "/docs/azure/roles" | relative_url }})
