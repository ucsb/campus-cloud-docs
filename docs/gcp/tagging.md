---
title: GCP Labels & Tags
description: Resource Manager Tags and project labels for Campus Cloud GCP projects — what they are, who sets them, and how to update them.
permalink: /docs/gcp/tagging
last_reviewed: 2026-03-30
---

## GCP Tags and Labels

GCP has two distinct metadata systems:

* **Resource Manager Tags** — Organization-level key-value pairs bound to
  projects. Used for governance, billing attribution, and automation (e.g.,
  Janitor Bot, Wiz scanning). These are set at the **project level**, not on
  individual resources.
* **Project Labels** — Flat key-value metadata on a project. Appear in billing
  exports. Set at project creation by the Cloud Team.

{% include alert.html type="info" title="No ucsb: prefix in GCP" content="Unlike AWS, GCP Resource Manager Tags do not use a ucsb: namespace prefix. Tag keys are simply environment, mission, protection-level, etc. They are scoped to the UCSB organization automatically." %}

---

## Resource Manager Tags

Tags are bound to your **project**, not to individual resources. Most are set
at project creation by the Cloud Team's provisioning automation. The 6
owner-settable tags can be changed by project owners at any time.

### Owner-Settable Tags

You are responsible for keeping these accurate. They drive billing reports,
cost attribution, and Security Command Center policy scoping.

| Tag Key | Allowed Values | Notes |
|---|---|---|
| `environment` | `dev`, `test`, `prod`, `other` | |
| `mission` | `academic`, `research`, `administrative`, `mixed` | |
| `protection-level` | `p1`, `p2`, `p3`, `p4` | |
| `availability-level` | `a1`, `a2`, `a3`, `a4` | |
| `recovery-level` | `r1`, `r2`, `r3`, `r4` | |
| `dept` | UCSB department code (e.g., `COMS`, `PHYS`, `IDCL`) | 4-letter code from the UCSB chart of accounts |

See [Tagging & Labels](/docs/general/tagging) for definitions of protection,
availability, and recovery levels.

---

## How to Update Owner-Settable Tags

### In the GCP Console

1. Go to **IAM & Admin → Tags** in the left menu, or navigate to the project's
   **Project info** card on the home page.
2. Click **Add tag** or the edit icon next to an existing tag.
3. Select the tag key and value from the dropdown lists.
4. Click **Save**.

### With gcloud CLI

```bash
# List current tag bindings on your project
gcloud resource-manager tags bindings list \
  --parent=//cloudresourcemanager.googleapis.com/projects/YOUR_PROJECT_ID

# Add or update a tag binding
gcloud resource-manager tags bindings create \
  --tag-value=YOUR_ORG_ID/environment/prod \
  --parent=//cloudresourcemanager.googleapis.com/projects/YOUR_PROJECT_ID
```

Replace `YOUR_ORG_ID` with the UCSB organization ID and `YOUR_PROJECT_ID` with
your numeric project ID.

---

## Project Labels

Project labels are set at creation time and appear in billing exports. They
are managed by the Cloud Team — you do not need to set these yourself.

| Label Key | Example Value | Purpose |
|---|---|---|
| `business_unit` | `its-ccid` | Identifies the owning business unit |
| `costing` | `gcp-core` | Cost allocation group for billing reports |

Labels cannot drive org policies or automation. They supplement tags for
billing visibility only.

---

## Checking Your Project's Tags

To view the tags currently bound to your project:

1. Navigate to **IAM & Admin → Tags** in the console.
2. All tag bindings for the project are listed there.

Or use gcloud:

```bash
gcloud resource-manager tags bindings list \
  --parent=//cloudresourcemanager.googleapis.com/projects/YOUR_PROJECT_ID
```

Security Command Center will flag projects with missing required tags.
