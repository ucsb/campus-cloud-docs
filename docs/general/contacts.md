---
title: Account Contacts
description: Best practices for setting cloud account contacts across all providers
permalink: /docs/general/contacts
last_reviewed: 2026-03-30
---

## Account Contacts

Every Campus Cloud account has contacts that receive critical notifications —
security findings, billing alerts, and service health events. Setting these
correctly is one of the first things you should do after account creation.

---

## Use Functional Email Addresses

{% include alert.html type="warning" title="Use functional email addresses" content="Avoid setting contacts to a personal email address. When people change roles or leave UCSB, contacts with personal addresses stop working. Use a department or team email (e.g., mylab-cloud@ucsb.edu) that can be managed by multiple people." %}

---

## Why Contacts Matter

Cloud providers send important notifications to your contacts:

* **Security** — alerts from security monitoring tools (GuardDuty, Defender for
  Cloud, Security Command Center), abuse reports, and potential account
  compromise notifications.
* **Operations** — service health events, scheduled maintenance, and
  infrastructure incidents that affect your resources.
* **Billing** — budget threshold alerts and billing issue notifications.

Missing or stale contacts mean your team may not hear about a security incident
or an unexpected billing spike in time to respond.

---

## Provider-Specific Setup

Each provider has a different way to configure contacts. Follow the guide for
your provider:

* [AWS First Steps — Set Account Contacts](docs/aws/first-steps#step-3--set-account-contacts) —
  Alternate contacts (Security, Operations, Billing) in the AWS Account
  Settings page.
* [Azure First Steps — Set Subscription Contacts](docs/azure/first-steps#step-4--set-subscription-contacts) —
  Defender email notifications, budget alert recipients, and Service Health
  alert rules.
* [GCP First Steps — Set Project Contacts](docs/gcp/first-steps#step-3--set-project-contacts) —
  Essential Contacts for Security, Technical, and Billing notification
  categories.

---

## Contacting the Cloud Team

For account-level contact changes you cannot make yourself, open a
[ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5).
