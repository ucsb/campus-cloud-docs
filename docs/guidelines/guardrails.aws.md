#### AWS Active Guardrails as of May 2020

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
