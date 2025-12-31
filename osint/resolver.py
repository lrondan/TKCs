import socket

def main(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        print(f"Domain {domain_name} resolved to IP: {ip_address}")
    except socket.gaierror:
        print(f"Could not resolve domain: {domain_name}")

    try:
        info = socket.getaddrinfo(domain_name, None, socket.AF_INET6)
        ipv6 = info[0][4][0]
        print(f"Domain {domain_name} has IPv6 address: {ipv6}")
    except socket.gaierror:
        print(f"No IPv6 address found for domain: {domain_name}")

if __name__ == "__main__":
    main()