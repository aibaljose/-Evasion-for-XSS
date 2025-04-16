# XSS WAF Evasion Script

This tool generates multiple variants of obfuscated XSS payloads designed to evade character-based filters typically used in Web Application Firewalls (WAFs).

## 🎯 Purpose

To test and demonstrate how XSS payloads can bypass WAF filters by encoding or modifying attack vectors.

## ⚙️ How It Works

- HTML Entity Encoding: `&#60;script&#62;`
- Hex Encoding: `\x3c\x73\x63\x72...`
- Unicode Encoding: `\u003c\u0073\u0063...`
- Random Casing: `<ScRiPt>`
- Event-based payloads: `<img src=x onerror=alert(1)>`

## ✅ Tested On

- DVWA with Medium Security + ModSecurity WAF
- bWAPP hosted on local Apache

## 📂 Output

The script prints all generated payloads to the console. Copy and paste into your target app input fields.

## 🧪 Observations

Some payloads bypass simple filters that only check for `<script>` or disallow `<` and `>`. Entity and hex encoding performed best.

## 🔐 Disclaimer

This project is for **educational purposes only**. Always have permission before testing any application.
