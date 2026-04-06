---
title: Azure Networking
description: Virtual WAN hub-spoke topology, VNet peering, and campus connectivity for Azure subscriptions.
permalink: /docs/azure/networking
last_reviewed: 2026-04-03
---

# Azure Networking Overview

UCSB Campus Cloud uses **Azure Virtual WAN** with a hub-spoke topology. A
centrally managed hub VNet is maintained by the Cloud Team. Subscription VNets
(spokes) peer to the hub for inter-subscription and campus network connectivity.

---

## Hub-Spoke Topology

```
[Campus Network]
       |
[Azure Virtual WAN Hub — West US 2]
  |         |         |
[VNet A] [VNet B] [VNet C]
(Sub-A)  (Sub-B)  (Sub-C)
```

* The **hub** is managed by the Cloud Team and is not visible in your subscription.
* Your **spoke VNet** peers to the hub and inherits campus network routes.
* Traffic between your VNet and the campus network routes through the hub.

---

## Regions

| Region | Usage |
|---|---|
| West US 2 (Washington) | Primary — use for all new workloads |
| West Central US (Wyoming) | Secondary / DR — use for replication or failover |

Most workloads should be deployed in **West US 2**. All other regions are
blocked by a Deny policy at the management group level.

---

## Requesting a VNet

If your subscription needs a Virtual Network:

1. Open a [ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5).
2. Specify:
   * Subscription name and ID
   * Whether campus connectivity is needed (hub peering)
   * Estimated number of hosts / address space needed
3. The Cloud Team will provision the VNet, allocate an address space from IPAM,
   and configure peering if requested.

**Do not create a VNet yourself unless you have confirmed the address space with
the Cloud Team.** Conflicting address ranges prevent peering from being
established.

---

## Campus Connectivity

{% include alert.html type="info" title="Campus connectivity availability" content="Campus-to-Azure connectivity over the hub VNet is available. Contact the Cloud Team to confirm the current connectivity path and campus firewall requirements for your use case." %}

Azure Virtual WAN supports **Site-to-Site VPN** connections as the path between the
hub and the UCSB campus network. When hub peering is configured on your VNet,
traffic to campus CIDRs will route through the hub automatically.

---

## Network Security

### Network Security Groups (NSGs)
* NSGs are your primary mechanism for controlling inbound and outbound traffic.
* Apply NSGs at the subnet level (recommended) or NIC level.
* Avoid rules that allow `0.0.0.0/0` on administrative ports (22, 3389).
* Azure Policy requires NSG Flow Logs to be enabled — this is configured
  automatically on provisioning. Do not disable flow logs.

### Azure Firewall
* A shared Azure Firewall may be deployed in the hub for central egress filtering.
* Contact the Cloud Team if you need to allow specific outbound traffic that is
  being blocked.

---

## DNS

* Azure-provided DNS (`168.63.129.16`) is configured by default in all VNets.
* Private DNS zones are available for internal service name resolution.
* Contact the Cloud Team to register a CNAME or A record in a UCSB-owned
  public DNS zone.

---

## Off-Campus Access

To reach resources in your Azure VNet from off campus:

1. Connect to the [UCSB campus VPN](https://it.ucsb.edu/network-infrastructure-services/ivanti-connect-secure-campus-vpn) on your laptop.
2. Once on VPN, your traffic routes through the campus network → Virtual WAN
   hub → your spoke VNet.

VM management should be done via **Azure Bastion** (browser-based SSH/RDP)
rather than opening SSH/RDP ports to the internet.
