---
title: AWS Guardrails & SCPs
description: Service Control Policies and Control Tower controls applied to all Campus Cloud AWS accounts.
permalink: /docs/aws/guardrails
last_reviewed: 2026-10-21
redirect_from:
  - /docs/guidelines/guardrails/aws
---

# AWS Guardrails

UCSB Campus Cloud enforces guardrails — automatic restrictions that keep every
AWS account aligned with university security policy
([UC IS-3](https://security.ucop.edu/policies/it-policies.html))
and the federal
[NIST 800-171]({{ "/glossary/" | relative_url }}) standard for
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
will fail with an `Access Denied` error. Additionally,
`ec2:ModifyInstanceMetadataOptions` is blocked entirely — you cannot change
metadata settings on a running instance.

---

## Root User

**Root credentials are managed centrally by the Cloud Team.** You don't sign
in as the root user, and creating root access keys is blocked. Use your
federated IAM roles for all normal work. If a task can only be done as the
root user, contact the Cloud Team and they will do it for you.

---

## Amazon Bedrock (Generative AI)

**In the two standard regions (us-east-1 and us-west-2), Bedrock works fully —
both the AWS Console and the API/CLI**, like any other allowed service.

An additional SCP exception allows **programmatic-only** Bedrock access in two
otherwise-blocked regions — **us-east-2** (Ohio) and **us-west-1**
(N. California) — for models that are not offered in the standard regions. In
these two regions:

* **Only the Bedrock model APIs work** — for example, invoking a model from the
  AWS SDK or CLI.
* **The Bedrock console will not work.** It depends on many other actions that
  remain blocked in us-east-2 and us-west-1, so you must call Bedrock
  programmatically there.
* All other AWS services remain blocked in these two regions.

---

## What You Can and Cannot Do

### You Can

* Create and manage resources in us-east-1 and us-west-2
* Create IAM roles and policies
* Manage Security Groups, NACLs, and VPC configuration within your account
* Enable any AWS service not explicitly restricted
* Configure budget alarms and billing preferences

### You Cannot

* Create resources outside us-east-1 / us-west-2
* Disable AWS CloudTrail (org-level trail is read-only)
* Modify or delete the Landing Zone AWS Config rules
* Use IMDSv1 on EC2 instances
* Act as root without Cloud Team assistance
* Modify or delete the Cloud Team's baseline resources (named `UCSB-BASELINE*`)
* Detach your account from the AWS Organization

---

## CloudFormation Checks

When you deploy with CloudFormation, Control Tower checks your templates before
creating resources. The deployment fails if a CloudWatch log group:

* is not encrypted with an AWS Key Management Service (KMS) key, or
* keeps logs for less than one year.

---

## Additional Controls in New and Imported Accounts

New and imported accounts are set up to align with NIST 800-171 (see
[Compliance]({{ "/docs/general/compliance" | relative_url }})). In these
accounts, Control Tower also **blocks** the actions below. Most people never
run into them:

* EC2 VM Import/Export
* The Amazon Elastic Block Store (EBS) direct APIs
* The older `RequestSpotFleet` and `RequestSpotInstances` APIs. Spot Instances
  still work through `RunInstances` and EC2 Fleet.
* Creating snapshots of unencrypted EBS volumes, attaching unencrypted volumes,
  and making EBS snapshots public
* Lambda function URLs that don't use IAM authentication
* Public AppSync GraphQL APIs
* KMS keys that use RSA-2048 for encryption and decryption, and the KMS
  key-policy lockout bypass flag (`BypassPolicyLockoutSafetyCheck`)
* Changes to S3 default encryption and S3 server access logging settings

Security Hub also checks these accounts against the **NIST SP 800-53 Rev. 5**
standard. It reports findings for things like SSH and other common ports open
to the internet, missing multi-factor authentication (MFA) on the root user or console users, unencrypted
storage, and public access to S3 buckets, snapshots, and other resources. See
[AWS Security]({{ "/docs/aws/security" | relative_url }}).

---

## Getting an Exception

If a guardrail blocks something you believe is legitimate, open a [ServiceNow
ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5). Explain the use case and the specific SCP or control that is blocking
you. The Cloud Team will evaluate the request and, if appropriate, grant a
targeted exception or suggest an alternative approach.

Exceptions are never granted for controls required by UC IS-3 or NIST 800-171.
