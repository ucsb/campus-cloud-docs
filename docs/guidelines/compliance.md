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
    In AWS, Control Tower and Guardrails work together to provide ongoing goverance for the Campus AWS environment. Control Tower implements preventive or detective controls that help govern resources and monitor compliance across groups of AWS accounts.  [Tagging](/campus-cloud-docs/glossary/#tags) of accounts and individual resources support compliance efforts. In AWS Gurdrails are rules that define policy. 
    
    * ### [AWS Active Guardrails as of Apr 2022](guardrails.aws)


* ### Azure Guardrails
    Azure utilizes built-in and custom policies to set guardrails in Subscriptions. Guardrails for Azure are built using Azure Policy and RBAC to enforce and audit policies for any Azure service.
    
    * ### [Azure Active Guardrails as of May 2020](guardrails.azure)

<br>

* ### Prisma Cloud from Palo Alto
    Prisma Cloud is a cloud native security platform that provides a unified view of security and compliance across the Campus Cloud's three Cloud Providers.  The product was deployed in the Campus Cloud LZ in the summer of 2022.
    
    Prisma Cloud allows us to audit NIST 800-171 compliance, generate account owner reports, centralize Alerts and to optionaly remediate findings. It is expected that AWS account owners will continue to use Security Hub to get Prisma Cloud Alerts as well as most other security related findings. The Cloud Team, NOC, SOC and other groups may use the the Prisma Cloud App for a unified view of security and compliance.
     
     * **Costs** - AWS Accounts currently experience a cost from GuardDuty that correlates to the number of CloudTrail events in their account(s) per Region. For a busy account it may be a small percentage of monthly costs.  We are actively investigating options to lower costs for account owners. In Oct 2022 we limited Prisma Cloud API calls to our two enabled AWS Regions which significantly reduced CloudTrail events and costs per account.
     * **Audit Compliance Reports** - While we are still early in the implenmentation if you are interested in recieving a regulary report on your AWS account compliance please reach out to the Cloud Team.
     * **Security & Compliance Findings** - To view Prisma Cloud Findings in AWS go to Security Hub/Integrations and search for 'prisma' in the Integrations search box at the top. Then click on 'See finding' from the "Palo Alto Networks: Prisma Cloud Enterprise" integration.  You can also search in Security Hub/Findings with the proper filters.

* ### NIST 800-171 Controls Evaluation for AWS
    The Cloud Team in coordination with the SOC has mapped the NIST 800-171 requirements to controls that are relevent to the Campus Cloud LZ for AWS.  Tracking the details of a control can help inform an accounts level of compliance. The compliance level of an account is dynamic in that the resources used may be changing, Controls/Guardrails may change (detective, protective, newly added or removed) and campus / System Compliance goals continue to evolve.  The Campus Cloud Team can provide a tool to help track Cloud account compliance.

    The Cloud Team has created a Sheet that allows an account owner (or resposible party) to track the current state, type, priority and scope of a control.  The Sheet provides and documents thae baseline compliance that is provided by the Campus Cloud LZ and defines a number of "Local Controls" that an account owner may use to examine, interview and test compliance for each requirement.  The account owner has the ability to and probably should create their own controls that assist in assuring compliance per requirment.  The Sheet provices color-coded tracking of progress and other automation along with Sheet Tabs to provide supporting information, dashboards, references in additon to the assemment.

    To request  a copy of the Sheet please send an email to info@cloud.ucsb.edu.  After access has been provided a copy of the Sheet should be made a kept locally and edited to track your compliance.  For more background information on the NIST 800-171 please see the following information


    The NIST requirements are organized into 14 families and within the family are specific requirements related to that family. For example, in the  "Access Control" family (3.1) the thrid requirement is "Control the flow of CUI in accordance with approved authorizations" (3.1.3). So the family sub-number for this requirement is 3.1.1.  This numbering system is utilized for each requirement family.  The 14th requirement family, "System and Information Integrity" can be referenced by its number, 3.14. Every requirement in this Family would have that prefix. Each requirement includes one or more assessment objectives labeled with the family sub-number and a letter (3.1.1[a])

    * NIST Special Publication 800-171A - 
[Assessing Security Requirements for
Controlled Unclassified Information](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-171A.pdf)
