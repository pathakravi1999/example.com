# update_hosts.py
import sys

def update_hosts_file(example):
    with open("/etc/hosts", "a") as f:
        f.write(f"\n127.0.0.1\t{example}\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python update_hosts.py <ravipathak.com>")
        sys.exit(1)

    example = sys.argv[1]
    update_hosts_file(example)
