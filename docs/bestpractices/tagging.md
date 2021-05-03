---
title: Resource Tagging
description: Security Guidelines
permalink: /docs/bestpractices/tagging
---


## Resource Tagging
Campus Cloud Tagging Documentation of resource tagging best practices.
More to come ....


## Vocabulary Definitions
* Tag = key and value(s)
* Max key length: 128 Unicode characters	
* Max value length: 256 Unicode characters
* Tags should not contain sensitive or private information
* Cost Allocation tags are only visible in Master Payee Account
* Use each Key only once for each resource
* Allowed characters:  letters, numbers, spaces representable in UTF-8, and the following characters: + - = . _ : / @
* Case sensitive
* Mandatory tags are used for compliance, created with automation and enforced
* Required tags may be applied as part of self-service capability, may be updated (from null) by account owner after creation due to compliance notification
* Optional tags may be applied with out any compliance or enforcement

## Namespace
* Reserved namespace prefix = aws:
* Reserved namespace prefix = ucsb:
* Reserved namespace prefix = ucsb:environment:name (added 4/29/21). Keep name suffix SHORT
* Local namespace prefix = ucsb:dept:\<CODE> with \<CODE> equal to 4 character Chart of Accounts code (capitalized)	
* Example: ucsb:dept:GSED
