# AxtraxNG.com — Site Reference Notes (Expanded)

Source: https://axtraxng.com (Rosslare Security North American Technical Support portal)
Captured: 2026-04-21

---

## 1. Key Notices

- **AxtraxNG End of Life: 12/31/2026** — software will not be available for download after this date.
- **AxtraxNG Support ends 12/31/2027.**
- Rosslare recommends using **AxtraxPro** for all new systems starting immediately.
- Technical support registration is now **REQUIRED** via the Zoho form on the landing page.

---

## 2. Software — Current Releases

### AxtraxNG (legacy, not recommended for new installs)

- Current / final version: **AxtraxNG 27.7.1.20** (release notes dated 2023-09-28, author Avi Eliav).
- Installer: `/support/AXTRAXNG/AxtraxNG_27_7_1_20.zip` (~655 MB, dated 2025-07-01).
- Documentation root: `/support/AXTRAXNG/documentation/`.
- Available patches (under `/support/AXTRAXNG/Patches/`):
  - AC-825 Access Denied patch 20
  - Access Denied patch (general)
  - AxtraxService 27_7_1_9 update
  - Keypad patch 27_7_1_19
  - Patch_Files_27_5_7_16
  - Patched_Client_19_photo
  - v27.7.1.18 patch

**Panel compatibility:** AC-825IP and AC-215/225/425 (Series A and Series B). AC-215U must be manufactured after 01/01/2011.

**Supported OS:** Windows 8.1, 10, 11; Windows Server 2012–2019; 32 or 64-bit. Windows XP and Windows 7 are NOT supported.

**SQL Server:** 2012 through 2019. Does NOT support SQL Server 2005.

**Minimum hardware:** Intel Core i5 dual-core 2.5 GHz, 8 GB RAM, 5 GB free storage.

### AxtraxPro (current / recommended)

- Current version: **AxtraxPro 28.0.5.2** (release notes 2024-04-27; 28.0.5.0 dated 2024-12-26; datasheet 2024-12-23).
- Installer: `/support/AXTRAXPRO/AxtraxPro_28_0_5_2.zip` (~680 MB, dated 2025-04-29).
- Documentation root: `/support/AXTRAXPRO/Documentation/`.
- Mobile app package available: `AxtraxPro_Mobile.zip`.

**Panel compatibility:** AC-825IP (MCU **must be type VG**) and AC-215/225/425 Series A/B.

**Supported OS:** Windows 10 or 11 64-bit; Windows Server 2016 or later.

**SQL Server:** 2019 only. Does NOT support SQL Server 2012.

**Minimum hardware:** Intel Core i5 dual-core 2.5 GHz, 8 GB RAM, 5 GB free storage.

**Upgrade path:** Existing AxtraxNG server must already be running 27.7.1.18 or later. Verify AC-825IP MCU type VG in Panel Properties from NG 27.7.1.18+ before attempting the upgrade.

---

## 3. Licensing

### AxtraxNG Licensing
- Licenses apply to video integration (AX-HIK / AX-DAU) and reader ports.
- No license required for systems with fewer than **256 reader ports**.
- Ordering a key requires the **HWID** of the server PC (obtain via `Rosslare_AxtraxNG_HWID_Utility.zip`; procedure in "AxtraxNG HWID.pdf").
- Activation bulletin: "How To Activate AxTraxNG License.pdf".

### AxtraxPro Licensing
- Licenses apply to video integration, web clients, and reader ports.
- No license required for systems with fewer than **6 reader ports**.
- Separate `Rosslare_AxTraxPRO_HWID_Utility.zip` generates Pro HWID (procedure in "AxtraxPro HWID.pdf").
- Pricing-model PDFs on site: `AxTraxPro_Licenses.pdf` and `AxTraxPro_Licensing_Packages.pdf` (under `/support/axtraxpro/documentation/Pricing model/`).

### Video Integration License Order Models (AxtraxNG)
From `/support/axtraxng/documentation/AxtraxNG Video Integration.txt`:

**Hikvision NVR (AX-HIK-Lx)** — L1: 2 cameras/1 NVR · L2: 4 cameras/2 DVRs · L3: 9 cameras/4 DVRs · L4: 16 cameras/8 DVRs · L5: unlimited cameras/12 DVRs.

**Dahua NVR (AX-DAH-Lx)** — L1: 2 cameras/1 DVR · L2: 4 cameras · L3: 9 cameras/4 DVRs · L4: 16 cameras/8 DVRs · L5: unlimited cameras/12 DVRs.

**Supported SDK versions:** Hikvision 5.3.2.15; Dahua 3.4.8.27787.

