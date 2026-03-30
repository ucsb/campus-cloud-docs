---
title: Azure Account Contacts
description: How to configure notification contacts for your Azure subscription to receive security, billing, and health alerts.
permalink: /docs/azure/contacts
last_reviewed: 2026-03-30
---

## Azure Subscription Contacts

Setting up the right contacts in your Azure subscription ensures your team
receives critical notifications for security alerts, billing overages, and
service health events.

{% include alert.html type="warning" title="Use functional email addresses" content="Avoid setting contacts to a personal @ucsb.edu address. When people change roles or leave UCSB, personal addresses stop working. Use a team or departmental email that can be managed by multiple people." %}

---

## Subscription-Level Contact (Azure Account Center)

The primary billing contact is managed by the Cloud Team at the enrollment
level. You do not need to change this.

---

## Security Alerts — Defender for Cloud

Microsoft Defender for Cloud sends security alerts to the email configured in
the subscription's Defender settings:

1. Navigate to **Microsoft Defender for Cloud → Environment settings**.
2. Click your subscription.
3. Click **Email notifications**.
4. Set:
   * **Email addresses for notifications**: your team's functional security email.
   * **Alert severity**: High as a minimum (All recommended).
   * **Also notify owners**: check this box if your Subscription Owner should
     receive duplicates.
5. Save.

---

## Budget Alerts — Cost Management

Billing alerts are sent to the email address configured in your budget:

1. Navigate to **Cost Management → Budgets**.
2. Click your budget (or create one if none exists).
3. Under **Conditions**, click **Manage alert recipients**.
4. Add your team's billing contact email address.

---

## Service Health Notifications

Azure Service Health alerts notify you when Azure services your subscription
relies on are degraded or have planned maintenance:

1. Navigate to **Service Health → Health alerts → + Create service health alert**.
2. Choose:
   * Subscription: your subscription
   * Services: the Azure services you use (e.g., Virtual Machines, SQL Database)
   * Regions: West US 2, West Central US
   * Event types: Service issue, Planned maintenance, Health advisories
3. Create an Action Group:
   * Add an Email/SMS action with your team's functional address.
4. Save the alert rule.

---

## Contacting the Cloud Team

For changes to your subscription that you cannot make yourself, open a
[ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5):

[ServiceNow](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5) → Information Technology Services → Advanced Technical Services →
Cloud Services → Cloud Question

Include your **Subscription ID** in all support requests.
