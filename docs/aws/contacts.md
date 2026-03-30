---
title: AWS Account Contacts
description: How to set and update technical and billing contacts for your AWS account.
permalink: /docs/aws/contacts
last_reviewed: 2026-03-30
---

## AWS Account Contacts

AWS allows two types of account contacts: a **Primary/Billing contact** and
**Alternate contacts** (Security, Operations, Billing). Campus Cloud accounts
should have all contacts set to departmental or functional email addresses
rather than individual people's NetIDs.

{% include alert.html type="warning" title="Use functional email addresses" content="Avoid setting contacts to a personal email address. When people change roles or leave UCSB, contacts with personal addresses stop working. Use a department or team email (e.g., mylab-cloud@ucsb.edu) that can be managed by multiple people." %}

---

## Contact Types

| Contact Type | Purpose | Who Controls It |
|---|---|---|
| Primary / Billing | AWS bills and account-level notices | Cloud Team (set to campus billing) |
| Alternate — Security | Security findings, GuardDuty alerts | Account owner (your team) |
| Alternate — Operations | Service health notifications | Account owner (your team) |
| Alternate — Billing | Spend alerts, budget notifications | Account owner (your team) |

The Cloud Team manages the Primary contact. **You are responsible for setting
Alternate contacts** for your account.

---

## How to Set Alternate Contacts

1. Sign in to your account at [aws.cloud.ucsb.edu](https://aws.cloud.ucsb.edu).
2. In the top-right dropdown, click your account name → **Account**.
3. Scroll to **Alternate contacts**.
4. Set the Security, Operations, and Billing contacts to your team's functional
   email addresses.
5. Save changes.

---

## Why Contacts Matter

AWS sends important notifications to these addresses:

* **Security contact** — receives alerts from Security Hub, GuardDuty findings,
  and abuse reports from AWS Trust & Safety.
* **Operations contact** — receives service health events and maintenance
  notifications.
* **Billing contact** — receives budget threshold alerts and monthly billing
  reminders.

Missing or stale contacts mean your team may not hear about a security incident
or an unexpected billing spike in time to respond.

---

## Contact the Cloud Team

For account-level changes you cannot make yourself (Primary contact updates,
bulk contact updates across multiple accounts), open a ServiceNow ticket:

ServiceNow → Information Technology Services → Advanced Technical Services →
Cloud Services → Cloud Question
