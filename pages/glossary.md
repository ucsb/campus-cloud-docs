---
title: Glossary
permalink: /glossary/
---

## Glossary

For general cloud terminology, these authoritative references stay current
without our maintenance:

- [AWS Glossary](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html)
- [AWS ↔ Azure ↔ GCP service comparison](https://cloud.google.com/docs/get-started/aws-azure-gcp-service-comparison) (Google)
- [AWS ↔ Azure service comparison](https://learn.microsoft.com/en-us/azure/architecture/aws-professional/services) (Microsoft)

The table below covers terms that are specific to the UCSB Campus Cloud or
that need a campus-specific definition.

---

| Term | Definition |
|---|---|
| **Allowed Regions** | US regions where you can deploy resources: AWS (us-east-1, us-west-2), Azure (West US 2, West Central US), GCP (us-central1, us-west1). |
| **Availability Level (A1–A4)** | How critical uptime is for your resources. Set via the `availability-level` tag. See [Tagging](/docs/general/tagging). |
| **Baseline** | The standard security configuration applied to every new account — audit logging, guardrails, budget alerts. |
| **Campus Cloud Account** | General term for your cloud workspace. AWS calls it an *Account*, Azure a *Subscription*, GCP a *Project*. |
| **Campus SSO** | Sign in with your UCSB NetID. AWS uses Shibboleth SAML; Azure and GCP use Entra ID federation. |
| **Cloud Team** | The ITS team (ITS-CCID) that operates the Campus Cloud. Reachable via [ServiceNow](https://ucsb.service-now.com/). |
| **CUI** | Controlled Unclassified Information — sensitive federal research data requiring NIST 800-171 protections. |
| **Data Management Plan (DMP)** | Documentation of how research data will be stored and managed. Use UC's [DMPTool](https://dmptool.org/). |
| **Essential Contacts** | Emails that receive billing alerts, security warnings, and suspension notices. GCP-specific term; the concept applies to all providers. |
| **FAU** | Fund Account Unit — UCSB financial tracking code used in procurement. |
| **Functional Email** | A shared group address (e.g., `mylab-cloud@ucsb.edu`) rather than a personal address — preferred so access survives staff changes. |
| **Gateway** | UCSB procurement portal at [gateway.procurement.ucsb.edu](https://gateway.procurement.ucsb.edu). Used to create Purchase Orders for cloud accounts. |
| **Guardrails** | Policy controls enforced across all provider accounts. Implemented as SCPs (AWS), Azure Policy (Azure), or Org Policies (GCP). |
| **Landing Zone** | The secure, pre-configured multi-account environment the Cloud Team maintains for each cloud provider. |
| **NIST 800-171** | Federal security standard for protecting CUI. Accounts handling CUI receive additional guardrails aligned to this standard. |
| **Protection Level (P1–P4)** | Data sensitivity: P1 = public, P2 = internal university data, P3 = sensitive (PII/FERPA), P4 = regulated (HIPAA/CUI). |
| **Purchase Order (PO)** | Funding authorization from UCSB Gateway. Required before a cloud account is created. |
| **Quarantine** | When the Cloud Team isolates a compromised or policy-violating account — network access cut, credentials disabled. |
| **Recovery Level (R1–R4)** | Backup and disaster-recovery requirements for your workload. Set via the `recovery-level` tag. |
| **Service Catalog** | Pre-approved infrastructure templates you can deploy yourself (VPCs, budgets, EC2 instances, etc.). Currently available in AWS. |
| **Tags / Labels** | Key-value pairs attached to resources for billing attribution, compliance, and governance. AWS and Azure call them *Tags*; GCP calls them *Labels*. |
| **UC Enterprise Discount** | UC system-wide pricing agreements with cloud providers (AWS EDP, Azure EA, GCP negotiated rates). Applied automatically to Campus Cloud accounts. |
| **UC Policy IS-3** | University of California Electronic Information Security Policy. Requires data classification and appropriate protections. |
| **Wiz** | The cloud security posture management (CSPM) tool used across all Campus Cloud environments for agentless vulnerability and misconfiguration scanning. |

