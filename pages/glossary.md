---
title: Glossary
description: Definitions of terms specific to the UCSB Campus Cloud.
permalink: /glossary/
last_reviewed: 2026-10-30
---

# Glossary

For general cloud terminology, see:

- [AWS Glossary](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html) (Amazon)
- [AWS ↔ Azure ↔ GCP service comparison](https://cloud.google.com/docs/get-started/aws-azure-gcp-service-comparison) (Google)
- [AWS ↔ Azure service comparison](https://learn.microsoft.com/en-us/azure/architecture/aws-professional/services) (Microsoft)

The table below covers terms that are specific to the UCSB Campus Cloud or
that need a campus-specific definition.

| Term | Definition |
|---|---|
| **Access Groups** | Per-account/project groups used to grant access by role instead of granting it to individuals. AWS uses role groups managed in [Identity Manager](https://im.ucsb.edu); GCP creates four Google Groups (owners, editors, viewers, billing) per project. See [Identity & Access]({{ "/docs/general/identity" | relative_url }}). |
| **Allowed Regions** | US regions where you can deploy resources: AWS (us-east-1, us-west-2), Azure (West US 2, West Central US, East US 2, Central US), GCP (us-central1, us-west1). |
| **Availability Level (a1–a4)** | How critical uptime is for your resources. Set via the `availability-level` tag. See [Tagging]({{ "/docs/general/tagging" | relative_url }}). |
| **Baseline** | The standard security configuration applied to every new account — audit logging, guardrails, and security monitoring. |
| **Campus Cloud Account** | General term for your cloud workspace. AWS calls it an *Account*, Azure a *Subscription*, GCP a *Project*. |
| **Campus Cloud Landing Zone** | The secure, pre-configured multi-account environment the Cloud Team maintains for each cloud provider. |
| **CCOA** | Common Chart of Accounts — the UC-wide account string UCSB has used since July 1, 2025, replacing the FAU. Used in procurement and in the `ucsb:costing` tag. See [Financial Management Modernization — CCOA](https://financemanagement.ucsb.edu/resources/CCOA). |
| **Cloud Team** | The ITS team (ITS-CCID) that operates the Campus Cloud. For support and service requests, use [ServiceNow](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5). For general questions and consulting, email [info@cloud.ucsb.edu](mailto:info@cloud.ucsb.edu). |
| **CUI** | Controlled Unclassified Information — sensitive federal research data requiring NIST 800-171 protections. |
| **Data Management Plan (DMP)** | Documentation of how research data will be stored and managed. Use UC's [DMPTool](https://dmptool.org/). |
| **DNSSEC** | DNS Security Extensions — cryptographic protocol that authenticates DNS responses to prevent spoofing. Required on GCP public DNS zones. |
| **EBS** | Elastic Block Store — AWS block-level storage for EC2 instances. Encryption at rest is enforced by guardrails. |
| **Essential Contacts** | Emails that receive billing alerts, security warnings, and suspension notices. GCP-specific term; the concept applies to all providers. |
| **FAU** | Full Accounting Unit — UCSB's former account string, replaced by the CCOA in July 2025. |
| **FERPA** | Family Educational Rights and Privacy Act — federal law protecting student education records. Data classified as Protection Level p3. |
| **Functional Email** | A shared group address (e.g., `mylab-cloud@ucsb.edu`) rather than a personal address — preferred so access survives staff changes. |
| **Gateway** | UCSB procurement portal at [gateway.procurement.ucsb.edu](https://gateway.procurement.ucsb.edu). Used to create Purchase Orders for cloud accounts. |
| **Guardrails** | Policy controls enforced across all provider accounts. Implemented as SCPs (AWS), Azure Policy (Azure), or Org Policies (GCP). |
| **HIPAA** | Health Insurance Portability and Accountability Act — federal law governing protected health information (PHI). Accounts handling PHI need additional controls; classified as Protection Level p4. |
| **IAP** | Identity-Aware Proxy — GCP service that controls access to applications based on user identity rather than network location. Used for browser-based SSH/RDP connections. |
| **IS-3 (UC Policy)** | University of California [Electronic Information Security Policy](https://policy.ucop.edu/advanced-search.html?action=search&op=results&lookup=1&keywords=IS-3&search=Search). Requires data classification and appropriate protections. |
| **ITAR** | International Traffic in Arms Regulations — U.S. export-control regulations for defense-related data and services. Classified as Protection Level p4. |
| **LDAP** | Lightweight Directory Access Protocol — protocol for accessing directory services such as Active Directory. |
| **NAT** | Network Address Translation — allows resources in a private subnet to reach the internet without a public IP address. Implemented as NAT Gateway (AWS) or Cloud NAT (GCP). |
| **NIST 800-171** | Federal security standard for protecting CUI. New and imported Campus Cloud accounts include controls aligned to this standard. |
| **NSG** | Network Security Group — Azure firewall rules that filter inbound and outbound traffic to resources in a virtual network. |
| **Organizational Unit (OU)** | An AWS group of accounts that share the same policies. Azure *management groups* and GCP *folders* play the same role. New and imported Campus Cloud accounts have the NIST 800-171 controls applied. See [Compliance]({{ "/docs/general/compliance" | relative_url }}). |
| **PII** | Personally Identifiable Information — data that can identify an individual (e.g., name, SSN, email). Classified as Protection Level p3 or higher. |
| **Protection Level (p1–p4)** | Data sensitivity: p1 = public, p2 = internal university data, p3 = sensitive (PII/FERPA), p4 = regulated (HIPAA/CUI). |
| **Purchase Order (PO)** | Funding authorization from UCSB Gateway. Required before a cloud account is created. |
| **Quarantine** | When the Cloud Team isolates a compromised or policy-violating account — network access cut, credentials disabled. |
| **Recovery Level (r1–r4)** | Backup and disaster-recovery requirements for your workload. Set via the `recovery-level` tag. |
| **RFC 1918** | Internet standard defining private IP address ranges (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16). Campus Cloud VPCs and VNets use addresses from these ranges. |
| **Secure Service Access (SSA)** | UCSB's off-campus access service for faculty, staff, and student employees. It uses the Zscaler Client Connector and replaces the Campus VPN (Ivanti), which retires January 22, 2027. Works with AWS and Azure; see [Secure Service Access (SSA)](https://it.ucsb.edu/services/secure-service-access). |
| **Service Catalog** | Pre-approved infrastructure templates you can deploy yourself (VPCs, IAM roles, instance scheduling, etc.). Currently available in AWS. |
| **SLO** | Service Level Objective — a target availability percentage (e.g., 99.9% uptime) for a workload. |
| **Tags / Labels** | Key-value pairs used for billing attribution, compliance, and governance. AWS and Azure call them *Tags* and attach them to resources. GCP uses two systems, both set on the project: required *Resource Manager Tags* (governance and cost attribution) and optional *project labels* (cost attribution only). See [Tagging & Labels]({{ "/docs/general/tagging" | relative_url }}). |
| **UC Enterprise Discount** | UC system-wide pricing agreements with cloud providers (AWS EDP, Azure EA, GCP negotiated rates). Applied automatically to Campus Cloud accounts. |
| **UCSB SSO** | Single sign-on with your UCSB netID. AWS uses Shibboleth SAML; Azure and GCP use Entra ID federation. |
| **VPC Family** | A preset network size and layout you pick when you launch the AWS Simple VPC product, named like `n2.medium.private`: the number of subnets (`n1`, `n2`, `n4`), the total IP addresses (`small` = 32 up to `xlarge` = 256), and whether the subnets are public, private, or mixed. Defined by the Cloud Team, not by AWS. See [VPC Families]({{ "/docs/aws/networking/#vpc-families" | relative_url }}). |
| **Wiz** | A cloud security posture management (CSPM) tool for agentless vulnerability and misconfiguration scanning. Available on all three providers; accounts are enrolled on an opt-in basis. See [Security]({{ "/docs/general/security/#wiz-cloud-security-posture-management" | relative_url }}). |
| **WORM** | Write Once, Read Many — a storage mode that prevents stored data from being deleted or modified. Used for audit logs in GCP (3-year retention). |
