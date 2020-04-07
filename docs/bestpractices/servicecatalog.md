## AWS Service Catalog

The AWS Service Catalog enables organizations to create and manage catalogs of products that are approved for use on AWS. The Campus Cloud Team and or the local Admininstrator of an account may create a Service Catalog. 

A Service Catalog created by a local Administrator is scoped to that account only.  A Service Catalog from the Campus Cloud Team is meant to provide features available to the Organization that can simply be applied to an account by selecting a Product from a menu. 

It is also possible for Account holders to submit services they have created for use in the campus Service Catalog.

Find more information, see [AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/dg/what-is-service-catalog.html).

## Key UCSB Service Catalog Products
The Service Catalog Products below are essential to building out your AWS projects as they provide network connectivity and initialize Group/Role use with UCSB Identity. Using these products will save you time and money.

### Simple VPC with Campus Connectivity
* Create a simple VPC with allocated private IP space. 

This Product provides connectivity between the account and back to campus via a Transit Gateway (TG) and supports VPN connectivity as needed.  Not only does this save the time and configuration to set up a VPC independently but, the Campus Cloud Team is covering the costs of traffice across the TG and VPN.

### Create Shiboleth Group to Role Mapping
* This Product creates an empty IAM Role (AWS) and map it to a group in the UCSB Identity system (LDAP). 

After creation of the empty Role configure your role permissions by attaching an existing policy or writing a new policiy in the [AWS IAM Service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html). Next manage your Shiboleth group membership via UCSB IM group tagger - https://im.ucsb.edu. (Be sure to login via SSO).

Learn more about Access Management, see [Permissions and Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_access-management.html)

![UCSB Service Catalog](/campus-cloud-docs/assets/img/ucsb-servicecatalog.png)
