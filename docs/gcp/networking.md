---
title: GCP Networking
description: VPC configuration, org policy constraints, campus connectivity, and networking rules for GCP projects.
permalink: /docs/gcp/networking
last_reviewed: 2026-03-30
---

## GCP Networking Overview

GCP networking in Campus Cloud is governed by organization policies that
enforce a secure network baseline across all projects. Key rules:

* **Custom-mode VPCs only** — Auto-mode VPC networks are blocked.
* **No external (public) IP addresses on VMs** — VMs must use private IPs only.
* **Allowed regions:** us-central1 (Iowa) and us-west1 (Oregon).

---

## Creating a VPC

**Auto-mode VPC creation is blocked by org policy.** All VPCs must be
custom-mode, where you define subnets manually.

To create a custom-mode VPC:

1. Navigate to **VPC Network → VPC networks → + Create VPC network**.
2. Under **Subnet creation mode**, select **Custom**.
3. Add one or more subnets in `us-central1` or `us-west1`.
4. Apply a subnet CIDR from RFC 1918 address space — coordinate with the
   Cloud Team to avoid conflicts with Shared VPC or on-premises ranges.
5. Enable **Private Google Access** on each subnet to allow VMs to reach
   Google APIs without an external IP.

---

## External IP Addresses

**VMs cannot have external (public) IP addresses by default.**

An org policy constraint blocks assignment of external IPs to VM instances.
This means:

* VMs are not directly reachable from the internet.
* VMs can still reach the internet for outbound traffic via **Cloud NAT**.
* If you need inbound internet traffic, use a **Cloud Load Balancer** in front
  of your VMs.

If you need an external IP for a specific workload, open a ServiceNow ticket
with a justification. Exceptions are reviewed individually.

---

## Cloud NAT (Outbound Internet Access)

To allow your VMs internet access without public IPs:

1. Navigate to your VPC in the console → **Cloud NAT**.
2. Click **+ Create Cloud NAT gateway**.
3. Select the VPC network, region, and Cloud Router (create one if needed).
4. Configure NAT IP allocation (auto or manual).

With Cloud NAT configured, VMs with only private IPs can make outbound internet
connections through the NAT gateway.

---

## Campus Connectivity

To route traffic between your GCP project and the UCSB campus network, contact
the Cloud Team. Campus-to-GCP connectivity options include:

* **Cloud VPN** — encrypted tunnel over the internet between GCP and the UCSB
  campus firewall. Suitable for most research workloads.
* **Cloud Interconnect** — dedicated private connectivity (if available).

Campus connectivity must be requested via ServiceNow and is provisioned by the
Cloud Team. It is not self-service.

---

## Shared VPC

For projects that need to share a VPC with other projects (e.g., a shared
network for a research group), the Cloud Team can configure Shared VPC:

* One **host project** owns the VPC and subnets.
* One or more **service projects** consume the shared network.

Contact the Cloud Team if your use case requires Shared VPC.

---

## Firewall Rules

GCP firewall rules control ingress and egress at the VPC level:

* Implicit deny-all ingress is the default — you must explicitly allow traffic.
* Best practice: allow only the minimum required ports from specific IP ranges.
* Avoid `0.0.0.0/0` inbound rules on administrative ports (22, 3389).
* Use **service account–based firewall rules** for VM-to-VM traffic within the
  project.

---

## Cloud DNS

* Each VPC has an implicit DNS resolver at the VPC's default gateway address.
* Private zones in Cloud DNS are available for internal name resolution.
* Contact the Cloud Team to register a record in a UCSB-owned public DNS zone.

---

## Off-Campus Access to Private VMs

To access a private GCP VM from off campus:

1. Connect to **UCSB ConnectUCSB GlobalProtect VPN** on your laptop.
2. Use **Identity-Aware Proxy (IAP) TCP tunneling** for SSH/RDP without a
   public IP:
   ```bash
   gcloud compute ssh <instance-name> --tunnel-through-iap --project <project-id>
   ```
3. IAP tunneling works over HTTPS (port 443) and does not require a VPN, but
   does require the `roles/iap.tunnelResourceAccessor` IAM permission.

IAP is the recommended method for SSH access to GCP VMs.
