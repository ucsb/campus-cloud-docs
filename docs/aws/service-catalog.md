---
title: AWS Service Catalog
description: Pre-approved, ready-to-deploy infrastructure products available via the AWS Service Catalog.
permalink: /docs/aws/service-catalog
last_reviewed: 2026-04-30
redirect_from:
  - /docs/bestpractices/servicecatalog
  - /docs/guidelines/servicecatalog
---

# AWS Service Catalog

The AWS Service Catalog in your account contains a curated set of
**pre-approved, compliance-ready infrastructure templates** created and
maintained by the Cloud Team.

Using a Service Catalog product is the **recommended** way to provision
common infrastructure because:

* Products are pre-configured for UCSB tagging requirements.
* Security defaults match Campus Cloud guardrails.
* IP address ranges are automatically allocated from the campus pool — no coordination needed.
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

| Product | What it creates |
|---|---|
| Advanced VPC | A fully configured private network with subnets across two availability zones, optional internet access, campus network connectivity via Transit Gateway (when private subnets are selected), and an S3 endpoint. You choose the size and subnet layout. **Use this for most workloads.** |
| Budget Alert and Action on Threshold (Effectual) | An alternative budget product that applies an IAM policy to your account when a spending threshold is reached, actively restricting further resource creation. Use this when you need a hard spending cap rather than just a notification. Deploy to your home region only. See the [Active Budget Controller docs](https://aws-ia.github.io/cloudformation-effectual-activebudgetcontroller/) for configuration details. |
| Create IAM Role to UCSB Identity Group | Creates an empty IAM role and a matching UCSB Identity group at the same time. Members of that group (managed at [im.ucsb.edu](https://im.ucsb.edu)) can sign in to AWS and assume the role. You add permissions to the role after creation. Role names are limited to 15 characters. |
| Fixed Monthly Budget with Notification | A monthly spending limit with email alerts. AWS emails you (and an optional second address) when your *forecasted* spend is on track to exceed the limit — by default the alert fires at 120% of your budget, so you get early warning before you actually go over. |
| Instance Scheduler | Automatically starts and stops your EC2 and RDS instances on a schedule. Use this to avoid paying for instances that run overnight or on weekends when no one needs them. See the [Instance Scheduler on AWS docs](https://docs.aws.amazon.com/solutions/instance-scheduler-on-aws/) for configuration details. |
| Local Security Notification | An email alert for guardrail violations. Whenever a resource in your account falls out of compliance with an AWS Config rule (a Campus Cloud guardrail), you get an email. Set this up so your team is notified of compliance issues without having to check the console. |
| Simple VPC with Campus Connectivity | An empty private network with a block of IP addresses reserved from the campus pool. No subnets or internet access are included — use this only if you need to build your network layout from scratch. |

{% include alert.html type="info" title="Product list may change" content="New products are added as the Cloud Team develops them. Log in to the AWS Console and check Service Catalog → Products for the current complete list." %}

---

## Choosing a VPC

Both VPC products reserve IP space from the campus-wide IP Address Manager (IPAM), so your address ranges won't conflict with other accounts.

| Product | Subnets included | Campus network access | Internet access | Use when |
|---|---|---|---|---|
| Advanced VPC | Yes — you choose size and layout (public, private, or both) | Yes, via Transit Gateway (when private subnets are selected) | Yes, via Internet Gateway (when public subnets are selected) | You need to run servers, databases, or anything that requires network connectivity |
| Simple VPC with Campus Connectivity | No — you create subnets yourself | No — Transit Gateway attachment is not included | No | You need full control over your network design from scratch |

For most workloads, use **Advanced VPC**. See [Networking]({{ "/docs/aws/networking" | relative_url }}) for more details.

---

## Self-Managed Resources

You are not required to use Service Catalog. You can create any AWS resource
directly via the Console, CLI, or IaC tools (Terraform, CloudFormation, CDK).
The same guardrails, tagging requirements, and region restrictions apply
regardless of how resources are created.

If you create resources outside of Service Catalog, you are responsible for
ensuring they comply with required [tags]({{ "/docs/general/tagging" | relative_url }}) and security
baseline settings.

---

## Requesting New Products

If you have a common infrastructure pattern that you think would benefit other
teams, suggest it to the Cloud Team via [ServiceNow](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5). The Cloud Team evaluates
product requests periodically.
