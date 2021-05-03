---
title: Tagging Guidelines
description: Tagging Guidelines
permalink: /docs/guidelines/tagging
---

## AWS & Azure Tagging
NOTE: Tagging guidelines have been updated as of 4/29/21 Cloud Champions meeting. See included notes below

### Tagging
Tagging allows customers to add a helpful labels to AWS resources. These labels are technically called Tags and help manage your resources.  The UCSB Campus Cloud team will utilize Tags to organize the AWS Campus Cloud Landing Zone (LZ) environment and to make invoicing efficient and user friendly.

Tags can also be used independently by account holders in the AWS Campus Cloud LZ.  In order to user Tags effectively we will define a namespace, vocabulary, and [best practices]({{ site.baseurl }}/docs/bestpractices).

Tags are custom attributes to your AWS resources that make it easier to identify, organize, and search for resources. Each tag has two parts:
  1.  ***key***  (for example, business-service). Tag keys are case sensitive.
  2. ***value***  (for example, kronos-webserver). An optional field. Tag values are also case sensitive.

You can use tags to categorize resources by po-number, environment, ~~data-classification~~ (changed 4/29/21) protection-level, business-service, mission, contact, costing, availability-level (added 4/29/21) or other criteria.

For more information, see [AWS Tagging Strategies](https://aws.amazon.com/answers/account-management/aws-tagging-strategies/) and [Azure Tagging Best Practices](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/naming-and-tagging)


#### Table of Contents
*   Namespace
*   Vocabulary
*   Vocabulary Definitions

### Namespace
You can think of the tag namespace as a container for a set of tag keys. AWS has their own reserved namespace for tags as does Azure. The Campus Cloud Team also requires its own namespace. Local account holders may also use a namespace,
*   Reserved namespace prefix = aws:
*   Reserved namespace prefix = ucsb:
*   Reserved namespace prefix = ucsb:environment:name  (added 4/29/21). Keep name suffix SHORT
*   Local namespace prefix = ucsb:dept:\<CODE> with \<CODE> equal to 4 character Chart of Accounts code (capitalized)
*   Example: ucsb:dept:GSED

### Vocabulary (LZ rev2)
Abbreviated vocabulary shown below. See CCC Tagging workgroup Documentation for more info.
```
Tag			Type			 Use Case	Cost Alloc	Namespace	LZ rev	Definition										Possible value(s)
ucsb:po-number		 Account:Mandatory	Business	yes		ucsb:		1	Account tag made up of fund account string associated with vendor blanket in Gateway	PO # in GW		
ucsb:environment	 Resource:Optional	Technical	yes		ucsb:		1	Resource tag to identify criticality of resource, support automation			prod, dev, test, other
ucsb:protection-level    Resource:Mandatory	Compliance			ucsb:		2	Resource tag to ensure compliance							p1, p2, p3, p4
ucsb:availability-level  Resource:Optional	Compliance			ucsb:		2	Resource tag to ensure compliance							a1, a2, a3, a4
ucsb:business-service	 Resource:Required	Technical	yes		ucsb:		1	Resource tag to organize resources that support an application or service		any
ucsb:mission		 Account:Mandatory	Business	yes		ucsb:		1	Resource tag to allow OCIO, executives breakdown by mission				academic, research, administrative, mixed
ucsb:contact		 Account:Required	Business			ucsb:		1	Account tag to make business contact info easily available				ucsb:contact:business=jane@ucsb.edu, ucsb:contact:security=doe@ucsb.edu, ucsb:contact:technical=john@ucsb.edu
ucsb:costing		 Resource:Optional	Business	yes		ucsb:		1	Tag to further breakdown your invoice (FAU, cost center,...)				any
```

### Vocabulary Definitions
*   Tag = key and value(s)
*   Max key length: 128 Unicode characters
*   Max value length: 256 Unicode characters
*   Tags should not contain sensitive or private information
*   Cost Allocation tags are only visible in Master Payee Account
*   Use each Key only once for each resource
*   Allowed characters:  letters, numbers, spaces representable in UTF-8, and the following characters: + - = . _ : / @
*   Case sensitive
*   Mandatory tags are used for compliance, created with automation and enforced
*   Required tags may be applied as part of self-service capability, may be updated (from null) by account owner after creation due to compliance notification
*   Optional tags may be applied with out any compliance or enforcement
