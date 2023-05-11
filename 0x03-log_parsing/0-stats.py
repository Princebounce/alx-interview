#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''import sys
from collections import defaultdict

# Initialize metrics
total_size = 0
status_codes = defaultdict(int)
line_count = 0

try:
    # Read input from stdin line by line
    for line in sys.stdin:
        # Split the line into components
        try:
            ip, _, date, request, status, size = line.split()
            if request != 'GET /projects/260 HTTP/1.1':
                continue
            size = int(size)
            status = int(status)
        except ValueError:
            # Skip lines that don't match expected format
            continue

        # Update metrics
        total_size += size
        status_codes[status] += 1
        line_count += 1

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print(f"Total file size: {total_size}")
            for code in sorted(status_codes.keys()):
                print(f"{code}: {status_codes[code]}")

except KeyboardInterrupt:
    # Print final metrics on keyboard interrupt
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

