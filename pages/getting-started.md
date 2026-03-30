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

For public cloud hosting, approved providers are Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform (GCP). Each cloud provider gives you an Account (AWS), a Subscription (Azure), or a Project (GCP). These docs refer to all three collectively as a **Campus Cloud Account**.

Using an approved provider means that:

*   You have access to account management and Campus Cloud solution architects — AWS, Azure, and GCP experts who can assist with how to use, and provide technical guidance on best practices.
*   Your vendor relationship falls under the University of California Terms & Conditions. This ensures that your agreement conforms to the UC Regents’ policies for procurement and business contracts, and reduces the financial risk to your department or division for agreements that are outside of Regental standing orders (especially with respect to third-party liability).

## [Training](#training)

The following resources can help you get up to speed on cloud concepts before you start.

* #### Campus resources
  The UCSB [LinkedIn Learning](https://www.learningcenter.ucsb.edu/content/linkedin-learning)
  library (free with UCSB NetID) includes:
  * [Cloud Computing courses](https://www.linkedin.com/learning/topics/cloud-computing-5)
  * [AWS courses](https://www.linkedin.com/learning/search?keywords=aws)
  * [Azure courses](https://www.linkedin.com/learning/search?keywords=azure)
  * [GCP courses](https://www.linkedin.com/learning/search?keywords=google+cloud)

* #### AWS
  * [AWS Cloud Practitioner Essentials](https://aws.amazon.com/training/learn-about/cloud-practitioner/) (free)
  * [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)

* #### Azure
  * [Microsoft Learn — Azure fundamentals](https://learn.microsoft.com/en-us/training/paths/az-900-describe-cloud-concepts/)
  * [Microsoft Cloud Adoption Framework](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/)

* #### GCP
  * [Google Cloud Skills Boost](https://www.cloudskillsboost.google/) (free learning paths)
  * [Google Cloud documentation](https://cloud.google.com/docs)

## [Consultation](#consultation)

*  Consult with your local IT staff. They may have processes or protocols in place for sharing responsibility for your Campus Cloud Account(s).  
*  Consult with the Campus Cloud Team.

## [Budgeting](#budgeting)
{% include alert.html type="warning" title="Warning" content="Audit, compliance and security tools are utilized in the Campus Cloud that generate costs in every account. It is important that you are aware of these costs. For a busy account it may be a small percentage of monthly costs." %}
Before you start the procurement process, you will need to estimate your monthly spend.

* [AWS Pricing Calculator](https://calculator.aws/)
* [Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/)
* [GCP Pricing Calculator](https://cloud.google.com/products/calculator)


## [Procure a Campus Cloud Account](#procure-a-campus-cloud-account)
{% include alert.html type="info" title="Information" content="AWS accounts requested with @ucsb.edu emails must be created in the Campus Cloud. You will receive an \"error processing your request\" when requesting a AWS Account with a @ucsb.edu email unless it is in the Campus Cloud LZ. <a href='/docs/guidelines/account-request'> &nbsp;&nbsp;More Info</a>" %}


All three providers use the same Gateway procurement process. Creating a Purchase Order (PO) is the first step for a new AWS account, Azure subscription, or GCP project — as well as for migrating an existing account.

You will not be able to access your account until all steps are completed and the Campus Cloud Team creates it.

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

5.  The Campus Cloud team will receive your Purchase Order and contact you to finalize setting up your account.
6.  After it is set up, you will receive an activation email with instructions to access your new account.
7.  Assign users to your Account Groups.
8.  Your account will be billed through the Master Payer Account with consolidated billing. Any monthly costs will be charged against the Purchase Order you submitted.

### Troubleshooting Gateway

**Requisition returned automatically?** Verify all three codes:
* Commodity Code: **81110000**
* Object Code: **7185**
* Sub: **3, 5, or 7**

**Can't enter the Object Code?** You may lack the required permissions. Forward your cart to a departmental procurement person who can enter the account string.

---

Once your account is active, follow the First Steps guide for your provider:
[AWS First Steps]({{ site.baseurl }}/docs/aws/first-steps) ·
[Azure First Steps]({{ site.baseurl }}/docs/azure/first-steps) ·
[GCP First Steps]({{ site.baseurl }}/docs/gcp/first-steps)