---

## 4. Installation Notes (AxtraxNG 27.7.1.2X)

Derived from `Installing_AxtraxNG_27_7_1_2X.pdf`:

**Prerequisites**
- Windows 7 SP1, 8.1, or 10 (32 or 64-bit) per the installer doc. (Landing-page copy states 8.1/10/11 — the installer PDF is older and also lists Win 7 SP1; treat 10/11 as current.)
- .NET Framework 4.5+.
- SQL Server 2012 or later (SQL Server Express 2019 bundled for new installs).
- Static IP addresses on the AxtraxNG server and any AC-825 panels.
- Broadcast (ARP) and UDP must be allowed between server and panels on the same subnet.

**Antivirus / firewall**
- Quoted verbatim: *"Microsoft Windows Defender is the ONLY antivirus software we have tested with and will support."*
- McAfee and Symantec are "not supported and not recommended."
- Windows Firewall is required; Rosslare "does not recommend disabling the firewall."

**Install sequence**
1. Extract the installer ZIP.
2. Right-click `AxtraxNGSetup.EXE` and run **as Administrator** (mandatory).
3. Select "Server with Server Monitor and Client" (Client-only option exists for remote workstations).
4. Accept defaults through Client → SQL Server → Server → Server Monitor sub-installers.
5. Do NOT select AxTime, Vitrax, or Vitrax LPR (deprecated).
6. No reboot required.
7. Post-install: apply the firewall rule (below).

**Upgrade rules**
- 27.x over 27.x or later (SQL 2012+ present): allowed; database upgrades automatically.
- Older than 27.x or coming from AxtraxAS525: **contact Technical Support first**; SQL 2005 instances cannot be reused.
- 27.7.1.20 over 24.x with SQL2012+: skip the bundled SQL 2019 install.

**Pre-upgrade backup (critical)**
1. In the AxtraxNG client: Tools → Database → "Backup Now".
2. In Task Manager, stop both `Server Monitor Process` and `AxtraxServerService` before running the installer — otherwise the service and monitor will not be upgraded.
3. After upgrade, open the client and push firmware to all panels (panels may flag "incompatible firmware" — click Yes to add, then update firmware).

**Remote client**
- Supported. Initial panel discovery must happen on the same physical LAN/subnet; remote management via VPN/WAN works thereafter.

---

## 5. Firewall Configuration

From `/support/axtraxng/documentation/firewall_rule.txt`:

After install, right-click `firewall.cmd` (in the extracted installer directory, e.g. `Downloads\AxtraxNG_27_7_x.x`) and **Run as administrator**. If that fails or a remote client / AC-825 can't initialize, create the inbound rule manually:

1. Control Panel → Windows Defender Firewall → Advanced Settings.
2. Inbound Rules → New Rule → Program.
3. Program path: `C:\Program Files (x86)\Rosslare\AxtraxNG Server\AxtraxService.exe` (64-bit OS) or `C:\Program Files\Rosslare\AxtraxNG Server\AxtraxService.exe` (32-bit OS).
4. Action: Allow the Connection. Keep all profiles selected.
5. Name: `axtraxng`.

A separate `AxtraxPro_firewall.zip` exists under `/support/AXTRAXPRO/` for Pro.

---

## 6. Panel Hardware Reference (from panels-B.html)

### AC-215IP-BU
2 doors, 2 reader ports, 2 REX inputs, 2 AUX/door inputs, 2 AUX outputs; no on-board expansion. RS-485/TCP-IP. 30 000 users, 20 000 events on board. 128 timezones. Power 90–265 VAC. Reader supply 300 mA @ 12 VDC. Lock supply 2.0 A @ 13.8 VDC. 12 V / 7 Ah battery support (~3 hr standby). 14.4" × 10.4" × 3.8", 8.4 lbs. Operating temp 32–120 °F.

### AC-225(IP)-BU
2/4 doors, 2/4 reader ports, 2/4 REX inputs, 2/4 AUX/door inputs, 2/4 AUX outputs. Expansion: one MD-D02B. RS-485 (plus TCP/IP on IP model). Capacity, power, enclosure same as AC-215 family.

### AC-425(IP)-BU
4/8 doors, 4/8 reader ports, 4/8 REX inputs. Expansion: one MD-D04B. RS-485 (plus TCP/IP on IP model). Note: in 1-reader-per-door mode there are no door-monitor/AUX inputs or outputs available; in 2-reader-per-door mode REX inputs 2 and 4 can be used as door-monitor or AUX inputs.

