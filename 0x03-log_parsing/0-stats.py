#!/usr/bin/python3
""" Script that reads stdin line by line and computes metrics """
import sys
import re
import signal

total_size = 0
status_counts = {}
line_count = 0
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

log_pattern = re.compile(
    r'^(\d{1,3}(\.\d{1,3}){3}) - \[[^\]]+\] '
    r'"GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)


def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys(), key=int):
        print("{}: {}".format(code, status_counts[code]))


def handle_interrupt(sig, frame):
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        match = log_pattern.match(line.strip())
        if match:
            code = match.group(3)
            size = int(match.group(4))
            total_size += size
            if code in valid_codes:
                status_counts[code] = status_counts.get(code, 0) + 1
            line_count += 1
            if line_count % 10 == 0:
                print_stats()
except Exception:
    pass
finally:
    print_stats()
