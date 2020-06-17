## Troublehsooting VPN Traffic

In order to troubleshoot traffic issues to or from the Campus VPN we need to validate a few things.

NOTE: Only traffic that is unable to use secure network protocols should be routed over the VPN.  The VPN path is not intended for commodity traffic. 

### FIRST - Check the Following

- Your Campus Cloud account's VPC has ~~a public and or~~ a private subnet(s)
- Those subnet(s) are using a 10.x.x.x RFC 1918 PRIVATE address space
- AWS Security Group (SG) is allowing your specific traffic
- AWS network ACL configured for the subnet is allowing your specific traffic IN and OUT (optional)

###  Common Solution - Campus-centric issues  

Most cases have been resolved by modifying a campus host based firewall to except traffic from the specific IP address/subnets being used in your Campus Cloud account.  

**Remember these RFC 1918 private addresses (e.g. 10.x.x.x) are being routed back to campus**

If the above items are all true then the issue is likely to be local to your service or host.  We suggest you check the folowing in this order:

1.  Host based firewall - update to allow traffic from the PRIVATE address space (e.g. 10.x.x.x) campus is using for its AWS Campus Landing Zone
2.  Campus network ACLs - Investigate ACLs for your campus networks
3.  UTM - the Palo Alto UTM could be disrupting traffic - make inquiry with the NOC


