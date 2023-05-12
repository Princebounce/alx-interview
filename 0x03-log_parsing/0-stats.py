#!/usr/bin/env python3
import sys

# Initialize metrics variables
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for i, line in enumerate(sys.stdin, 1):
        # Parse the input line
        parts = line.split()
        if len(parts) != 7:
            continue
        ip_address, date, method, path, protocol, status_code, file_size = parts
        if method != "GET" or protocol != "HTTP/1.1":
            continue
        try:
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        # Update the metrics
        total_file_size += file_size
        status_codes[status_code] += 1

        # Print the metrics every 10 lines
        if i % 10 == 0:
            print(f"File size: {total_file_size}")
            for status_code, count in sorted(status_codes.items()):
                if count > 0:
                    print(f"{status_code}: {count}")

except KeyboardInterrupt:
    # Print the final metrics on CTRL-C
    print(f"File size: {total_file_size}")
    for status_code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{status_code}: {count}")