### AC-825(IP)
4/8 doors (standard/expanded), 4/8 reader ports, 4/8 REX inputs, 6/10 AUX/door inputs, 2 AUX outputs. 60 000 users, **500 000 events** stored on board. 256 timezones. TCP/IP only. Power 100–240 VAC @ 1.6 A. Reader supply 500 mA, lock supply **2.5 A @ 13.8 VDC** (requires jumper from PSU board to relays). 12 V / 7 Ah battery. 13.6" × 15.9" × 4.0", 10.1 lbs. Operating temp 23–122 °F.

Expansion for AC-825 is OSDP-attached and includes up to **12 expansion modules**:
- **D-805** — adds 4 doors/readers.
- **R-805** — adds 16 Form-C relay outputs.
- **S-805** — adds 16 supervised inputs.
- **P-805** — adds 8 Form-C outputs + 16 supervised inputs.

Two OSDP readers can be added to the base board to bring the standard 4-reader capacity up to 6 without an expansion.

**Legacy note:** Series A panels (AC-215F, AC-225, AC-425 Rev A) are discontinued. Use Rev B; contact Tech Support for interoperability, software update may be required.

**RS-485 / Ethernet runs:** RS-485 up to 2 000 ft on 22-ga 120 Ω STP; Ethernet 330 ft on Cat5e/Cat6. AxtraxNG supports 32 networks × up to 32 panels = **1 023 panels max**.

---

## 7. Expansion Modules (Series B) Compatibility

| Module | Compatibility | Function |
|---|---|---|
| MD-D02B | AC-225-BU | 2-door expansion |
| MD-D04B | AC-425-BU | 4-door expansion |
| MD-IO84B | AC-225-BU & AC-425-BU | 0 doors, 4 inputs, 4 relays |
| D/R/S/P-805 | AC-825IP | See §6 |

---

## 8. AxtraxPro-Only Content on the Site

Brochures: `AxTraxPro-brochure-upd-V010.pdf`, plus subfolders for AxtraxPro Development Tools, Milestone XProtect VMS integration, and Hikvision MinMoe biometric terminals.

Technical notes and integration guides (under `/support/axtraxpro/documentation/Technical notes and guides/`):
- `AxTraxPro+IDEMIA+Biometric+On+Card+Integration+Guide+V2024_04_01.pdf`
- `AxTraxPro+KONE+Elevator+Control+Integration+Guide+V2024_02_06.pdf`
- `Hikvision+MinMoe+Setup+Guide+V2023_09_28.pdf`
- Desktop-client, Web-client, and Milestone / Hikvision MinMoe integration sub-folders.
- `Technical Note Rolling Back from AxTraxPro to AxTraxNG V2022_03_20.pdf`
- `Technical Note Rosslare OSDP Support Commands V2022_04_06.pdf`
- `Upgrade Guide from AxTraxNG to AxTraxPro V2022_03_20.pdf`

NDAA compliance PDF (`NDAA Compliance and AxTraxPro Integration.pdf`, dated 2025-08-29) is posted under both `/support/axtraxng/documentation/` and `/support/AXTRAXPRO/Documentation/`.

---

## 9. Training & Installation Guides (from training.html)

PDF guides:
- Hardware Installation Guide (`installation_hardware.pdf`)
- AxtraxNG Installation Guide (`installing_axtraxNG_27_7_1_2X.pdf`)
- Creating Networks & Finding Panels (`installing_create_networks.pdf`)
- Creating ACLinks / Automations (`installing_ACLinks.pdf`)
- Managing Users and Access Groups (`installing_manage_users.pdf`)
- Managing Databases incl. Upgrades (`installing_backup-restore.pdf`)
- Setup Antipassback and Parking (`installing_antipassback-parking.pdf`)
- Installing Remote Client (`installing_remote_client_27.pdf`)
- Moving AxtraxNG (`move_axtraxng.pdf`)
- Firmware Update (`firmware.pdf`)
- Replace AC-825IP SD Card (`AC-825_SD_Card_replacement.pdf`)
- AC-825IP Wiring (`AC_825_wiring.pdf`)

YouTube video guides: AxtraxNG Overview, Wiring an AC Panel, Adding Users/Credentials, Troubleshooting Connection Issues, Backups, Setting Up Automatic Door Unlock, Card Design, Car Park, Elevator Control, Standalone Controller Wiring, Standalone Controller Programming.

---

## 10. Manuals (manuals.html)

Panels: AC-215, AC-215x-B, AC-215IP, AC-225x-B, AC-225x Rev A, AC-425x-B, AC-825IP, AC-115 (hardware & software), AC-Q4x, AC-F/G 43/44.

