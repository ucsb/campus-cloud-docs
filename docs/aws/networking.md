---
title: AWS Networking
description: VPC options, campus connectivity, Transit Gateway, and IP address management for AWS accounts.
permalink: /docs/aws/networking
last_reviewed: 2026-03-30
redirect_from:
  - /docs/bestpractices/vpn
  - /docs/guidelines/networking
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

| Link | Type | Regions | Purpose |
|---|---|---|---|
| Direct Connect Circuit 1 | Private VIF | us-east-1, us-west-2 | Primary campus connectivity |
| Direct Connect Circuit 2 | Private VIF | us-east-1, us-west-2 | Redundancy / failover |
| Site-to-Site VPN | IPsec over internet | us-east-1, us-west-2 | Tertiary failover |

Routing preference: Direct Connect → Site-to-Site VPN. Failover is automatic
and generally transparent to workloads. Traffic from your VPC to campus
resources routes through the Transit Gateway automatically — you do not need to
configure this yourself.

{% include alert.html type="info" title="Campus VPN not needed for cloud workloads" content="If your EC2 instance or Lambda is inside a VPC attached to the Transit Gateway, it can reach campus resources directly — you do not need to run the campus VPN on the server. The VPN is for your laptop, not for cloud workloads." %}

---

## VPC Families (Service Catalog)

When you request a VPC, the Cloud Team (or Service Catalog) creates a VPC in
one of the following families. The family determines the IP address range and
whether a Transit Gateway attachment is included.

| Family | Use Case | TGW Attached | Approx CIDR |
|---|---|---|---|
| Campus-connected | Access campus file systems, on-prem databases | Yes | /24 from enterprise range |
| Internet-only | Public-facing apps with no campus dependency | No | /24 from RFC 1918 range |

Specify which family you need in your account request or [ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5). You
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
external vendor, open a [ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5) and the Cloud Team will provide the
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

## Campus Network Firewall

Traffic from AWS to campus resources passes through the UCSB campus firewall.
If you need to allow traffic from AWS to a specific campus host or service:

1. Identify the AWS egress IP range (ask the Cloud Team).
2. Submit a firewall rule request through the appropriate campus IT process for
   your department.

---

## Requesting Networking Changes

All persistent networking changes (new CIDR, new TGW attachment, firewall rule
changes at the TGW level) require a [ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5). Day-to-day Security
Group and NACL changes within your account do not require a ticket.

---

## VPN Client Access

If you need to connect to resources in a Campus Cloud VPC from a laptop or
workstation that is not on the UCSB campus network:

1. Connect to the **UCSB campus VPN** on your endpoint.
2. The VPN routes your traffic through the campus network → Direct Connect →
   Transit Gateway → your VPC.

Download and configure the VPN client at:
[https://it.ucsb.edu/network-infrastructure-services/ivanti-connect-secure-campus-vpn](https://it.ucsb.edu/network-infrastructure-services/ivanti-connect-secure-campus-vpn)

{% include alert.html type="info" title="VPN is for your laptop, not for servers" content="Cloud workloads (EC2, Lambda, containers) inside a campus-connected VPC can reach campus resources directly through the Transit Gateway. The campus VPN is only for your laptop or workstation when working off-campus." %}

---

## Troubleshooting Connectivity

### Cannot Reach a Private IP in AWS

1. Confirm you are connected to the campus VPN (check the tray icon).
2. Confirm the resource's Security Group allows inbound traffic from the campus
   CIDR ranges. Ask the Cloud Team for the current list if unsure.
3. Confirm the VPC has a Transit Gateway attachment
   (Console → VPC → Transit Gateway Attachments).
4. Ping or traceroute from your laptop to inspect where the path breaks.

### High Latency Between Campus and AWS

* Direct Connect should show < 5 ms latency to us-west-2 and < 60 ms to us-east-1.
* Latency significantly above these values may indicate the VPN failover path is
  in use. Check the AWS Health Dashboard and open a [ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5) if the
  issue persists.

### Resource Inside AWS Cannot Reach Campus

1. Verify the EC2 instance is in a campus-connected VPC (not an internet-only VPC).
2. Check the Security Group allows outbound to the campus IP range.
3. Verify the campus firewall allows inbound from the AWS egress IP range.
   (Contact the Cloud Team for the AWS NAT IPs to whitelist.)

---


