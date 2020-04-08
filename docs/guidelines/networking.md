---
title: Networking Offerings
description: Networking Offerings and Campus Connectivity
permalink: /docs/guidelines/networking
---

## AWS Networking Architecture

Introduction


![assets/img/UCSB-AWS-LZ-Network-Architecture-Production-Organization.png]({{site.url}}assets/img/gatewayhome.png)


AWS Production Landing Zone
RFC 1918 Allocation
10.226.0.0/16 (us-west-2)
10.227.0.0/16 (us-east-1)

Campus-side VPN Endpoints (us-west-2)
128.111.38.197

Transit Gateway
The Transit Gateway is the networking hub for the organization.  Each VPC in a child account has one Transit Gateway Attachment allowing traffic to route between VPCs.  The Transit Gateway also provides routes for private subnets in child accounts to reach UCSB (via a VPN) or the general internet (via NAT).  Transit Gateways are region-wide assets.

Campus VPN Connection
The VPN connection to UCSB is attached to the Transit Gateway.  This link is the default route for traffic from any private subnet on a child account to UCSB.  Note: Resources on public subnets route to UCSB over their own internet gateway.