Standalone: AYC-F/G/M 60, AYC-Q60, AYC-F/G 54/64, AYC-Q 54/64, AYC-x6355, AY-x6255, AY-H6355BT, AY-x12C, AY-x20.

Readers: MD-N32, MD-N33, LK-M03, LK-M06L, LK-M12L, EX-06/16, EX-07/17, PS-C25T, MD-W11.

Quick Guide: `Standalone_Quick_Guide.pdf`.

Browse all: `/support/Manuals/`.

---

## 11. Tech Support Bulletins (`/support/tech_support/Tech_Support_Bulletins/`)

Key bulletins available:
- AxTraxNG client fails to capture user image using webcam
- AxtraxNG HWID (2025-01-20)
- axtraxng_date_2016
- AxtraxNG HIDPI display
- AxtraxPro HWID (2025-01-20)
- How To Activate AxTraxNG License
- **How to set up Email Notification on AxTraxNG**
- Tech Note AC-825IP bootloader v2.0 support for AxTraxNG 27.5.7.16
- Tech Note AxTraxNG Server Licensing Update (2016 original)
- tech_note reset pw
- Technical Bulletin — AxTraxNG to NVR Integration V1.3 (Jan 2019)
- Technical Note AxTraxNG Log File Size
- Technical Note AxTraxNG Setting Network Adapter Priority
- Technical Note BLE Readers Password (2019-06-24)
- Technical Note Firmware update procedure for X-805 expansion units (2020-12-10)
- Technical Note FW Update with RS-485 (2022-03-23)
- Technical Note MD-N32 v1.2.4 lost communication (2019-06-11)

---

## 12. Other Support Files (`/support/tech_support/`)

- `AC-825 SD card replacement.pdf`
- `AY-K35_V3_FW.zip` — AY-K35 V3 firmware
- `AY-X12C wiring.PNG`
- `CSN vs O2S.pdf` — card-number format comparison
- `D-805.pdf`
- `Dipswith Settings.pdf`
- `Install_SQL_2005.pdf`, `Install_SQL_2012.pdf`
- `No_FC_26bit_card_format.pdf` — no-facility-code 26-bit card format
- `Programing a Stand Alone Reader.pdf`
- `QueryExPlus.zip` — SQL query utility
- `RSP_2014_Access_Control_Catalog_Credentials_Appendix.pdf`
- `Single-Product-Warranty2-May2019.pdf`
- `SQL/` folder and `SQL2019.zip` (~267 MB full SQL 2019 installer)
- `Start Services.pdf`
- `toggle main relay(standalone).txt`
- `vcredist_x86.zip`
- `Wiring Diagram.pdf`

Top-level `/support/` also exposes product-specific folders: `AC-825IP`, `AS-B01`, `AS-IP01`, `AY-U920BT`, `CPR-27`, `CSN_Select`, `Digitool`, `MD-14U`, `MD-N32`, `Network_Config_Tool`, `Utilities`, plus `Product_Warranty.pdf`.

---

## 13. Sunset / Migration Strategy Summary

AxtraxNG is Rosslare's legacy on-prem access-control platform, now in formal sunset. 27.7.1.20 is the last release, downloads stop 12/31/2026, and support ends 12/31/2027. Rosslare is pushing customers to AxtraxPro 28.x, which shares the same panel families (AC-825IP, AC-215/225/425) but requires Windows 10/11 64-bit, SQL Server 2019, and — for AC-825IP — an MCU revision type VG. Licensing thresholds dropped dramatically: Pro requires a license above 6 reader ports versus 256 on NG, so almost every production deployment needs a license post-migration. Both products use HWID-bound licensing tied to the server PC.

Standard migration workflow: verify NG is at 27.7.1.18+, confirm each AC-825IP reports MCU type VG in Panel Properties, back up the NG database, stop NG services, run the AxtraxPro installer, migrate the DB, re-issue licenses against the new HWID, and update panel firmware. A rollback procedure exists ("Technical Note Rolling Back from AxTraxPro to AxTraxNG V2022_03_20").

---

## 14. Contact Information (North American Tech Support)

- Tech Support email: support.na@rosslaresecurity.com
- Sales email: sales.na@rosslaresecurity.com
- Phone: 866-632-1101
- TeamViewer QuickSupport download link is on the landing page.
- Knowledge base: https://support.rosslaresecurity.com/
- YouTube: https://www.youtube.com/channel/UCUdUvwv9mUkVvuxwaP280dQ
- Tech Support Registration (required): Zoho form linked from the landing page.
- Mailing / shipping (new address):
  - Synerion USA
  - 1600 Hart St, Suite 103
  - Southlake, TX 76092
