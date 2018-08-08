#!/usr/bin/python
#
#    File: scan.py
#
#    Description: Scan methods
#


class scan():
    """
    Do the scan
    """

    def __init__(self, scan_type, targets):
        """
        Init for scan
        """
        self.scan_type = scan_type
        self.targets = targets

    def send_icmp_packet(self):
        """
        Send ICMP packet to the target
        """
        for target in self.targets:
            print(("\tSending ICMP packet to %s." % target))

    def recv_icmp_packet(self):
        """
        Receive ICMP packet from target
        """
        for target in self.targets:
            print(("\tReceiving ICMP packet from %s." % target))

    def show_results(self):
        """
        Show scan results
        """
        print("\n####################################\n")
        print(("Results for scan: %s." % self.scan_type))
        for target in self.targets:
            print(("\tTarget: %s." % target))
        print("\n####################################\n")


class ping(scan):
    """
    Do the PING scan
    """

    def send_icmp_packet(self):
        """
        Send ICMP request packet to the target
        """
        for target in self.targets:
            print(("\tSending ICMP request packet to %s." % target))

    def recv_icmp_packet(self):
        """
        Receive ICMP reply packet from target
        """
        for target in self.targets:
            print(("\tReceiving ICMP reply packet from %s." % target))


class sweep(scan):
    """
    Do the SWEEP scan
    """

    def send_icmp_packet(self):
        """
        Send ICMP sweep packet to the target
        """
        for target in self.targets:
            print(("\tSending ICMP sweep packet to %s." % target))

    def recv_icmp_packet(self):
        """
        Receive ICMP sweep packet from target
        """
        for target in self.targets:
            print(("\tReceiving ICMP sweep packet from %s." % target))
