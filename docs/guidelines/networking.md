---
title: Networking Offerings
description: Networking Offerings and Campus Connectivity
permalink: /docs/guidelines/networking
---

## AWS Networking Architecture

### Introduction

While AWS allows you to create a resource (e.g. EC2 instance) that can be assigned a random public IP address in the AWS address space, an Amazon VPC allows you to create an isolated portion of the AWS cloud for public and/or private subnets in UCSB Campus cloud address space. A VPC provides a number of benefits and is an elementary piece of security in the Cloud.

Review the basic concepts of [AWS networking and VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html).

### Campus Landing Zone Network Architecture
The Landing Zone has a presence in two Regions currently, us-west-2 (Oregon), and, us-east-1 (Virgina).  These regions have advantages in pricing and early AWS feature releases.

#### Production Landing Zone, RFC 1918 Allocation
  - 10.226.0.0/16 (us-west-2)
  - 10.227.0.0/16 (us-east-1)

The Campus Cloud is using the RFC 1918 **PRIVATE** address space within its Organization structure to provide Landing Zone services to the campus community.  This private address space is also being routed over the UCSB campus networks via a VPN Gateway.

The Campus Landing Zone's Network account is at the center of most of the traffic flow. This design provides:

  - Visibility for the Network Operations Center (NOC) for
     - traffic through the transit gateway and to
     - collect and view VPC Flow Logs from individual child accounts
  - VPN connectivity back to the campus network
  - Inter account connectivity and NAT gateway access for private subnets using the transit gateway.
  - Centralizing the cost for some of the traffic flow

#### Landing Zone Network Diagram
![assets/img/UCSB-AWS-LZ-Network-Architecture-Production-Organization.png]({{site.url}}assets/img/UCSB-AWS-LZ-Network-Architecture-Production-Organization.png)

#### How does traffic flow ?
Public and/or private subnets in child account VPCs are using a private address space and therefore require additional networking resources to move traffic between the general internet and campus.  

Public subnet traffic in a child account utilizes the local account Internet Gateway.

Private subnet traffic in a child account will use the Transit Gateway in the Network account, and then either the NAT Gateway or the VPN Gateway depending on the destination. Next, lets define these items:

**Transit Gateway**
The [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) is the networking hub for the Organization.  Each VPC in a child account has one Transit Gateway Attachment allowing traffic to route between VPCs.  The Transit Gateway also provides routes for private subnets in child accounts to reach UCSB (via a VPN) or the general internet (via NAT).  Transit Gateways are region-wide assets.

**NAT Gateway**
The [AWS NAT Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) provides a similar function to a normal NAT gateway in that in enables connectivity for account resources in private subnet while preventing the internet for initiating connections to those resources.

**VPN Gateway** (VPN connection to campus)
The [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) connection to UCSB is attached to the Transit Gateway.  This link is the default route for traffic from any private subnet in a child account to UCSB.  The VPN link is not intended for commodity traffic and should be used when secure network protocols are unavailable.

Note: Resources on public subnets route to UCSB over their own internet gateway.
 
 - Campus-side VPN Endpoints (us-west-2):  128.111.38.197


*IF you are having trouble getting traffic from a private subnet back to campus please see our Best Practice for enabling [VPN traffic]({{ site.baseurl }}/docs/bestpractices/vpn/) back to campus.*

### Campus Cloud Service Catalog VPC Product
The above network resources need to be available to a child account. To simplify the creation of a VPC with these resources configured the Cloud Team has created a, [Simple VPC Service Catalog Product]({{ site.baseurl }}/docs/bestpractices/servicecatalog#VPC) that you "Launch" from your child account.  

The outcome is a functional VPC with private and or public subnets and the required connectivity to the Internet and or Campus. Note: If this VPC Product is not used you will need to setup these resources on your own.
