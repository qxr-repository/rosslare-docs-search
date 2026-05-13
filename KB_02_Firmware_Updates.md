# How to Update Panel Firmware

**Last Updated:** April 30, 2026  
**Audience:** All Users  
**Products:** AxTraxNG, AxtraxPro, AC-Series Panels

## Overview

Firmware updates add new features, improve stability, and are **required** before a panel can connect to your network. This guide walks you through the firmware update process step-by-step.

---

## What Is Firmware?

Firmware is the software that runs on your access control panel. Think of it like the operating system on your computer—without it, the panel cannot function. Many newly shipped panels arrive without firmware pre-installed.

**Signs your panel needs firmware:**
- Panel shows "No firmware installed" in the software
- Firmware version displays as "0.0" or "None"
- Panel won't connect to the network despite correct cabling
- You receive a "Firmware update available" notification

---

## Prerequisites

Before starting:

- **Access to the control software** (AxTraxNG 27.7.1.20 or AxtraxPro 28.0.5.2+) installed on your computer
- **Physical access to the panel** and power supply
- **Ethernet cable** to connect the panel to your computer (direct connection recommended for first-time updates)
- **15-30 minutes** of uninterrupted time (do not interrupt the update process)
- **Backup power or UPS** (optional but recommended to prevent interruption if power is lost)

### Supported Panel Models

Firmware updates are available for the following access control panels:

- **AC-215 / AC-215IP** — 2-door controller
- **AC-225 / AC-225IP** — 2-4 door controller (Series A and B)
- **AC-425 / AC-425IP** — 4-8 door controller (Series B)
- **AC-825IP** — 4-8 door controller with up to 12 expansion modules

**Legacy Note:** If you have a Series A AC-225 or AC-425 manufactured before 2011, contact support before updating—your panel may require special handling.

---

## Update Process

### Step 1: Prepare Your Setup

**Best practice:** Connect the panel directly to your computer with an Ethernet cable instead of through a network switch. This avoids network interruptions during the update.

1. Locate your panel and the Ethernet cable
2. Unplug the Ethernet cable from your panel (if currently connected)
3. **Plug the Ethernet cable directly into your computer**
4. **Plug the other end directly into the panel's network port**
5. Verify the panel is powered on (look for LED indicator on the front)

---

### Step 2: Launch the Software

1. **Open your access control software** (AxTraxNG, AxtraxPro, etc.)
2. **Go to the main configuration screen** or "Device Management"
3. **Look for a "Search" or "Add Device" button** (exact name varies by software version)
4. Click to scan for available panels on your network

---

### Step 3: Locate and Select Your Panel

1. **Wait for the scan to complete** (typically 10-20 seconds)
2. **Your panel should appear in the list** with a status or model number
3. **Click to select your panel**
4. **Review the panel information:**
   - Model number
   - Current firmware version (may show as "0.0" or "Not installed")
   - Any available updates

---

### Step 4: Start the Firmware Update

1. **Right-click on the panel** in the AC Networks tree on the left side of the software
2. **Select "Firmware Update"** from the context menu
3. **A dialog will appear** asking "Are you sure you want to update the firmware of the panel?"
4. **Do NOT change any settings** in this dialog—the panel type and firmware file should be pre-selected
5. **Click "OK"** to start the firmware download to the panel

**If you see a warning:** "Some panels have incompatible firmware. Are you sure you want to add them?" — **Click "Yes"** to proceed anyway. This is normal when updating older firmware versions.

---

### Step 5: Monitor the Update Progress

**Important:** Do NOT disconnect power or unplug the Ethernet cable during this process.

1. **After clicking OK, the dialog closes and you return to the main window**
2. **Select the Network in the left panel** (under AC Networks)
3. **Look at the "Downloads" column** in the right panel—it will show progress like "452 / 472" (bytes downloaded)
4. **The download typically takes 3-5 minutes** depending on the firmware size
5. **Watch the "Status" column**—it should show "Download in progress" then change to complete
6. **Check the Events log at the bottom** for status messages like "Started Firmware update" and "Firmware update" events
7. **Wait until the status shows the download is finished**

**Successful update indicators:**
- Status changes from "Download in progress" to normal
- Events log shows "Firmware update" event with the panel name
- Downloads column stops incrementing
- Panel automatically restarts (you may see a brief connectivity interruption)

**If you see errors in the Events log:**
- **"Invalid Firmware"** — The firmware file may be corrupted or incompatible. Try the update again
- **"Connection Lost"** — Restart the panel and try again with a direct Ethernet connection
- **"Wrong value is ac225v05_00_14"** — Firmware version mismatch. Verify you're using the correct firmware for your panel model

---

### Step 6: Verify the Update

1. **Once the update completes**, the panel will show a new firmware version (not "0.0")
2. **Restart the panel** (unplug and plug back in)
3. **Reconnect to your network** (if you used a direct connection, now return the Ethernet cable to your network)
4. **Search for the panel again** in the software to confirm it appears on your network
5. **You should now be able to configure the panel normally**

---

## Troubleshooting Update Issues

### "Update Fails" or "Connection Lost"

**Cause:** The connection was interrupted (network disconnection, power loss, or software crash)

**Fix:**
1. Restart the panel (unplug for 30 seconds, then plug back in)
2. Try a direct Ethernet connection to your computer (not through a network switch)
3. Attempt the firmware update again
4. If it continues to fail, try on a different computer

### "Panel Disappears During Update"

**Cause:** The panel lost power or network connectivity mid-update

**Fix:**
1. Check that the power supply is firmly connected
2. Check that the Ethernet cable is fully inserted
3. Restart both the panel and your software
4. Try the update again with a direct Ethernet connection

### "Firmware Version Doesn't Change"

**Cause:** The update may not have completed fully

**Fix:**
1. Manually restart the panel (unplug, wait 30 seconds, plug back in)
2. Open the software and check the firmware version again
3. If still showing old version, attempt the update a second time

---

## After Your Update

### Next Steps

1. **Configure the panel** with your facility code, readers, doors, and cards
2. **Test all connected readers** to ensure they're responding
3. **Verify all doors unlock/lock properly**
4. **Schedule a follow-up firmware check** in 6 months to stay current with security patches

### Regular Updates

- **Check for firmware updates** every 6 months
- **New firmware versions** may include security improvements and bug fixes
- **Keep your documentation current** with the firmware version in use

---

## Prevention

- **Update firmware immediately** when you receive a new panel
- **Don't skip firmware updates** thinking the panel will work without it
- **Use quality power supplies** to prevent interruptions during updates
- **Back up your panel configuration** before major updates (some updates reset settings)
- **Update during low-usage hours** to minimize disruption if something goes wrong

---

## Still Having Issues?

If your firmware update isn't working:

- **Note the panel model number** and current firmware version
- **Document the exact error message** you received
- **Check your software version** (Help > About)
- **Try a direct Ethernet connection** instead of through your network
- **Contact support** with this information

---

## Related Articles

- [Panel Not Connecting to Network](KB_01_Panel_Connectivity_Issues.md)
- [Software Installation & Setup Guide](software-install.md)
- [Troubleshooting: Panel Communication Errors](advanced-troubleshooting.md)

---

## Revision History

| Date | Change |
|------|--------|
| Apr 30, 2026 | Initial publication based on 18 support tickets |
