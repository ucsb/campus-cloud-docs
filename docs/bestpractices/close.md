## Cloud Account Closure

When you are ready to close your Campus Cloud account(AWS, Azure) please follow the steps below.  It is important to understand that once the account is CLOSED any data, analysis, reports, objects in S3 buckets or Azure storage and all other resources will be unavailable. The associated PO should NOT be closed until 1 month AFTER the final invoicing from the Campus Cloud Team.

It is imperative that you destroy all resources that you have created AFTER backing up any/all data you wish to maintain.

A request to close a Campus Cloud account is NOT completed until all Resources created by the Owner have been destroyed. A good indicator that this has been accomplished is the account charges are minimal (<$5-10/mo).  A nominal dollar amount per month is normal to maintain an account in the Landing Zone.

⚠️ WARNING - once you CONFIRM your account for closure in step 4 below, you are confirming there is nothing in the account that you need and ALL resources, data, etc can be destroyed.  This is not a reversible process. There is no "undo".

### Procedure for Account Closure

1. Destroy Resources - Owner of account Destroys all Resources created in account.
2. Backup DATA - Owner of account backups/downloads all Data that needs to be saved or archived.
3. Create ServiceNow (SN) ticket to close account. (https://ucsb.service-now.com/).

   * Home -> Information Technology Services -> Advanced Technical Services -> Cloud Services -> Cloud Question
   * Include **Account#/Subscription#**, **PO#** and **date** for account to be closed.
 
5. CONFIRM in the ServiceNow Ticket each list item below is complete to authorize the closure of the account.
   * Remove Data sources - Confirm all regulated data, Datasets, etc. have been removed.
   * Remove Data created - Confirm all data, reports, analysis, etc have been removed from the account or can be deleted.
   * Destroy Resources - Confirm all owner created resources have been destroyed.

   **Above confirmations are implied for *ALL* users of the account**.

6. If Owner does not or can not shut down ALL Resources they authorize the Cloud Team to Destroy all Resources and data.
7. Cloud Team will wait 15 days to Destroy all remaining Resources, Data, etc.
8. Cloud Team will wait 5 additional days to remove access to Account.

<br>

### Final Invoice for Purchase Order (PO)

ℹ️ IMPORTANT - The PO associated with the account should not be closed for 30 days after the final invoicing to ensure Accounting has time to process the invoice. The Cloud team invoices for the previous months costs about 3 weeks after the end of the month.

{% include alert.html type="warning" title="Warning" %}


The PO associated with the account should not be closed for 30 days after the final invoicing to ensure Accounting has time to process the invoice. The Cloud team invoices for the previous months costs about 3 weeks after the end of the month.

<br>

The Service Now Ticket will be closed after the final invoice has been submitted.  All corespondence regarding an account closure should be included in the Service Now Ticket.
