# Campus Cloud Documentation — Redesign Plan

> **Last updated:** 2026-03-30
>
> Cross-references the live landing zone repos (`campus-cloud-aws-landing-zone`,
> `campus-cloud-azure-landing-zone`, `campus-cloud-gcp-landing-zone`) against
> the current docs site at docs.cloud.ucsb.edu.

---

## Executive Summary

The current site has three problems:

1. **It's AWS-only in practice.** Azure has an 8-line stub. GCP says "coming
   soon" — but GCP has been live for over a year with 200+ managed resources.
2. **The information architecture doesn't match how people think.** Splitting
   content into "Guidelines," "Best Practices," and "First Steps" forces users
   to hunt across folders for related information. A researcher setting up a
   new AWS account needs to check at least four different pages.
3. **Much of the content is stale.** The AWS guardrails page is dated Feb 2023.
   The Azure guardrails are from Dec 2020. Links to the AWS Simple Monthly
   Calculator (deprecated) are still present.

The fix: reorganize around **what users need to do**, with parallel structure
across all three cloud providers, written in plain language for the campus
community.

---

## Design Principles

These should guide every page on the site:

1. **Write for researchers and faculty, not engineers.** No one comes to this
   site to learn about Transit Gateways. They come to figure out how to get a
   cloud account and start using it.

2. **Answer one question per page.** "How do I log in?" "What's enforced in my
   account?" "How do I manage costs?" Each page should have a clear purpose a
   user can identify in 5 seconds.

3. **Same structure for every provider.** If AWS has a networking page, Azure
   and GCP should too. Parallel structure makes it obvious where to look and
   makes gaps visible.

4. **Short pages that link out.** A 2,000-word guardrails page is better than
   a 200-word one, but a 500-word page that links to the relevant console
   screens is better than both.

5. **Use "you" and active voice.** "You'll sign in with your UCSB credentials"
   beats "The Campus Cloud team has configured new accounts to use campus
   single sign on for user authentication."

6. **Keep it current or remove it.** Outdated docs are worse than no docs.
   Every page should show a last-reviewed date.

---

## Style & Tone

