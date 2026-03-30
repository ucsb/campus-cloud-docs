# Campus Cloud Documentation — Future Update Plan

> Generated 2025-03-25 by cross-referencing the current docs site against the
> actual `campus-cloud-aws-landing-zone`, `campus-cloud-azure-landing-zone`,
> and `campus-cloud-gcp-landing-zone` repositories.

> **Audience reminder:** This site (docs.cloud.ucsb.edu) serves **campus cloud
> customers** — researchers, faculty, and department IT staff who request and
> operate cloud accounts. Content should tell users what they can do, what
> guardrails are enforced, and how to get help. Internal implementation details
> (Terraform files, automation scripts, deployment pipelines) belong in the
> landing zone repos, not here. Where this plan references repo files, those
> are notes for the **doc authors** indicating where to find authoritative
> source information — not content to publish on the site.

---

## 1. Proposed Restructure

The current layout mixes provider-specific and cross-cutting content across
`bestpractices/` and `guidelines/` folders. A provider-centric structure makes
coverage gaps immediately visible and sets a clear expectation of parity.

### Proposed directory layout

```
pages/
  about.md                 # Keep — cloud computing overview
  getting-started.md       # Keep — procurement, budgeting, training
  glossary.md              # Expand significantly (see §5)
  docs.md                  # Keep — hub page
  tags.html                # Keep

docs/
  general/                 # Cloud-agnostic guidance
    cost-models.md         # NEW (currently empty stub)
    tagging.md             # MERGE guidelines/tagging.md + bestpractices/tagging.md
    compliance.md          # MOVE from guidelines/ (already multi-provider)
    research.md            # MOVE from bestpractices/
    close-account.md       # MOVE from bestpractices/close.md
    migrate.md             # MOVE from guidelines/
    dmp.md                 # MOVE from guidelines/
    security-overview.md   # NEW — shared responsibility concept across all 3 CSPs
    iam-overview.md        # NEW — federated identity patterns across all 3 CSPs

  aws/
    overview.md            # REFACTOR from guidelines/description.md (AWS sections)
    first-steps.md         # MOVE from firststeps/awsfirststeps.md
    networking.md          # MOVE from guidelines/networking.md
    guardrails.md          # MOVE from guidelines/guardrails.aws.md
    security.md            # MOVE from guidelines/security.md
    service-catalog.md     # MOVE from bestpractices/servicecatalog.md
    contacts.md            # MOVE from bestpractices/contacts.md
    vpn.md                 # MOVE from bestpractices/vpn.md
    quicksight.md          # MOVE from guidelines/quicksight.dashboards.md

  azure/
    overview.md            # NEW — architecture, CAF Enterprise Scale, management groups
    first-steps.md         # EXPAND from firststeps/azurefirststeps.md (currently a stub)
    networking.md          # NEW — Virtual WAN, VPN, hub-spoke, NSGs
    guardrails.md          # EXPAND from guidelines/guardrails.azure.md
    security.md            # NEW — Defender, Key Vault, Entra ID, shared responsibility
    custom-roles.md        # NEW — the 4 custom RBAC roles
    contacts.md            # NEW — billing/security/operations contacts for Azure
    cost-management.md     # NEW — Azure Cost Management + budgets

  gcp/
    overview.md            # NEW — org/folder/project hierarchy, landing zone architecture
    first-steps.md         # EXPAND from firststeps/gcpfirststeps.md (currently a stub)
    networking.md          # NEW — networking guardrails, connectivity, VPN modules
    guardrails.md          # NEW — org policies, custom constraints, deny policies
    security.md            # NEW — SCC, audit logging, IAM, VPC Service Controls
    tagging.md             # NEW — Resource Manager tags, 9 tag keys, 530+ values
    billing.md             # NEW — billing sub-accounts, cost viewing, budget alerts
    contacts.md            # NEW — notification contacts configuration
```

### Files to remove or consolidate

