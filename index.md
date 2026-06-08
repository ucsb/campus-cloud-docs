---
layout: page
title: "Campus Cloud Docs - Home"
description: UCSB Campus Cloud documentation — managed, policy-compliant AWS, Azure, and GCP environments for the campus community.
permalink: /
last_reviewed: 2026-06-08
redirect_from:
  - /about/
---

# UCSB Campus Cloud

The UCSB Campus Cloud provides managed, policy-compliant cloud environments on
AWS, Azure, and GCP for the campus community. The Cloud Team (ITS-CCID) operates
a Campus Cloud Landing Zone for each provider — a pre-configured, secure multi-account
environment that gives you a head start on security, compliance, and networking.

Using the Campus Cloud means:

* **UC enterprise pricing.** The UC system has negotiated discounts with AWS
  (Enterprise Discount Program), Azure (Enterprise Agreement), and GCP. You
  benefit automatically.
* **Compliance built in.** Every account includes guardrails aligned with UC
  Policy IS-3 and, for research accounts, NIST 800-171.
* **Campus network connectivity.** AWS accounts can communicate with UCSB
  on-premises systems over private networking. If you need campus connectivity
  for Azure or GCP, contact us to discuss options.
* **Support options.** AWS Business Support and Azure support plans are
  available to Campus Cloud accounts. Contact the Cloud Team to discuss the
  right support tier for your workload.

New here? Start with [General Guidance]({{ "/docs/general/" | relative_url }}) or
[Getting Started]({{ "/getting-started" | relative_url }}).

{% capture alert_content %}
<p>Please note: UCSB has updated its approach to purchasing paid cloud services from Microsoft Azure and Google Cloud. The Azure change took effect in January. The matching change for Google Cloud takes effect on Tuesday, June 16, 2026.</p>
<p>In both cases, new paid subscriptions and projects must go through the campus <a href="{{ "/getting-started" | relative_url }}">Gateway procurement process</a> instead of being set up with a personal or departmental credit card. The campus agreements offer better pricing, give departments a clearer view of cloud spending, and protect users from unexpected charges on individual cards.</p>
<h5>Microsoft Azure (in effect since January 2026)</h5>
<ul>
  <li><strong>New paid Azure subscriptions can no longer be created with a credit card.</strong> Free Azure subscriptions can no longer be upgraded to paid subscriptions using a credit card. To set up a new paid Azure subscription, contact the Campus Cloud Team and use the Gateway procurement process.</li>
  <li><strong>Existing Azure subscriptions are not affected</strong>, even if they have a credit card associated. Azure for Students is also not affected. Students with a verified ucsb.edu email can still sign up for Azure for Students and get $100 in credit for 12 months with no credit card required. Other educational subscription types, such as MSDN and Visual Studio Enterprise, are also unchanged.</li>
</ul>
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

### Amazon Web Services (AWS)

Your AWS account includes campus SSO login, networking connected to UCSB, a
Service Catalog of self-service products (VPCs, budgets, IAM roles), and
security monitoring pre-configured. UC enterprise pricing and Enterprise Support
are included automatically.

[AWS Overview]({{ "/docs/aws" | relative_url }}) · [AWS First Steps]({{ "/docs/aws/first-steps" | relative_url }})

---

### Microsoft Azure

Your Azure Subscription is placed inside the UCSB management hierarchy with
pre-configured policies, Defender for Cloud monitoring, and network connectivity
via Virtual WAN. UC enterprise pricing through the Azure EA applies automatically.

[Azure Overview]({{ "/docs/azure" | relative_url }}) · [Azure First Steps]({{ "/docs/azure/first-steps" | relative_url }})

---

### Google Cloud Platform (GCP)

Your GCP Project lives in the UCSB organization with org-wide policies,
centralized audit logging, Security Command Center monitoring, and billing
sub-accounts for cost attribution. UC enterprise pricing is included.

[GCP Overview]({{ "/docs/gcp" | relative_url }}) · [GCP First Steps]({{ "/docs/gcp/first-steps" | relative_url }})

---

### Who Is This For?

The Campus Cloud is available to UCSB faculty, researchers, staff, and students
for academic, research, and administrative work. If you are doing research that
involves sensitive data (HIPAA, CUI, FERPA), the Cloud Team can help you select
the right account type and compliance controls.

For personal or student projects outside of sponsored research, free-tier accounts
directly with cloud providers may be more appropriate. Contact
[info@cloud.ucsb.edu](mailto:info@cloud.ucsb.edu) if you are not sure which to use.

---

### Questions / Contact

* General questions — [info@cloud.ucsb.edu](mailto:info@cloud.ucsb.edu)
* Account issues — open a [ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5)
