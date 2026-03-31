---
title: AWS Cost Visualization with QuickSight
description: How to access the UCSB AWS cost dashboard in Amazon QuickSight to monitor spending across your account.
permalink: /docs/aws/quicksight
last_reviewed: 2026-03-30
redirect_from:
  - /docs/guidelines/quicksight-dashboards
---

## Cost Dashboards with Amazon QuickSight

The Cloud Team maintains a centralized **Amazon QuickSight** dashboard that
shows cost and usage data across all Campus Cloud AWS accounts. This gives
account owners visibility into their spending over time, broken down by service,
region, and tag.

---

## Accessing the Dashboard

1. Sign in to AWS at [aws.cloud.ucsb.edu](https://aws.cloud.ucsb.edu).
2. In the AWS Console, navigate to **Amazon QuickSight** (search in the top bar).
3. If you see a QuickSight sign-in prompt, click **Sign in with Active Directory /
   SAML** and use your UCSB credentials.

{% include alert.html type="warning" title="QuickSight access is not automatic" content="QuickSight access must be provisioned separately from your AWS account. If you cannot access QuickSight, request access via [ServiceNow](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5)" %}

**Account name for QuickSight:** `ucsb-campus-cloud`

---

## What the Dashboard Shows

| Dashboard View | Description |
|---|---|
| Account Summary | Total monthly spend by account |
| Service Breakdown | Cost per AWS service (EC2, RDS, S3, etc.) |
| Daily Trend | Daily spend over the selected date range |
| Tag Analysis | Spend by team, mission, or environment tag |

Data in the dashboard is updated daily from AWS Cost and Usage Reports.
There is typically a 24–48 hour lag before new charges appear.

---

## Cost Explorer (Per-Account View)

For a per-account, more granular view, use **AWS Cost Explorer** directly
in the console:

1. Navigate to **Billing → Cost Explorer**.
2. Group by Service, Tag, or Region to slice the data.
3. Use the **Usage Type** dimension to identify specific resource charges
   (e.g., EC2 instance hours vs. EBS storage).

Cost Explorer is available to any role with Billing permissions in your account.

---

## Budget Alarms

Budget alarms notify you by email when actual or forecasted spend crosses a
threshold you define. A billing alarm was set during account provisioning.
To verify or update it:

1. Navigate to **Billing → Budgets**.
2. Review the existing budget(s) and their notification thresholds.
3. To add a threshold (e.g., 80% warning + 100% alert), edit the budget or
   create a new one.

See [Cost Management](docs/general/cost-management) for guidance on setting
appropriate budget alerts.

---

## Requesting Dashboard Access

Open a [ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5) with:
* Your AWS Account ID
* Your UCSB NetID
* Whether you need read-only or author access to QuickSight
