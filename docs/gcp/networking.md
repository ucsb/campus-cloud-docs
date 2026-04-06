---
title: GCP Networking
description: Networking constraints, current limitations, and how to request network resources for GCP projects.
permalink: /docs/gcp/networking
last_reviewed: 2026-04-06
---

# GCP Networking Overview

Networking in the GCP Campus Cloud is centrally managed. **You cannot create
VPC networks yourself** — a deny policy blocks VPC creation for all users. Only
the Cloud Team's automation account can provision network resources.

If your project needs networking, open a [ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5) to request it.

---

## Current State

| Capability | Available? |
|---|---|
| User-created VPCs | No — blocked by policy |
| Internet egress via Cloud NAT | Provisioned with your VPC — provides outbound internet access |
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
  Outbound internet access is provided via Cloud NAT.
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
SSH and RDP access. IAP tunnels traffic securely without requiring a VPN or
public IP.

See Google's official guide: [Using IAP for TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding)

### Network Tags for IAP Access

Your VM must have the correct **network tag** for IAP to reach it. Without
these tags, no inbound traffic is allowed — not from the internet, not from
IAP.

| Network Tag | What It Enables |
|---|---|
| `allow-iap-ssh` | SSH access (port 22) via IAP |
| `allow-iap-rdp` | RDP access (port 3389) via IAP |
| `allow-win-activation` | Windows license activation (KMS egress) |

**How to add a network tag:**

* **Console:** Go to your VM instance → **Edit** → scroll to **Networking** →
  enter the tag name in the **Network tags** field → **Save**.
* **gcloud:** `gcloud compute instances create my-vm --tags=allow-iap-ssh`
  (or add to an existing VM with `gcloud compute instances add-tags`).
* **Terraform:** Add `tags = ["allow-iap-ssh"]` to your
  `google_compute_instance` resource.

{% include alert.html type="info" title="Network tags are not Resource Manager Tags" content="Network tags are simple strings on a VM used for firewall targeting. They are separate from Resource Manager Tags (the structured key-value pairs like <code>environment=prod</code> used for billing and compliance)." %}

### SSH Access

* **Console SSH button:** Open the VM in the Cloud Console and click
  **SSH**. This uses IAP automatically — no local software needed.
* **gcloud:** `gcloud compute ssh VM_NAME --tunnel-through-iap`

### RDP Access

* **IAP Desktop (recommended):** Download
  [IAP Desktop](https://googlecloudplatform.github.io/iap-desktop/) — a
  free Windows app that handles IAP tunneling and RDP in a single window. No
  `gcloud` installation required.
* **gcloud tunnel:** `gcloud compute start-iap-tunnel VM_NAME 3389
  --local-host-port=localhost:3389`, then connect your RDP client to
  `localhost:3389`.

### Required IAM Roles

To connect via IAP, users need:

* `roles/iap.tunnelResourceAccessor` — permission to create IAP tunnels
* `roles/compute.osLogin` (or `roles/compute.osAdminLogin`) — OS Login
  access to the VM

### OS Login

[OS Login](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin)
is **enforced by org policy** across all GCP Campus Cloud projects. This
means SSH access uses your Google identity — there are no project-wide SSH
keys to manage, share, or rotate.

What this means for you:

* **Console SSH just works.** Click the SSH button in the Cloud Console; it
  handles OS Login automatically.
* **gcloud SSH just works.** `gcloud compute ssh` uses your Google identity
  by default.
* **You cannot disable OS Login** in project metadata. The org policy
  overrides any project-level setting.
* **Traditional SSH keys** (project metadata or instance metadata) are
  ignored when OS Login is enforced.

If your project has a specific need to disable OS Login (e.g. a Marketplace
image that is incompatible), open a
[ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5)
and the Cloud Team will evaluate an exception.

---

## Public-Facing Services

**Serverless services** like Cloud Run, Cloud Functions, and API Gateway can
serve public internet traffic by default — no org policy exception is needed.

For **VM-based workloads** that need a public-facing endpoint (e.g., a web
application behind a load balancer), open a
[ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5).
The Cloud Team will provision an external
[Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/application-load-balancer)
with
[Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)
(Google's WAF and DDoS protection) on your behalf. You cannot create
external load balancers yourself — they are blocked by org policy.

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

