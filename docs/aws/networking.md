---
title: AWS Networking
description: VPC options, campus connectivity, Transit Gateway, and IP address management for AWS accounts.
permalink: /docs/aws/networking
last_reviewed: 2026-03-30
---

## AWS Networking Overview

UCSB Campus Cloud uses **AWS Transit Gateway** as the central hub for network
connectivity. Every account that needs to reach the campus network receives a
VPC that is attached to the Transit Gateway. Internet-only accounts use
standalone VPCs without a Transit Gateway attachment.

---

## How to Connect to Campus

UCSB has **two AWS Direct Connect connections** and a **Site-to-Site VPN** between
the AWS us-east-1 / us-west-2 regions and the UCSB campus network:

* **AWS Direct Connect** — two dedicated private circuits (primary path)
* **AWS Site-to-Site VPN** — encrypted tunnel over the internet (backup path)

Traffic from your VPC to campus resources automatically routes through the
Transit Gateway and uses the best available path. You do not need to configure
this yourself.

{% include alert.html type="info" title="ConnectUCSB VPN not needed" content="If your EC2 instance or Lambda is inside a VPC attached to the Transit Gateway, it can reach campus resources directly — you do not need to run the ConnectUCSB VPN on the server. The GlobalProtect VPN is for your laptop, not for cloud workloads." %}

---

## VPC Families (Service Catalog)

When you request a VPC, the Cloud Team (or Service Catalog) creates a VPC in
one of the following families. The family determines the IP address range and
whether a Transit Gateway attachment is included.

| Family | Use Case | TGW Attached | Approx CIDR |
|---|---|---|---|
| Campus-connected | Access campus file systems, on-prem databases | Yes | /24 from enterprise range |
| Internet-only | Public-facing apps with no campus dependency | No | /24 from RFC 1918 range |

Specify which family you need in your account request or ServiceNow ticket. You
can have both types in the same account.

---

## IP Address Management (IPAM)

UCSB uses **AWS IPAM** to manage IP address space across all accounts
in the organization. CIDR blocks for campus-connected VPCs are assigned by
the Cloud Team from a shared pool.

Do **not** manually assign a CIDR that conflicts with campus address space
(172.16.0.0/12 or 10.0.0.0/8 subnets used by UCSB). Conflicts will prevent
routing and cause VPN connectivity failures.

---

## Egress IP Addresses

Traffic leaving your account to the internet will appear to come from UCSB-managed
NAT Gateway IP addresses. If you need to whitelist UCSB cloud egress IPs with an
external vendor, open a ServiceNow ticket and the Cloud Team will provide the
current IP list.

---

## Public IP Addresses

* Internet-facing resources (load balancers, EC2 instances with public subnets)
  can use Elastic IPs or auto-assigned public IPs.
* If your workload needs a persistent public IP address, allocate an Elastic IP
  in your account.
* IPv6 is not currently available in Campus Cloud accounts.

---

## Security Groups and NACLs

* You are responsible for designing and maintaining Security Groups for your
  resources.
* Network ACLs are available but Security Groups are the preferred method.
* SCPs do not restrict Security Group rules, but best practices apply:
  * Avoid `0.0.0.0/0` inbound on sensitive ports (22, 3389, database ports).
  * Prefer inbound rules scoped to campus CIDR ranges for administrative access.

---

## DNS

* Private hosted zones in Route 53 are available for internal service discovery.
* There is no UCSB-managed internal DNS zone shared by default. Each team manages
  its own private hosted zones.
* Contact the Cloud Team if you need a CNAME or A record in a UCSB-owned public
  DNS zone.

---

## VPN Client Access

If you need to connect to resources in a Campus Cloud VPC from a laptop or
workstation that is not on the UCSB campus network:

1. Use the **UCSB ConnectUCSB GlobalProtect VPN** on your endpoint.
2. ConnectUCSB routes your traffic through the campus network, which then
   reaches the Transit Gateway and your VPC.
3. See [VPN Setup](/docs/aws/vpn) for configuration details.

---

## Requesting Networking Changes

All persistent networking changes (new CIDR, new TGW attachment, firewall rule
changes at the TGW level) require a ServiceNow ticket. Day-to-day Security
Group and NACL changes within your account do not require a ticket.
