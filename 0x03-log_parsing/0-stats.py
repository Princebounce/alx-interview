import sys

STATUS_CODES = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        # Split the line into components
        try:
            _, _, _, request, status, size = line.split()
        except ValueError:
            # Skip lines that don't match expected format
            continue

        if request != 'GET /projects/260 HTTP/1.1':
            continue

        # Update metrics
        status = str(status)
        if status in STATUS_CODES:
            STATUS_CODES[status] += 1
        total_size += int(size)
        line_count += 1

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print(f"File size: {total_size}")
            for code in sorted(STATUS_CODES):
                if STATUS_CODES[code] > 0:
                    print(f"{code}: {STATUS_CODES[code]}")

except KeyboardInterrupt:
    # Print final metrics on keyboard interrupt
    print(f"File size: {total_size}")
    for code in sorted(STATUS_CODES):
        if STATUS_CODES[code] > 0:
            print(f"{code}: {STATUS_CODES[code]}")