Match the voice of [it.ucsb.edu](https://it.ucsb.edu/): professional,
welcoming, action-oriented. Short paragraphs. Bullet points for steps. Tables
for comparisons. Avoid jargon; when a technical term is necessary, link to the
glossary or explain it inline.

**Good:** "Your account comes with four pre-configured roles. You manage
who gets each role through the UCSB Identity Manager at im.ucsb.edu."

**Bad:** "The Campus Cloud team has configured new accounts to use campus
single sign on for user authentication and a mapping of identity groups to
AWS Roles for authorization."

---

## Proposed Site Structure

### Top-level pages (in `pages/`)

| Page | Purpose |
|---|---|
| **Home** (`index.md`) | One-paragraph welcome, quick links to each provider + Getting Started |
| **About** (`about.md`) | What cloud computing is, why UCSB offers managed cloud, who it's for |
| **Getting Started** (`getting-started.md`) | Training → budgeting → procurement → what happens next |
| **Glossary** (`glossary.md`) | Campus-specific terms + links to provider glossaries |

### Documentation (in `docs/`)

```
docs/
  general/                 # Applies to all three providers
    security.md            # Shared responsibility, data classification, reporting incidents
    identity.md            # How you sign in, how roles work, adding team members
    tagging.md             # Required tags across all providers, why they matter
    compliance.md          # NIST 800-171, UC IS-3, how to request a compliant account
    cost-management.md     # Pricing models, UC discounts, cost calculators, baseline costs
    research.md            # Cloud for research, ARA credits, Cloud Team consulting
    data-management.md     # DMP guidelines, DMPTool, archiving requirements
    migrate.md             # Migrating personal/free accounts to Campus Cloud
    close-account.md       # How to close an account (process + warnings)

  aws/
    index.md               # AWS overview: what you get, how it's organized
    first-steps.md         # Sign in, set up budget, verify security, create VPC, add users
    networking.md          # VPC options, campus connectivity, NAT IPs, address space
    guardrails.md          # What's enforced, what happens if you violate a rule
    service-catalog.md     # Self-service products: VPC, budget, roles, notifications
    contacts.md            # Account contacts setup (what's automatic, what you configure)
    vpn.md                 # VPN troubleshooting
    quicksight.md          # Accessing cost/usage dashboards
    account-request.md     # Why @ucsb.edu accounts must be in the Landing Zone

  azure/
    index.md               # Azure overview: subscriptions, management groups, what you get
    first-steps.md         # Sign in, budget alerts, security check, network, support plan
    networking.md          # Virtual WAN, VPN, requesting a VNet
    guardrails.md          # Azure Policy enforcement, required tags, NIST compliance
    security.md            # Defender for Cloud, logging, compliance status
    roles.md               # Four custom RBAC roles and what they can do
    contacts.md            # Setting up contacts for your subscription

  gcp/
    index.md               # GCP overview: org/folder/project hierarchy, what you get
    first-steps.md         # Sign in, budget alerts, SCC findings, IAM, support plan
    networking.md          # VPC restrictions, allowed regions, requesting network resources
    guardrails.md          # Org policies, what you can/can't do, NIST mapping
    security.md            # Audit logging, SCC, identity restrictions, quarantine
    tagging.md             # Tags you manage vs tags the Cloud Team sets
    billing.md             # Sub-accounts, budget alerts, billing limits, cost reports
    contacts.md            # Essential contacts and notification setup
```

### What gets removed

| Current file | Disposition |
|---|---|
| `guidelines/description.md` | Split → `aws/index.md` (AWS content), `azure/index.md`, `gcp/index.md` |
| `guidelines/servicecatalog.md` | Delete (empty stub; real content in `bestpractices/servicecatalog.md`) |
| `bestpractices/costmodels.md` | Delete (empty, just says "Cost Models") → `general/cost-management.md` |
| `bestpractices/tagging.md` | Merge into `general/tagging.md` |
| `guidelines/tagging.md` | Merge into `general/tagging.md` |
| `firststeps/index.md` | Remove (replaced by provider index pages) |
| `bestpractices/index.md` | Remove (replaced by navigation) |
| `guidelines/index.md` | Remove (replaced by navigation) |

---

## Page-by-Page Specifications

For each page, Author Source notes point doc writers to the relevant repo
files — these references are for authors, not for publication.

### Home (index.md)

Rewrite completely. Current version buries the lead with a features list.

New structure:
- One sentence: what the Campus Cloud is
- Three cards/links: AWS | Azure | GCP — each with a one-line description
- "New here? Start with [Getting Started]"
- Contact: info@cloud.ucsb.edu / ServiceNow

### About (about.md)

Lightly edit. The current cloud computing explainer is solid. Add:
- Mention GCP alongside AWS and Azure
- Brief note on UC enterprise agreements

### Getting Started (getting-started.md)

Update existing page:
- Fix "coming soon" → GCP is live
- Remove deprecated AWS Simple Monthly Calculator link
- Replace broken Azure pricing calculator URL with clean link
- Add GCP training resources (Cloud Skills Boost, certifications)
- Add GCP cost calculator link
- Update SSO/identity language to mention Entra ID for Azure/GCP

### Glossary (glossary.md)

Replace current 6 AWS-centric bullet points with:

**Section 1: External references** — for cross-cloud vocabulary, link to
authoritative sources that stay current without our maintenance:
- [AWS Glossary](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html)
- [Google: AWS ↔ Azure ↔ GCP service comparison](https://cloud.google.com/docs/get-started/aws-azure-gcp-service-comparison)
- [Microsoft: AWS ↔ Azure service comparison](https://learn.microsoft.com/en-us/azure/architecture/aws-professional/services)

**Section 2: Campus Cloud terms** — only terms unique to UCSB or that need
campus-specific definitions. Alphabetized table:

| Term | Definition |
|---|---|
| Allowed Regions | US regions where you can deploy: AWS (us-east-1, us-west-2), Azure (West US 2, West Central US), GCP (us-central1, us-west1). |
| Availability Level (A1–A4) | How critical uptime is for your resources. |
| Baseline | Standard security configuration applied to every new account — audit logging, guardrails, budget alerts, network connectivity. |
| Campus Cloud Account | General term for your cloud workspace. AWS calls it an Account, Azure a Subscription, GCP a Project. |
| Campus SSO | Sign in with your UCSB NetID. AWS uses Shibboleth SAML; Azure and GCP use Entra ID federation. |
| CUI | Controlled Unclassified Information — sensitive federal research data requiring extra protections. |
| Data Management Plan (DMP) | Required research documentation. Use UC's [DMPTool](https://dmptool.org/) to create one. |
| Essential Contacts | Emails that receive billing alerts, security warnings, and suspension notices. |
| FAU | Fund Account Unit — UCSB financial tracking code for cost breakdown. |
| Functional Email | Shared group address (e.g., dept-cloud@ucsb.edu) — preferred over personal email so access survives staff changes. |
| Gateway | UCSB procurement portal ([gateway.procurement.ucsb.edu](https://gateway.procurement.ucsb.edu)) for requisitions. |
| Guardrails | Governance rules enforced across all providers. AWS officially calls them "controls." |
| Landing Zone | The secure, managed multi-account environment the Cloud Team maintains for each provider. |
| NIST 800-171 | Federal security standard for CUI. Accounts handling CUI get additional guardrails. |
| Protection Level (P1–P4) | Data sensitivity: P1 = public, P2 = internal, P3 = sensitive (PII/FERPA), P4 = regulated (HIPAA/CUI). |
| Purchase Order (PO) | Funding authorization from UCSB Gateway. Required before creating an account. |
| Quarantine | When the Cloud Team isolates a compromised account — network cut, credentials disabled. |
| Recovery Level (R1–R4) | Backup and disaster-recovery requirements. |
| Service Catalog | Pre-approved cloud products you can deploy yourself (VPCs, budgets, roles). Currently in AWS. |
| Tags / Labels | Key-value pairs for billing, ownership, and compliance tracking. AWS/Azure say Tags; GCP says Labels. |
| UC Enterprise Discount | System-wide pricing (AWS EDP, Azure EA, GCP negotiated). You benefit automatically. |
| UC Policy IS-3 | University of California information security policy requiring data classification and protection. |

---

### General Pages

#### general/security.md — Security & Shared Responsibility

> *Author source:* AWS shared responsibility model, Azure `platform/management/`,
> GCP `org-audit.tf`, `org-iam.tf`

- Shared Responsibility Model: the cloud provider secures infrastructure; you
  secure your data, access, and configurations
- Data classification levels (P1–P4) and what each means
- Availability (A1–A4) and Recovery (R1–R4) levels
- How classification determines which guardrails apply
- How to report a security incident
- Links to each provider's security page for details

#### general/identity.md — Identity & Access

> *Author source:* AWS `templates/identity/`, Azure `custom-iam-roles/`,
> GCP `org-iam.tf`

- AWS: Sign in at aws.cloud.ucsb.edu → Shibboleth SSO → four default roles
  (Administrator, PowerUser, ReadOnly, Billing)
- Azure: UCSB Entra ID → four custom RBAC roles (Subscription Owner,
  Application Owner, Network Ops, Security Ops)
- GCP: UCSB Entra ID → Google Workspace → IAM roles
- How to add/remove team members (im.ucsb.edu for AWS, Entra ID for Azure/GCP)
- Least-privilege principles

#### general/tagging.md — Tagging & Labels

> *Author source:* AWS `ucsb-org-tagging-compliance.json`, Azure
> `policy_definition_ucsb_resource_groups_without_required_tags.json`,
> GCP `tags.tf`

- Why tags matter (billing, compliance, operations)
- Required tags across all three providers — side-by-side table:

| Tag | AWS | Azure | GCP | Set by |
|---|---|---|---|---|
| PO Number | `ucsb:po-number` | `ucsb:po-number` | — | Cloud Team |
| Environment | `ucsb:environment` | `ucsb:environment` | `environment` | You |
| Mission | `ucsb:mission` | `ucsb:mission` | `mission` | You |
| Protection Level | `ucsb:protection-level` | `ucsb:protection-level` | `protection-level` | You |
| Availability Level | `ucsb:availability-level` | `ucsb:availability-level` | `availability-level` | You |
| Recovery Level | `ucsb:recovery-level` | — | `recovery-level` | You |
| Department | `ucsb:dept` | — | `dept` | You |
| Billing Limit | — | — | `billing-limit` | Cloud Team |
| Expiry Date | — | — | `expiry-date` | Cloud Team |

- What happens if you don't tag (AWS: compliance alert, Azure: deployment
  blocked for resource groups, GCP: audit)
- Namespace conventions (`ucsb:` prefix for AWS/Azure)

#### general/compliance.md — Compliance & Governance

Retain and update existing `guidelines/compliance.md`:
- NIST 800-171 and UC IS-3 overview
- How to request a NIST-compliant account
- Prisma Cloud monitoring (brief mention, cross-provider) — ⚠️ *confirm still active before publishing*
- Link to each provider's guardrails page for enforcement details
- AWS Config and Security Hub cost guidance

#### general/cost-management.md — Costs & Billing

> *Author source:* AWS Service Catalog budget product, Azure policies,
> GCP `billing-accounts.tf`

- Cloud pricing basics (on-demand, reserved/committed, spot/preemptible)
- UC Enterprise Discounts: AWS EDP, Azure EA, GCP negotiated
- Cost calculators: [AWS](https://calculator.aws/) |
  [Azure](https://azure.microsoft.com/en-us/pricing/calculator/) |
  [GCP](https://cloud.google.com/products/calculator)
- Baseline costs in every account (audit logging, security tooling)
- How to set up budget alerts (link to each provider's first-steps page)

#### general/research.md — Cloud for Research

Update existing `bestpractices/research.md`:
- Remove "see bottom of page" links (use direct links)
- Update language to address all three providers, not just AWS
- Keep ARA section, Cloud Team consulting, FAQ

#### general/data-management.md — Data Management Plans

Move existing `guidelines/dmp.md` with light edits:
- Clean up formatting
- Ensure links still work

#### general/migrate.md — Migrating to Campus Cloud

Move existing `guidelines/migrate.md` with light edits:
- Remove Google Earth Engine workaround note (issue resolved)
- Add note about GCP project migration path

#### general/close-account.md — Closing Your Account

Move existing `bestpractices/close.md`:
- Update to mention all three providers (not just AWS/Azure)
- GCP project decommission process

---

### AWS Pages

#### aws/index.md — AWS Overview

> *Author source:* `guidelines/description.md` (AWS sections), AWS LZ repo
> `README.md`, `foundation/` directory

- What a Campus Cloud AWS Account gives you
- How accounts are organized (Control Tower, OUs — in plain language)
- Supported regions: us-west-2 (Oregon, recommended), us-east-1 (N. Virginia)
- What's pre-configured: security baselines, logging, budget framework,
  network connectivity, SSO
- Link to Getting Started for procurement process

#### aws/first-steps.md — AWS First Steps

Update existing `firststeps/awsfirststeps.md`:
- Clean up language (active voice, "you" not "the Campus Cloud team has configured")
- Consolidate duplicate information about roles
- Update Security Hub guidance with current integrations
- Keep step-by-step structure: sign in → budget → verify security → contacts →
  VPC → add users → support

#### aws/networking.md — AWS Networking

Update existing `guidelines/networking.md`:
- Keep the good content (VPC families table, architecture diagram, traffic flow)
- Add: NAT Gateway IP addresses for firewall allowlisting
- Add: how to request address space (plain-language IPAM summary)
- Add: cross-cloud connectivity note (if your project spans multiple providers)

#### aws/guardrails.md — AWS Guardrails

> *Author source:* `foundation/policies/service-control-policies/`,
> Control Tower docs

Rewrite `guidelines/guardrails.aws.md`:
- Frame as "what's enforced in your account"
- Group by what users experience:
  - **You can't do:** use root credentials, deploy outside allowed regions,
    delete campus-managed resources, use IMDSv1
  - **Auto-remediation:** S3 encryption, EFS encryption, VPC flow logs,
    CloudWatch encryption, IAM admin-access detection
  - **Detective controls:** public access checks, encryption checks, MFA
    compliance
- Include Bedrock region exception and how to use it
- Remove Feb 2023 date; add last-reviewed date

#### aws/service-catalog.md — AWS Service Catalog

Update existing `bestpractices/servicecatalog.md`:
- Verify product list against `campus-cloud-aws-shared-sc` repo
- Current confirmed products: Simple VPC, Advanced VPC, Budget Notification,
  Security Notifications, IAM Role-to-Group, Effectual Budget, Instance
  Scheduler, SNS Topic
- Keep VPC families table (very useful)
- Clean up language

#### aws/contacts.md — AWS Account Contacts

Update existing `bestpractices/contacts.md`:
- Clarify which contacts Cloud Team pre-configures vs what you set up
- Emphasize functional email addresses over personal ones
- Update "root user" guidance to link to guardrails (root is locked)

#### aws/vpn.md — VPN Troubleshooting

Move existing `bestpractices/vpn.md`. Update to note that AWS campus connectivity
uses **two Direct Connect connections plus a VPN**. No equivalent page needed
for Azure or GCP (no campus direct connectivity for those providers).

#### aws/quicksight.md — QuickSight Dashboards

Move existing `guidelines/quicksight.dashboards.md` with minor cleanup.

#### aws/account-request.md — Account Request Restrictions

Move existing `guidelines/account-request.md` with minor cleanup.

---

### Azure Pages

All Azure pages are **new content**. The current site has only an 8-line stub.

#### azure/index.md — Azure Overview

> *Author source:* `core/main.tf`, `core/locals.tf`, `core/locals.ucsb-subscriptions.tf`

- What a Campus Cloud Azure Subscription gives you
- Management Group hierarchy (plain language — "your subscription is placed in
  a group that determines which policies apply")
- Subscription types: Legacy, Learning, Sponsorship, Baseline V1, Sandbox
- Supported regions: West US 2 (primary), West Central US (secondary)
- What's pre-configured: policies, logging, security monitoring, tagging
  enforcement, network connectivity
- Link to Getting Started for procurement process

#### azure/first-steps.md — Azure First Steps

> *Author source:* `core/locals.ucsb-subscriptions.tf`, `custom-iam-roles/`

- Sign in with your UCSB NetID (Entra ID)
- Available RBAC roles and what each can do (brief; link to roles.md for detail)
- Set up budget alerts via Azure Cost Management
- Check security posture in Microsoft Defender for Cloud
- Verify network connectivity
- Consider an Azure support plan for production services

#### azure/networking.md — Azure Networking

> *Author source:* `platform/archive-code/modules/connectivity/`, VPN configs

- Hub-spoke architecture via Virtual WAN
- Primary region: West US 2; secondary: West Central US
- Request a VNet for your subscription
- Network security: NSG flow logging enforced
- ⚠️ *Confirm whether Azure has campus VPN/ExpressRoute connectivity before publishing*

#### azure/guardrails.md — Azure Policies & Guardrails

> *Author source:* `core/lib/` policy definitions, archetype configurations

- What Azure Policy does and how it affects you
- Required tags on resource groups (5 tags; deployment blocked if missing)
- Security policies: no public blob storage, NSG flow logs deployed
  automatically, NIST 800-171 R2 audit
- Policies specifically not enforced (IP forwarding, RDP in some groups)
- How to check compliance in the Azure portal

#### azure/security.md — Azure Security

> *Author source:* `platform/management/`, Defender for Cloud configs

- Microsoft Defender for Cloud: what's monitored, how to view findings
- Centralized logging: Log Analytics workspace, 120-day retention
- NIST 800-171 compliance audit (what findings mean)
- Identity: Entra ID SSO

#### azure/roles.md — Azure Custom Roles

> *Author source:* `custom-iam-roles/` JSON definitions

- Four roles and what each can do:

| Role | Purpose | Key Restrictions |
|---|---|---|
| Subscription Owner | Full subscription control | No VPN/ExpressRoute management |
| Application Owner | App-level management | No auth writes, no networking, no Key Vault purge |
| Network Operations | Platform connectivity | VPN, ExpressRoute, route tables, NSGs |
| Security Operations | Security admin | Policies, roles, Key Vault purge, Defender |

- How to request a role assignment

#### azure/contacts.md — Azure Contacts

- Budget alerts via Azure Cost Management (you configure)
- Security alerts via Defender for Cloud
- Operational contacts: use functional email addresses

---

### GCP Pages

All GCP pages are **new content**. The current site has only an 8-line stub.

#### gcp/index.md — GCP Overview

> *Author source:* `docs/gcp-landing-zone.md`, `terraform/workspaces/ucsb-management/folder-structure.tf`

- What a Campus Cloud GCP Project gives you
- Organization → Folders → Projects hierarchy:
  - **UCSB NIST Baseline** — where most projects live
  - **Sandbox Unfunded** — for sandbox/unfunded projects ⚠️ *confirm folder exists and whether self-service creation is available*
  - **UCSB Legacy** — pre-existing projects with relaxed policies
  - **UCSB Quarantine-Disabled** — isolated compromised projects
- Identity: UCSB SSO via Entra ID federation to Google Workspace
- Supported regions: us-central1, us-west1
- What's pre-configured: org policies, audit logging, billing sub-account,
  required tags, security monitoring

#### gcp/first-steps.md — GCP First Steps

> *Author source:* `docs/gcp-scripts.md`, `docs/gcp-org-roles.md`

- Sign in with your UCSB credentials (Entra ID → Google Workspace)
- Your project is in the NIST Baseline folder by default
- What's already set up: billing, tags, audit logging, security policies
- Set up budget alerts
- Review Security Command Center findings
- Manage team access via IAM
- Google Cloud support plan options
- Training: Cloud Skills Boost, Google Cloud certifications

#### gcp/networking.md — GCP Networking

> *Author source:* `docs/gcp-guardrails.md` (networking), org-policies.tf

- You cannot create VPCs yourself — request from Cloud Team
- Custom-mode VPCs only (no auto-mode)
- No external IPs on VMs (use Cloud NAT or IAP)
- Internal load balancers only
- VPC flow logs, firewall logging, DNS logging required
- DNSSEC required on public DNS zones
- TLS 1.2+ required
- Available regions: us-central1 and us-west1 only
- Cross-cloud connectivity to campus, AWS, Azure

#### gcp/guardrails.md — GCP Organization Policies

> *Author source:* `docs/gcp-guardrails.md`, `org-policies.tf`,
> `org-deny-policies.tf`, `org-custom-constraints.tf`

Frame as "what you can and can't do":
- **Storage:** No public Cloud Storage buckets
- **Compute:** Shielded VMs, OS Login (no SSH keys in metadata), no external
  IPs, no IP forwarding
- **Identity:** Only @ucsb.edu accounts; no @gmail.com, no allUsers
- **Location:** us-central1 and us-west1 only
- **Audit:** Detailed logging for all services, automatically
- **Service accounts:** Keys being phased out org-wide (use Workload Identity)
- **What you can't change:** folder structure, billing assignments, org settings,
  VPCs, essential contacts

#### gcp/security.md — GCP Security & Audit

> *Author source:* `org-audit.tf`, `org-iam.tf`, `ucsb-core-vpc-sc.tf`

- All API calls and data access events logged automatically
- Audit logs stored centrally, immutable (you can't delete them)
- Security Command Center scans for misconfigurations
- Only @ucsb.edu accounts can be granted access
- No service account keys — use Workload Identity Federation
- What quarantine means and how to request restoration

#### gcp/tagging.md — GCP Tags

> *Author source:* `docs/gcp-tagging.md`, `tags.tf`

- **Tags the Cloud Team sets** (you can't change):
  - `expiry-date`, `billing-limit`, `wiz-scanning`
- **Tags you manage:**
  - `environment`, `mission`, `protection-level`, `availability-level`,
    `recovery-level`, `dept`
- How to view and update tags in the GCP Console

#### gcp/billing.md — GCP Billing & Cost Management

> *Author source:* `docs/gcp-billing-subaccounts.md`, `billing-accounts.tf`

- Billing sub-accounts per department
- View costs via the GCP Billing Account console
- Set up budget alerts
- Billing limit tags — what happens when you hit your cap

#### gcp/contacts.md — GCP Essential Contacts

> *Author source:* `docs/gcp-landing-zone.md`, `org-essential-contacts.tf`

- What notifications you'll receive (billing, security, suspension)
- Pre-configured contacts (set by Cloud Team, protected by policy)
- How to add project-level contacts
- Why contacts are protected from deletion

---

## Navigation

### _data/toc.yml

```yaml
- title: Documentation
  links:
    - title: Getting Started
      url: getting-started
    - title: General Guidance
      url: docs/general
      children:
        - title: Security & Shared Responsibility
          url: docs/general/security
        - title: Identity & Access
          url: docs/general/identity
        - title: Tagging & Labels
          url: docs/general/tagging
        - title: Compliance & Governance
          url: docs/general/compliance
        - title: Costs & Billing
          url: docs/general/cost-management
        - title: Cloud for Research
          url: docs/general/research
        - title: Data Management Plans
          url: docs/general/data-management
        - title: Migrate to Campus Cloud
          url: docs/general/migrate
        - title: Close an Account
          url: docs/general/close-account
    - title: Amazon Web Services (AWS)
      url: docs/aws
      children:
        - title: Overview
          url: docs/aws
        - title: First Steps
          url: docs/aws/first-steps
        - title: Networking
          url: docs/aws/networking
        - title: Guardrails
          url: docs/aws/guardrails
        - title: Service Catalog
          url: docs/aws/service-catalog
        - title: Account Contacts
          url: docs/aws/contacts
        - title: VPN Troubleshooting
          url: docs/aws/vpn
        - title: QuickSight Dashboards
          url: docs/aws/quicksight
        - title: Account Request Restrictions
          url: docs/aws/account-request
    - title: Microsoft Azure
      url: docs/azure
      children:
        - title: Overview
          url: docs/azure
        - title: First Steps
          url: docs/azure/first-steps
        - title: Networking
          url: docs/azure/networking
        - title: Guardrails & Policies
          url: docs/azure/guardrails
        - title: Security
          url: docs/azure/security
        - title: Custom RBAC Roles
          url: docs/azure/roles
        - title: Contacts
          url: docs/azure/contacts
    - title: Google Cloud Platform (GCP)
      url: docs/gcp
      children:
        - title: Overview
          url: docs/gcp
        - title: First Steps
          url: docs/gcp/first-steps
        - title: Networking
          url: docs/gcp/networking
        - title: Guardrails & Org Policies
          url: docs/gcp/guardrails
        - title: Security & Audit
          url: docs/gcp/security
        - title: Tags & Labels
          url: docs/gcp/tagging
        - title: Billing
          url: docs/gcp/billing
        - title: Contacts
          url: docs/gcp/contacts
    - title: Glossary
      url: glossary
```

### _data/navigation.yml

```yaml
- title: About
  url: about
- title: Getting Started
  url: getting-started
- title: AWS
  url: docs/aws
- title: Azure
  url: docs/azure
- title: GCP
  url: docs/gcp
```

---

## Staleness Fixes (Do First)

These are quick corrections to make before the restructure:

| Item | Fix |
|---|---|
| `getting-started.md`: "coming soon" for GCP | GCP is live — update language |
| `getting-started.md`: AWS Simple Monthly Calculator | Remove (deprecated by AWS) |
| `getting-started.md`: Azure pricing calculator URL | Replace with clean URL |
| `guardrails.aws.md`: "Feb 9, 2023" | Update to current Control Tower controls |
| `guardrails.azure.md`: "Dec 2020" | Update to current CAF policies |
| `description.md`: "20+ AWS regions" | Now 30+ |
| `glossary.md`: All AWS-only, "Namespace" undefined | Full rewrite per §Glossary above |
| `index.md`: No mention of GCP | Add GCP alongside AWS and Azure |
| `compliance.md`: Prisma Cloud cost info | Verify current guidance |

---

## Implementation Sequence

### Phase 1 — Quick Fixes (no restructure needed)
- Fix stale content listed above
- Update home page to mention GCP
- Update getting-started.md

### Phase 2 — Create New Directory Structure
- Create `docs/general/`, `docs/aws/`, `docs/azure/`, `docs/gcp/`
- Move existing content into new locations
- Update permalinks and navigation
- Test all links

### Phase 3 — Write New Content
- Azure: All 7 pages (biggest gap)
- GCP: All 8 pages (second biggest gap)
- General: security.md, identity.md, cost-management.md (new cross-cutting pages)

### Phase 4 — Update Existing Content
- AWS guardrails: rewrite with current controls
- AWS first-steps: clean up language
- AWS networking: add missing practical details
- Tagging: merge two pages, add cross-provider table
- Glossary: full rewrite

### Phase 5 — Polish
- Consistent formatting across all pages
- Add last-reviewed dates
- Verify all external links
- Remove old directory stubs and index pages

---

## Decisions & Follow-ups

### Confirmed

- **Procurement:** All three providers use the same Gateway PO process. Getting
  Started should describe one workflow and make clear it applies to AWS,
  Azure, and GCP equally.

- **GCP self-service:** The Vending Machine has not been deployed. All GCP
  projects are request-only via Gateway PO. Update `gcp/index.md` and
  `getting-started.md` accordingly — do not describe self-service project
  creation as available.

- **AWS networking:** AWS now has **two Direct Connect connections plus a VPN**.
  Update `aws/networking.md` to reflect this. There is no direct campus
  connectivity for Azure or GCP — remove the VPN troubleshooting page from
  the Azure and GCP nav (no equivalent page needed).

- **NIST-compliant accounts:** The request process (Gateway PO + "NIST Compliant
  Account" selection) applies to all three providers. Update `general/compliance.md`
  to confirm this parity.

- **Cost dashboards:** AWS uses QuickSight. GCP uses the native GCP Billing
  Account interface. Keep `aws/quicksight.md`. For GCP, document the
  GCP Billing console in `gcp/billing.md`.

- **Google Earth Engine:** The GEE project-creation issue has been resolved.
  Remove the open-issue note from `general/migrate.md`.

### Needs Follow-up Before Publishing

> ⚠️ **Theme/design:** Evaluate options that align with the UCSB brand
> guidelines at https://brand.ucsb.edu/tools-and-templates/websites before
> deciding whether to keep the current Docsy Jekyll theme or switch. This
> can be deferred until content is stable.

> ⚠️ **Azure active subscriptions:** Confirm the number of active subscriptions
> and any Azure-specific onboarding nuances before publishing `azure/index.md`.

> ⚠️ **Prisma Cloud:** Confirm whether Prisma Cloud is still actively used for
> cross-cloud monitoring before updating or removing the reference in
> `general/compliance.md`.

> ⚠️ **Azure cost dashboards:** Confirm the primary cost dashboard/tool for
> Azure subscriptions before publishing `azure/index.md` and
> `general/cost-management.md`.

> ⚠️ **Azure self-service:** Confirm whether Azure resource provisioning is
> entirely via ServiceNow tickets, or whether there is a self-service mechanism
> (equivalent to AWS Service Catalog), before publishing `azure/first-steps.md`.