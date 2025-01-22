---
title: Service Catalog
description: Service Catalog Offerings
permalink: /docs/bestpractices/servicecatalog
---

## AWS Service Catalog

The AWS Service Catalog enables organizations to create and manage catalogs of products that are approved for use on AWS. The Campus Cloud Team and or the local Admininstrator of an account may create a Service Catalog.

A Service Catalog created by a local Administrator is scoped to that account only.  A Service Catalog from the Campus Cloud Team is meant to provide features available to the Organization that can simply be applied to an account by "Launching" a Product from a menu.

It is also possible for Account holders to submit services they have created for use in the campus Service Catalog.

Find more information, see [AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/dg/what-is-service-catalog.html).



## UCSB Service Catalog Products
The Service Catalog Products below are essential to building out your AWS projects as they provide network connectivity and initialize Group/Role use with UCSB Identity. Using these products will save you time and money. Goto the "Service Catalog" service in the AWS Console and click on the "Product List" to see the Products available.

![assets/img/ucsb-servicecatalog.png]({{site.url}}assets/img/ucsb-servicecatalog.png)
![UCSB Service Catalog](/campus-cloud-docs/assets/img/ucsb-servicecatalog.png)

### [Local Security Notifications](#localsecurity)
  * This Product will create a local security SNS topic, subscribe an email, and enable notifications for AWS Config compliance (Guardrails).

### [Fixed Monthly Budget with Notification](#monthlybudget)
  * This Product will create a fixed cost monthly budget, and notification based on forecasted threshold.

Learn more about Budgets, see [Managing your costs with AWS Budgets](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html)

### [Budget Alert and Action on Threshold (Effectual)](#budegetalertandaction)
  * Creates a Budget, Budget Alert, and Budget Action to apply IAM policy when threashold is reached. Deploy to home Region only. For more info see [AWS' Effectual Product](https://aws-ia.github.io/cloudformation-effectual-activebudgetcontroller/)

### [Instance Scheduler](#instancescheduler)
  * A simple solution that allows you to create automatic start and stop schedules for your Amazon EC2 and Amazon RDS instances.

### [Create IAM Role to UCSB Identity Group](#rolemapping)
  * This will create an Empty IAM Role and map it to a Group in UCSB Identity.

After creation of the empty Role configure your role permissions by attaching an existing policy or writing a new policiy in the [AWS IAM Service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html). Next Manage your UCSB Identity Group membership via UCSB tools at https://im.ucsb.edu. (Be sure to login via SSO).

Learn more about Access Management, see [Permissions and Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_access-management.html)


### [Simple VPC with Campus Connectivity](#VPC)
  * This Product will create a simple VPC with allocated private IP space.

This Product provides connectivity between the account and back to campus via a Transit Gateway (TGW) and supports VPN connectivity as needed.  Not only does this save the time and configuration to set up a VPC independently, but the costs of the NAT Gateways and VPN are a shared service instead of per account.

Feb 2024 added support for "xlarge" VPC sizes supporting 256 IP addresses.

Description of the VPC Families offered:

|  VPC Family          |  # of Subnets  |  VPC CIDR Size  |  Type of Subnets     |  # of Availability Zones  |
|:------------------:|:--------------:|:---------------:|:--------------------:|:-------------------------:|
|  n1.small.public   |       1        |     32 IPs      |       1 public       |             1             |
|  n1.small.private  |       1        |     32 IPs      |       1 private      |             1             |
|  n1.medium.public  |       1        |     64 IPs      |       1 public       |             1             |
|  n1.medium.private |       1        |     64 IPs      |       1 private      |             1             |
|  n1.large.public   |       1        |     128 IPs     |       1 public       |             1             |
|  n1.large.private  |       1        |     128 IPs     |       1 public       |             1             |
|  n2.medium.public  |       2        |     64 IPs      |       2 public       |             2             |
|  n2.medium.private |       2        |     64 IPs      |       2 private      |             2             |
|  n2.medium.mixed   |       2        |     64 IPs      |  1 public 1 private  |             1             |
|  n2.large.public   |       2        |     128 IPs     |       2 public       |             2             |
|  n2.large.private  |       2        |     128 IPs     |       2 private      |             2             |
|  n2.large.mixed    |       2        |     128 IPs     |  1 public 1 private  |             1             |
|  n4.large.mixed    |       4        |     128 IPs     |  2 public 2 private  |             2             |
|  n2.xlarge.public   |       2        |     256 IPs     |       2 public       |             2             |
|  n2.xlarge.private  |       2        |     256 IPs     |       2 private      |             2             |
|  n2.xlarge.mixed    |       2        |     256 IPs     |  1 public 1 private  |             1             |
|  n4.xlarge.mixed    |       4        |     256 IPs     |  2 public 2 private  |             2             |

### [Advanced VPC](#VPC)
 * This Product will create an advanced VPC supporting allocation of a large private IP address space. Provides the foundation for Campus Connectivity via the TGW.

This Product does not create Transit Gateway (TGW) attachments nor subnets nor associated Route Tables.  It creates an empty VPC with a Main Route Table offering VPC sizes of small, medium, large and xlarge.  Owner will be reponsible creating desired network connectivity.
