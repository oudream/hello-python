#!/usr/bin/python
#
#    File: icmp_scan.py
#
#    Description: A program that uses ICMPv4/v6 protocol to find and
#                 map which hosts are up in a network.
#

from optparse import OptionParser
import sys
import re

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

scan_types = ["ping","sweep","broadcast"]

def valid_scan_type(scan_type):
    """
    Check if it's a valid scan type.
    """
    if scan_type in scan_types:
        return True
    else:
        return False

def valid_ip_address(ip_address):
    """
    Check if it's a valid IP address.
    """
    ip_pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    pattern = re.compile(ip_pattern)

    if pattern.match(ip_address):
        return True
    else:
        return False


if __name__ == '__main__':

    scan_type = "ping"
    targets = []

    # Parse command line
    usage = "usage: %prog [options] list_of_targets"
    parser = OptionParser(usage=usage)
    parser.add_option("-s","--scan",dest="scan",help="type of ICMP scan")
    (options,args) = parser.parse_args()

    # Validate scan type
    if options.scan:
        if not valid_scan_type(options.scan):
            print("SCAN TYPE \"%s\" is not valid." % options.scan)
            parser.print_help()
            sys.exit(EXIT_FAILURE)
        else:
            scan_type = options.scan

    # Validate target(s)
    if not args:
        print("TARGET is missing.")
        parser.print_help()
        sys.exit(EXIT_FAILURE)
    else:
        for target in args:
            if not valid_ip_address(target):
                print("TARGET \"%s\" is not valid." % target)
                parser.print_help()
                sys.exit(EXIT_FAILURE)
            else:
                targets.append(target)

    # Do the scan
    import scan

    if scan_type == 'ping':
        s = scan.ping(scan_type, targets)
    elif scan_type == 'sweep':
        s = scan.sweep(scan_type, targets)
    else:
        s = scan.scan(scan_type, targets)

    s.send_icmp_packet()
    s.recv_icmp_packet()
    s.show_results()

    sys.exit(EXIT_SUCCESS)

##############################################################################
