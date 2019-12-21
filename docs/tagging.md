# Tagging
Campus Cloud Tagging Documentation.  Document will evolve over time as tagging needs, best practices and use cases develop.

Table of Contents
  * Workgroup
  * Vocabulary
  * Vocabulary Definitions
  * Namespace
  
## Workgroup
* In September of 2019 a UCSB Tagging Workgroup was created from the larger Campus Cloud Champions members. 
* Be an active workgroup facilitating the launch and evolution of a tagging framework.
* The tagging workgroup met 3 times in Sep and Oct.
*  Delivered LZ rev1 Tagging Vocabulary to the UCSB Cloud Teaam on Oct 22, 2019.
  
## Vocabulary
```
Tag	Type	Use Case	Cost Alloc	Namespace	Definition	LZ rev	Possible value(s)
po-number	Account:Mandatory	Business	yes	ucsb:	Account tag made up of fund account string associated with vendor blanket in Gateway	1	PO # in GW
Name	AWS Reserved			no prefix	Resource tag (except S3?) assigned/used in Manangement Console		
environment	Resource:Optional	Technical	yes	ucsb:	Resource tag to identify criticality of resource, support automation	1	prod, dev, test, other
data-classification	Resource:Mandatory	Compliance		ucsb:	Resource tag to ensure compliance	1	p1, p2, p3, p4
business-service	Resource:Required	Technical	yes	ucsb:	Resource tag to organize resources that support an application or service	1	any 
mission	Account:Mandatory	Business	yes	ucsb:	Resource tag to allow OCIO, executives breakdown by mission	1	academic, research, administrative, mixed
lifecycle		Technical		ucsb:	Resource tag to provide some info on lifecyle		end-date:yyyymmdd, none, ephemeral ?
contact	Account:Required	Business		ucsb:	Account tag to make business contact info easily available	1	ucsb:contact:business=jane@ucsb.edu, ucsb:contact:security=doe@ucsb.edu, ucsb:contact:technical=john@ucsb.edu
costing	Resource:Optional	Business	yes	ucsb:	Tag to furtherbreakdown your invoice (FAU, cost center,...)	1	any
```

## Vocabulary Definitions (as of LZ rev1)
* Tag = key and value(s)
* Max key length: 128 Unicode characters	
* Max value length: 256 Unicode characters
* Tags should not contain sensitive or private information
* Cost Allocation tags are only visible in Master Payee Account
* Use each Key only once for each resource
* Allowed characters:  letters, numbers, spaces representable in UTF-8, and the following characters: + - = . _ \: / @
* Case sensitive

## Namespace
* Reserved namespace prefix = aws:
* Reserved namespace prefix = ucsb:
* Local namespace prefix = ucsb:dept\:<CODE> with <CODE> equal to 4 character Chart of Accounts code (capitalized)	
	Example\: ucsb\:dept:GSED
