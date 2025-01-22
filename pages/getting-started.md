---
layout: page
title: "Getting Started"
permalink: /getting-started/
tags:
 - cloud
 - aws
 - azure
 - gcp
 - github
---

# Getting Started

The UCSB Campus Cloud allows faculty, researchers and staff to provision and use computing resources from approved vendors that have agreements in place with the University of California.

For public cloud hosting, approved providers are Amazon Web Services (AWS), Microsoft Azure and coming soon Google Cloud Platform (GCP). Each cloud provider provides an Account, a Subscription or a Project, respectively.  These Campus Cloud Docs will collectively refer to these resources as a [Campus Cloud Account](/campus-cloud-docs/glossary/#campuscloudaccount) when specificity is not required. 

Using an approved provider means that:

*   You have access to account management and solution architects — AWS and Azure staff who can assist with how to use, and provide technical guidance on best practices.
*   Your vendor relationship falls under the University of California Terms & Conditions. This ensures that your agreement conforms to the UC Regents’ policies for procurement and business contracts, and reduces the financial risk to your department or division for agreements that are outside of Regental standing orders (especially with respect to third-party liability).

## [Training](#training)

It is highly recommended to have an understanding of Cloud environment concepts and methodologies. Specifically, AWS' [Well Architected Framework](https://aws.amazon.com/architecture/well-architected/) and [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/).

[Microsoft's Cloud Adoption Framework for Azure](https://azure.microsoft.com/en-us/cloud-adoption-framework/#:~:text=The%20Cloud%20Adoption%20Framework%20provides,the%20framework%20is%20updated%20regularly.) is similiarly recomended for Azure.



* ### Campus Training Resources
	The UCSB [Learning Center](https://www.learningcenter.ucsb.edu/) and more specifically, [Linkedin Learning](https://www.learningcenter.ucsb.edu/content/linkedin-learning) offers courses for Cloud Computing and AWS.
	* [Cloud Computing Topic](https://www.linkedin.com/learning/topics/cloud-computing-5)
	* [AWS Courses](https://www.linkedin.com/learning/search?keywords=aws)
	* [Azure Courses](https://www.linkedin.com/learning/search?keywords=azure)

* ### AWS Training Resources

	*   Take the free [Cloud Practitioners Training](https://www.aws.training/Details/Curriculum?id=27076)

* ### Azure Training Resources

	* [Azure on Microsoft Learn](https://docs.microsoft.com/en-us/learn/azure/)

## [Consultation](#consultation)

*  Consult with your local IT staff. They may have processes or protocols in place for sharing responsibility for your Campus Cloud Account(s).  
*  Consult with the Campus Cloud Team.

## [Budgeting](#budgeting)
{% include alert.html type="warning" title="Warning" content="Audit, compliance and security tools are utilized in the Campus Cloud that generate costs in every account. It is important that you are aware of these costs. For a busy account it may be a small percentage of monthly costs." %}
Before you start the procurement process, you will need to estimate your monthly spend.

*   AWS Cost Calculator
    *   [Simple Monthly Calculator](https://calculator.s3.amazonaws.com/index.html)
	  *   The new [Pricing Calculator](https://calculator.aws/#/)
*   Azure Pricing Calculator
	  * [Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/?&ef_id=Cj0KCQjwvr6EBhDOARIsAPpqUPHPjtVqbRjubykatJR6m_x7p-TMY9WOmVU-YjF-LqNc4-ambKzOU8AaAk02EALw_wcB:G:s&OCID=AID2100131_SEM_Cj0KCQjwvr6EBhDOARIsAPpqUPHPjtVqbRjubykatJR6m_x7p-TMY9WOmVU-YjF-LqNc4-ambKzOU8AaAk02EALw_wcB:G:s&gclid=Cj0KCQjwvr6EBhDOARIsAPpqUPHPjtVqbRjubykatJR6m_x7p-TMY9WOmVU-YjF-LqNc4-ambKzOU8AaAk02EALw_wcB)   	  

{::comment} ℹ️ IMPORTANT - Audit, compliance and security tools are utilized in the Campus Cloud that generate costs in every account. It is important that you are aware of these costs. For a busy account it may be a small percentage of monthly costs.{:/comment} 


## [Procure a Campus Cloud Account](#procure-a-campus-cloud-account)
{% include alert.html type="info" title="Information" content="AWS accounts created wtih @ucsb.edu emails must be created in the Campus Cloud." %}

Creating a Purchase Order is the first step to procuring a new Azure Subscription, a new AWS Accounts or migrating an existing AWS Accounts to the Campus Cloud.
A Campus Cloud Account is used for UCSB business is covered under an enterprise agreement and in compliance with UC policy and applicable laws. Follow the instructions below to create the Purchase Order.

You will only be able to access the Campus Cloud Account and its resources after all steps below are completed and the UCSB Campus Cloud team creates your account.

1.  Log in to the UCSB Gateway Procurement System
2.  Complete the Campus Cloud Form.

	![assets/img/gatewayhome.png]({{site.url}}assets/img/gatewayhome.png)

    * Please note the instructions on the left side of the form, and provide the requested information. Build in lead time for your start date. The estimated expenditure is for the duration of the PO.
    * The expected duration is one year. The purchase order should then be renewed annually. If your procurement group is willing to support multi-year blankets, please limit your max duration to three years.
    * The form is for the one Account. You can not request multiple accounts with a single form. You will want to fill out multiple forms and add them as line items in your cart.
    * _NOTE: Your Gateway Admin may be needed to input Object Code and Sub Number (See Troubleshooting Section below)_

	![assets/img/gatewayform.png]({{site.url}}assets/img/gatewayform.png)

3.  Add the completed form to your Cart.
	
	Verify that you have set the correct Commodity Code: **81110000**
	
	![assets/img/gatewaycart-commoditycode.png]({{site.url}}assets/img/gatewaycart-commoditycode.png)
	
	and Object Code: **7185**
	
	![assets/img/gatewaycart-objectcode.png]({{site.url}}assets/img/gatewaycart-objectcode.png)	 
	
	and Sub **3, 5 or 7**. Your requisition will be returned if these codes are not correct. SUBMIT your requisition.

5.  The Campus Cloud team will receive your Purchase Order and contact you to schedule a meeting finalizing your account.
6.  After this meeting you will receive an activation email from AWS/Azure:
    *  Confirming that the account is set up for invoicing under the UC AWS or Azure agreement, and
    *  Providing final instructions to activate your account
7.  Assign users to your Account Groups.
8.  Your account will be billed through the Master Payer Account with consolidated billing. Any monthly costs will be charged against the Purchase Order you submitted.

NOTE: As of May 16th 2020, you may use Sub 5 or Sub 7 in additional to the original requirement of Sub 3. 

### Troubleshooting the Procurement Process

 Q1. Did your requisition get returned with an error? 
 
 Gateway will auto-return the requistion if any of the following is incorrect:
*   Commodity Code __81110000__
*   Object Code __7185__
*   Sub __3, 5 or 7__

Q2. Were you able to enter the commodity code, but **NOT** the object code?
*   You may NOT have the required permissions to enter the object code and/or the account string
*   Forward the cart on to a Departmental procurement person who does and finish entering in the required information

### Proceed to the [First Steps]({{ site.baseurl }}/docs/firststeps) to set up your Account
