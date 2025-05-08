#!/usr/bin/python3
"""
Log parsing script
Reads stdin line by line and computes metrics
"""
import sys
import re
import signal

# Allowed status codes
STATUS_CODES = ['200', '301', '400', '401', '403', '404', '405', '500']
status_counts = {}
total_size = 0
line_count = 0

# Compile regex pattern for line validation
log_pattern = re.compile(
    r'^(\d+\.\d+\.\d+\.\d+)'
    r' - \[[^\]]+\]'
    r' "GET /projects/260 HTTP/1.1"'
    r' (\d{3})'
    r' (\d+)$'
)


def print_stats():
    """Print the current stats"""
    print("File size: {}".format(total_size))
    for code in sorted(STATUS_CODES):
        if code in status_counts:
            print("{}: {}".format(code, status_counts[code]))


def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)"""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)
        if match:
            status_code = match.group(2)
            file_size = int(match.group(3))
            total_size += file_size
            if status_code in STATUS_CODES:
                status_counts[status_code] = status_counts.get(
                    status_code, 0) + 1
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
except Exception:
    pass
finally:
    print_stats()
