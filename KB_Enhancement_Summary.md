# KB Article Enhancement Summary

**Date:** April 30, 2026  
**Status:** Complete — All 3 articles enhanced with official documentation references

---

## Enhancement Overview

The three KB articles were verified and enhanced using official Rosslare documentation from your workspace:

1. ✅ **KB_01_Panel_Connectivity_Issues.md**
2. ✅ **KB_02_Firmware_Updates.md**
3. ✅ **KB_03_Card_Credential_Management.md**

---

## Documentation Sources Used

### AxtraxNG_Site_Reference.md
- Panel models and specifications (AC-215/225/425/825IP)
- Network requirements (Ethernet vs RS-485 distances)
- Software version details (AxtraxNG 27.7.1.20 final, AxtraxPro 28.0.5.2 current)
- Firewall configuration requirements
- System scale capabilities (up to 1,024 panels across 32 networks)
- Card capacity by panel model

### firmware.pdf
- Exact UI steps for firmware updates in AxtraxNG
- Screenshot confirmation of the "incompatible firmware" warning dialog
- Firmware update dialog details and settings
- Progress monitoring via Downloads column and Events log
- Status indicators (Download in progress, completion)
- Error message interpretation

### AxtraxNG Installation & Support Bulletins
- Network configuration best practices
- Windows Firewall configuration procedures
- IP address management
- Remote client connectivity requirements

---

## Specific Enhancements

### Article 1: Panel Connectivity & Network Issues

**Added Technical Specifications:**
- Network cable distance limits (330 ft Ethernet, 2,000 ft RS-485)
- Cable type specifications (Cat5e/Cat6 for Ethernet, 22 AWG 120Ω STP for RS-485)
- System scale reference (up to 1,024 panels supported)

**Enhanced Troubleshooting:**
- Specific Windows Firewall configuration steps
- ARP/UDP broadcast requirements
- Static IP address recommendation
- Remote vs. local network connectivity clarification

**Improved Prevention:**
- Windows Firewall enablement requirement
- Static IP configuration emphasis
- Regular connectivity testing guidance

---

### Article 2: Firmware Updates & Installation

**Added Panel Model Reference:**
- Supported models with capacity details:
  - AC-215 / AC-215IP (2-door)
  - AC-225 / AC-225IP (2-4 door, Series A/B)
  - AC-425 / AC-425IP (4-8 door, Series B)
  - AC-825IP (4-8 door with expansion)
- Legacy Series A hardware note

**Enhanced Step-by-Step Process:**
- Exact software menu path: Right-click panel > Firmware Update
- Official dialog handling: "Do NOT change any settings"
- Warning message clarification: Click "Yes" for incompatible firmware
- Progress monitoring via "Downloads" column (e.g., "452 / 472")
- Events log review for status updates

**Improved Error Handling:**
- Error message examples directly from official documentation
- "Invalid Firmware" interpretation
- "Wrong value" firmware version mismatch explanation

**Added Software Version Reference:**
- AxTraxNG 27.7.1.20 (final release)
- AxtraxPro 28.0.5.2+ (current recommended)

---

### Article 3: Card & Credential Management

**Added Panel Capacity Reference:**
- AC-215/225 max: 30,000 users, 20,000 events
- AC-425 max: 30,000 users, 20,000 events
- AC-825IP max: 60,000 users, 500,000 events

**Enhanced Facility Code Section:**
- Added card format technical detail (26-bit standard vs. no-FC format)
- Clarified facility code is a system identifier (0-255 range)
- Expanded troubleshooting for capacity limits
- Added data archiving guidance for high-volume systems

**Improved Biometric Reader Guidance:**
- Technical explanation of facility code + card ID binding
- Configuration mode vs. demo mode distinction
- Reader reconfiguration procedures

---

## Verification Checklist

| Item | Status | Notes |
|---|---|---|
| **Panel models listed** | ✅ Verified | AC-215/225/425/825 confirmed in official docs |
| **Network specifications** | ✅ Verified | 330ft Ethernet, 2,000ft RS-485 from reference |
| **Firmware steps** | ✅ Verified | Matches firmware.pdf UI screenshots |
| **Software versions** | ✅ Verified | AxtraxNG 27.7.1.20 & AxtraxPro 28.0.5.2 |
| **Firewall config** | ✅ Verified | Windows Firewall required, AxtraxService.exe rules |
| **Card capacity** | ✅ Verified | Per-model capacities from reference docs |
| **Facility code format** | ✅ Verified | 26-bit standard, optional no-FC variant |

---

## Alignment with Ticket Data

These articles address the top issues from your 287-ticket analysis:

- **Panel Connectivity** (64 tickets) → Article 1 with expanded network troubleshooting
- **Firmware Updates** (18 tickets) → Article 2 with exact UI steps and error handling
- **Card Management** (22 tickets) → Article 3 with capacity planning and facility code guidance

---

## Notes for Implementation

1. **AxtraxNG End-of-Life:** Per official docs, AxtraxNG downloads end 12/31/2026, support ends 12/31/2027. Consider noting this for customers on older versions.

2. **AxtraxPro Migration:** Customers on AxtraxNG may need migration support. AC-825IP panels require MCU type VG for AxtraxPro compatibility.

3. **Windows Requirements:** Both AxtraxNG and AxtraxPro require Windows Firewall enabled. McAfee and Symantec antivirus are not supported.

4. **Firewall Configuration:** The manual `firewall.cmd` script in the installer directory can auto-configure firewall rules—mention this to users having connectivity issues.

---

## Next Steps (Optional)

Consider creating additional KB articles for:
- Reader configuration and troubleshooting (21 tickets in analysis)
- Software installation and migration (17 tickets)
- Schedule/timezone configuration (7 tickets)
- Advanced network configuration (for RS-485 systems)
- Database backup and recovery procedures

---

## Files Updated

- `KB_01_Panel_Connectivity_Issues.md` (6.0 KB → 7.2 KB)
- `KB_02_Firmware_Updates.md` (7.0 KB → 8.4 KB)
- `KB_03_Card_Credential_Management.md` (9.7 KB → 11.5 KB)

All articles now include official documentation references and verified technical specifications.
