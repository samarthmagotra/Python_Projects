import pyshark

# Load the PCAP file
capture = pyshark.FileCapture('http_traffic.pcap')
print(capture)
print(type(capture))
for packet in capture:
    with open('pcap.txt', 'a+') as f:
        f.write(str(packet))


for packet in capture:
    if 'IP' in packet:
        print(f"Source IP: {packet.ip.src}, Destination IP: {packet.ip.dst}")
    if 'TCP' in packet:
        print(f"Source Port: {packet.tcp.srcport}, Destination Port: {packet.tcp.dstport}")

filtered_capture = pyshark.FileCapture('http_traffic.pcap', display_filter='http')
for packet in filtered_capture:
    with open('http.txt', 'a+') as f:
        f.write(str(packet))
    #print(packet.http.host)  # Access the host field in the HTTP layer

for packet in capture:
    print(f"Packet Length: {packet.length}, Timestamp: {packet.sniff_time}")
'''
filtered_capture = pyshark.FileCapture('http_traffic.pcap', display_filter='tcp')
filtered_capture.save_to_file('filtered_output.pcap')
'''