---
title: AWS Networking
description: VPC options, campus connectivity, Transit Gateway, and IP address management for AWS accounts.
permalink: /docs/aws/networking
last_reviewed: 2026-10-30
redirect_from:
  - /docs/bestpractices/vpn
  - /docs/guidelines/networking
---

<!-- markdownlint-disable-next-line MD022 -->
# AWS Networking Overview
{:.no_toc}

UCSB Campus Cloud uses **AWS Transit Gateway** as the central hub for network
connectivity. Every account that needs to reach the campus network receives a
Virtual Private Cloud (VPC), a private network in AWS, attached to the Transit
Gateway. Internet-only accounts use standalone VPCs
without a Transit Gateway attachment.

* TOC
{:toc}

---

## How to Connect to Campus

UCSB has **two AWS Direct Connect connections** and a **Site-to-Site VPN**
between AWS and the UCSB campus network. All three connect in us-west-2.
VPCs in us-east-1 reach campus through us-west-2.

| Link | Region | Purpose |
|---|---|---|
| Direct Connect connection 1 | us-west-2 | Campus connectivity |
| Direct Connect connection 2 | us-west-2 | Campus connectivity, from a second location, so one connection can fail without an outage |
| Site-to-Site VPN (an encrypted tunnel over the internet) | us-west-2 | Backup if both Direct Connect connections fail |

Routing preference: Direct Connect → Site-to-Site VPN. Failover is automatic
and transparent to workloads. Traffic from your VPC to campus resources routes
through the Transit Gateway — you do not need to configure this yourself.

---

## Requesting Networking Changes

Open a
[ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5)
for any lasting change to how your VPC connects to other networks:

* **More IP addresses** for your VPC (a new IP address range, also called a
  Classless Inter-Domain Routing (CIDR) block).
* **Connecting a VPC** to the Transit Gateway, so it can reach campus.
* **Changing which networks your VPC can reach** through the Transit Gateway,
  such as campus or another VPC. The Cloud Team makes these changes to the
  Transit Gateway's routing, which works like a shared address book of where to
  send traffic.

