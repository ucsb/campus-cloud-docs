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
- [Data privacy classification Tagging](/campus-cloud-docs/guidelines/tagging) on account and per resource
- Use of account must be in accordance with UC Policy IS-3

### How we audit and maintain compliance

The Campus Cloud Providers - AWS, Azure, GCP - may differ in the specific terminology and tools used to audit and maintain compliance. However, each Cloud Provider offers resources to help maintain compliance.  One important resource are Guardrails.  

* ### AWS Guardrails
    In AWS Control Tower and  Guardrails work together to provide ongoing goverance for the Campus AWS environment. Control Tower implements preventive or detective controls that help govern resources and monitor compliance across groups of AWS accounts.  [Tagging](/campus-cloud-docs/glassoary/tags) of accounts and individual resources support compliance efforts. In AWS Gurdrails are rules that define policy. 
    
    * ### [AWS Active Guardrails as of May 2020](compliance/guardrails.aws)



* ### Azure Guardrails
    Azure utilized built-in and custom policies to set guardrails in your subscriptions. Guardrails for Azure are built using Azure Policy and RBAC to enforce and audit policies for any Azure service.
    
    * ### [Azure Active Guardrails as of May 2020](compliance/guardrails.azure)