| Current file | Action | Reason |
|---|---|---|
| `docs/guidelines/servicecatalog.md` | DELETE | Empty stub; real content is in `bestpractices/servicecatalog.md` |
| `docs/bestpractices/costmodels.md` | DELETE or REPLACE | Completely empty — replace with `general/cost-models.md` |
| `docs/bestpractices/tagging.md` | MERGE into `general/tagging.md` | Overlaps with `guidelines/tagging.md`; ends with "More to come...." |
| `docs/guidelines/description.md` | SPLIT | AWS section → `aws/overview.md`; Azure/GCP sections are empty placeholders |
| `docs/firststeps/index.md` | REPLACE | Becomes unnecessary with provider-based layout |
| `docs/bestpractices/index.md` | REPLACE | Becomes unnecessary with provider-based layout |
| `docs/guidelines/index.md` | REPLACE | Becomes unnecessary with provider-based layout |

---

## 2. AWS Documentation Gaps

The AWS docs are the most complete but still have gaps when compared to the
actual landing zone infrastructure.

### 2a. `aws/overview.md` — Landing Zone Architecture

Current `guidelines/description.md` covers the basics. Should be expanded to include:

- How the Campus Cloud AWS environment is organized (Control Tower, Organizational Units)
- What happens when you request a new account (provisioning workflow from the customer's perspective)
- What's pre-configured in every new account (security baselines, budgets, contacts)
- Available regions (us-east-1, us-west-2) and why others are restricted

### 2b. `aws/service-catalog.md` — Update Product List

Cross-reference with the actual `service-catalog/products/` directory:

| Product in Docs | In Landing Zone Repo | Status |
|---|---|---|
| Local Security Notifications | `sc-product-security-notifications.yaml` | ✅ Matches |
| Fixed Monthly Budget with Notification | `sc-product-budget.yaml` | ✅ Matches |
| Budget Alert and Action on Threshold (Effectual) | Not found in repo | ⚠️ May be deprecated — verify |
| Instance Scheduler | Not found in repo | ⚠️ May be external — verify |
| Create IAM Role to UCSB Identity Group | Shibboleth integration in identity templates | ✅ Exists differently |
| Simple VPC with Campus Connectivity | VPC products in service-catalog | ✅ Matches |
| Advanced VPC | VPC products in service-catalog | ✅ Matches |
| SNS Topic product | `service-catalog/products/` | ❌ Not documented |

### 2c. `aws/guardrails.md` — Update Guardrail List

The current guardrails page is dated Feb 2023 and missing several enforced controls
that users need to know about. Add customer-facing descriptions of:

- UCSB-BASELINE budget/stack protections — users cannot delete campus-managed resources
- Root user lockout — root credentials cannot be used (explain what to do instead)
- EC2 IMDSv2 requirement — instance metadata v1 is blocked; what this means for your AMIs
- Region restrictions — only us-east-1 and us-west-2, with a Bedrock exception (explain how to use it)
- Auto-remediation rules: S3 encryption, EFS encryption, VPC flow logs, CloudWatch encryption,
  IAM admin-access detection — explain what happens if you create non-compliant resources

### 2d. `aws/networking.md` — Add Practical Details

The existing networking page is good but missing some things users frequently need:

- NAT Gateway IP addresses — users need these for firewall allowlisting
- How IP address space is allocated for your VPC (users don't need to know about
  IPAM internals, but should know the process for requesting address space)
- Cross-cloud connectivity — if your project spans AWS and Azure/GCP, how does routing work?

### 2e. `aws/contacts.md` — Clarify What's Automatic vs. Manual

Users should understand:
- Which contacts are pre-configured for you during account setup
- Which contacts you need to set up yourself (and how)
- How to update contacts after initial setup
- That PO numbers are automatically tagged — but how to verify yours is correct

---

## 3. Azure Documentation — Major Expansion Needed

The Azure landing zone repo reveals substantial infrastructure that is
**completely undocumented**. Every file below needs to be written essentially
from scratch.

### 3a. `azure/overview.md` — Architecture & Management Groups

> *Author source:* `core/main.tf`, `core/locals.tf`

Outline:
- How the Campus Cloud Azure environment is organized
- Management Group hierarchy (what group your subscription lands in and what that means)
- Available subscription types: Legacy, Learning, Sponsorship, Baseline V1, Sandbox
- What's pre-configured in every new subscription
- How to request a new subscription
- Comparison to AWS: Management Groups ≈ OUs, Subscriptions ≈ Accounts

### 3b. `azure/first-steps.md` — Subscription Onboarding

> *Author source:* `core/locals.ucsb-subscriptions.tf`

Outline:
- Azure SSO login via UCSB credentials
- Subscription placement in management group hierarchy
- Available custom RBAC roles (see §3f)
- Setting up budget alerts (Azure Cost Management)
- Verifying security posture (Defender for Cloud, policy compliance)
- Network connectivity options
- Azure support plan information
- Identity management via Entra ID

### 3c. `azure/networking.md` — Virtual WAN & Connectivity

> *Author source:* `platform/archive-code/modules/connectivity/`, VPN configs

Outline:
- Campus Cloud Azure networking architecture (hub-and-spoke via Virtual WAN)
- Available regions: West US 2 (primary), West Central US (secondary)
- How to request a VNet for your subscription
- VPN connectivity: how your subscription connects to campus, AWS, and GCP
- What network security is enforced (NSG flow logging, allowed regions)

### 3d. `azure/guardrails.md` — Policies & Compliance

> *Author source:* `core/lib/` policy definitions, archetype configurations

Outline:
- What Azure Policy does and how it affects your subscription
- Required tags on all resources (and what happens if you forget them):
  - `ucsb:po-number`, `ucsb:environment`, `ucsb:mission`, `ucsb:protection-level`, `ucsb:availability-level`
- Security policies enforced on your subscription:
  - No public blob storage
  - NSG flow logs deployed automatically
  - NIST 800-171 R2 compliance audit (what findings you may see)
- Policies that are *not* enforced (opted out of defaults)
  — e.g., IP forwarding and RDP are allowed in certain management groups
- How to check your compliance status in the Azure portal

### 3e. `azure/security.md` — Security Posture

> *Author source:* `platform/management/`, Security Center configs

Outline:
- Azure Shared Responsibility Model (what Microsoft manages vs. what you manage)
- Microsoft Defender for Cloud — what it monitors and how to review findings
- How to view your compliance status and security recommendations
- Centralized logging — what's collected on your behalf, how long it's retained
- Identity management via Entra ID (UCSB SSO)

### 3f. `azure/custom-roles.md` — RBAC Roles

> *Author source:* `custom-iam-roles/` directory

Outline:
- Four custom roles available to you:

| Role | Purpose | Key Restrictions |
|---|---|---|
| **UCSB Subscription Owner** | Full subscription control | Cannot manage VPN Gateways, ExpressRoute, VPN Sites |
| **UCSB Application Owner** | Application-level management | No authorization writes, no networking writes, no Key Vault purge |
| **UCSB Network Operations** | Platform connectivity | VPN, ExpressRoute, Route Tables, NSGs |
| **UCSB Security Operations** | Enterprise security admin | Policies, roles, Key Vault purge, Security Center |

- How roles are assigned
- Comparison to AWS: Custom Roles ≈ IAM Roles, Management Groups ≈ permission boundaries

### 3g. `azure/cost-management.md` — Budgets & Cost Tracking

Outline:
- Azure Cost Management + Billing
- Budget alerts setup
- Tagging-based cost allocation (`ucsb:po-number`)
- Subscription-level cost tracking
- Comparison to AWS QuickSight dashboards

---

## 4. GCP Documentation — Build from Scratch

The GCP landing zone is fully built and operational. The landing zone repo
contains extensive internal documentation and Terraform code that doc authors
can reference when writing the customer-facing pages below.

> *Author reference:* Internal docs are in `docs/` (8 primary docs + implementation
> notes). Terraform is in `terraform/workspaces/gcp-bootstrap/` (WIF setup) and
> `terraform/workspaces/ucsb-management/` (30+ .tf files, 200+ resources). The
> top-level `environment/` and `modules/` directories are copies of Google’s
> Cloud Foundation Fabric (FAST) reference and are **not** used directly.

### 4a. `gcp/overview.md` — Landing Zone Architecture

> *Author source:* `docs/gcp-landing-zone.md`, `terraform/workspaces/gcp-bootstrap/`,
> `terraform/workspaces/ucsb-management/folder-structure.tf`, `main.tf`

Outline:
- How the Campus Cloud GCP environment is organized:
  - Organization → Folders → Projects (analogous to AWS OUs → Accounts)
  - `/UCSB NIST Baseline` — where most projects live (production workloads)
  - `/Sandbox Unfunded` — no-billing sandbox projects for experimentation
  - `/UCSB Legacy` — pre-existing projects with relaxed policies
  - `/UCSB Quarantine-Disabled` — isolated projects (compromised or decommissioned)
- What's pre-configured in every new project:
  - Budget alerts and billing sub-account
  - Required tags (environment, mission, protection-level, etc.)
  - Organization-wide security policies automatically apply
  - Centralized audit logging
- Identity: UCSB SSO via Entra ID federation to Google Workspace
- Available regions: us-central1, us-west1 (others restricted)
- Comparison to AWS: Folders ≈ OUs, Projects ≈ Accounts, Org Policies ≈ SCPs

### 4b. `gcp/first-steps.md` — Project Onboarding

> *Author source:* `docs/gcp-scripts.md`, `docs/gcp-org-roles.md`

Outline:
- GCP Console login via UCSB SSO (Entra ID federation)
- How to request a new project
- What folder your project will be placed in (NIST Baseline by default)
- What's already set up for you (billing, tags, audit logging, security policies)
- Setting up billing budget alerts
- Reviewing Security Command Center findings in your project
- Your available IAM roles and how to manage team access
- Google Cloud Support plan information
- Links to GCP training resources (Cloud Skills Boost, certifications)

### 4c. `gcp/networking.md` — Networking & Connectivity

> *Author source:* `docs/gcp-guardrails.md` (networking policies), `terraform/modules/hub_vpn/`

Outline:
- What networking rules apply to your project:
  - Custom-mode VPCs only (no auto-mode)
  - No external IPs on VMs (use Cloud NAT or IAP for outbound/inbound access)
  - Internal load balancers only
  - VPC flow logs, firewall logging, and DNS logging required on all resources
  - DNSSEC required on public DNS zones
  - TLS 1.2+ required (weak cipher suites blocked)
- Available regions: us-central1 and us-west1 only
- You cannot create VPCs yourself — request network resources from the Campus Cloud Team
- Cross-cloud connectivity: how your project connects to campus, AWS, and Azure
- How to request network resources for your project

### 4d. `gcp/guardrails.md` — Organization Policies & What They Mean for You

> *Author source:* `docs/gcp-guardrails.md`, `terraform/workspaces/ucsb-management/org-policies.tf`,
> `org-deny-policies.tf`, `org-custom-constraints.tf`

Outline (framed as "what you can and can't do"):
- **Storage:** No public Cloud Storage buckets
- **Compute:** Shielded VMs required, OS Login enforced (no SSH keys in metadata),
  no external IPs, no IP forwarding, only Google-managed images
- **Identity:** Only @ucsb.edu accounts can be granted access — no @gmail.com,
  no allUsers/allAuthenticatedUsers
- **Location:** Resources restricted to us-central1 and us-west1
- **Networking:** See §4c for full list
- **Audit:** Detailed audit logging enabled for all services automatically
- **Service account keys:** Being phased out org-wide — use Workload Identity
  Federation instead
- **What you cannot change yourself:**
  - Folder structure, billing account assignments, organization-level settings
  - You cannot create VPCs (managed by Campus Cloud Team)
  - You cannot modify essential contacts (preserved by policy)
- Comparison to AWS Control Tower guardrails and Azure Policy

### 4e. `gcp/security.md` — Security & Audit Logging

> *Author source:* `docs/gcp-org-roles.md`, `docs/gcp-guardrails.md`,
> `terraform/workspaces/ucsb-management/org-audit.tf`, `org-iam.tf`, `ucsb-core-vpc-sc.tf`

Outline:
- GCP Shared Responsibility Model (what Google manages vs. what you manage)
- What’s monitored and logged on your behalf:
  - All API calls and data access events are logged automatically
  - Audit logs are stored centrally and retained for compliance (you can’t delete them)
  - Security Command Center scans for misconfigurations
- Identity and access:
  - Only @ucsb.edu accounts can be granted access
  - UCSB SSO via Entra ID federation
  - No service account keys — use Workload Identity Federation instead
- How to review your project’s security posture in the GCP Console
- How to report a security concern- What happens if your project is quarantined (network cut off, credentials
  disabled) and how to request restoration
### 4f. `gcp/tagging.md` — Required Tags for Your Project

> *Author source:* `docs/gcp-tagging.md`, `terraform/workspaces/ucsb-management/tags.tf`

Outline:
- **Tags the Campus Cloud Team sets for you** (you can’t change these):
  - `expiry-date` — when your project will be reviewed/cleaned up
  - `billing-limit` — spending cap ($20/$50/$100)
  - `wiz-scanning` — whether Wiz cloud security monitoring is enabled

- **Tags you manage on your project:**
  - `environment` — dev / test / prod / other
  - `mission` — academic / research / administrative / mixed
  - `protection-level` — P1 (public) through P4 (restricted)
  - `availability-level` — A1 through A4
  - `recovery-level` — R1 through R4
  - `dept` — your UCSB department code

- How to view and update your project’s tags in the GCP Console
- Comparison to AWS tags and Azure tags

### 4g. `gcp/billing.md` — Billing & Cost Management

> *Author source:* `docs/gcp-billing-subaccounts.md`, `terraform/workspaces/ucsb-management/billing-accounts.tf`

Outline:
- How GCP billing works for campus projects (billing sub-accounts per department)
- How to view your project’s costs (BigQuery billing export, Looker Studio)
- How to set up budget alerts
- Billing limit tags — what happens when you hit your cap
- Comparison to AWS Cost Explorer / QuickSight

### 4h. `gcp/contacts.md` — Notification Contacts

> *Author source:* `docs/gcp-landing-zone.md`, `terraform/workspaces/ucsb-management/org-essential-contacts.tf`

Outline:
- What notifications you’ll receive (billing alerts, security findings, suspension warnings)
- Pre-configured contacts (set by Campus Cloud Team)
- How to add or update project-level contacts
- What happens if you don’t have contacts configured


---

## 5. Cross-Cutting Content Improvements

### 5a. `pages/glossary.md` — Replace with Links + Campus-Specific Terms

Current format: 6 bullet-point definitions, all AWS-centric. Replace with
external links for generic cloud vocabulary, plus a table of terms that only
UCSB can define.

---

#### Cross-cloud service comparisons — link out, don't maintain

For "what's the GCP equivalent of an AWS Account?" or "what's the Azure version
of S3?" style questions, link to the authoritative comparison pages maintained
by Google and Microsoft (they stay current; we don't have to):

- **AWS:** [AWS Glossary](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html) — comprehensive A-Z definitions of all AWS services and concepts.
- **Google Cloud:** [AWS → Azure → GCP service mapping](https://cloud.google.com/docs/get-started/aws-azure-gcp-service-comparison) — covers organization, compute, storage, databases, networking, security, identity, monitoring, serverless, containers, billing, and more.
- **Microsoft:** [AWS → Azure service comparison](https://learn.microsoft.com/en-us/azure/architecture/aws-professional/services) — comprehensive AWS-to-Azure mapping with links to Azure docs.

These pages cover the generic cross-cloud vocabulary (VPC vs VNet, IAM roles vs
RBAC roles, S3 vs Blob Storage vs Cloud Storage, etc.) far better than we could
maintain ourselves.

#### Campus-specific terms (not provider-specific)

| Term | Description |
|---|---|
| **Allowed Regions** | Campus Cloud restricts resources to specific US regions: AWS (us-east-1, us-west-2), Azure (West US 2, West Central US), GCP (us-central1, us-west1). |
| **Availability Level (A1–A4)** | Optional classification of how critical uptime is for your resources. |
| **Baseline** | The standard security configuration automatically applied to every new workspace — includes audit logging, guardrails, budget alerts, and network connectivity. |
| **Campus Cloud Account** | The Cloud Team's general term for your workspace, regardless of provider. Formally an AWS Account, Azure Subscription, or GCP Project. |
| **Campus SSO** | How you sign in with your UCSB credentials — no separate cloud password needed. AWS uses Shibboleth (SAML); Azure and GCP use Entra ID federation. |
| **CUI (Controlled Unclassified Information)** | Sensitive federal research data requiring specific protection controls (e.g., export-controlled, defense-related). |
| **Data Management Plan (DMP)** | Required documentation for research data — describes handling, retention, sharing, and archiving. Use UC's DMPTool to create one. |
| **Essential Contacts** | Email addresses that receive cloud notifications (billing alerts, security warnings, suspension notices). GCP's official term; AWS uses SNS topics, Azure uses Action Groups. |
| **FAU (Fund Account Unit)** | UCSB financial tracking code. Can be tagged on resources for cost breakdown. |
| **Functional Email** | A shared group email address (e.g., dept-cloud@ucsb.edu) — preferred over personal email for account contacts so access survives staff changes. |
| **Gateway** | UCSB's procurement portal (gateway.procurement.ucsb.edu) where you create requisitions for cloud accounts. |
| **Guardrails** | High-level governance rules enforced across all providers. Expressed in plain language; implemented differently in each cloud. AWS now officially calls these "controls." |
| **Landing Zone** | The secure, pre-configured multi-account environment the Cloud Team maintains. Each provider has its own implementation (AWS Control Tower, Azure CAF Enterprise Scale, GCP custom Terraform), but the concept is the same. |
| **Namespace** | *(define — currently undefined in the existing glossary)* |
| **NIST 800-171** | Federal security standard for Controlled Unclassified Information (CUI). Accounts handling CUI are placed in a dedicated OU/folder with additional guardrails. |
| **Prisma Cloud** | Palo Alto Networks security platform the Cloud Team uses for unified compliance and security monitoring across all three cloud providers. |
| **Protection Level (P1–P4)** | Data sensitivity classification. P1 = public, P2 = internal, P3 = sensitive (PII/FERPA), P4 = regulated (HIPAA/CUI). Determines which guardrails apply. |
| **Purchase Order (PO)** | Funding authorization obtained through the UCSB Gateway procurement system. Required before your workspace can be created. |
| **Quarantine** | When the Cloud Team isolates a compromised or decommissioned workspace — network access is cut and credentials are disabled. Contact the Cloud Team to request restoration. |
| **Recovery Level (R1–R4)** | Optional classification of backup and disaster-recovery requirements. |
| **Service Catalog** | A curated set of pre-approved, pre-configured cloud products you can deploy yourself (VPCs, budgets, IAM roles, etc.). Available in AWS; similar patterns in Azure and GCP. |
| **Shared Responsibility Model** | The cloud provider secures the infrastructure; you secure your data, access, and configurations. Each provider frames this differently — see their docs — but the principle is the same everywhere. |
| **Tags / Labels** | Key-value pairs attached to resources for billing, ownership, and compliance tracking. AWS and Azure call them Tags; GCP calls them Labels. See the [tagging page](/docs/general/tagging/) for required Campus Cloud tags. |
| **UC Enterprise Discount** | System-wide pricing agreements with each cloud provider (AWS EDP, Azure EA, GCP negotiated). You benefit automatically. |
| **UC Policy IS-3** | University of California information security policy mandating data classification and protection controls. |

### 5b. `general/cost-models.md` — NEW (replaces empty stub)

Outline:
- Cloud pricing fundamentals (pay-as-you-go, reserved/committed, spot/preemptible)
- AWS pricing: On-Demand, Reserved Instances, Savings Plans, Spot
- Azure pricing: Pay-As-You-Go, Reserved Instances, Azure Hybrid Benefit
- GCP pricing: On-Demand, Committed Use Discounts (CUDs), Sustained Use Discounts, Preemptible/Spot VMs
- UC Enterprise Discount Programs (AWS EDP, Azure EA, GCP negotiated)
- Cost calculators: [AWS](https://calculator.aws/), [Azure](https://azure.microsoft.com/en-us/pricing/calculator/), [GCP](https://cloud.google.com/products/calculator)
- Baseline costs: audit/compliance/security tooling in every account

### 5c. `general/tagging.md` — MERGE & Expand

Merge `guidelines/tagging.md` (comprehensive vocabulary) with `bestpractices/tagging.md`
(namespace definitions). Add:
- Side-by-side comparison of required tags across all 3 providers
- Azure required tags from policy (po-number, environment, mission, protection-level, availability-level)
- GCP Resource Manager tags (9 keys, 530+ values)
- Tag enforcement mechanisms per provider (AWS tag policies, Azure Policy deny, GCP org policy)

### 5d. `general/security-overview.md` — NEW

Outline:
- Shared Responsibility Model — concept is universal; implementation differs
  - AWS: "Security OF the cloud" vs "Security IN the cloud"
  - Azure: Microsoft vs Customer responsibility matrix
  - GCP: Google vs Customer shared fate model
- Data classification: P1 (public) → P4 (restricted/regulated)
- Availability levels: A1 → A4
- Recovery levels: R1 → R4
- How classification drives which guardrails apply to your account/project/subscription
- How to report a security concern
- Links to each provider's security page

### 5e. `general/iam-overview.md` — NEW

Outline:
- How you log in to each provider:
  - AWS: UCSB SSO → AWS IAM Identity Center
  - Azure: UCSB Entra ID → Azure RBAC
  - GCP: UCSB Entra ID → Google Workspace groups
- What roles are available to you in each provider
- How to request access for team members
- Least-privilege principles — request only what you need

### 5f. `pages/getting-started.md` — Updates Needed

- Add GCP training resources:
  - [Google Cloud Skills Boost](https://www.cloudskillsboost.google/)
  - [Google Cloud Certifications](https://cloud.google.com/learn/certification)
- Add GCP Cost Calculator: https://cloud.google.com/products/calculator
- Update "coming soon" language for GCP — it's live now
- Replace broken/long Azure pricing calculator URL
- Add Entra ID context for Azure/GCP SSO

### 5g. `pages/about.md` — Minor Updates

- Mention Google Cloud Platform alongside AWS and Azure explicitly
- Update CSP descriptions with current service counts/capabilities

---

## 6. Staleness Audit

Items that need date/version verification:

| File | Issue | Action |
|---|---|---|
| `guidelines/guardrails.aws.md` | Guardrail list dated "Feb 9, 2023" | Update to current Control Tower guardrails |
| `guidelines/guardrails.azure.md` | Policy list dated "Dec 2020" | Update to match current `core/lib/` policies |
| `guidelines/description.md` | Says "20+ AWS regions" | Now 30+; update |
| `bestpractices/servicecatalog.md` | Deprecation notice from June 2024 | Verify current product list against repo |
| `pages/getting-started.md` | GCP described as "coming soon" | GCP is live; update language |
| `pages/getting-started.md` | AWS Simple Monthly Calculator link | Deprecated by AWS; remove |
| `pages/glossary.md` | All definitions are AWS-only bullet points | Replace with cross-cloud concept-mapping table (see §5a) |
| `guidelines/compliance.md` | Spreadsheet links may be stale | Verify all external links |

---

## 7. Navigation & Site Structure Updates

When reorganizing, update these files:

- `_data/navigation.yml` — restructure for provider-centric layout
- `_data/toc.yml` — restructure TOC to match new directory layout
- `pages/docs.md` — update hub links

Suggested navigation:

```yaml
- title: Getting Started
  url: /getting-started/

- title: General Guidance
  sublinks:
    - title: Security Overview
      url: /docs/general/security-overview/
    - title: IAM & Identity
      url: /docs/general/iam-overview/
    - title: Tagging
      url: /docs/general/tagging/
    - title: Compliance
      url: /docs/general/compliance/
    - title: Cost Models
      url: /docs/general/cost-models/
    - title: Research
      url: /docs/general/research/
    - title: Data Management Plans
      url: /docs/general/dmp/
    - title: Migrate to Campus Cloud
      url: /docs/general/migrate/
    - title: Close an Account
      url: /docs/general/close-account/

- title: Amazon Web Services (AWS)
  sublinks:
    - title: Overview
      url: /docs/aws/overview/
    - title: First Steps
      url: /docs/aws/first-steps/
    - title: Networking
      url: /docs/aws/networking/
    - title: Guardrails
      url: /docs/aws/guardrails/
    - title: Security
      url: /docs/aws/security/
    - title: Service Catalog
      url: /docs/aws/service-catalog/
    - title: Contacts
      url: /docs/aws/contacts/
    - title: VPN Troubleshooting
      url: /docs/aws/vpn/
    - title: QuickSight Dashboards
      url: /docs/aws/quicksight/

- title: Microsoft Azure
  sublinks:
    - title: Overview
      url: /docs/azure/overview/
    - title: First Steps
      url: /docs/azure/first-steps/
    - title: Networking
      url: /docs/azure/networking/
    - title: Guardrails & Policies
      url: /docs/azure/guardrails/
    - title: Security
      url: /docs/azure/security/
    - title: Custom RBAC Roles
      url: /docs/azure/custom-roles/
    - title: Contacts
      url: /docs/azure/contacts/
    - title: Cost Management
      url: /docs/azure/cost-management/

- title: Google Cloud Platform (GCP)
  sublinks:
    - title: Overview
      url: /docs/gcp/overview/
    - title: First Steps
      url: /docs/gcp/first-steps/
    - title: Networking
      url: /docs/gcp/networking/
    - title: Guardrails & Org Policies
      url: /docs/gcp/guardrails/
    - title: Security & Audit
      url: /docs/gcp/security/
    - title: Tagging & Labels
      url: /docs/gcp/tagging/
    - title: Billing & Cost Attribution
      url: /docs/gcp/billing/
    - title: Contacts
      url: /docs/gcp/contacts/

- title: Glossary
  url: /glossary/
```

---

## 8. Priority Order

Suggested implementation sequence:

1. **Quick wins** — Fix stale dates, remove empty stubs, merge duplicate tagging files
2. **GCP documentation** — Richest repo docs to draw from; biggest public-facing gap
3. **Azure documentation** — Infrastructure is deployed; docs need to be written
4. **AWS updates** — Update guardrails, SCP documentation, service catalog list
5. **Cross-cutting pages** — Glossary expansion, cost models, security overview, IAM overview
6. **Restructure** — Move files into provider-centric layout, update navigation
7. **Pages updates** — Getting started, about page, docs hub

> Steps 1–5 can proceed in the current directory structure. Step 6 (restructure)
> should be a single coordinated change that updates files, navigation, and
> permalinks together to avoid broken links.
