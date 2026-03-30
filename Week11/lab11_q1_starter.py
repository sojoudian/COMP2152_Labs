import socket

class PortScanner:
    def __init__(self, target):
        self.target = target
        self.open_ports = []

    def scan_port(self, port):
        # Create the socket connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
        try:
            # connect_ex returns 0 if the port is open
            result = sock.connect_ex((self.target, port))
            if result == 0:
                print(f"  Port {port}: OPEN")
                self.open_ports.append(port)
                return True
            return False
        finally:
            # Always close the socket to be safe
            sock.close()

    def scan_range(self, start_port, end_port):
        print(f"  Scanning {self.target} ports {start_port}-{end_port}...")
        # Use +1 because range() is exclusive
        for port in range(start_port, end_port + 1):
            self.scan_port(port)

    def display_results(self):
        print(f"  Results for {self.target}:")
        if not self.open_ports:
            print("    No open ports found.")
        else:
            for port in self.open_ports:
                print(f"    Port {port}")
