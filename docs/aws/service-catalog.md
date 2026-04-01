---
title: AWS Service Catalog
description: Pre-approved, ready-to-deploy infrastructure products available via the AWS Service Catalog.
permalink: /docs/aws/service-catalog
last_reviewed: 2026-03-30
redirect_from:
  - /docs/bestpractices/servicecatalog
  - /docs/guidelines/servicecatalog
---

## AWS Service Catalog

The AWS Service Catalog in your account contains a curated set of
**pre-approved, compliance-ready infrastructure templates** created and
maintained by the Cloud Team.

Using a Service Catalog product is the **recommended** way to provision
common infrastructure because:

* Products are pre-configured for UCSB tagging requirements.
* Networking is set up for you (correct VPC, subnets, security groups).
* Security defaults match Campus Cloud guardrails.
* You spend minutes provisioning instead of hours.

---

## How to Launch a Product

1. In the AWS Console, navigate to **Service Catalog → Products**.
2. Select a product and click **Launch Product**.
3. Fill in the required parameters (name, environment, tags, etc.).
4. Click **Launch** and wait for the stack to complete (usually 5–10 minutes).
5. Find your new resources in the **Provisioned Products** list.

You can update or terminate a product from the **Provisioned Products** list.

---

## Available Products

| Product | Description |
|---|---|
| Simple VPC | Basic VPC for internet-only workloads |
| Advanced VPC | VPC with Transit Gateway attachment for campus network access |
| Budget Notification | CloudWatch billing alarm wired to your team's email |
| Security Notifications | SNS-based alerts for security events |
| IAM Role-to-Group | Maps IAM roles to IdP groups for federated access |
| SNS Topic | Pre-configured SNS topic for notifications |
| Effectual Budget | Enhanced budget management product |
| Instance Scheduler | Automated start/stop scheduling for EC2 and RDS instances |

{% include alert.html type="info" title="Product list may change" content="New products are added as the Cloud Team develops them. Log in to the AWS Console and check Service Catalog → Products for the current complete list." %}

---

## VPC Families

When requesting a VPC, choose the family that matches your connectivity needs:

| VPC Type | Campus Network Access | Internet Access | Use When |
|---|---|---|---|
| Advanced VPC (Campus Connected) | Yes (via Transit Gateway) | Yes (via NAT) | You need to reach on-prem file shares, databases, or LDAP |
| Simple VPC (Internet Only) | No | Yes (via NAT) | Public-facing apps with no campus dependency |

You can have both types in the same account. See [Networking](/docs/aws/networking)
for more details.

---

## Self-Managed Resources

You are not required to use Service Catalog. You can create any AWS resource
directly via the Console, CLI, or IaC tools (Terraform, CloudFormation, CDK).
The same guardrails, tagging requirements, and region restrictions apply
regardless of how resources are created.

If you create resources outside of Service Catalog, you are responsible for
ensuring they comply with required [tags](/docs/general/tagging) and security
baseline settings.

---

## Requesting New Products

If you have a common infrastructure pattern that you think would benefit other
teams, suggest it to the Cloud Team via [ServiceNow](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5). The Cloud Team evaluates
product requests periodically.
