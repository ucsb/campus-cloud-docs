---
title: Shared Responsibility
description: How responsibilities are divided between the cloud providers, the Campus Cloud Team, and you
permalink: /docs/general/shared-responsibility
last_reviewed: 2026-04-06
---

## Shared Responsibility

The Campus Cloud operates on a shared responsibility model. Three parties each
own a distinct layer:

* **The cloud provider** secures the underlying infrastructure.
* **The Campus Cloud Team** secures the Landing Zone configuration, policies, and platform tooling.
* **You** are responsible for how you configure and use the resources in your account.

This model applies across all three providers (AWS, Azure, GCP) and across every
domain — security, cost, compliance, and data management.

---

## Responsibilities by Party

### What the Cloud Provider Is Responsible For

* Physical data center security, hardware, and networking infrastructure
* The underlying compute, storage, and network systems that managed services
  run on
* Software patches and updates for managed services (RDS, Cloud SQL, Azure SQL, etc.)

### What the Campus Cloud Team Is Responsible For

* Landing Zone configuration: guardrails, org policies, management group
  structure
* Centralized audit logging and security monitoring
* Campus network connectivity
* Identity federation (UCSB SSO to each provider)
* Platform-level compliance controls (NIST 800-171 baseline)
* Baseline security tooling that runs continuously in every account (these
  incur a small cost — see [Baseline Costs]({{ "/docs/general/cost-management#baseline-costs" | relative_url }}))

### What You Are Responsible For

* **Security:** Configuring your workloads securely (storage bucket permissions,
  security groups, firewall rules) and responding to security findings in your
  account — see [Security]({{ "/docs/general/security" | relative_url }})
* **Cost:** Monitoring your spending, setting up budget alerts, and rightsizing
  resources — see [Costs & Billing]({{ "/docs/general/cost-management" | relative_url }})
* **Compliance:** Classifying your data, applying required tags, and ensuring
  your use complies with UC Policy IS-3 and applicable regulations — see
  [Compliance]({{ "/docs/general/compliance" | relative_url }})
* **Data:** Managing access to your data and planning for archiving and
  retention — see [Data Management]({{ "/docs/general/data-management" | relative_url }})
* **Access:** Granting the minimum role necessary to each person in your
  account

---

## Summary

| Domain | Cloud Provider | Campus Cloud Team | You |
|---|---|---|---|
| **Security** | Infrastructure security, managed-service patching | Guardrails, audit logging, security monitoring, SSO | Workload configuration, access control, finding remediation |
| **Cost** | Billing and invoicing | Baseline tooling (runs at a cost to you), UC enterprise discount negotiation | Budget alerts, spend monitoring, rightsizing |
| **Compliance** | Certifications (SOC 2, ISO 27001, etc.) | Landing Zone controls, NIST 800-171 baseline, compliance tracking tools | Data classification, tagging, regulatory adherence |
| **Data** | Storage durability, encryption at rest | Encryption defaults, audit trail of data access | Data classification, retention planning, access management |

For the cloud providers' own descriptions of shared responsibility, see:
* [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)
* [Azure Shared Responsibility](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility)
* [GCP Shared Responsibility and Shared Fate](https://cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate)
