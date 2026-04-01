---
title: GCP Guardrails & Org Policies
description: Organization policy constraints and IAM deny policies applied to all Campus Cloud GCP projects.
permalink: /docs/gcp/guardrails
last_reviewed: 2026-03-30
---

## GCP Guardrails

UCSB Campus Cloud enforces guardrails — automatic restrictions that keep every
GCP project aligned with university security policy
([UC IS-3](https://security.ucop.edu/policies/institutional-information-and-it-resource-classification.html))
and the federal
[NIST 800-171]({{ site.baseurl }}/glossary#nist-800-171) standard for
protecting sensitive research data.

Guardrails are designed to maintain a safe, compliant baseline without getting
in the way of normal cloud usage. You will only notice them if you attempt
something outside that baseline. The sections below describe what is and is not
allowed.

---

## Built-in Organization Policy Constraints

### Networking

| Constraint | Effect |
|---|---|
| Deny external IPs on VMs (`vmExternalIpAccess`) | VMs cannot have public IP addresses |
| Require custom-mode VPCs only (custom constraint) | Auto-mode VPC creation is blocked |
| Restrict protocol forwarding | Both external and internal protocol forwarding blocked |
| Restrict external load balancers | All external load balancer types are blocked (`in:EXTERNAL`) |
| Restrict resource locations | Only us-central1 and us-west1 allowed for most resources |
| Restrict Compute storage resources | Disk/image sharing restricted to within the org |

### Identity and Access

| Constraint | Effect |
|---|---|
| Domain-restricted sharing (`allowedPolicyMemberDomains`) | Access can only be granted to UCSB organization members |
| Disable default SA auto-grants | GCP will not auto-grant editor access to default service accounts |

### Storage

| Constraint | Effect |
|---|---|
| Public access prevention (`publicAccessPrevention`) | Internet-accessible GCS buckets are blocked |

### Compute

| Constraint | Effect |
|---|---|
| Require OS Login | OS Login must be enabled on all Compute Engine instances |
| Require Shielded VMs | Shielded VM features (Secure Boot, vTPM) required |
| Restrict VM images | Only approved Google-published images allowed |
| Detailed audit logging mode | Data Access audit logs enabled for all services |

---

## IAM Deny Policies (Organization-Wide)

IAM deny policies operate before role bindings are evaluated — they are
absolute restrictions. The Campus Cloud Landing Zone uses 4 deny policies at the org level:

| Policy | What It Blocks | Exceptions |
|---|---|---|
| Resource Manager Lockdown | Creating/deleting folders, removing project deletion protection, moving projects between folders, changing billing account assignments | Cloud Team automation, org admins (break-glass) |
| Networking Lockdown | Creating VPC networks | Cloud Team automation only |
| Automation Account Protection | Modifying org-level access policies outside of the standard process | Cloud Team automation, org admins (break-glass) |
| Contact Preservation | Deleting or modifying Essential Contacts | Cloud Team automation, org admins, billing admins |

---

## Additional Security Constraints

These guardrails enforce additional NIST 800-171 controls beyond the built-in
policies above.

### Enforced Org-Wide

| Constraint | Effect |
|---|---|
| Disable Gmail members | Granting access to `@gmail.com` accounts is blocked |
| Disable public access grants | Granting access to `allUsers` or `allAuthenticatedUsers` is blocked |
| Disable IP forwarding | VMs cannot be created with IP forwarding enabled |
| Require VPC flow logs | Subnets cannot be created without flow logs enabled |
| Require DNS logging | DNS policies must have logging enabled |
| Require DNSSEC on public zones | Public DNS zones must have DNSSEC enabled |
| Require custom-mode VPC | Auto-mode VPCs (subnets in every region) are blocked |
| Require firewall logging | VPC firewall rules must have logging enabled (GKE-managed rules excluded) |
| Require backend service logging | Load balancer backend services must have logging enabled |
| Disable weak SSL policies | SSL policies with TLS < 1.2 or weak cipher suites are blocked |

---

## What You Can and Cannot Do

### You Can
* Create VMs with private IP addresses only
* Make outbound internet connections from VMs freely (outbound traffic is not restricted)
* Request VPC and networking resources via [ServiceNow](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5) (provisioned by Cloud Team)
* Enable any GCP API not explicitly restricted
* Create Cloud Storage buckets with bucket-level IAM (no ACLs)
* Grant IAM roles to any `@ucsb.edu` user

### You Cannot
* Create any VPC networks (deny policy blocks `networks.create` for all users)
* Create auto-mode VPCs
* Assign external public IPs to VMs
* Set public access permissions (`allUsers`, `allAuthenticatedUsers`)
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
[ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5). Describe the use case and the specific constraint. The
Cloud Team will evaluate whether an exemption is appropriate.

Exceptions are never granted for constraints that directly support UC IS-3 or
NIST 800-171 compliance requirements.

---

## Platform Admin Roles

Certain platform-level permissions (organization administration, folder
management, and billing account assignments) are reserved for the Campus Cloud
Team and cannot be self-assigned. The IAM Deny Policies above block these
actions for all users except Cloud Team automation accounts. If you need an
action that requires platform-level access, open a
[ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5).
