---
title: GCP Labels & Tags
description: Required labels and GCP resource tags for Campus Cloud GCP projects, how to set them, and what the platform controls automatically.
permalink: /docs/gcp/tagging
last_reviewed: 2026-03-30
---

## GCP Labels and Tags

GCP has two distinct metadata concepts:

* **Labels** — Key-value pairs attached to individual resources (VMs, buckets,
  BigQuery datasets, etc.). Visible in billing data.
* **Tags (Resource Manager Tags)** — Hierarchical key-value pairs attached to
  resources or projects at the organization level. Used to enforce org policies
  and control access.

UCSB Campus Cloud uses both. Labels are required for cost and compliance
attribution. Resource Manager Tags are used for platform governance and
some are managed by the Cloud Team, not by you.

---

## Required Labels

Apply these labels to all resources you create. Label enforcement is active
— unlabeled resources may be flagged by Security Command Center.

| Label Key | Required? | Allowed Values | Notes |
|---|---|---|---|
| `ucsb:environment` | Yes | `production`, `staging`, `development`, `sandbox` | |
| `ucsb:mission` | Yes | `research`, `academic`, `administrative`, `infrastructure` | |
| `ucsb:protection-level` | Yes | `p1`, `p2`, `p3`, `p4` | Lowercase for GCP labels |
| `ucsb:availability-level` | Yes | `a1`, `a2`, `a3`, `a4` | Lowercase for GCP labels |
| `ucsb:recovery-level` | Yes | `r1`, `r2`, `r3`, `r4` | |
| `ucsb:dept` | Yes | Department code (e.g., `chem`, `engineering`) | |

See [Tagging](/docs/general/tagging) for definitions of protection, availability,
and recovery levels.

---

## Platform-Managed Tags (Do Not Modify)

Three Resource Manager Tags on each project are managed by the Cloud Team
and should not be changed:

| Tag Key | Purpose | Who Manages It |
|---|---|---|
| `ucsb:expiry-date` | Track project expiration | Cloud Team (automated) |
| `ucsb:billing-limit` | Set maximum spend allowed on the project | Cloud Team |
| `ucsb:wiz-scanning` | Control Wiz security scanning enrollment | Cloud Team |

If any of these tags are missing or incorrect on your project, contact the
Cloud Team. Do not modify them.

---

## How to Add Labels to a Resource

### In the GCP Console

Most resources have a **Labels** section in their detail view:

1. Open the resource (e.g., a VM instance or storage bucket).
2. Click **Edit** (or the pencil icon on the Labels section).
3. Click **+ Add label** and enter the key-value pairs.
4. Save.

### At Resource Creation

When creating a resource, add labels in the **Labels** section of the creation
form before confirming.

### With gcloud CLI

```bash
# Add labels to a VM
gcloud compute instances add-labels INSTANCE_NAME \
  --labels=ucsb:environment=production,ucsb:mission=research \
  --zone=us-central1-a

# Add labels to a GCS bucket
gcloud storage buckets update gs://my-bucket \
  --update-labels=ucsb:environment=production,ucsb:mission=research
```

### With Terraform

```hcl
resource "google_compute_instance" "example" {
  name         = "my-instance"
  machine_type = "e2-standard-4"
  zone         = "us-central1-a"

  labels = {
    "ucsb:environment"       = "production"
    "ucsb:mission"           = "research"
    "ucsb:protection-level"  = "p2"
    "ucsb:availability-level" = "a2"
    "ucsb:recovery-level"    = "r2"
    "ucsb:dept"              = "chemistry"
  }
  # ...
}
```

---

## Checking Label Compliance

To check whether your resources have the required labels:

1. Navigate to **Cloud Asset Inventory** → **Asset list**.
2. Filter by resource type and your project.
3. Export to a spreadsheet and check for missing label keys.

Alternatively, Security Command Center findings will flag resources that are
missing required labels.
