## AWS Service Catalog

The AWS Service Catalog enables organizations to create and manage catalogs of products that are approved for use on AWS. The Campus Cloud Team and or the local Admininstrator of an Account may create a Service Catalog. 

A Service Catalog created by a local Administrator is scoped to that account only.  A Service Catalog from the Campus Cloud Team is meant to provide features available to the Organization that can simply be applied to an account by selecting a Product from a menu. 

It is also possible for Account holders to submit services they have created for use in the campus Service Catalog.

Find out more about the [AWS Service Catalog] (https://docs.aws.amazon.com/servicecatalog/latest/dg/what-is-service-catalog.html).

## Key Service Catalog items
The Service Catalog Products below are essential to building out your AWS projects as they provide network connectivity and initialize Group/Role use with UCSB Identity.

### Simple VPC with Campus Connectivity
* Create a simple VPC with allocated private IP space. Connectivity between account and back to campus provided by transit gateway and vpn.

### Create Shiboleth Group to Role Mapping
* This will create an Empty IAM Role and map it to a group in UCSB Identity. Configure your role permissions after creation. Manage your shiboleth group membership via UCSB IM Group Tagger.

![UCSB Service Catalog](/assets/img/ucsb-servicecatalog.png)
