---
title: AWS Security
description: Security monitoring, audit logging, and threat detection in Campus Cloud AWS accounts.
permalink: /docs/aws/security
last_reviewed: 2026-03-30
---

## AWS Security

Every Campus Cloud AWS account comes with security tools already turned on.
You don't need to set any of this up — it's ready when your account is
provisioned. The main tools are **CloudTrail** (audit logging),
**Security Hub** (security checks), **GuardDuty** (threat detection), and
**AWS Config** (compliance rules).

---

## AWS CloudTrail

[CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
records every action taken in your account — who did what, when, and from where.

* **Always on** — CloudTrail cannot be turned off in Campus Cloud accounts.
* **Centralized** — Logs are stored in a secure archive managed by the Cloud
  Team.

You can create additional trails for specific needs (e.g., logging data access
to S3 buckets), but you cannot modify or delete the organization-wide trail.

---

## AWS Security Hub

[Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)
checks your account's resources against security best practices and compliance
standards (including NIST 800-53). It gives you a single dashboard showing
what needs attention.

### Reviewing Findings

1. Open **Security Hub → Findings** in the AWS console.
2. Filter by severity — start with Critical and High.
3. Click a finding to see which resource is affected and how to fix it.

Address Critical and High findings promptly. The Cloud Team may follow up if
they remain unresolved.

For details, see the
[AWS Security Hub User Guide](https://docs.aws.amazon.com/securityhub/latest/userguide/).

---

## Amazon GuardDuty

[GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)
watches for suspicious activity in your account — things like unusual API calls,
potentially compromised instances, or unexpected network traffic.

* GuardDuty is always on and managed at the organization level.
* Findings are automatically forwarded to the Cloud Team.
* You can also view your findings in the GuardDuty console.

For details, see the
[Amazon GuardDuty User Guide](https://docs.aws.amazon.com/guardduty/latest/ug/).

---

## AWS Config

[AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)
tracks changes to your resources and checks them against compliance rules. The
following rules are active in all Campus Cloud accounts:

| Rule | What It Checks |
|---|---|
| S3 encryption | S3 buckets have encryption enabled |
| EFS encryption | EFS file systems are encrypted |
| No admin IAM policies | IAM policies don't grant unrestricted admin access |
| CloudWatch log encryption | Log Groups are encrypted |
| VPC Flow Logs | Network traffic logging is enabled |
| S3 access logging | S3 bucket access is logged |
| Unused credentials | Flags IAM credentials unused for 180+ days |
| Access key rotation | Flags access keys older than 365 days |
| Password policy | Account password policy meets minimum standards |
| Redshift encryption & TLS | Redshift clusters use encryption and TLS |

Resources that don't meet these rules show up as findings in Security Hub.

---

## Automated Security Alarms

The Cloud Team monitors automated alarms that detect critical account-level
events, including:

* Unauthorized API calls
* Console sign-in without MFA
* Root account usage
* IAM policy changes
* CloudTrail configuration changes
* Security group changes

These alarms are based on the
[CIS AWS Foundations Benchmark](https://docs.aws.amazon.com/securityhub/latest/userguide/cis-aws-foundations-benchmark.html)
and are managed centrally — no action is needed on your part.

---

## IAM Access Analyzer

[IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)
is enabled on every Campus Cloud account. It checks whether any of your
resources (S3 buckets, IAM roles, etc.) are accidentally shared with external
accounts or the public.

---

## Security Notifications (Optional)

You can set up email notifications when resources in your account fall out of
compliance. The **Local Security Notifications** product in the
[Service Catalog](/docs/aws/service-catalog) creates an email subscription that
alerts you to AWS Config compliance changes.

This is optional but recommended so your team is aware of issues as they arise.

---

## Wiz Cloud Security Posture Management

Wiz is available across all Campus Cloud platforms (AWS, Azure, GCP). See
[Security & Shared Responsibility — Wiz](/docs/general/security#wiz-cloud-security-posture-management)
for details.

---

## Incident Response

Follow the general
[incident response steps](/docs/general/security#reporting-a-security-incident)
for all suspected security events. The section below covers AWS-specific
emergency actions.

### Emergency Isolation

If an EC2 instance is actively compromised and you need to stop the attack:

* Replace the instance's **Security Group** with one that denies all inbound and
  outbound traffic while preserving the instance for forensics.
* Do **not** terminate or stop the instance — forensic snapshots of the EBS
  volumes may be needed.
* If a compromised IAM user or role is involved, attach a **deny-all inline
  policy** to the entity rather than deleting it, to preserve CloudTrail
  attribution.

For guardrails and service control policies applied to your account, see
[Guardrails & SCPs](/docs/aws/guardrails).
