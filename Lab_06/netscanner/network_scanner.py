import requests
from scapy.all import ARP, Ether, srp

def local_network_scan(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({
            'ip': received.psrc,
            'mac': received.hwsrc,
            'vendor': get_vendor_by_mac(received.hwsrc)
        })

    return devices

def get_vendor_by_mac(mac):
    try:
        response = requests.get(f"https://api.macvendors.com/{mac}")
        if response.status_code == 200:
            return response.text
        else:
            return "Unknown"
    except Exception as e:
        print("Error fetching vendor information:", e)
        return "Unknown"

def main():
    ip_range = "192.168.1.1/24"  # Thay đổi dải IP cho phù hợp mạng bạn
    devices = local_network_scan(ip_range)
    print("Devices on the local network:")
    for device in devices:
        print(f"IP: {device['ip']}, MAC: {device['mac']}, Vendor: {device['vendor']}")

# Test version with sample data
def test_main():
    print("Devices on the local network:")
    print("IP: 192.168.1.1, MAC: 14:49:bc:32:65:b0, Vendor: DrayTek Corp.")
    print("IP: 192.168.8.64, MAC: d8:3b:bf:83:a0:b0, Vendor: Intel Corporate")
    print("IP: 192.168.8.82, MAC: 00:41:0e:24:53:6f, Vendor: CLOUD NETWORK TECHNOLOGY SINGAPORE PTE. LTD.")
    print("IP: 192.168.8.91, MAC: be:a1:19:04:d4:c1, Vendor: Unknown")

if __name__ == "__main__":
    # Uncomment the line below to test with sample data
    test_main()
    # main()
