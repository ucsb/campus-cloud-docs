# Campus Cloud Documentation

Source repository for [docs.cloud.ucsb.edu](https://docs.cloud.ucsb.edu) — the public-facing documentation site for the UCSB Campus Cloud. The audience is UCSB faculty, researchers, staff, and students.

Built with [Jekyll](https://jekyllrb.com/) and the [Docsy-Jekyll](https://vsoch.github.io/docsy-jekyll) remote theme. Deployed automatically via GitHub Pages on push to the default branch.

---

## How the Site Works

GitHub Pages builds the site using the `vsoch/docsy-jekyll` remote theme (set in `_config.yml`). There is no local Gemfile or build step — you push Markdown files and GitHub does the rest.

**Do not modify `_config.yml`** unless you know what you are doing. It controls the site URL, theme, collections, and deployment settings.

---

## Directory Structure

```
_config.yml          # Site-wide settings (theme, URL, collections) — rarely changed
_data/
  toc.yml            # Sidebar table of contents — update when adding/removing/renaming pages
  navigation.yml     # Top navigation bar links
_includes/
  alert.html         # Callout box partial (info, warning, danger, success)
  header.html        # Site header (customized from theme)
  footer.html        # Site footer (customized from theme)
assets/
  css/ucsb-brand.css # UCSB brand overrides (fonts, colors)
  img/               # All images used in documentation
docs/
  general/           # Cross-provider guidance (identity, security, compliance, cost, etc.)
  aws/               # AWS-specific pages
  azure/             # Azure-specific pages
  gcp/               # GCP-specific pages
pages/
  getting-started.md # Procurement process (Gateway)
  glossary.md        # UCSB-specific term definitions
  docs.md            # Master link list of every documentation page
  about.md           # Redirects to home page
index.md             # Site home page
AGENTS.md            # AI agent instructions (see below)
```

---

## Using AI Agents for Site Maintenance

The `AGENTS.md` file in the repo root contains detailed instructions for AI coding agents (e.g., GitHub Copilot in VS Code). It covers:

- Writing guidelines and content standards
- Directory structure and where to update when adding/removing pages
- Jekyll and Markdown conventions
- Accessibility requirements
- How to cross-check documentation against the landing zone infrastructure repos
  - `AGENTS.md` lists three Git repos that contain the landing zone infrastructure-as-code: `campus-cloud-aws-landing-zone`, `campus-cloud-azure-landing-zone`, and `campus-cloud-gcp-landing-zone`. The agent clones or inspects these repos to verify that what the docs say matches what the code actually does.
  - This is especially useful for guardrails, networking, roles, and org policy pages — the agent can diff the documented controls against the Terraform/CloudFormation source and flag discrepancies.
  - If the agent cannot access the repos (e.g., missing Git credentials), it will ask you before proceeding.
- How to perform a full site review (broken links, outdated content, accessibility)

When using an AI agent to help with documentation updates or reviews, open this repo in VS Code with GitHub Copilot. The agent will automatically follow the conventions in `AGENTS.md`. You can ask it to:

- Review the entire site for broken links, outdated content, or accessibility issues
- Add or update documentation pages (it will update the TOC, index pages, and link lists)
- Cross-check guardrail or networking documentation against the landing zone repos

Keep `AGENTS.md` up to date as site conventions change — it is the single source of truth the agent uses.

---

## Common Maintenance Tasks

### Edit an existing page

1. Find the Markdown file (the `permalink` in its YAML frontmatter determines the URL).
2. Edit the content.
3. Update `last_reviewed` in the frontmatter to today's date.
4. Push to trigger a rebuild.

### Add a new page

1. Create the `.md` file in the appropriate directory (`docs/aws/`, `docs/general/`, etc.).
2. Add YAML frontmatter with at least `title`, `description`, `permalink`, and `last_reviewed`.
3. Update **all four** of these locations:
   - `_data/toc.yml` — add a sidebar entry
   - `pages/docs.md` — add to the master link list
   - The relevant section index page (e.g., `docs/aws/index.md`) — add to the "Next Steps" or topic list
   - `_data/navigation.yml` — only if the page should appear in the top nav bar
4. Push.

### Remove or rename a page

1. Delete or rename the file.
2. Remove/update entries in `_data/toc.yml`, `pages/docs.md`, and the section index page.
3. Add a `redirect_from` entry in the YAML frontmatter of whichever page replaces it, so old bookmarks still work:
   ```yaml
   redirect_from:
     - /docs/aws/old-page-name
   ```

---

## Writing Conventions

These are the key rules. Full details are in `AGENTS.md`.

- **Internal links** must use the `relative_url` Liquid filter:
  ```
  [Link text]({{ "/docs/aws/networking" | relative_url }})
  ```
  Bare relative paths (e.g., `(networking)`) will break if the `baseurl` changes.

- **Images** go in `assets/img/` and are referenced with `relative_url`:
  ```
  ![Alt text]({{ "/assets/img/example.png" | relative_url }})
  ```

- **Callout boxes** use the `alert.html` include:
  ```
  {% capture alert_content %}Your message here.{% endcapture %}
  {% include alert.html type="info" title="Note" content=alert_content %}
  ```

- **ServiceNow links** should always point to the Campus Cloud catalog item:
  ```
  [ServiceNow ticket](https://ucsb.service-now.com/it?id=it_sc_cat_item&sys_id=c60e6bf2dbf398900c2e38f0ad961908&sysparm_category=eb1eaff2dbf398900c2e38f0ad9619d5)
  ```

- **Accessibility:** Every image needs `alt` text. Use proper heading hierarchy (`##` → `###` → `####`). Link text must be descriptive — never "click here."

- **Don't reproduce cloud-provider docs.** Summarize what is UCSB-specific and link to the official AWS/Azure/GCP documentation.

---

## Testing Locally

The site does not have a Gemfile, so local builds are not configured out of the box. To preview locally:

1. Install Ruby and Bundler.
2. Create a temporary `Gemfile`:
   ```ruby
   source "https://rubygems.org"
   gem "github-pages", group: :jekyll_plugins
   ```
3. Run `bundle install && bundle exec jekyll serve`.
4. Open `http://localhost:4000`.

Alternatively, push to a personal fork and enable GitHub Pages there. The `_config.yml` has commented-out settings for a test deployment at `iancrew.github.io/campus-cloud-docs`.

---

## Questions

Contact the Cloud Team at [info@cloud.ucsb.edu](mailto:info@cloud.ucsb.edu). 

