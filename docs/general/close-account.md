---
title: Close an Account
description: How to close a Campus Cloud account on AWS, Azure, or GCP
permalink: /docs/general/close-account
last_reviewed: 2026-03-30
---

## Close an Account

{% include alert.html type="warning" title="This cannot be undone" content="Once account closure is confirmed, all resources and data in the account are permanently destroyed. Back up everything you need before starting this process." %}

When you are ready to close a Campus Cloud AWS account, Azure subscription, or
GCP project, follow the steps below. All providers follow the same general
process.

---

## Before You Start

1. **Back up your data.** Download or transfer any data you need to keep. Once
   closure is confirmed, data cannot be recovered.
2. **Destroy your resources.** Delete VMs, databases, storage buckets, and any
   other resources you created. A good indicator you are done: your monthly bill
   drops to under $5–10 (a small nominal charge is normal to maintain an account
   in the Landing Zone).
3. **Remove regulated data.** Confirm that all regulated datasets (PII, FERPA,
   CUI, HIPAA) have been removed or transferred appropriately.

---

## Closure Process

1. **Open a ServiceNow ticket.**
   * Go to [ucsb.service-now.com](https://ucsb.service-now.com/)
   * Navigate to: Information Technology Services → Advanced Technical Services
     → Cloud Services → Cloud Question
   * Include your **Account #** (AWS) or **Subscription #** (Azure) or
     **Project ID** (GCP), your **PO #**, and your requested **closure date**.

2. **Confirm in the ticket** that each of the following is complete:
   * All regulated data removed
   * All data that needs saving has been backed up or exported
   * All owner-created resources have been destroyed
   * All users understand that access will be terminated

   If you cannot destroy all resources yourself, you may authorize the Cloud
   Team to destroy remaining resources and data.

3. **The Cloud Team will:**
   * Wait 15 days after your confirmation before destroying remaining resources
   * Wait an additional 5 days before removing access
   * Close the ticket after the final invoice is submitted

---

## Final Invoice and PO Closure

{% include alert.html type="warning" title="Do not close your PO immediately" content="The PO associated with the account should not be closed for 30 days after the final invoice to ensure Accounting has time to process it. The Cloud Team invoices for the previous month's costs approximately three weeks after month-end." %}

The Service Now ticket will remain open until the final invoice is submitted.
All correspondence about the account closure should be in the ticket.

---

## Provider-Specific Notes

### AWS
Account deletion severs the root email association and removes the account from
the organization. Some AWS services retain data for a short period after deletion.

### Azure
Subscription deletion removes all resources and the subscription from the
management group hierarchy.

### GCP
Project deletion enters a 30-day deletion pending state before permanent removal.
The Cloud Team manages this process to ensure billing sub-accounts are updated
correctly.
