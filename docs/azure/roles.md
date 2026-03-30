---
title: Azure Roles & Access
description: The four custom RBAC roles used in Campus Cloud Azure subscriptions and how to manage user access.
permalink: /docs/azure/roles
last_reviewed: 2026-03-30
---

## Azure Roles & Access

UCSB Campus Cloud Azure subscriptions use **four custom RBAC roles** that are
purpose-built for campus cloud workloads. These roles replace the built-in
Azure roles (Owner, Contributor, Reader) to provide more appropriate
permission scopes.

All user access is managed through **UCSB Microsoft Entra ID**. Users sign in
with their `@ucsb.edu` account — no local passwords or service accounts.

---

## The Four Custom Roles

| Role | Who Should Use It | Key Permissions | Key Restrictions |
|---|---|---|---|
| **UCSB Subscription Owner** | PI or department head (1–2 people max) | Manage all resources, assign roles | Cannot modify root-level management group policies |
| **UCSB Application Owner** | Developers, researchers, lab managers | Create/manage compute, storage, databases, deploy code | Cannot manage RBAC assignments; cannot modify network hub resources |
| **UCSB Network Operations** | Networking staff | Manage VNets, NSGs, route tables, peerings | Read-only outside of network resources |
| **UCSB Security Operations** | Security reviewers, compliance staff | Read all resources, view Defender alerts, manage Key Vault | No write access to data-plane resources |

### Choosing the Right Role

* **Day-to-day work** → Application Owner
* **Initial setup, RBAC management** → Subscription Owner (temporary elevation recommended)
* **Audits, compliance reviews** → Security Operations (read-only)

---

## Viewing Your Role Assignment

1. Navigate to your subscription in the Azure portal.
2. Click **Access control (IAM) → Role assignments**.
3. Find yourself in the list to see your assigned role.

---

## Adding a User

Subscription Owners can add new users to their subscription:

1. Navigate to the subscription → **Access control (IAM) → + Add → Add role assignment**.
2. Select the appropriate custom role from the list.
3. Search for the user by their `@ucsb.edu` email address.
4. Click **Review + assign**.

{% include alert.html type="warning" title="UCSB accounts only" content="Only users with a UCSB Entra ID account (@ucsb.edu) can be assigned roles. External collaborators need a sponsored UCSB account or an alternative access approach — contact the Cloud Team." %}

---

## Removing a User

1. Navigate to the subscription → **Access control (IAM) → Role assignments**.
2. Find the user and click the checkbox next to their assignment.
3. Click **Remove** at the top of the pane.
4. Confirm the removal.

Removing a user from a role immediately revokes their access.

---

## Service Principals and Managed Identities

For automated workloads (pipelines, scripts, applications):

* Prefer **Managed Identities** over Service Principals where possible —
  they do not require credential management.
* If a Service Principal is required, use the Application Owner or a custom
  scoped role (not Subscription Owner) and rotate the secret regularly.
* Do not embed service principal credentials in code or checked-in files.
  Use Azure Key Vault instead.

---

## Requesting Role Changes

Changes to the custom role definitions themselves (not role assignments) must
be made by the Cloud Team. Open a ServiceNow ticket if the available roles do
not match your team's needs.
