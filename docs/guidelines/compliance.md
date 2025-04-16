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

    **[AWS Active Guardrails](guardrails.aws)**

* ### Azure Guardrails
    Azure utilizes built-in and custom policies to set guardrails in Subscriptions. Guardrails for Azure are built using Azure Policy and RBAC to enforce and audit policies for any Azure service.
    
    **[Azure Active Guardrails](guardrails.azure)**

* ### Prisma Cloud from Palo Alto
    Prisma Cloud is a cloud native security platform that provides a unified view of security and compliance across the Campus Cloud's three Cloud Providers.  The product was deployed in the Campus Cloud LZ in the summer of 2022.
    
    Prisma Cloud allows us to audit NIST 800-171 compliance, generate account owner reports, centralize Alerts and to optionaly remediate findings. It is expected that AWS account owners will continue to use Security Hub to get Prisma Cloud Alerts as well as most other security related findings. The Cloud Team, NOC, SOC and other groups may use the the Prisma Cloud App for a unified view of security and compliance.
     
     * **Costs** - AWS Accounts currently experience a cost from GuardDuty that correlates to the number of CloudTrail events in their account(s) per Region. For a busy account it may be a small percentage of monthly costs.  We are actively investigating options to lower costs for account owners. In Oct 2022 we limited Prisma Cloud API calls to our two enabled AWS Regions which significantly reduced CloudTrail events and costs per account.
     * **Audit Compliance Reports** - While we are still early in the implenmentation if you are interested in recieving a regulary report on your AWS account compliance please reach out to the Cloud Team.
     * **Security & Compliance Findings** - To view Prisma Cloud Findings in AWS go to Security Hub/Integrations and search for 'prisma' in the Integrations search box at the top. Then click on 'See finding' from the "Palo Alto Networks: Prisma Cloud Enterprise" integration.  You can also search in Security Hub/Findings with the proper filters.

<br>

## Do you need a NIST 800-171 compliant Cloud Account ? ##
If you require a NIST 800-171 compliant Cloud account or need to audit compliance in an existing Cloud account the Cloud team has a few options to get you started.

### New NIST-800-171 Compliant Account ###
**OU = UCSB Baseline v2**

You can request a compliant AWS Cloud account buy following our normal process for [requesting an AWS account]({{ site.baseurl }}getting-started/#procure-a-campus-cloud-account) but requesting a "NIST Complaint Account" which will allow us to create your AWS account in a special Organization Unit (OU) that has a special Security Standard and additional Controls applied to accounts.  These Controls detect and prevent certain actions to help your stay in compliance.  There may be cases where certain tasks or services need to be engaged in an alternative way to maintain compliance.  For example, instead of creating a unencrypted S3 bucket you could be required to create an encypted S3 bucket.

### Make Exisiting AWS Account NIST-800-171 Compliant ###
**currently in OU = UCSB Baseline v1**

If you already have an AWS account in the UCSB Cloud LZ that is NOT in the NIST Compliant OU you have TWO options:
1. Migrate your account to the NIST Compliant OU
2. Enable Controls / Security Standard to  make your existing account more compliant

   Please create a SN Ticket or contact us via email at info@cloud.ucsb.edu to start a discussion.


## Do you need to audit or track your NIST 800-171 Compliance ? ##

If you have a NIST Compliant account there will be more Controls enabled in the account and it will likely have fewer responsibities for your to document or define. However, there are additional responsiblities for you to assume and document as there are many NIST compliance Requirements that are not accomplished via technical methods alone. You will require you to have safe and responsible processes around access, authentication, least priviledge, incident response, etc. For example, different account uses should had differnt levels of access to your AWS Account.

If you do not have NIST Compliant account you will have more responsiblities and local Controls to establish.

To assist with the Cloud Team is preparing a tool that is reflective of the type of AWS Account you are using. Please see below.

### NIST 800-171 Controls Evaluation for AWS ###

#### A tool to help track compliance ####
The Cloud Team in coordination with the SOC has mapped NIST 800-171 requirements to controls to help define, highlight and document responsiblitites relevent to the Campus Cloud LZ for AWS. In this context a "control" is a process, system or product that asserts compliance with a requirement. Tracking controls can help detail the compliance level of an account. The compliance level of an account is dynamic in that the resources used may be changing, Controls/Guardrails may change (detective, preventive, new or removed) plus Campus / System Compliance goals continue to evolve.  The Campus Cloud Team can provide a tool to help track Cloud account compliance.

The Cloud Team has created a Controls Evaluation spreadsheet that allows an account owner (or resposible party) to track the responsiblity, current state, type, priority and scope of a control.  The Sheet documents baseline compliance provided by the Campus Cloud LZ and defines a number of "Local Controls" an account owner may use to examine, interview, test or assert compliance for each requirement.  The account owner has the ability to (and probably should) create their own controls that assist in assuring compliance per requirment.  The spreadhsheet provides color-coded tracking of progress and other automation along with additional Tabs with supporting information, dashboards and references in additon to the assemment.



To request  a copy of the Google Sheet please send an email to info@cloud.ucsb.edu.  After access has been provided a copy of the Sheet should be made and kept locally and upated reqularly to track your compliance.  For more background information on NIST 800-171 assessment please, see the following information:

<br>

NIST Special Publication 800-171A - 
[Assessing Security Requirements for
Controlled Unclassified Information](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-171A.pdf)

* Family - The NIST requirements are organized into 14 families. Within the family are specific requirements related to that family.
    * The 14th requirement family, "System and Information Integrity" can be referenced by its number, 3.14. Every requirement in this Family would have that prefix. 
* sub-Family number - A sub number is ennumerated for each requirement in a family.  
    *  For example, in the  "Access Control" family (3.1) the third requirement is "Control the flow of CUI in accordance with approved authorizations" (3.1.3). 
* Objective - Each requirement includes one or more assessment objectives labeled with the family sub-number and a letter (3.1.1[a])


