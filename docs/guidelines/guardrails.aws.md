The Campus Cloud uses the AWS Control Tower Service as the primary tool for creating, maintaining, and implementing policies and controls in AWS.
Guardrails are the high-level rules that help define AWS policy.

Guardrails are categorized according to their behavior and their guidance. The behavior of each guardrail is either preventive or detective. Guardrail guidance refers to the recommended practice for how to apply each guardrail to your OUs. The guidance of a guardrail is independent of whether its behavior is preventive or detective.

See AWS Documentation for a complete [Guardrail Reference](https://docs.aws.amazon.com/controltower/latest/userguide/guardrails-reference.html)


### AWS Active Guardrails as of Feb 9, 2023 (rel of CT v3.1)

Mandatory Guardrails are enabled by default when you set up Control Tower Landing Zone and can't be disabled. AWS Maintains the list of [Mandatory Guardrails](https://docs.aws.amazon.com/controltower/latest/userguide/mandatory-guardrails.html).

Strongly Recommended Guardrails that have been enabled:

- [Disallow Creation of Access Keys for the Root User](https://docs.aws.amazon.com/controltower/latest/userguide/strongly-recommended-guardrails.html#disallow-root-access-keys) September 5, 2019 

- [Detect whether encryption is enabled for Amazon EBS volumes attached to Amazon EC2 instances (Previously Enable Encryption for Amazon EBS Volumes Attached to Amazon EC2 Instances)](https://docs.aws.amazon.com/controltower/latest/userguide/strongly-recommended-guardrails.html#ebs-enable-encryption)  August 25, 2019 (name updated) √

- ~~[Disallow Internet Connection Through RDP](https://docs.aws.amazon.com/controltower/latest/userguide/strongly-recommended-guardrails.html#rdp-disallow-internet)~~

- [Detect whether unrestricted internet connection through SSH is allowed (Previously Disallow Internet Connection Through SSH)](https://docs.aws.amazon.com/controltower/latest/userguide/strongly-recommended-guardrails.html#ssh-disallow-internet) June 24, 2019 

- [Detect whether MFA for the root user is enabled (Previously Enable MFA for the Root User)](https://docs.aws.amazon.com/controltower/latest/userguide/strongly-recommended-guardrails.html#enable-root-mfa)  June 24, 2019 

- [Detect whether public access to Amazon RDS database snapshots is enabled (Previously Disallow Public Access to Amazon RDS Database Snapshots)](https://docs.aws.amazon.com/controltower/latest/userguide/strongly-recommended-guardrails.html#disallow-rds-snapshot-public-access) August 25, 2019 

- [Detect whether storage encryption is enabled for Amazon RDS database instances (Previously Disallow Amazon RDS Database Instances That Are Not Storage Encrypted)](https://docs.aws.amazon.com/controltower/latest/userguide/strongly-recommended-guardrails.html#disallow-rds-storage-unencrypted) August 25, 2019 

-  [Detect whether unrestricted incoming TCP traffic is allowed](https://docs.aws.amazon.com/controltower/latest/userguide/strongly-recommended-controls.html#rdp-disallow-internet) November 15, 2018 

-  [Detect whether public write access to Amazon S3 buckets is allowed](https://docs.aws.amazon.com/controltower/latest/userguide/strongly-recommended-controls.html#s3-disallow-public-write) November 15, 2018 

Elective Guardrails that have been enabled:

- [Detect whether replication instances for AWS Database Migration Service are public](https://docs.aws.amazon.com/controltower/latest/userguide/data-residency-guardrails.html#dms-replication-not-public)  November 30, 2021

- [Detect whether Amazon EBS snapshots are restorable by all AWS accounts](https://docs.aws.amazon.com/controltower/latest/userguide/data-residency-guardrails.html#ebs-snapshot-public-restorable-check)  ~~November 30~~ December 1, 2021

- [Detect whether any Amazon EMR cluster master nodes have public IP addresses](https://docs.aws.amazon.com/controltower/latest/userguide/data-residency-guardrails.html#emr-master-no-public-ip)   November 30, 2021

- [Detect whether the AWS Lambda function policy attached to the Lambda resource blocks public access](https://docs.aws.amazon.com/controltower/latest/userguide/data-residency-guardrails.html#lambda-function-public-access-prohibited)   November 30, 2021

- [Detect whether public routes exist in the route table for an Internet Gateway (IGW)](https://docs.aws.amazon.com/controltower/latest/userguide/data-residency-guardrails.html#no-unrestricted-route-to-igw)   November 30, 2021 (Currently being re-evaluated in DEV)

- [Detect whether Amazon Redshift clusters are blocked from public access](https://docs.aws.amazon.com/controltower/latest/userguide/data-residency-guardrails.html#redshift-cluster-public-access-check)   November 30, 2021

- [Deny access to AWS based on the requested AWS Region](https://docs.aws.amazon.com/controltower/latest/userguide/data-residency-guardrails.html#primary-region-deny-policy)   ~~November 30, 2021~~ July 26, 2022 (Currently being re-evaluated in DEV)

-  [Detect whether Amazon S3 settings to block public access are set as true for the account](https://docs.aws.amazon.com/controltower/latest/userguide/data-residency-guardrails.html#s3-account-level-public-access-blocks-periodic)   November 30, 2021

- [Detect whether AWS Systems Manager documents owned by the account are public](https://docs.aws.amazon.com/controltower/latest/userguide/data-residency-guardrails.html#ssm-document-not-public)  November 30, 2021

- [Detect whether MFA is enabled for AWS IAM users of the Console (Previously Disallow Console Access to IAM Users Without MFA)](https://docs.aws.amazon.com/controltower/latest/userguide/elective-guardrails.html#disallow-console-access-mfa) ~~August 25~~ July 30, 2019
