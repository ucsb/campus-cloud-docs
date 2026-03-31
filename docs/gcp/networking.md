---
title: GCP Networking
description: Networking constraints, current limitations, and how to request network resources for GCP projects.
permalink: /docs/gcp/networking
last_reviewed: 2026-03-30
---

## GCP Networking Overview

Networking in the GCP Campus Cloud is centrally managed. **You cannot create
VPC networks yourself** — a deny policy blocks VPC creation for all users. Only
the Cloud Team's automation account can provision network resources.

If your project needs networking, open a [ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5) to request it.

---

## Current State

| Capability | Available? |
|---|---|
| User-created VPCs | No — blocked by policy |
| Internet egress via Cloud NAT | Not required — outbound internet traffic is not restricted |
| VPC peering | Not available (VPC creation is blocked; contact Cloud Team if needed) |
| Shared VPC attachment | Not available (contact Cloud Team if needed) |

{% include alert.html type="warning" title="Campus connectivity not available" content="There is currently no VPN or Interconnect between GCP and the UCSB campus network. If your workload requires campus connectivity, contact the Cloud Team to discuss options." %}

---

## Org Policy Networking Constraints

The following constraints are enforced across all projects:

* **No VPC creation** — users cannot create VPC networks; only the Cloud
  Team's automation can provision them.
* **Custom-mode VPCs only** — auto-mode VPCs (which create subnets in every
  region) are blocked by a custom constraint.
* **No external IP addresses on VMs** — VMs may not have public IPs.
* **Allowed regions:** us-central1 (Iowa) and us-west1 (Oregon) only.
* **VPC flow logs required** — subnets without flow logs cannot be created.

---

## Requesting Network Resources

All networking must be provisioned by the Cloud Team. Submit a [ServiceNow
ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5) (Cloud Services) with:

* Your GCP project ID
* The connectivity you need (Cloud NAT, a VPC subnet, etc.)
* The region (us-central1 or us-west1)
* Any specific CIDR or peering requirements

---

## Accessing Private VMs Without a Public IP

Since VMs cannot have external IPs, use **Identity-Aware Proxy (IAP)** for
browser-based SSH and RDP access. IAP tunnels traffic securely without
requiring a VPN or public IP.

**Requirements:** the `roles/iap.tunnelResourceAccessor` IAM permission on
the target VM or project, and the `gcloud` CLI.

```bash
gcloud compute ssh INSTANCE_NAME --tunnel-through-iap --project PROJECT_ID --zone ZONE
```

IAP is the recommended and supported method for interactive access to GCP VMs.

---

## Services That Work Without a VPC

Many GCP services do not require a VPC at all:

* Cloud Storage
* BigQuery
* Pub/Sub
* Cloud Functions
* Cloud Run
* Vertex AI

If your workload uses only managed services, you may not need to request
network provisioning.

