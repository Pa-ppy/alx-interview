#!/usr/bin/python3
"""
Log parsing script
Reads stdin line by line and computes metrics
"""

import sys
import re
import signal

# Track total size and status code counts
total_size = 0
status_counts = {}
line_counter = 0

# Valid status codes
valid_status = ['200', '301', '400', '401', '403', '404', '405', '500']

# Compile strict log line format regex
log_pattern = re.compile(
    r'^(\d{1,3}(\.\d{1,3}){3}) - \[[^\]]+\] '
    r'"GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)


def print_stats():
    """Prints the accumulated stats"""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys(), key=int):
        print("{}: {}".format(code, status_counts[code]))


def handle_interrupt(sig, frame):
    """Print stats on keyboard interrupt (CTRL+C)"""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)
        if match:
            status_code = match.group(3)
            file_size = int(match.group(4))
            total_size += file_size
            if status_code in valid_status:
                if status_code not in status_counts:
                    status_counts[status_code] = 0
                status_counts[status_code] += 1
        line_counter += 1
        if line_counter % 10 == 0:
            print_stats()
except Exception:
    pass
finally:
    print_stats()
