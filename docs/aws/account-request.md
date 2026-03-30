---
title: Request an AWS Account
description: How to request a new Campus Cloud AWS account, what information is required, and what happens next.
permalink: /docs/aws/account-request
last_reviewed: 2026-03-30
---

## Request a New AWS Account

New AWS accounts are provisioned through the standard Campus Cloud procurement
process via UCSB Gateway (Marketplace). The Cloud Team provisions account
once the PO is approved.

---

## Requirements

Before you can request a Campus Cloud account you need:

1. **A UCSB NetID** — All account owners and users must have a UCSB NetID ending
   in `@ucsb.edu`. External collaborators without a UCSB NetID cannot be added
   directly. Contact the Cloud Team if you have collaborators who need access.
2. **An estimate of your expected monthly spend** — Used to set your initial
   budget alarm.
3. **A funding source** — A departmental or grant-funded account number to pay
   for cloud costs (billed through Gateway).

---

## Why @ucsb.edu Is Required

All AWS accounts in the UCSB organization use **Shibboleth federated identity**
via UCSB NetID. Access is gated to the `ucsb.edu` domain by the identity
provider configuration.

There is no mechanism to add users outside this domain to the standard role
structure. If you have an external collaborator who needs access to data or
compute in your account, the recommended approaches are:

* **Share data** via pre-signed S3 URLs or a public S3 bucket with scoped
  access.
* **Set up federated access** via SAML or OIDC for the collaborator's home
  institution identity provider (advanced, requires Cloud Team involvement).
* **Create a sponsored UCSB NetID** for the collaborator through UCSB IT.

---

## How to Request an Account

1. Go to the [Getting Started](/getting-started) page for procurement
   instructions.
2. Complete a Gateway (Marketplace) purchase request for the desired cloud
   provider and account type.
3. Provide the following in the request:
   * Account owner name and NetID
   * Department and funding account number
   * Estimated monthly spend
   * Use case description (research, coursework, admin, etc.)
   * Desired region preference (us-east-1 or us-west-2, or both)
   * Whether campus network connectivity (Transit Gateway) is needed

4. After PO approval, the Cloud Team will provision the account within
   **approximately 2 business days** and send a confirmation email.

---

## After Provisioning

See [AWS First Steps](/docs/aws/first-steps) for what to do once your account
is ready.

---

## Modifying an Existing Account

For changes to an existing account (add networking, change budget alarm, move
between OUs, add users), open a ServiceNow ticket:

ServiceNow → Information Technology Services → Advanced Technical Services →
Cloud Services → Cloud Question
