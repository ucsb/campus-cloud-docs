---
title: AWS Guardrails & SCPs
description: Service Control Policies and Control Tower controls applied to all Campus Cloud AWS accounts.
permalink: /docs/aws/guardrails
last_reviewed: 2026-03-30
---

## AWS Guardrails

UCSB Campus Cloud enforces guardrails — automatic restrictions that keep every
AWS account aligned with university security policy
([UC IS-3](https://security.ucop.edu/policies/institutional-information-and-it-resource-classification.html))
and the federal
[NIST 800-171]({{ site.baseurl }}/glossary#nist-800-171) standard for
protecting sensitive research data.

Guardrails are designed to maintain a safe, compliant baseline without getting
in the way of normal cloud usage. You will only notice them if you attempt
something outside that baseline. The sections below describe what is and is not
allowed.

---

## Region Restriction

**All resources must be created in us-east-1 or us-west-2.**

Attempts to create resources in any other region will return an `Access Denied`
error from the SCP. This applies to EC2, S3, RDS, Lambda, and most other
services.

**Exceptions:** AWS global services (IAM, Route 53, STS, CloudFront, WAF) are
not region-specific and are always available.

---

## EC2 Instance Metadata

**IMDSv2 (Instance Metadata Service v2) is required on all EC2 instances.**

IMDSv1 is disabled by SCP. If your application or AMI relies on IMDSv1 calls,
update it to use IMDSv2 before launching in Campus Cloud. The AWS SDKs (v2+)
and recent Amazon Linux AMIs support IMDSv2 by default.

Attempting to launch an EC2 instance with `optional` or `disabled` IMDSv2
will fail with an `Access Denied` error.

---

## Root Account Activity

**Direct root account use is blocked by SCP.**

The root credentials for your account exist but are protected. Normal
operations should always use federated IAM roles. If you believe you need root
access for a specific task, contact the Cloud Team — most root-only tasks can
be performed by the organization management account instead.

---

## Amazon Bedrock (Generative AI)

**Amazon Bedrock is available in us-east-1, us-west-2, and also us-east-2.**

Bedrock works in both standard allowed regions (us-east-1 and us-west-2). An
additional SCP exception allows Bedrock API calls in **us-east-2** (Ohio) for
models that are not available in the standard regions. All other services remain
blocked in us-east-2.

---

## What You Can and Cannot Do

### You Can
* Create and manage resources in us-east-1 and us-west-2
* Create IAM roles and policies (subject to permission boundaries set by Control Tower)
* Manage Security Groups, NACLs, and VPC configuration within your account
* Enable any AWS service not explicitly restricted
* Configure budget alarms and billing preferences

### You Cannot
* Create resources outside us-east-1 / us-west-2
* Disable AWS CloudTrail (org-level trail is read-only)
* Disable AWS Config
* Use IMDSv1 on EC2 instances
* Act as root without Cloud Team assistance
* Modify or delete the default IAM roles created by the Cloud Team
* Detach your account from the AWS Organization

---

## Compliance Controls (NIST Accounts)

Accounts in the Research OU with NIST 800-171 requirements have additional
controls applied automatically by Control Tower:

* Mandatory MFA for console access
* S3 bucket public-access block enforced
* EBS/RDS/S3 encryption at rest enforced
* VPC Flow Logs enabled
* GuardDuty enabled

See [Compliance](docs/general/compliance) for more information on requesting a
NIST-baseline account.

---

## Getting an Exception

If a guardrail blocks something you believe is legitimate, open a [ServiceNow
ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5). Explain the use case and the specific SCP or control that is blocking
you. The Cloud Team will evaluate the request and, if appropriate, grant a
targeted exception or suggest an alternative approach.

Exceptions are never granted for controls required by UC IS-3 or NIST 800-171.
