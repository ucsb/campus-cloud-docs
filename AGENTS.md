# AGENTS.md — Campus Cloud Documentation

## About This Repository

This is the **public-facing cloud documentation site for the University of California, Santa Barbara (UCSB)**. It is published at <https://docs.cloud.ucsb.edu> and built with Jekyll + GitHub Pages using the `vsoch/docsy-jekyll` remote theme.

The audience is **faculty, researchers, staff (including IT staff), and students** at UCSB. Many readers are not cloud professionals. Write for that audience.

## Writing Guidelines

1. **Be clear, concise, and simple.** Use short sentences and plain language. Avoid jargon; when a technical term is unavoidable, define it on first use or link to the Glossary (`pages/glossary.md`).
2. **Spell out acronyms on first use** (e.g., "Service Control Policy (SCP)"). After that, the acronym alone is fine within the same page.
3. **Do not reproduce cloud-provider documentation.** Never copy procedural steps, service descriptions, or reference material from AWS, Azure, or GCP docs. Instead, summarize what UCSB users need to know in one or two sentences and **link to the official docs**.
4. **Focus on what is UCSB-specific.** The value of this site is the campus context — SSO setup, guardrails, procurement, compliance posture, support contacts, and campus networking. Everything else should point to the provider's docs.
5. **Keep pages short.** If a page exceeds ~800 words, consider splitting it or trimming content that belongs in provider docs.
6. **Don't repeat yourself (DRY).** If information already exists on another page of this site, link to it instead of restating it. Duplicated content becomes a maintenance burden and leads to inconsistencies.
7. **Use the Glossary for definitions.** When a UCSB-specific term needs defining, add it to `pages/glossary.md` in alphabetical order — don't define it inline on the page. The Glossary links to provider glossaries (AWS, Azure, GCP) at the top; never duplicate terms that already appear there unless there is a UCSB-specific reason. Suggest new Glossary entries when it seems sensible.

## Content Structure

```
docs/
  general/   # Cross-provider guidance (identity, security, compliance, cost, etc.)
  aws/       # AWS-specific pages
  azure/     # Azure-specific pages
  gcp/       # GCP-specific pages
pages/       # Top-level site pages (getting-started, glossary, about, docs index)
_data/       # Navigation and TOC definitions
_includes/   # Reusable HTML partials (alerts, header, footer)
assets/      # CSS, images
```

* **`_data/toc.yml`** defines the sidebar table of contents. When you add or rename a page, update the TOC entry to match.
* **`_data/navigation.yml`** defines the top navigation bar.
* **`pages/docs.md`** contains a full link list of every documentation page. Update it whenever a page is added or removed.
* **Provider and section index pages** (e.g., `docs/aws/index.md`, `docs/general/index.md`) often list links to their child pages at the bottom. Update those links when adding or removing pages in that section.
* Pages in `docs/` use the `docs` collection (defined in `_config.yml`). Their `permalink` frontmatter controls the URL.
* **When removing a page**, always add a `redirect_from` entry in the YAML frontmatter of whichever page replaces it, so existing bookmarks and search-engine links continue to work:
  ```yaml
  redirect_from:
    - /docs/aws/old-page-name
  ```

## Jekyll & Markdown Conventions

* Every content file starts with YAML frontmatter (`---` delimiters). Required fields: `title`, `description`, `permalink`. Include `last_reviewed` (ISO date) when updating a page. **Update `last_reviewed` to today's date whenever you make substantive changes to a page.**
* **Internal links** must use the `relative_url` filter so the site works under any `baseurl`:
  ```
  {% raw %}[Link text]({{ "/docs/aws/networking" | relative_url }}){% endraw %}
  ```
* **Images** go in `assets/img/`. Reference them with `relative_url`:
  ```
  {% raw %}![Alt text]({{ "/assets/img/example.png" | relative_url }}){% endraw %}
  ```
* Use the `alert.html` include for callout boxes:
  ```
  {% raw %}{% capture alert_content %}Your message here.{% endcapture %}
  {% include alert.html type="info" title="Note" content=alert_content %}{% endraw %}
  ```
  Supported types: `info`, `warning`, `danger`, `success`.
* Use Markdown tables, headings (`##`, `###`), and bullet lists. Avoid raw HTML unless required for accessibility or layout.
* Use `---` (horizontal rule) to separate major sections on a page.
* **ServiceNow links:** When directing users to open a support ticket, always link to the Campus Cloud ServiceNow catalog item:
  ```markdown
  [ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5)
  ```

## Web Accessibility

All content must meet **WCAG 2.1 AA** guidelines (<https://www.w3.org/TR/WCAG21/>). Follow the UCSB Web Accessibility Standards at <https://webguide.ucsb.edu/accessibility-0>.

Key requirements:
* Every image must have meaningful `alt` text. Decorative images use `alt=""`.
* Use proper heading hierarchy (`##` → `###` → `####`). Never skip levels.
* Links must have descriptive text — never use "click here" or bare URLs as link text.
* Tables must have header rows. Keep tables simple; avoid nested or merged cells.
* Ensure sufficient color contrast (4.5:1 for normal text, 3:1 for large text).

## Landing Zone Repositories (Source of Truth)

The following GitHub repositories contain the infrastructure-as-code that defines each provider's landing zone. Use `git` on the command line to clone or inspect them when you need to verify how the landing zones actually work.

Before accessing these repos, verify that `git` is available and configured (e.g., run `git ls-remote` on one of the repos). If it is not available or authentication fails, ask the user how to proceed and explain that you need repo access to verify accuracy.

| Provider | Repository |
|----------|------------|
| AWS | `campus-cloud-aws-landing-zone` |
| Azure | `campus-cloud-azure-landing-zone` |
| GCP | `campus-cloud-gcp-landing-zone` |

Rules for using these repos:

* **Verify accuracy.** These repos are the source of truth. Before writing or updating documentation about guardrails, networking, roles, org policies, or any landing zone behavior, cross-check the relevant repo. Push back on the user if a requested change contradicts what the code actually does.
* **GCP repo: ignore `/modules` and `/environment` folders.** Those directories are not relevant to documentation. Focus on the other top-level directories.
* **Only document customer-facing information.** Do not expose back-end implementation details such as internal project names, folder IDs, group names, OU IDs, or infrastructure plumbing. The audience cares about what they can see and do in their own accounts — not how the platform is built behind the scenes.

## Agent Behavior

* **Push back on bad ideas.** If a proposed change would duplicate provider docs, break accessibility, introduce jargon, contradict the landing zone repos, or make the site harder to maintain, say so and suggest an alternative.
* **Ask clarifying questions.** When the request is ambiguous, when instructions conflict, or when you are unsure about the intended outcome, ask the user rather than guessing. More questions lead to better clarity, which leads to better results.
* **Do not add pages or TOC entries** without confirming the intent and updating all affected locations: `_data/toc.yml`, `_data/navigation.yml`, `pages/docs.md`, and the relevant section index pages. See **Content Structure** above for details.
* **Do not modify `_config.yml`** without explicit approval — it controls site-wide settings and the deployment URL.
* **Site reviews:** When asked to review the site, check what's out-of-date, or suggest improvements, read every page of the site thoroughly. Compare content against the current state of the landing zone git repos and the accessibility guidelines. Also check every internal link: verify the target permalink exists, ensure all links use the `relative_url` filter (not bare relative paths), and confirm anchor fragments point to real headings. When fixing or removing a link target, add a `redirect_from` entry on the destination page so existing bookmarks and search-engine links continue to work. Present prioritized suggestions to the user — accuracy issues, broken links, and accessibility violations first, then style and content improvements.
