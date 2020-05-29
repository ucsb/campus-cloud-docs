## Troublehsooting VPN Traffic



### FIRST - Check the Following

In order to troubleshoot traffic issues to or from the Campus VPN validate the following:

- Your Campus LZ account VPC has a public and or private subnet
- Those subnet(s) are using a 10.x.x.x RFC 1918 PRIVATE address space
- You are using the VPN route only for traffic that is unable to use secure network protocols
- AWS Security Group (SG) is allowing this specific traffic
- AWS network ACL configured for the subnet is allowing this specific traffic IN and OUT (optional)

###  Campus-centric issues - Common Solution  

Most cases have been resolved by modifying the host based firewall to except traffic from the specific IP address or subnets being used in your AWS Campus Cloud child account.  **REMEMBER these are RFC 1918 private addresses (e.g. 10.x.x.x)**

If the above items are all true then the issue is likely to be local to your service or host.  We suggest you check the folowing in this order:

- The host based firewall has been updated to allow traffic from the Campus AWS PRIVATE address space (e.g. 10.x.x.x)
- Campus network ACLs be investigated with the NOC
- Palo Alto UTM could be disrupting traffic - make inquiry with the NOC


