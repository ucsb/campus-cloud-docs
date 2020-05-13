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
While many security principles are similar in a IaaS environment, like the idea of "defense in depth" and the use firewalls, they have evolved and are applied differently in the cloud. The cloud security model has evolved to a layered stack of integrated tools and components that are largely software-defined.

- Network Security: VPC - an isolation tool, Security Groups, NACLs 
- Encryption & Key Management - key storage,backup, revokation, recovery ("you left your Key on the image!")
- Configuration Managment - everything can be looked at as a software object
- Event Managment: Logging & Monitoring.  Logging is critical! (i.e VPC flow logs)
- Identity Access & Managmeent:  IAM accounts, roles, groups, policy
- Data life cycle - ownership, classification, rentention, disposal, ...

For more info see:
  [Security, Identity, and Compliance on AWS](https://aws.amazon.com/products/security/?nc=sn&loc=2)
 or the [Amazon Security Blog](https://aws.amazon.com/blogs/security/tag/best-practices/)
