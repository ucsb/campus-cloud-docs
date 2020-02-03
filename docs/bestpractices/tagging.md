---
title: Resource Tagging
description: Security Guidelines
permalink: /docs/bestpractices/tagging
---


## Tagging
Campus Cloud Tagging Documentation.
Document will evolve over time as tagging needs, best practices and use cases develop.

Table of Contents
  * Workgroup
  * Vocabulary
  * Vocabulary Definitions
  * Namespace
  
## Workgroup
* September of 2019 a UCSB Tagging Workgroup was created from the larger Campus Cloud Champions members. 
* Mission - Be an active workgroup facilitating the launch and evolution of a tagging framework.
* Tagging workgroup met 3 times in Sep and Oct.
* Delivered LZ rev1 tagging vocabulary to the UCSB Cloud Teaam on Oct 22, 2019.
  
## Vocabulary (LZ rev1)
(abbreviated, see workgroup working Docs for more info)
```
Tag			Type			Use Case	Cost Alloc	Namespace	LZ rev	Definition										Possible value(s)
po-number		Account:Mandatory	Business	yes		ucsb:		1	Account tag made up of fund account string associated with vendor blanket in Gateway	PO # in GW		
environment		Resource:Optional	Technical	yes		ucsb:		1	Resource tag to identify criticality of resource, support automation			prod, dev, test, other
data-classification	Resource:Mandatory	Compliance			ucsb:		1	Resource tag to ensure compliance							p1, p2, p3, p4
business-service	Resource:Required	Technical	yes		ucsb:		1	Resource tag to organize resources that support an application or service		any 
mission			Account:Mandatory	Business	yes		ucsb:		1	Resource tag to allow OCIO, executives breakdown by mission				academic, research, administrative, mixed
contact			Account:Required	Business			ucsb:		1	Account tag to make business contact info easily available				ucsb:contact:business=jane@ucsb.edu, ucsb:contact:security=doe@ucsb.edu, ucsb:contact:technical=john@ucsb.edu
costing			Resource:Optional	Business	yes		ucsb:		1	Tag to furtherbreakdown your invoice (FAU, cost center,...)				any
```

## Vocabulary Definitions
* Tag = key and value(s)
* Max key length: 128 Unicode characters	
* Max value length: 256 Unicode characters
* Tags should not contain sensitive or private information
* Cost Allocation tags are only visible in Master Payee Account
* Use each Key only once for each resource
* Allowed characters:  letters, numbers, spaces representable in UTF-8, and the following characters: + - = . _ : / @
* Case sensitive

## Namespace
* Reserved namespace prefix = aws:
* Reserved namespace prefix = ucsb:
* Local namespace prefix = ucsb:dept:\<CODE> with \<CODE> equal to 4 character Chart of Accounts code (capitalized)	
* Example: ucsb:dept:GSED