Day-to-day changes to Security Groups and network access control lists (NACLs)
within your account do not need a ticket. To open access on the campus side,
see [Campus Network Firewall](#campus-network-firewall).

---

## Security Groups and NACLs

* You manage Security Groups for your own resources.
* NACLs are available but Security Groups are the preferred method.
* [Service Control Policies (SCPs)]({{ "/docs/aws/guardrails" | relative_url }})
  do not restrict Security Group rules, but best practices apply:
  * Avoid `0.0.0.0/0` inbound on sensitive ports (22, 3389, database ports).
  * Prefer inbound rules scoped to campus CIDR ranges for administrative access.

**Other Campus Cloud VPCs can reach yours.** Every VPC attached to the Transit
Gateway has a network route to every other attached VPC, including VPCs in
other departments' accounts. Only your Security Groups and network ACLs stand
between them. Scope inbound rules to the specific sources that need access —
not the whole Landing Zone range (`10.226.0.0/15`).

---

## DNS

* VPCs the Cloud Team creates look up names with the Domain Name System (DNS)
  service that AWS provides. It finds public names, including public
  `ucsb.edu` names.
* Private hosted zones in Route 53 are available for internal service discovery.
* There is no UCSB-managed internal DNS zone shared by default. Each team
  manages its own private hosted zones.
* Names that exist only on the campus network don't resolve from AWS by
  default. If your workload needs them, you can set up
  [Route 53 Resolver forwarding](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-outbound-queries.html)
  in your account to send those lookups to campus. Open a
  [ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5)
  if you need help.
* Contact the Cloud Team if you need a CNAME or A record in a UCSB-owned public
  DNS zone.

---

## Off-Campus Access

To reach resources in your Campus Cloud VPC from a laptop that is **not** on the
UCSB campus network, use **Secure Service Access (SSA)**. SSA uses the Zscaler Client Connector,
which you install on your laptop and sign in to with UCSB SSO. It replaces the
Campus VPN (Ivanti), which is being retired on January 22, 2027. SSA is
licensed to faculty, staff, and student employees. To get the connector, see
[Secure Service Access (SSA)](https://it.ucsb.edu/services/secure-service-access).

{% include alert.html type="info" title="SSA is for your laptop, not for servers" content="Cloud workloads (EC2, Lambda, containers) inside a campus-connected VPC can reach campus resources directly through the Transit Gateway. SSA is only for your laptop or workstation when working off campus." %}

---

## Campus Network Firewall

Traffic from AWS to campus resources passes through the UCSB campus firewall.
If you need to allow traffic from AWS to a specific campus host or service:

1. Identify the source addresses the campus host will see:
   * From a **private subnet**, traffic reaches campus through Direct Connect
     with its private IP address. Use your VPC's IP address range (its CIDR
     block, shown in the VPC console, within `10.226.0.0/16` or
     `10.227.0.0/16`). Do not use the shared Network Address Translation (NAT)
     Gateway IPs listed under [Egress IP Addresses](#egress-ip-addresses); those
     apply only to internet traffic.
   * From a **public subnet**, traffic reaches campus over the internet, from
     the resource's public IP address.
2. Submit a firewall rule request through the appropriate campus IT process for
   your department.

---

## Troubleshooting Connectivity

### Cannot Reach a Campus Resource from AWS

1. Verify the EC2 instance is in a **private subnet** of a campus-connected
   VPC. Public subnets have no route to campus over Direct Connect.
2. Check the Security Group allows outbound to the campus IP range.
3. Verify the campus firewall allows inbound from your VPC's IP address range
   (see [Campus Network Firewall](#campus-network-firewall)). Request firewall
   changes through your department IT if needed.
4. Check that the campus host's local firewall accepts traffic from your VPC's
   IP address range.

### Cannot Reach a Private IP in AWS from Your Laptop

1. Confirm the Zscaler Client Connector is turned on and signed in (see
   [Off-Campus Access](#off-campus-access)).
2. Confirm the resource's Security Group allows inbound traffic from the campus
   CIDR ranges (`128.111.0.0/16` and `169.231.0.0/16`).
3. Confirm the VPC has a Transit Gateway attachment
   (Console → VPC → Transit Gateway Attachments).
4. Ping or traceroute from your laptop to inspect where the path breaks.
5. If all of the above are correct, the issue may be a campus host-based firewall
   or the campus network firewall. Contact the
   [ITS Service Desk](https://ithelp.ucsb.edu) and ask for the Network
   Operations Center (NOC).

### High Latency Between Campus and AWS

* Direct Connect should show < 5 ms latency to us-west-2 and < 60 ms to
  us-east-1.
* Latency significantly above these values may indicate the Site-to-Site VPN
  failover path is in use. Check the
  [AWS Health Dashboard](https://health.aws.amazon.com/health/status) and open a
  [ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5)
  if the issue persists.

---

## Network Architecture Details

This section provides technical details about the Landing Zone network
infrastructure for users who need them for firewall rules, troubleshooting, or
vendor allowlisting.

### Architecture Diagram

![Diagram of the Campus Cloud AWS network. The same information is described in text in the paragraph below the diagram.]({{ "/assets/img/UCSB-AWS-LZ-Network-Architecture-v3.png" | relative_url }})

The diagram shows two regions. In us-west-2, the campus network connects to
the Cloud Team's Transit Gateway through two Direct Connect connections, with a
Site-to-Site VPN as backup. The us-east-1 Transit Gateway reaches campus
through us-west-2. Private subnets in your VPC send traffic that leaves the VPC
to the Transit Gateway, which sends internet traffic out through the shared NAT
Gateways. The exception is Amazon S3 in the same region, which private subnets
reach through an S3 gateway endpoint. Public subnets use your VPC's own
Internet Gateway and have no route to campus. The
sections [How to Connect to Campus](#how-to-connect-to-campus),
[How Traffic Flows](#how-traffic-flows), and
[Egress IP Addresses](#egress-ip-addresses) give the details.
[View the diagram at full size]({{ "/assets/img/UCSB-AWS-LZ-Network-Architecture-v3.png" | relative_url }}).

### Regions and IP Address Space

The Landing Zone is deployed in two regions:

| Region | Location | Private CIDR Allocation |
|---|---|---|
| us-west-2 | Oregon | 10.226.0.0/16 |
| us-east-1 | N. Virginia | 10.227.0.0/16 |

These private addresses ([RFC 1918]({{ "/glossary/" | relative_url }})) are routed between AWS and the UCSB campus
network. Individual account VPCs receive a smaller block (from /27 to /24,
depending on the [VPC family](#vpc-families)) from these ranges via the Cloud
Team's IP address management system.

Do **not** manually assign a CIDR that overlaps with these ranges or with the
UCSB campus address space (`128.111.0.0/16`, `169.231.0.0/16`). Conflicts will
break routing.

### How Traffic Flows

* **Public subnet** traffic in your account goes directly through the account's
  Internet Gateway — it does not travel through the Transit Gateway, so it
  cannot reach campus or other Campus Cloud VPCs over private addresses.
* **Private subnet** traffic that leaves your VPC routes to the Transit
  Gateway, which sends it
  to one of:
  * The central **NAT Gateway** (for internet-bound traffic),
  * **Direct Connect / VPN** (for campus-bound traffic), or
  * Another Campus Cloud VPC.
* **Amazon S3** traffic from private subnets to buckets in the same region
  uses a
  [gateway endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html)
  in your VPC. It stays on the AWS network and does not use the NAT Gateway.
  Requests to buckets in another region go through the NAT Gateway like other
  internet traffic.

### Egress IP Addresses

Traffic leaving your private subnets to the internet appears to come from
centrally managed NAT Gateway IP addresses.

{% include alert.html type="warning" title="These IPs may change" content="The NAT Gateway addresses change only if the Cloud Team replaces the NAT Gateways, which is rare. Before you use them for vendor allowlisting or firewall rules, confirm the current list with the Cloud Team via a ServiceNow ticket. Amazon S3 requests from private subnets to buckets in the same region do not come from these addresses; requests to buckets in another region do (see How Traffic Flows)." %}

| Region | NAT Gateway IPs |
|---|---|
| us-west-2 | `44.231.186.204`, `44.232.156.254` |
| us-east-1 | `3.213.17.213`, `54.86.139.106` |

**Campus-side VPN endpoint (us-west-2):** `128.111.38.197`

For the most current values, open a
[ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5).

### Public IP Addresses

* Internet-facing resources (load balancers, EC2 instances in public subnets)
  can use Elastic IPs or auto-assigned public IPs.
* If your workload needs a persistent public IP, allocate an Elastic IP in your
  account.
* IPv6 is not set up. The VPCs the Cloud Team creates use IPv4 addresses only,
  and the connection to campus carries IPv4 only.

---

## VPC Options

When your account is provisioned, the Cloud Team creates a VPC using one of two
product types from the
[Service Catalog]({{ "/docs/aws/service-catalog" | relative_url }}):

| VPC Type | Subnets | Campus Network Access | Use When |
|---|---|---|---|
| Simple VPC with Campus Connectivity | Yes — you choose a family (below) | Yes, via Transit Gateway, for families with a private subnet. `*.public` families have no campus connection | Most workloads — running servers, databases, or anything needing network connectivity |
| Advanced VPC | No — an empty VPC you build out yourself | Not by default — the product does not create a Transit Gateway attachment, so you configure any campus connection yourself | You need full control over your network design from scratch |

Specify which type you need in your account request or
[ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5).
You can have both types in the same account.

### VPC Families

When you launch the **Simple VPC** product, choose a **family** that determines
the number of subnets, their type, and the total IP address space:

| Family | Subnets | IPs | Subnet Type | Availability Zones |
|---|---|---|---|---|
| n1.small.public | 1 | 32 | 1 public | 1 |
| n1.small.private | 1 | 32 | 1 private | 1 |
| n1.medium.public | 1 | 64 | 1 public | 1 |
| n1.medium.private | 1 | 64 | 1 private | 1 |
| n1.large.public | 1 | 128 | 1 public | 1 |
| n1.large.private | 1 | 128 | 1 private | 1 |
| n2.medium.public | 2 | 64 | 2 public | 2 |
| n2.medium.private | 2 | 64 | 2 private | 2 |
| n2.medium.mixed | 2 | 64 | 1 public, 1 private | 1 |
| n2.large.public | 2 | 128 | 2 public | 2 |
| n2.large.private | 2 | 128 | 2 private | 2 |
| n2.large.mixed | 2 | 128 | 1 public, 1 private | 1 |
| n4.large.mixed | 4 | 128 | 2 public, 2 private | 2 |
| n2.xlarge.public | 2 | 256 | 2 public | 2 |
| n2.xlarge.private | 2 | 256 | 2 private | 2 |
| n2.xlarge.mixed | 2 | 256 | 1 public, 1 private | 1 |
| n4.xlarge.mixed | 4 | 256 | 2 public, 2 private | 2 |

The `n2.*.public`, `n2.*.private`, and `n4.*` families spread subnets across two
Availability Zones (AZs) for higher availability. The `n2.*.mixed` families put
both subnets in a **single AZ**. If you need public and private subnets in two
AZs, choose `n4.large.mixed` or `n4.xlarge.mixed`.

Families with a private subnet (`*.private` and `*.mixed`) are attached to the
Transit Gateway and can reach campus. `*.public` families are not.
