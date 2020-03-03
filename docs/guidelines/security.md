---
title: Security Guidelines
description: Security Guidelines
permalink: /docs/guidelines/security
---

## Security Guidelines

### AWS Security

#### User Access

We strongly recommend that you do not use the [root user](/glossary#rootuser) for your everyday tasks, even the administrative ones.
Instead, adhere to the best practice of using UCSB Identity Account using Single Sign-On.
Then securely lock away the root user credentials and use them to perform only a few account and service management tasks.
To view the tasks that require you to sign in as the root user, see [AWS Tasks That Require Root User](https://docs.aws.amazon.com/general/latest/gr/aws_tasks-that-require-root.html).
