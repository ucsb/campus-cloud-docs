---
title: GCP Project Contacts
description: How to configure Essential Contacts for your GCP project so your team receives security, billing, and operational alerts.
permalink: /docs/gcp/contacts
last_reviewed: 2026-03-30
---

## GCP Project Contacts

GCP uses **Essential Contacts** to send critical notifications to designated
contacts at the organization and project level. Contacts are categorized by
purpose (Security, Legal, Product Updates, etc.).

Setting up contacts for your project ensures your team receives alerts from
Security Command Center, billing, and GCP service health.

{% include alert.html type="warning" title="Use functional email addresses" content="Do not set contacts to a personal @ucsb.edu address. When people change roles or leave UCSB, personal address contacts stop working. Use a team or department email that can be managed by multiple people." %}

---

## Org-Level Contacts (Pre-configured)

The Cloud Team has configured organization-level Essential Contacts that apply
to all GCP projects. These route organization-wide security and legal
notifications to the appropriate Cloud Team addresses. You do not need to change
org-level contacts.

---

## Project-Level Contacts (Your Responsibility)

You should set project-level contacts so that notifications specific to your
project reach your team:

1. Navigate to [console.cloud.google.com/iam-admin/essentialcontacts](https://console.cloud.google.com/iam-admin/essentialcontacts)
   with your project selected.
2. Click **+ Add contact**.
3. Enter a functional email address and select the notification categories:
   * **Security** — Security Command Center findings, VPC Service Controls alerts
   * **Technical** — Maintenance and service disruption notices
   * **Billing** — Budget alerts and billing issue notifications
4. Confirm by clicking the link in the verification email sent to that address.
5. Repeat for each category that needs a different address.

---

## Contact Categories Reference

| Category | Types of Notifications |
|---|---|
| Security | Security Command Center findings, potential account compromise alerts |
| Technical | VM maintenance notifications, service disruptions, infrastructure events |
| Billing | Budget alert emails, billing account suspensions |
| Legal | Data processing instructions, policy updates |
| Product Updates | New feature announcements, deprecation notices |

For most Campus Cloud projects, setting Security, Technical, and Billing
contacts to your team's functional email addresses is sufficient.

---

## Verifying Contacts Are Active

Unverified contacts do not receive notifications. After adding a contact:

1. Check the inbox for the verification email from Google.
2. Click the link in the email to confirm.
3. Return to Essential Contacts and confirm the contact shows as **Verified**.

---

## Updating or Removing Contacts

To update a contact email (e.g., when your team's functional address changes):

1. Go to Essential Contacts in the project.
2. Delete the old contact.
3. Add the new address and complete verification.

---

## Contacting the Cloud Team

For org-level contact changes or support tickets:

[ServiceNow](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5) → Information Technology Services → Advanced Technical Services →
Cloud Services → Cloud Question

Include your **GCP Project ID** in all support requests.
