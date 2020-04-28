---
title: Security Guidelines
description: Security Guidelines
permalink: /docs/guidelines/security
---

## Security Guidelines

### AWS Security

#### AWS Shared Responsibility Model

Security is a shared responsibility between AWS, the Campus Cloud Team, and individual users. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security of the cloud and security in the cloud:

Security of the cloud – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. The effectiveness of our security is regularly tested and verified by third-party auditors as part of the [AWS compliance programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to AWS Control Tower, see AWS Services in Scope by Compliance Program.

Security in the cloud – Your responsibility is determined by the AWS services that you use. You are also responsible for other factors including the sensitivity of your data, your organization's requirements, and applicable laws and regulations.

#### User Access

We strongly recommend that you do not use the [root user](/glossary#rootuser) for your everyday tasks, even the administrative ones.
Instead, adhere to the best practice of using UCSB Identity Account using Single Sign-On.
Then securely lock away the root user credentials and use them to perform only a few account and service management tasks.
To view the tasks that require you to sign in as the root user, see [AWS Tasks That Require Root User](https://docs.aws.amazon.com/general/latest/gr/aws_tasks-that-require-root.html).
