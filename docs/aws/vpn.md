---
title: AWS VPN & Campus Connectivity
description: Using the UCSB VPN to reach resources in Campus Cloud AWS accounts from off-campus.
permalink: /docs/aws/vpn
last_reviewed: 2026-03-30
---

## VPN and Campus Connectivity

Campus Cloud AWS accounts with campus-connected VPCs route traffic through a
combination of **AWS Direct Connect** (primary) and **Site-to-Site VPN**
(backup) links between AWS and the UCSB campus network. This connectivity is
managed by the Cloud Team and is transparent to workloads running inside the VPC.

---

## Accessing AWS Resources From Your Laptop

If you are working off campus and need to connect to a private IP address in a
campus-connected AWS VPC (e.g., an RDS database, an EC2 instance without a
public IP, or an internal load balancer):

1. Connect to **UCSB ConnectUCSB GlobalProtect VPN** on your laptop.
2. Once on VPN, your traffic routes through the campus network → Direct Connect
   → Transit Gateway → your VPC.

**You do not need a separate AWS VPN Client or any additional configuration.**
The campus VPN is sufficient.

{% include alert.html type="info" title="VPN for your laptop, not for servers" content="Cloud workloads (EC2, Lambda, containers) that are already inside a campus-connected VPC do not need VPN. The VPN is only for your laptop or workstation when working off-campus." %}

---

## Setting Up GlobalProtect

Download and configure the UCSB ConnectUCSB VPN client:

* Instructions: [www.connect.ucsb.edu](https://www.connect.ucsb.edu/)
* Gateway: `connect.ucsb.edu`
* Authentication: UCSB NetID + Duo MFA

---

## Troubleshooting Connectivity

### Issue: Cannot Reach a Private IP in AWS

1. Confirm you are connected to GlobalProtect VPN (check the tray icon).
2. Confirm the resource's Security Group allows inbound traffic from the campus
   CIDR ranges. Ask the Cloud Team for the current list if unsure.
3. Confirm the VPC in your account has a Transit Gateway attachment
   (Console → VPC → Transit Gateway Attachments).
4. Ping or traceroute from your laptop — inspect where the path breaks.

### Issue: High Latency Between Campus and AWS

* Direct Connect should show < 5 ms latency to us-west-2 and < 60 ms to us-east-1.
* Latency significantly above these values may indicate the VPN failover path is
  in use. Check the AWS Health Dashboard and open a ServiceNow ticket if the
  issue persists.

### Issue: Resource Inside AWS Cannot Reach Campus

1. Verify the EC2 instance is in a campus-connected VPC (not the internet-only VPC).
2. Check the Security Group allows outbound to the campus IP range.
3. Verify the campus firewall allows inbound from the AWS egress IP range.
   (Contact the Cloud Team for the AWS NAT IPs to whitelist.)

---

## Direct Connect and Site-to-Site VPN Details

| Link | Type | Regions | Purpose |
|---|---|---|---|
| Direct Connect Circuit 1 | Private VIF | us-east-1, us-west-2 | Primary campus connectivity |
| Direct Connect Circuit 2 | Private VIF | us-east-1, us-west-2 | Redundancy / failover |
| Site-to-Site VPN | IPsec over internet | us-east-1, us-west-2 | Tertiary failover |

The routing preference is: Direct Connect → Site-to-Site VPN. Failover is
automatic and generally transparent to workloads.

---

## Campus Network Firewall

Traffic from AWS to campus resources passes through the UCSB campus firewall.
If you need to allow traffic from AWS to a specific campus host or service:

1. Identify the AWS egress IP range (ask the Cloud Team).
2. Submit a firewall rule request through the appropriate campus IT process for
   your department.
