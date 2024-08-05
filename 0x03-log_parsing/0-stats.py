#!/usr/bin/python3
import sys
import signal

def print_stats(total_size, status_counts):
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts):
        print(f"{status_code}: {status_counts[status_code]}")

def process_line(line, total_size, status_counts):
    parts = line.split()
    if len(parts) != 7:
        return total_size

    try:
        ip, dash, date, request, status_code, file_size = parts[0], parts[1], parts[2], parts[3] + ' ' + parts[4] + ' ' + parts[5], parts[6], parts[7]
        if not (date.startswith('[') and date.endswith(']') and request.startswith('"GET /projects/260 HTTP/1.1"')):
            return total_size
        file_size = int(file_size)
        total_size += file_size
        status_code = int(status_code)
        if status_code in status_counts:
            status_counts[status_code] += 1
        else:
            status_counts[status_code] = 1
    except (ValueError, IndexError):
        return total_size

    return total_size

def main():
    total_size = 0
    status_counts = {}
    line_count = 0

    def signal_handler(sig, frame):
        print_stats(total_size, status_counts)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    for line in sys.stdin:
        line_count += 1
        total_size = process_line(line.strip(), total_size, status_counts)

        if line_count % 10 == 0:
            print_stats(total_size, status_counts)

    print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()
