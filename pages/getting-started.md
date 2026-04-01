---
layout: page
title: "Get a Campus Cloud Account"
permalink: /getting-started
last_reviewed: 2026-04-01
redirect_from:
  - /getting-started/procurement
---

## Get a Campus Cloud Account

### Budgeting

Before you start the procurement process, estimate your monthly spend.
See [Costs & Billing]({{ "/docs/general/cost-management" | relative_url }}) for
pricing calculators, UC enterprise discounts, baseline costs, and tips on
managing your cloud budget.

---

### Gateway Procurement Process

{% capture alert_content %}AWS accounts requested with @ucsb.edu emails must be created in the Campus Cloud. You will receive an "error processing your request" when requesting a AWS Account with a @ucsb.edu email unless it is in the Campus Cloud Landing Zone. <a href='{{ "/docs/general/identity#external-collaborators" | relative_url }}'>More Info</a>{% endcapture %}
{% include alert.html type="info" title="Information" content=alert_content %}

All three providers use the same Gateway procurement process. Creating a Purchase Order (PO) is the first step for a new AWS account, Azure subscription, or GCP project — as well as for migrating an existing account.

You will not be able to access your account until all steps are completed and the Campus Cloud Team creates it.

1.  Log in to the [UCSB Gateway Procurement System](https://it.ucsb.edu/administration-business/gateway)
2.  Complete the Campus Cloud Form.

    ![Gateway Procurement System home page showing the Campus Cloud form link]({{ "/assets/img/gatewayhome.png" | relative_url }})

    * Please note the instructions on the left side of the form, and provide the requested information. Build in lead time for your start date. The estimated expenditure is for the duration of the PO.
    * The expected duration is one year. The purchase order should then be renewed annually. If your procurement group is willing to support multi-year blankets, please limit your max duration to three years.
    * The form is for the one Account. You can not request multiple accounts with a single form. You will want to fill out multiple forms and add them as line items in your cart.
    * _NOTE: Your Gateway Admin may be needed to input Object Code and Sub Number (See Troubleshooting Section below)_

    ![Campus Cloud procurement form with fields for account details]({{ "/assets/img/gatewayform.png" | relative_url }})

3.  Add the completed form to your Cart.
    
    Verify that you have set the correct Commodity Code: **81110000**
    
    ![Gateway cart showing Commodity Code field set to 81110000]({{ "/assets/img/gatewaycart-commoditycode.png" | relative_url }})
    
    and Object Code: **7185**
    
    ![Gateway cart showing Object Code field set to 7185]({{ "/assets/img/gatewaycart-objectcode.png" | relative_url }})	 
    
    and Sub **3, 5 or 7**. Your requisition will be returned if these codes are not correct. SUBMIT your requisition.

5.  The Campus Cloud team will receive your Purchase Order and contact you to finalize setting up your account.
6.  After it is set up, you will receive an activation email with instructions to access your new account.
7.  Assign users to your Account Groups.
8.  Your account will be billed through the Master Payer Account with consolidated billing. Any monthly costs will be charged against the Purchase Order you submitted.

---

### Troubleshooting Gateway

**Requisition returned automatically?** Verify all three codes:
* Commodity Code: **81110000**
* Object Code: **7185**
* Sub: **3, 5, or 7**

**Can't enter the Object Code?** You may lack the required permissions. Forward your cart to a departmental procurement person who can enter the account string.

---

Once your account is active, follow the First Steps guide for your provider:
[AWS First Steps]({{ "/docs/aws/first-steps" | relative_url }}) ·
[Azure First Steps]({{ "/docs/azure/first-steps" | relative_url }}) ·
[GCP First Steps]({{ "/docs/gcp/first-steps" | relative_url }})
