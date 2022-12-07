---
title: Compliance & Governance
description: Compliance & Governance
permalink: /docs/guidelines/compliance
---

## Compliance & Governance
In order to receive Federal funding the Campus needs to comply with NIST 800-171 Federal standards.  UC Policy, IS-3, mandates our requirements for Information Security. The Campus Cloud environment is designed to comply with these standards.

### NIST 800-171
* [NIST 800-171 Rev 2](https://csrc.nist.gov/publications/detail/sp/800-171/rev-2/final)

### IS-3 UC Information Security
* [IS-3](https://security.ucop.edu/policies/it-policies.html)

### Account Compliance
The following are critical compliance requirements for each Campus Cloud account:
- Enable MFA for the root user
- Define contact information for the account owner and for incident response
- [Data privacy classification Tagging](tagging) on account and per resource
- Use of account must be in accordance with UC Policy IS-3

### How we Audit and Maintain Compliance

The Campus Cloud Providers - AWS, Azure, GCP - may differ in the specific terminology and tools used to audit and maintain compliance. However, each Cloud Provider offers resources to help maintain compliance.  One important resource is Guardrails.  

* ### AWS Guardrails
    In AWS Control Tower and  Guardrails work together to provide ongoing goverance for the Campus AWS environment. Control Tower implements preventive or detective controls that help govern resources and monitor compliance across groups of AWS accounts.  [Tagging](/campus-cloud-docs/glossary/#tags) of accounts and individual resources support compliance efforts. In AWS Gurdrails are rules that define policy. 
    
    * ### [AWS Active Guardrails as of Apr 2022](guardrails.aws)


* ### Azure Guardrails
    Azure utilized built-in and custom policies to set guardrails in your subscriptions. Guardrails for Azure are built using Azure Policy and RBAC to enforce and audit policies for any Azure service.
    
    * ### [Azure Active Guardrails as of May 2020](guardrails.azure)

<br>

* ### Prisma Cloud from Palo Alto
    Prisma Cloud is a cloud native security platform that provides a unified view of security and compliance across the Campus Cloud's three Cloud Providers.  The product was deployed in the Campus Cloud LZ in the summer of 2022.
    
    Prisma Cloud allows us to audit NIST 800-171 compliance, generate account owner reports, centralize Alerts and to optionaly remedeiate findings. It is expected that AWS account owners will continue to use Security Hub to get Prisma Cloud Alerts as well as most other security related findings. The Cloud team, NOC, SOC and other groups may use the the Prisma Cloud App for a unified view of security and compliance.
     
     * **Costs** - AWS Accounts currently experience a cost from GuardDuty that correlates to the number of CloudTrail events in their account(s) per Region. For a busy account it may be a small percentage of monthly costs.  We are actively investigating options to lower costs for account owners. In Oct 2022 we limited Prisma Cloud API calls to our two enabled AWS Regions which significantly reduced CloudTrail events and costs per account.
     * **Audit Compliance Reports** - While we are still early in the implenmentation if you are interested in recieving a regulary report on your AWS account compliance please reach out to the Cloud Team.
     * **Security & Compliance Findings** - To view Prisma Cloud Findings in AWS go to Security Hub/Inegrations and search from 'prisma' in the Integrations seach box at the top. The click on 'See finding' from the Palo Alto Netwoks: Prisma Cloud Enterprise integration.  You can also search in Security Hub/Findings with the proper filters.
