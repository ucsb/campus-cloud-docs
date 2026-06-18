---
title: GCP Overview
description: Overview of the UCSB Campus Cloud GCP environment — org hierarchy, folders, projects, regions, and what is pre-configured.
permalink: /docs/gcp/
last_reviewed: 2026-06-18
---

# GCP at UCSB

The UCSB Campus Cloud GCP platform is organized as a **Google Cloud
Organization** with a structured folder hierarchy managed by the Cloud Team.
Every project is provisioned inside a folder with organization-level policies
and guardrails, giving your team a compliant starting point without manual
security setup.

{% capture alert_content %}
<p>Please note: UCSB has updated its approach to purchasing paid cloud services from Microsoft Azure and Google Cloud. The Azure change took effect in January. The matching change for Google Cloud takes effect on Tuesday, June 16, 2026.</p>
<p>In both cases, new paid subscriptions and projects must go through the campus <a href="{{ "/getting-started" | relative_url }}">Gateway procurement process</a> instead of being set up with a personal or departmental credit card. The campus agreements offer better pricing, give departments a clearer view of cloud spending, and protect users from unexpected charges on individual cards.</p>
<h5>Google Cloud (effective June 16, 2026)</h5>
<ul>
  <li><strong>New projects that need billing</strong> must be requested through the <a href="{{ "/getting-started" | relative_url }}">Gateway procurement process</a>. Personal and departmental credit cards can no longer be attached. Existing funded projects are not affected.</li>
  <li><strong>Google&#8217;s $300 new-account credit can no longer be activated with a ucsb.edu email account.</strong> This applies to individual users, including students. For coursework or research, faculty should look at the campus <a href="{{ "/docs/general/cost-management#research-credits" | relative_url }}">Research Credits and Teaching Credits</a> program. Research Credits offer up to $5,000 for faculty, PhD students, and postdocs. Teaching Credits are applied for on a per-course by faculty for student use.</li>
  <li><strong>Free sandbox projects are still available.</strong> Any ucsb.edu user can create a project in the Sandbox Unfunded folder to explore Google Cloud, use Apps Script, or access free-tier services. No approval is needed. <a href="{{ "/docs/gcp/" | relative_url }}">Learn more about Google Cloud at UCSB</a>.</li>
  <li><strong>Networking is now managed centrally for new projects.</strong> Outbound internet access, such as installing packages or calling APIs, works automatically. Inbound access from the internet is blocked by default. Virtual machines cannot have public IPs, and external load balancers must be provisioned by the Cloud Team. Existing projects keep their current networks. If your new project needs inbound connectivity, <a href="{{ "/docs/gcp/networking" | relative_url }}">submit a request</a>.</li>
</ul>
<p><strong>Other new protections for new and unfunded Google Cloud projects:</strong></p>
<ul>
  <li>Allowed regions are now us-central1 in Iowa and us-west1 in Oregon only.</li>
  <li>Cloud Storage buckets cannot be made publicly accessible.</li>
</ul>
<p>These controls are part of an ongoing effort to bring UCSB&#8217;s Google Cloud environment in line with university security requirements. Existing funded projects are not affected at this time.</p>
<p><strong>Learn more:</strong><br>
<a href="{{ "/docs/gcp/" | relative_url }}">Google Cloud at UCSB</a><br>
<a href="{{ "/docs/gcp/networking" | relative_url }}">Networking</a><br>
<a href="{{ "/docs/gcp/guardrails" | relative_url }}">Guardrails &amp; Org Policies</a><br>
<a href="{{ "/docs/gcp/security" | relative_url }}">Security</a></p>
<p><strong>Questions?</strong> Email <a href="mailto:info@cloud.ucsb.edu">info@cloud.ucsb.edu</a> or open a <a href="https://ucsb.service-now.com/it?id=it_sc_cat_item&amp;sys_id=c60e6bf2dbf398900c2e38f0ad961908&amp;sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5">ServiceNow request</a>.</p>
{% endcapture %}
{% include alert.html type="warning" title="Campus Cloud Service Updates — June 2026" content=alert_content %}

---

## Key Facts

| Item | Value |
|---|---|
| Sign-in URL | [console.cloud.google.com](https://console.cloud.google.com) |
| Identity Provider | UCSB Google Workspace (via Entra ID) — sign in with `@ucsb.edu` |
| Supported Regions | us-central1 (Iowa), us-west1 (Oregon) |
| New Project Turnaround | ~2 business days after PO is approved |

---

## Organization Hierarchy

GCP resources are organized in a tree: **Organization → Folders → Projects**.
Policies applied at a higher level are inherited by every project underneath.

| Folder | Purpose |
|---|---|
| UCSB NIST Baseline | Production workloads — funded research, academic, and administrative projects with full org-policy enforcement |
| Sandbox Unfunded | Self-service exploration — any `@ucsb.edu` user can create a project here, but billing cannot be attached |
| UCSB Legacy | Pre-existing projects that predate the landing zone |

{% include alert.html type="info" title="Sandbox Unfunded — self-service, no billing" content="Any @ucsb.edu user can create a project in the Sandbox Unfunded folder — including projects created automatically by tools like Apps Script. Billing cannot be attached, so most paid services (Compute Engine, Cloud SQL, GKE) are unavailable. Use this folder for exploring the GCP console, IAM, and free-tier services." %}

---

## What Is Pre-configured

When your project is provisioned, the Cloud Team will:

* **Create per-project access groups** — Four Google Groups (owners, editors,
  viewers, billing) that carry project, billing, and Shared VPC access; manage
  access through these instead of granting roles directly (see
  [Identity & Access]({{ "/docs/general/identity" | relative_url }}))
* **Block high-risk operations** — Policies prevent actions like granting
  public access or disabling audit logs
* **Enable Cloud Audit Logs** — Admin Activity logs are stored securely for 3 years
* **Enable Security Command Center** — Central dashboard for security findings
* **Require project tags** — Enforce your team's required tags, set at the
  project level (see [Tagging]({{ "/docs/general/tagging" | relative_url }}))
* **Restrict networking** — Only the Cloud Team can create VPC networks; request
  networking resources if your project needs them
* **Route notifications to your team** — Essential Contacts are configured
  automatically and point at your project's access groups, so security, billing,
  and operational notices reach the right people
* **Set a billing budget alert** — Notifies you when spend approaches your
  specified threshold (funded projects only)

---

## Regions

All workloads should use **us-central1** or **us-west1**. Org policies allow
other regions in some cases, but networking, compliance tooling, and support
are tested primarily in these two regions.

---

## Next Steps

* [Request a Project]({{ "/getting-started" | relative_url }})
* [First Steps]({{ "/docs/gcp/first-steps" | relative_url }})
* [Networking]({{ "/docs/gcp/networking" | relative_url }})
* [Guardrails & Org Policies]({{ "/docs/gcp/guardrails" | relative_url }})
* [Security]({{ "/docs/gcp/security" | relative_url }})

