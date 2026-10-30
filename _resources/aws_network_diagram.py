"""Draws the AWS network diagram on the AWS Networking page (docs/aws/networking.md).

Output: assets/img/UCSB-AWS-LZ-Network-Architecture-v3.png

The facts in the diagram (Direct Connect and VPN in us-west-2 only, us-east-1
peered to us-west-2, NAT Gateway IPs, public subnets reaching campus only over
the internet, the S3 gateway endpoint) were verified against the live AWS organization on
2026-10-30. See DOCS-SITE-VERIFICATION.md (section 3E) in
campus-cloud-aws-landing-zone before changing them, and keep the page text,
the image's alt text and the description under it in step with any change.

Requirements: Python 3, the `diagrams` package (pip install diagrams) and
Graphviz (brew install graphviz).

Run from the repository root (the output name has no .png extension):
    python3 _resources/aws_network_diagram.py assets/img/UCSB-AWS-LZ-Network-Architecture-v3

Files in folders starting with "_" are not published to the website.
"""
import html
import sys
from pathlib import Path

import diagrams
from diagrams import Cluster, Diagram, Edge
from diagrams.aws.general import GenericOfficeBuilding, InternetAlt1
from diagrams.aws.network import (
    DirectConnect,
    Endpoint,
    InternetGateway,
    NATGateway,
    PrivateSubnet,
    PublicSubnet,
    SiteToSiteVpn,
    TransitGateway,
)
from diagrams.aws.storage import SimpleStorageServiceS3

out = sys.argv[1]


def icon(cls, label):
    """A fixed-size icon with its caption below, drawn as one HTML-like label.

    The library's own nodes are a fixed 1.4in box, so long captions spill past
    them, over cluster borders and edges. This node grows to fit its caption.
    """
    src = Path(diagrams.__file__).parent.parent / cls._icon_dir / cls._icon
    text = "<BR/>".join(html.escape(line) for line in label.split("\n"))
    table = (f'<<TABLE BORDER="0" CELLSPACING="4">'
             f'<TR><TD FIXEDSIZE="TRUE" WIDTH="100" HEIGHT="100"><IMG SRC="{src}" SCALE="TRUE"/></TD></TR>'
             f'<TR><TD>{text}</TD></TR></TABLE>>')
    return cls(table, image="", shape="plaintext", fixedsize="false", width="0", height="0", margin="0")


graph_attr = {"fontsize": "30", "pad": "0.4", "nodesep": "1.6", "ranksep": "1.3",
              "fontname": "Helvetica", "labelloc": "t", "splines": "spline"}
node_attr = {"fontsize": "22", "fontname": "Helvetica"}
edge_attr = {"fontsize": "20", "fontname": "Helvetica"}
cluster_font = {"fontsize": "24", "fontname": "Helvetica-Bold", "pencolor": "#4A5560", "penwidth": "1.5"}

DX = {"fontsize": "20", "color": "darkgreen", "penwidth": "2.5"}
VPN = {"fontsize": "20", "color": "darkorange3", "style": "dashed", "penwidth": "2"}
PRIV = {"fontsize": "20", "color": "purple4", "penwidth": "2"}
NET = {"fontsize": "20", "color": "gray30", "penwidth": "1.5"}

with Diagram("UCSB Campus Cloud: AWS network", filename=out, outformat="png",
             show=False, direction="TB", graph_attr=graph_attr, node_attr=node_attr, edge_attr=edge_attr):
    with Cluster("us-west-2 (Oregon)", graph_attr={**cluster_font, "labeljust": "r"}):
        with Cluster("Cloud Team network hub", graph_attr={**cluster_font, "labelloc": "b"}):
            dx1 = icon(DirectConnect, "Direct Connect 1")
            dx2 = icon(DirectConnect, "Direct Connect 2")
            vpn = icon(SiteToSiteVpn, "Site-to-Site VPN\n(backup)")
            tgw_w = icon(TransitGateway, "Transit Gateway")
            nat_w = icon(NATGateway, "NAT Gateways\n44.231.186.204\n44.232.156.254")
        with Cluster("Your VPC (10.226.x.x)", graph_attr=cluster_font):
            pub_w = icon(PublicSubnet, "Public subnet\n(reaches campus only\nover the internet)")
            igw_w = icon(InternetGateway, "Internet Gateway")
            priv_w = icon(PrivateSubnet, "Private subnet")
            s3e = icon(Endpoint, "S3 gateway\nendpoint")
        s3 = icon(SimpleStorageServiceS3, "Amazon S3\n(same region)")

    with Cluster("us-east-1 (N. Virginia)", graph_attr={**cluster_font, "labeljust": "r"}):
        with Cluster("Your VPC, optional (10.227.x.x)", graph_attr=cluster_font):
            priv_e = icon(PrivateSubnet, "Private subnet")
        with Cluster("Cloud Team network hub", graph_attr={**cluster_font, "labelloc": "b"}):
            tgw_e = icon(TransitGateway, "Transit Gateway")
            # Invisible spacer left of the NAT Gateways, so the hub's title sits
            # under empty space and the NAT line to the internet clears it
            spacer = diagrams.Node("", style="invis", width="1.6", height="0.1")
            nat_e = icon(NATGateway, "NAT Gateways\n3.213.17.213\n54.86.139.106")

    campus = icon(GenericOfficeBuilding, "UCSB campus network")

    internet = icon(InternetAlt1, "Internet")

    # Campus links: both Direct Connect connections and the VPN end in us-west-2 only
    campus >> Edge(label="Direct Connect", **DX) >> [dx1, dx2]
    campus >> Edge(label="VPN over\nthe internet", **VPN) >> vpn
    [dx1, dx2] >> Edge(**DX) >> tgw_w
    vpn >> Edge(**VPN) >> tgw_w
    tgw_w - Edge(label="peering: us-east-1 reaches\ncampus through us-west-2",
                 constraint="false", color="darkgreen", penwidth="2.5", fontsize="20") - tgw_e

    # Private subnets send everything else leaving the VPC to the Transit Gateway
    priv_w >> Edge(label="all other\ntraffic", **PRIV) >> tgw_w
    priv_e >> Edge(label="all other\ntraffic", **PRIV) >> tgw_e

    # Central egress to the internet
    tgw_w >> Edge(label="internet-bound", **NET) >> nat_w >> Edge(**NET) >> internet
    tgw_e >> Edge(style="invis") >> spacer
    tgw_e >> Edge(label="internet-bound", **NET) >> nat_e >> Edge(**NET) >> internet

    # Public subnets go straight to the internet; same-region S3 traffic skips the NAT
    pub_w >> Edge(**NET) >> igw_w >> Edge(label="public traffic", **NET) >> internet
    priv_w >> Edge(label="S3 traffic\n(same region)", style="dotted", **NET) >> s3e >> Edge(style="dotted", **NET) >> s3
