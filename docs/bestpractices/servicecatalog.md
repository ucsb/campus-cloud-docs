---
title: Service Catalog
description: Service Catalog Offerings
permalink: /docs/bestpractices/servicecatalog
---

## AWS Service Catalog

The AWS Service Catalog enables organizations to create and manage catalogs of products that are approved for use on AWS. The Campus Cloud Team and or the local Admininstrator of an account may create a Service Catalog.

A Service Catalog created by a local Administrator is scoped to that account only.  A Service Catalog from the Campus Cloud Team is meant to provide features available to the Organization that can simply be applied to an account by selecting a Product from a menu.

It is also possible for Account holders to submit services they have created for use in the campus Service Catalog.

Find more information, see [AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/dg/what-is-service-catalog.html).

## Key UCSB Service Catalog Products
The Service Catalog Products below are essential to building out your AWS projects as they provide network connectivity and initialize Group/Role use with UCSB Identity. Using these products will save you time and money. Goto the "Service Catalog" service in the AWS Console and click on the "Product List" to see the Products available.
![UCSB Service Catalog](/campus-cloud-docs/assets/img/ucsb-servicecatalog.png)

### [Simple VPC with Campus Connectivity](#VPC)
* Create a simple VPC with allocated private IP space.

This Product provides connectivity between the account and back to campus via a Transit Gateway (TG) and supports VPN connectivity as needed.  Not only does this save the time and configuration to set up a VPC independently, but the costs of the NAT Gateways and VPN are a shared service instead of per account.

Description of the VPC Families offered:

|  VPC Name          |  # of Subnets  |  VPC CIDR Size  |  Type of Subnets     |  # of Availability Zones  |
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


### [Create Shiboleth Group to Role Mapping](#rolemapping)
* This Product creates an empty IAM Role (AWS) and map it to a group in the UCSB Identity system (LDAP).

After creation of the empty Role configure your role permissions by attaching an existing policy or writing a new policiy in the [AWS IAM Service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html). Next manage your Shiboleth group membership via UCSB IM group tagger - https://im.ucsb.edu (Be sure to login via SSO).

Learn more about Access Management, see [Permissions and Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_access-management.html)
