---
title: Compliance & Governance
description: NIST 800-171, UC IS-3, and how to request a compliant account
permalink: /docs/general/compliance
last_reviewed: 2026-03-30
---

## Compliance & Governance

The Campus Cloud is designed to align with two key standards:

* **[UC Policy IS-3](https://security.ucop.edu/policies/it-policies.html)** —
  University of California information security policy. All Campus Cloud
  accounts must comply.
* **[NIST 800-171 Rev 2](https://csrc.nist.gov/publications/detail/sp/800-171/rev-2/final)** —
  federal standard for protecting Controlled Unclassified Information (CUI).
  Required to receive federal research funding involving sensitive data.

---

## Compliance Built Into Every Account

Every Campus Cloud account gets a baseline set of controls at creation:

* Audit logging of all API calls and console actions
* Detection controls for common misconfigurations (unencrypted storage,
  public access, missing MFA)
* Security monitoring via provider-native tools (Security Hub, Defender for
  Cloud, Security Command Center)
* Guardrails that prevent high-risk actions (deploying outside allowed regions,
  disabling audit logging, using root credentials)

These controls satisfy a significant portion of IS-3 and NIST 800-171
requirements, but they do not cover everything. You are responsible for the
remaining controls that depend on your specific workloads and processes.

---

## Do You Need a NIST 800-171 Compliant Account?

If your research involves Controlled Unclassified Information (CUI) — such as
federally funded research with export controls, or data subject to ITAR, HIPAA,
or similar frameworks — you should request a NIST-compliant account.

This applies to **all three providers**. The request process is the same:
follow the standard [procurement process](/getting-started/procurement)
and select **"NIST Compliant Account"** on the Campus Cloud form.

A NIST-compliant account is placed in an Organizational Unit (AWS), Management
Group (Azure), or Folder (GCP) with additional controls enabled:

* Additional detective controls check encryption, access, and network configuration
* Additional preventive controls block non-compliant configurations
* Regular automated compliance reports are available on request

### Migrating an Existing Account to NIST-Compliant

If you already have a Campus Cloud account that is not in the NIST-compliant
tier, you have two options:

1. **Migrate your account** to the NIST-compliant OU/folder. The Cloud Team
   can help with this process.
2. **Enable additional controls** on your existing account to increase
   compliance coverage.

Open a [ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5) or email
[info@cloud.ucsb.edu](mailto:info@cloud.ucsb.edu) to discuss your options.

---

## Compliance Tracking Tool

The Cloud Team has developed a NIST 800-171 Controls Evaluation Spreadsheet that
maps each NIST requirement to controls available in the Campus Cloud. It
documents what the Campus Cloud Landing Zone provides, what local controls you own, and
provides progress tracking with color-coded dashboards.

To request a copy: [info@cloud.ucsb.edu](mailto:info@cloud.ucsb.edu)

---

## Cross-Provider Security Monitoring

Each provider's security monitoring tools send findings to consolidated views:

* **AWS:** Security Hub aggregates GuardDuty, Config, and other findings.
  Prisma Cloud integration may be available — contact the Cloud Team for
  current status.
* **Azure:** Microsoft Defender for Cloud provides the unified security posture.
* **GCP:** Security Command Center provides organization-wide findings.

---

## Account Compliance Requirements

Regardless of account type, every Campus Cloud account must:

1. Have the root/admin password secured and MFA enabled
2. Have valid alternate contacts (billing, security, operations)
3. Apply data classification tags to resources
4. Use the account only for UCSB business purposes in accordance with UC IS-3

For provider-specific controls, see:
[AWS Guardrails](/docs/aws/guardrails) ·
[Azure Guardrails](/docs/azure/guardrails) ·
[GCP Guardrails](/docs/gcp/guardrails)
