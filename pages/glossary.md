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
| **Availability Level (a1–a4)** | How critical uptime is for your resources. Set via the `availability-level` tag. See [Tagging](/docs/general/tagging). |
| **Baseline** | The standard security configuration applied to every new account — audit logging, guardrails, budget alerts. |
| **Campus Cloud Account** | General term for your cloud workspace. AWS calls it an *Account*, Azure a *Subscription*, GCP a *Project*. |
| **Campus Cloud Landing Zone** | The secure, pre-configured multi-account environment the Cloud Team maintains for each cloud provider. |
| **Campus SSO** | Sign in with your UCSB NetID. AWS uses Shibboleth SAML; Azure and GCP use Entra ID federation. |
| **Cloud Team** | The ITS team (ITS-CCID) that operates the Campus Cloud. Reachable via [ServiceNow](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5). |
| **CUI** | Controlled Unclassified Information — sensitive federal research data requiring NIST 800-171 protections. |
| **Data Management Plan (DMP)** | Documentation of how research data will be stored and managed. Use UC's [DMPTool](https://dmptool.org/). |
| **DNSSEC** | DNS Security Extensions — cryptographic protocol that authenticates DNS responses to prevent spoofing. Required on GCP public DNS zones. |
| **EBS** | Elastic Block Store — AWS block-level storage for EC2 instances. Encryption at rest is enforced by guardrails. |
| **Essential Contacts** | Emails that receive billing alerts, security warnings, and suspension notices. GCP-specific term; the concept applies to all providers. |
| **FAU** | Fund Account Unit — UCSB financial tracking code used in procurement. |
| **FERPA** | Family Educational Rights and Privacy Act — federal law protecting student education records. Data classified as Protection Level p3. |
| **Functional Email** | A shared group address (e.g., `mylab-cloud@ucsb.edu`) rather than a personal address — preferred so access survives staff changes. |
| **Gateway** | UCSB procurement portal at [gateway.procurement.ucsb.edu](https://gateway.procurement.ucsb.edu). Used to create Purchase Orders for cloud accounts. |
| **Guardrails** | Policy controls enforced across all provider accounts. Implemented as SCPs (AWS), Azure Policy (Azure), or Org Policies (GCP). |
| **HIPAA** | Health Insurance Portability and Accountability Act — federal law governing protected health information (PHI). Accounts handling PHI need additional controls; classified as Protection Level p4. |
| **IAP** | Identity-Aware Proxy — GCP service that controls access to applications based on user identity rather than network location. Used for browser-based SSH/RDP connections. |
| **ITAR** | International Traffic in Arms Regulations — U.S. export-control regulations for defense-related data and services. Classified as Protection Level p4. |
| **LDAP** | Lightweight Directory Access Protocol — protocol for accessing directory services such as Active Directory. |
| **NAT** | Network Address Translation — allows resources in a private subnet to reach the internet without a public IP address. Implemented as NAT Gateway (AWS) or Cloud NAT (GCP). |
| **NIST 800-171** | Federal security standard for protecting CUI. Accounts handling CUI receive additional guardrails aligned to this standard. |
| **NSG** | Network Security Group — Azure firewall rules that filter inbound and outbound traffic to resources in a virtual network. |
| **PII** | Personally Identifiable Information — data that can identify an individual (e.g., name, SSN, email). Classified as Protection Level p3 or higher. |
| **Protection Level (p1–p4)** | Data sensitivity: p1 = public, p2 = internal university data, p3 = sensitive (PII/FERPA), p4 = regulated (HIPAA/CUI). |
| **Purchase Order (PO)** | Funding authorization from UCSB Gateway. Required before a cloud account is created. |
| **Quarantine** | When the Cloud Team isolates a compromised or policy-violating account — network access cut, credentials disabled. |
| **Recovery Level (r1–r4)** | Backup and disaster-recovery requirements for your workload. Set via the `recovery-level` tag. |
| **RFC 1918** | Internet standard defining private IP address ranges (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16). Campus Cloud VPCs and VNets use addresses from these ranges. |
| **RPO** | Recovery Point Objective — maximum acceptable data loss measured in time (e.g., a 24-hour RPO means you could lose up to one day of data). |
| **RTO** | Recovery Time Objective — maximum acceptable downtime before a service must be restored. |
| **Service Catalog** | Pre-approved infrastructure templates you can deploy yourself (VPCs, budgets, EC2 instances, etc.). Currently available in AWS. |
| **SLO** | Service Level Objective — a target availability percentage (e.g., 99.9% uptime) for a workload. |
| **Tags / Labels** | Key-value pairs attached to resources for billing attribution, compliance, and governance. AWS and Azure call them *Tags*; GCP calls them *Labels*. |
| **UC Enterprise Discount** | UC system-wide pricing agreements with cloud providers (AWS EDP, Azure EA, GCP negotiated rates). Applied automatically to Campus Cloud accounts. |
| **UC Policy IS-3** | University of California Electronic Information Security Policy. Requires data classification and appropriate protections. |
| **Wiz** | The cloud security posture management (CSPM) tool used across all Campus Cloud environments for agentless vulnerability and misconfiguration scanning. |
| **WORM** | Write Once, Read Many — a storage retention mode that prevents log deletion or modification. Used for audit logs in GCP (3-year retention). |

