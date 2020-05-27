---
title: Compliance & Governance
description: Compliance & Governance
permalink: /docs/guidelines/compliance
---

## Compliance & Governance
In order to receive Federal funding the Campus needs to comply with NIST 800-171 Federal standards.  UC Policy, IS-3, mandates our requirements for Information Security. The Campus Cloud environment is designed to comply with these standards.

### NIST 800-171 - [NIST 800-171 Rev 2](https://csrc.nist.gov/publications/detail/sp/800-171/rev-2/final)
### IS-3 UC Information Security - [IS-3](https://security.ucop.edu/policies/it-policies.html)

### Account Compliance
The following are critical compliance requirements for each Campus Cloud account:
- Enable MFA for the root user
- Define contact information for the account owner and for incident response
- [Data privacy classification Tagging](/campus-cloud-docs/guidelines/tagging) on account and per resource
- Use of account must be in accordance with UC Policy IS-3

### How we audit and maintain compliance?

AWS Control Tower and  Guardrails work together to provide ongoing goverance for the Campus AWS environment. Control Tower implements preventive or detective controls that help govern resources and monitor compliance across groups of AWS accounts.  [Tagging](/campus-cloud-docs/glassoary/tags) of accounts and individual resources support compliance efforts. 

### AWS Control Tower & Guardrails

The Campus Cloud uses the AWS Control Tower Service as the primary tool for creating, maintaining, and implementing policies and controls.
Guardrails are the high-level rules that help define AWS policy.

Guardrails are categorized according to their behavior and their guidance. The behavior of each guardrail is either preventive or detective. Guardrail guidance refers to the recommended practice for how to apply each guardrail to your OUs. The guidance of a guardrail is independent of whether its behavior is preventive or detective.

See AWS Documentation for a complete [Guardrail Reference](https://docs.aws.amazon.com/controltower/latest/userguide/guardrails-reference.html)

#### The List of Active Guardrails as of May 2020

Mandatory Guardrails are enabled by default when you set up Control Tower Landing Zone and can't be disabled. AWS Maintains the list of [Mandatory Guardrails](https://docs.aws.amazon.com/controltower/latest/userguide/mandatory-guardrails.html).

Strongly Recommended Guardrails that have been enabled:

- [Disallow Creation of Access Keys for the Root User](https://docs.aws.amazon.com/controltower/latest/userguide/strongly-recommended-guardrails.html#disallow-root-access-keys)

- [Enable Encryption for Amazon EBS Volumes Attached to Amazon EC2 Instances](https://docs.aws.amazon.com/controltower/latest/userguide/strongly-recommended-guardrails.html#ebs-enable-encryption)

- [Disallow Internet Connection Through RDP](https://docs.aws.amazon.com/controltower/latest/userguide/strongly-recommended-guardrails.html#rdp-disallow-internet)

- [Disallow Internet Connection Through SSH](https://docs.aws.amazon.com/controltower/latest/userguide/strongly-recommended-guardrails.html#ssh-disallow-internet)

- [Enable MFA for the Root User](https://docs.aws.amazon.com/controltower/latest/userguide/strongly-recommended-guardrails.html#enable-root-mfa)

- [Disallow Public Write Access to Amazon S3 Buckets](https://docs.aws.amazon.com/controltower/latest/userguide/strongly-recommended-guardrails.html#s3-disallow-public-write)

- [Disallow Public Access to Amazon RDS Database Snapshots](https://docs.aws.amazon.com/controltower/latest/userguide/strongly-recommended-guardrails.html#disallow-rds-snapshot-public-access)

- [Disallow Amazon RDS Database Instances That Are Not Storage Encrypted](https://docs.aws.amazon.com/controltower/latest/userguide/strongly-recommended-guardrails.html#disallow-rds-storage-unencrypted)

Elective Guardrails that have been enabled

- [Disallow Console Access to IAM Users Without MFA](https://docs.aws.amazon.com/controltower/latest/userguide/elective-guardrails.html#disallow-console-access-mfa)
