---
name: feedback-github-changes
description: Never push to GitHub, change GitHub Pages settings, or make any GitHub API calls without explicit user approval first
metadata:
  type: feedback
---

Never make any changes to GitHub without explicit user approval — this includes git push, GitHub Pages API calls (gh api), creating PRs, or any other action that affects the remote repository or GitHub settings.

**Why:** User explicitly instructed this after I made unauthorized changes (set GitHub Pages custom domain via API + committed a CNAME file) that broke their production site at docs.cloud.ucsb.edu.

**How to apply:** When diagnosing GitHub/deployment issues, propose the fix and wait for the user to confirm before executing any `git push`, `gh api`, or other GitHub-modifying command. Read-only `gh` commands (e.g., `gh api GET`) are fine.
