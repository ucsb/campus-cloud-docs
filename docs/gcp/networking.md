---
title: GCP Networking
description: Networking constraints, current limitations, and how to request network resources for GCP projects.
permalink: /docs/gcp/networking
last_reviewed: 2026-11-18
---

# GCP Networking Overview

The Cloud Team manages networking for all GCP Campus Cloud projects. Your
project is attached to the campus Shared VPC when it is created, so your VMs
get outbound internet access through Cloud NAT right away. You cannot create
VPC networks of your own.

Many services need no VPC at all, including Cloud Storage, BigQuery, Pub/Sub,
Cloud Run, Cloud Functions, and Vertex AI. If you use only services like these,
you can skip most of this page.

---

## What's Available

| Capability | Available? |
|---|---|
| Outbound internet from VMs (Cloud NAT) | Yes. Automatic, no ticket needed. |
| Your own VPC networks | No. Blocked by policy. |
| Public IP addresses on VMs | No. Use a load balancer instead. |
| Public website or API on VMs | Yes. Build your own load balancer. See [Public-Facing Services](#public-facing-services). |
| Public Cloud Run or Cloud Functions | No. Every caller must log in. |
| VPC peering | Not available. Contact the Cloud Team if you need it. |
| Connection to the UCSB campus network (VPN or Interconnect) | Not available yet. Contact the Cloud Team to discuss options. |

You can create resources only in us-central1 (Iowa) and us-west1 (Oregon). See
[GCP Guardrails]({{ "/docs/gcp/guardrails" | relative_url }}) for every policy
that applies to your project.

---

## Requesting Network Resources

For anything beyond outbound internet access, such as more subnets, VPC
peering, or firewall rule changes, open a
[ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5)
with:

* Your GCP project ID
* What you need and why
* The region (us-central1 or us-west1)
* Any specific CIDR or peering requirements

---

## Creating Compute Instances

When you create a VM in the Cloud Console, the **Network interfaces** section
shows **Networks in this project** by default. That list is always empty,
because your project has no VPC of its own. If you see "No more networks
available in this project," this is why.

To place your VM on the campus Shared VPC, on the **Networking** tab:

1. Click **Add a network interface** (or **Add a Dynamic Network Interface**).
2. Click **Networks shared with me**.
3. Choose a subnet from the **Shared subnetwork** dropdown.
4. Click **Done**.

If **Networks shared with me** shows no subnets, you may not have Shared VPC
access yet. See the next section.

---

## Adding Team Members to the Shared VPC

Your project and its default service accounts can use the Shared VPC right
away. To give a person access, add them to the project's
`-owners@gcp.cloud.ucsb.edu` or `-editors@gcp.cloud.ucsb.edu` Google Group.
They get Shared VPC access automatically, and no ticket is needed. See
[Adding and Removing Users]({{ "/docs/gcp/first-steps#adding-and-removing-users" | relative_url }}).
Allow up to 30 minutes for access to take effect.

---

## Network Tags

Shared VPC firewall rules apply only to VMs that carry the right **network
tag**. Each tag lets in only the traffic listed below. See Google's guide to
[adding and removing network tags](https://cloud.google.com/vpc/docs/add-remove-network-tags).

| Network Tag | What It Allows |
|---|---|
| `allow-iap-ssh` | SSH (port 22) through IAP |
| `allow-iap-rdp` | RDP (port 3389) through IAP |
| `allow-lb-backend` | Traffic from Google Cloud load balancers and their health checks |
| `allow-win-activation` | Windows license activation |

Network tags are not the same as the tags described in
[Tagging & Labels]({{ "/docs/general/tagging" | relative_url }}).

---

## Accessing Private VMs Without a Public IP

Use **Identity-Aware Proxy (IAP)** to SSH or RDP into your VMs. IAP tunnels
your connection through Google, so you need no VPN or public IP. Give the VM
the `allow-iap-ssh` or `allow-iap-rdp` [network tag](#network-tags), then
connect:

* **SSH:** Click **SSH** on the VM in the Cloud Console, or run
  `gcloud compute ssh VM_NAME --tunnel-through-iap`.
* **RDP:** Use [IAP Desktop](https://googlecloudplatform.github.io/iap-desktop/),
  a free Windows app that needs no `gcloud` install.

See Google's guide to
[using IAP for TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding)
for other options.

### IAP Access for Editors

Project owners can open IAP tunnels already. The Editor role cannot. For
editors to use SSH or RDP, an owner grants the **IAP-secured Tunnel User** role
(`roles/iap.tunnelResourceAccessor`) to the project's editors group. Grant it
to the group, not to individuals, as described in
[Adding and Removing Users]({{ "/docs/gcp/first-steps#adding-and-removing-users" | relative_url }}).

### OS Login

[OS Login](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin)
is enforced by org policy. You sign in over SSH with your Google identity, so
there are no SSH keys to manage. SSH keys in project or instance metadata are
ignored, and you cannot turn OS Login off. If your project needs an exception
(for example, a Marketplace image that does not support OS Login), open a
[ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5).

---

## Traffic Between VMs

VMs cannot receive traffic from other VMs by default, even in the same project.
The only inbound traffic allowed is SSH and RDP through IAP, and load balancer
traffic to VMs tagged `allow-lb-backend`. If your VMs need to talk to each
other, open a
[ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5)
to request a firewall rule.

---

## Public-Facing Services

**You can publish a public website or API on VMs yourself, with no ticket.**
Build a global external
[Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/application-load-balancer)
in your project, in front of your VMs. This is the only load balancer type
open to the internet. It costs about $18–25 a month plus traffic, billed to
your project.

1. **Tag your VMs** with the [network tag](#network-tags) `allow-lb-backend`.
2. **Build the load balancer** with
   [Google's guide for a VM backend](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-compute).
   Org policy requires logging on the backend service (`--enable-logging`).
   If you add a custom SSL policy, it must require TLS 1.2 or later.
3. **Point your DNS name** at the load balancer's IP address.

{% capture alert_content %}Your load balancer has <strong>no Web Application Firewall (WAF)</strong> unless you add one. <a href="https://docs.cloud.google.com/armor/docs/cloud-armor-overview">Cloud Armor</a> (Google's WAF and DDoS protection) attaches to your backend service. Consider it for anything with a login or a form. For an internal tool, a policy that allows only UCSB campus and VPN addresses (<code>128.111.0.0/16</code> and <code>169.231.0.0/16</code>) is a good start. Cloud Armor adds a small monthly cost, billed to your project.{% endcapture %}
{% include alert.html type="info" title="Consider adding a WAF" content=alert_content %}

**Cloud Run and Cloud Functions cannot be public.** Every caller must log in
with a Google identity. If you need a public serverless app, or help designing
any public app, open a
[ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5).
