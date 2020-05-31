---
title: Security Guidelines
description: Security Guidelines
permalink: /docs/guidelines/security
---

## Security Guidelines

### AWS Security

#### AWS Shared Responsibility Model

Security is a shared responsibility between AWS, the Campus Cloud Team, and individual users. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security of the cloud and security in the cloud:

Security OF the cloud – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. The effectiveness of our security is regularly tested and verified by third-party auditors as part of the [AWS compliance programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to AWS Control Tower, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).

Security IN the cloud – Your responsibility is determined by the AWS services that you use. You are also responsible for other factors including the sensitivity of your data, your organization's requirements, and applicable laws and regulations.

#### Lift & Shift vs Well Architected Framework
For many reasons, taking your on-prem assests and just "lift & shift"ing them to the cloud in not ideal. It is better and more secure to re-architect your service or application for the cloud. AWS has develeoped a comprehensive framework called the [Well Architected Framework](https://aws.amazon.com/architecture/well-architected/) to build secure, high-performing, resilient, and efficient infrastructure in the cloud

#### User/root Access

We strongly recommend that you do not use the [root user](/glossary#rootuser) for your everyday tasks, even the administrative ones.
Instead, adhere to the best practice of using UCSB Identity Account using Single Sign-On.
Then securely lock away the root user credentials and use them to perform only a few account and service management tasks.
To view the tasks that require you to sign in as the root user, see [AWS Tasks That Require Root User](https://docs.aws.amazon.com/general/latest/gr/aws_tasks-that-require-root.html).

#### Key Security Areas

While many security principles are similar in a IaaS environment, like the idea of "defense in depth" and the use firewalls, they have evolved and are applied differently in the cloud. The cloud security model has evolved to a layered stack of integrated tools and components that are largely software-defined. The following areas areas are critical to cloud security:

- **Define & categorize your data**:
  - Policy needs to be continually reviewed and updated to define, idenitfy, analyze and address risks
  - Data privacy classification is required to be identified by resource with the use of Tags 
  - Data life cycle - ownership, classification, rentention, disposal, ...
- **Manage AWS accounts, IAM users, Groups, Roles**:
  - AWS accounts and IAM accounts should be given least priviledge and use MFA where available, additionally use separate accounts for diffent functions or environments
  - Groups are a powerful tool for managing access to resources.  It is a best practice to use Groups even for one or two users
  - Roles are an extremely useful way to delegate access to users or services in an secure/temporary way
- **Network Security**: 
  - VPC - is an isolation tool and elementary part of security in the Cloud, 
  - Security Groups (SG) are analogous to a stateful host based firewall
  - Network ACLs are applied to a subnet and are stateless.
- **Encryption & Key Management** 
   - Protect data at rest and in transit - encrypt by default is a best practice
   - Key Management - storage, backup, revokation, recovery. Got a secret, store it in AWS Secrets Manager
- **Manage and Monitor your environment**
   - Configuration Managment - everything can be looked at as a software object. Automate IaaS and Dev processes where possible
   - Event Managment: Logging & Monitoring.  Logging is critical! (i.e VPC flow logs)
   - Alarms & Notifications

For more info see:
  [Security, Identity, and Compliance on AWS](https://aws.amazon.com/products/security/?nc=sn&loc=2)
 or the [Amazon Security Blog](https://aws.amazon.com/blogs/security/tag/best-practices/)
