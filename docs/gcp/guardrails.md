---
title: GCP Guardrails & Org Policies
description: Organization policy constraints and IAM deny policies applied to all Campus Cloud GCP projects.
permalink: /docs/gcp/guardrails
last_reviewed: 2026-03-30
---

## GCP Guardrails

UCSB Campus Cloud enforces guardrails using two mechanisms:

* **Organization Policies** — Resource-level constraints applied to the
  entire organization or specific folders. These prevent specific operations
  regardless of IAM permissions.
* **IAM Deny Policies** — Deny-first rules that block specific IAM actions
  even if a role would otherwise allow them.

---

## Key Organization Policy Constraints

### Networking

| Constraint | Effect |
|---|---|
| Prohibit auto-mode VPC networks | Auto-mode VPC creation is blocked; use custom-mode only |
| Restrict external IPs on VMs | VMs cannot have public IP addresses |
| Restrict Cloud VPN peer IPs | Only approved VPN endpoints can be used |
| Restrict protocol forwarding | Forwarded protocol traffic to external IPs is blocked |
| Allowed resource regions | Only us-central1 and us-west1 allowed for most resources |

### Identity and Access

| Constraint | Effect |
|---|---|
| Domain-restricted sharing | IAM bindings for `allUsers` or `allAuthenticatedUsers` are blocked; public access to resources is prevented |
| Restrict workforce identity federation | Only UCSB-approved identity providers can be used |

### Storage and Data

| Constraint | Effect |
|---|---|
| Enforce uniform bucket-level access | Fine-grained ACLs on Cloud Storage are blocked; bucket-level IAM only |
| Require retention policy on Cloud Storage | Retention policies required on GCS buckets in NIST folder |

### Compute

| Constraint | Effect |
|---|---|
| Require OS Login | OS Login must be enabled on all Compute Engine instances |
| Restrict VM images | Only approved images allowed (blocks arbitrary public images in NIST folder) |
| Disable serial port access | Serial port access to VMs is blocked |
| Require shielded VMs | Shielded VM features (Secure Boot, vTPM) required in NIST folder |

---

## IAM Deny Policies (Organization-Wide)

IAM deny policies operate before role bindings are evaluated — they are
absolute restrictions:

| Denied Action | Applies To |
|---|---|
| Disable Data Access audit logs | All principals |
| Set public IAM bindings (`allUsers`, `allAuthenticatedUsers`) | All principals except Cloud Team service accounts |
| Attach a billing account (in Sandbox folder) | All principals (prevents billing in Sandbox Unfunded) |
| Delete organization policies | All principals except break-glass accounts |

---

## Custom Constraints

The UCSB Landing Zone includes custom org policy constraints that enforce
specific NIST 800-171 controls not covered by standard constraints.
Examples include requiring CMEK encryption keys for specific services and
restricting database connection methods. These are applied in the UCSB NIST
Baseline folder.

---

## What You Can and Cannot Do

### You Can
* Create custom-mode VPCs with subnets in us-central1 and us-west1
* Create VMs with private IP addresses only
* Use Cloud NAT for outbound internet access
* Enable any GCP API not explicitly restricted
* Create Cloud Storage buckets with bucket-level IAM (no ACLs)
* Grant IAM roles to any `@ucsb.edu` user

### You Cannot
* Create auto-mode VPCs
* Assign external public IPs to VMs
* Set public access IAM bindings (`allUsers`, `allAuthenticatedUsers`)
* Disable audit logs
* Create resources in regions outside us-central1 / us-west1 (for most services)
* Attach a billing account to a Sandbox Unfunded project
* Create resources using unapproved VM images (in NIST folder)

---

## Org Policy Violations

When an org policy blocks an action, you will see an error like:

```
ERROR: (gcloud.compute.instances.create) Could not fetch resource:
  - Constraint 'constraints/compute.vmExternalIpAccess' violated for project ...
```

If you believe the block is in error or need a specific exception, open a
ServiceNow ticket. Describe the use case and the specific constraint. The
Cloud Team will evaluate whether an exemption is appropriate.

Exceptions are never granted for constraints that directly support UC IS-3 or
NIST 800-171 compliance requirements.
