---
title: Azure Overview
description: Overview of the UCSB Campus Cloud Azure environment — subscriptions, management groups, regions, and what is pre-configured.
permalink: /docs/azure/
last_reviewed: 2026-06-25
---

# Azure at UCSB

The UCSB Campus Cloud Azure platform provides every subscription inside a
shared management group hierarchy with pre-applied policies, networking, and
security monitoring. Your team can start building right away with a consistent
security baseline.

{% capture alert_content %}
<p>Please note: UCSB has updated its approach to purchasing paid cloud services from Microsoft Azure and Google Cloud. The Azure change took effect in January. The matching change for Google Cloud takes effect on Tuesday, June 16, 2026.</p>
<p>In both cases, new paid subscriptions and projects must go through the campus <a href="{{ "/getting-started" | relative_url }}">Gateway procurement process</a> instead of being set up with a personal or departmental credit card. The campus agreements offer better pricing, give departments a clearer view of cloud spending, and protect users from unexpected charges on individual cards.</p>
<h5>Microsoft Azure (in effect since January 2026)</h5>
<ul>
  <li><strong>New paid Azure subscriptions can no longer be created with a credit card.</strong> Free Azure subscriptions can no longer be upgraded to paid subscriptions using a credit card. To set up a new paid Azure subscription, contact the Campus Cloud Team and use the Gateway procurement process.</li>
  <li><strong>Existing Azure subscriptions are not affected</strong>, even if they have a credit card associated. Azure for Students is also not affected. Students with a verified ucsb.edu email can still sign up for Azure for Students and get $100 in credit for 12 months with no credit card required. Other educational subscription types, such as MSDN and Visual Studio Enterprise, are also unchanged.</li>
</ul>
<p><strong>Questions?</strong> Email <a href="mailto:info@cloud.ucsb.edu">info@cloud.ucsb.edu</a> or open a <a href="https://ucsb.service-now.com/it?id=it_sc_cat_item&amp;sys_id=c60e6bf2dbf398900c2e38f0ad961908&amp;sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5">ServiceNow request</a>.</p>
{% endcapture %}
{% include alert.html type="warning" title="Campus Cloud Service Updates — June 2026" content=alert_content %}

---

## Key Facts

| Item | Value |
|---|---|
| Sign-in URL | [portal.azure.com](https://portal.azure.com) |
| Identity Provider | UCSB Microsoft Entra ID (Azure AD) |
| Allowed Regions | West US 2 (recommended), West Central US, East US 2, Central US |
| New Subscription Turnaround | ~2 business days after PO is approved |

---

## Management Group Hierarchy

Azure subscriptions are organized into a management group hierarchy.
Policies applied at a higher level are inherited by all subscriptions
below it.

| Management Group | Purpose |
|---|---|
| UCSB Baseline V1 | Production workloads — research, administrative, and departmental subscriptions with full guardrails |
| UCSB Learning | Coursework, labs, and student projects |
| UCSB Sponsorship | Subscriptions funded through Microsoft sponsorship credits |
| UCSB Legacy | Pre-existing subscriptions that predate the Campus Cloud |

Your subscription is placed in the management group that matches your use
case. Policies applied to the management group govern all resources in
your subscription.

---

## What Is Pre-configured

When your subscription is provisioned, the Cloud Team will:

* **Assign four custom RBAC roles** to your team (see [First Steps]({{ "/docs/azure/first-steps" | relative_url }}))
* **Enable Microsoft Defender for Cloud** across all supported resource types
* **Deploy Log Analytics workspace** for security monitoring (90-day retention)
* **Apply Azure Policy** for NIST 800-171 audit compliance
* **Connect networking** — your subscription receives a Virtual Network
  with hub-spoke peering to the Campus Cloud Virtual WAN (if requested)
* **Require Resource Group tags** — policy audits RG creation for
  the four required tags

---

## Resource Groups and Tags

All resources must be inside a **Resource Group** with the four required tags.
Azure Policy audits this — Resource Groups missing tags will be flagged as
non-compliant but can still be created.

See [Tagging]({{ "/docs/general/tagging" | relative_url }}) for the full list of required tags and
allowed values.

---

## Regions

Four regions are available: **West US 2**, **West Central US**, **East US 2**,
and **Central US**. West US 2 is recommended for most workloads. All other
regions are blocked by a Deny policy at the management group level.

---

## Microsoft Support

You can contact Microsoft directly from the Azure portal — unlike AWS, there is
no separate enrollment step. From anywhere in the portal, select the **?** (Help)
icon in the top header, or open **Help + support**, then choose **Create a
support request**.

What Microsoft can help with depends on your subscription:

* **Subscription management** — billing, quota increases, and account questions
  are included for every subscription at no cost.
* **Technical support** — subscriptions provisioned by the Campus Cloud Team are
  covered by the campus **Microsoft Unified Support** agreement, so you can open
  technical support requests for them at no extra cost. When you create a request
  for one of these subscriptions, select **Unified Support** as the support plan.
* **Student, MSDN, and Visual Studio subscriptions** are not covered by the
  campus agreement and receive **Basic** support only — subscription management
  and billing, but no Microsoft technical support. See
  [Compare Azure support plans](https://azure.microsoft.com/support/plans) for
  the difference.

To open a request, you need the **UCSB Subscription Owner** or **UCSB
Application Owner** role on the subscription (see
[First Steps]({{ "/docs/azure/first-steps" | relative_url }})).

For step-by-step instructions, see Microsoft's official guide,
[How to create an Azure support request](https://learn.microsoft.com/azure/azure-portal/supportability/how-to-create-azure-support-request).

{% include alert.html type="info" title="Open a Campus Cloud ticket first for platform issues" content="For issues related to subscription access, networking, guardrails, or Campus Cloud configuration, <a href='https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5'>open a ServiceNow ticket with the Cloud Team</a> rather than a Microsoft support request. Use Microsoft support for service-specific questions about your workloads." %}

---

## Next Steps

* [Request a Subscription]({{ "/getting-started" | relative_url }})
* [First Steps]({{ "/docs/azure/first-steps" | relative_url }})
* [Networking]({{ "/docs/azure/networking" | relative_url }})
* [Guardrails & Policies]({{ "/docs/azure/guardrails" | relative_url }})
* [Security]({{ "/docs/azure/security" | relative_url }})

