# Panel Not Connecting to Network

**Last Updated:** May 1, 2026  
**Audience:** All Users  
**Products:** AxTraxNG, AxtraxPro, AC-Series Panels

## Overview

If your access control panel won't appear in the software's configuration, or you can't locate it on your network, this guide will help you diagnose and resolve the connection issue.

---

## Symptoms

You're experiencing one or more of the following:

- Panel doesn't appear when searching in the software configuration
- Panel worked before but disappeared from the network
- Panel shows in the software list but won't respond to commands
- Network connectivity indicator shows as offline or disconnected
- Software simply won't locate the panel on the network

---

## Common Causes

**Panel Needs a Restart**  
The panel has lost network synchronization and a simple power cycle restores connectivity. This is the most common fix.

**Fresh Installation or Replacement Panel**  
New or replacement panels sometimes need a restart or firmware update to establish network communication.

**Network Changed by IT**  
The network topology or IP addressing scheme was changed (common after IT infrastructure updates), and the panel hasn't reconnected yet.

**Panel Moved Physically**  
The panel was moved to a different location or subnet but the network configuration wasn't updated.

**Firmware Not Installed**  
New panels sometimes don't have firmware pre-installed and cannot communicate on the network until updated.

---

## Solutions

### Option 1: Power Cycle the Panel (Most Common Fix)

A simple restart resolves most connectivity issues.

**Steps:**

1. **Locate the power supply** connected to your panel
2. **Unplug the power cable** from the wall outlet or UPS
3. **Wait 30 seconds** (this ensures a full power drain)
4. **Plug the power back in** and wait for startup (typically 10-30 seconds)
5. **Check the LED status light** on the front of the panel (should be solid or slowly blinking green)
6. **Try to locate the panel again** in your software

**What to expect:** The panel will display a startup sequence. Once fully booted, the network connectivity should restore automatically.

---

### Option 2: Test Panel Communication & Update Firmware if Needed

If a power cycle didn't work, test whether the panel can communicate with your software.

**Steps:**

1. **In your access control software**, go to **Device Configuration** or **Panel Setup**
2. **Right-click on the panel** and select **Test** or **Verify Connection**
3. **If the test passes**, the firmware is fine—move to Option 3
4. **If the test fails**, the panel cannot communicate and likely needs a firmware update:
   - Connect the panel directly to your computer using an Ethernet cable (bypassing your network if possible)
   - Right-click the panel and select **Firmware Update**
   - Click **OK** and allow 3-5 minutes for the update to complete
   - Once complete, the panel should restart and reconnect to your network

**What to expect:** A successful test means the panel can communicate. If firmware update was needed, the panel may go offline briefly during the update, then automatically reconnect.

---

### Option 3: Verify Physical Connections & Basic Network Setup

Check the hardware and basic network configuration.

**Steps:**

1. **Verify the Ethernet cable is connected:**
   - Confirm the cable is fully inserted into both the panel's network port and your computer/switch
   - Look for a solid or blinking green light on the Ethernet port
   - Try a different Ethernet cable if one is available

2. **Check if your computer can see the panel's IP:**
   - In your software's Device Configuration, look for the panel's IP address
   - Try to ping that address from Command Prompt: type `ping [panel-ip-address]`
   - If ping works, the panel is reachable on your network

3. **For AC-825 panels**, check Windows Firewall settings:
   - Go to Control Panel > Windows Defender Firewall > Advanced Settings
   - Confirm that `AxtraxService.exe` has an inbound rule allowing connections
   - If no rule exists, create one: allow all connections for `AxtraxService.exe`

4. **If nothing above worked**, the panel may be on a different network than your computer:
   - This happens if the panel was moved to a different location or your IT department changed the network
   - Contact your IT department to verify both the panel and computer are on the same network segment
   - They may need to assign the panel a static IP address

---

### Option 4: Contact Your IT Department

If the above steps didn't work, this is likely a network issue that requires IT support.

**Information to provide to IT:**

- **Panel IP address** (from your software's Device Configuration)
- **Panel model number** (e.g., AC-215, AC-425, AC-825IP)
- **What changed recently** (IT infrastructure updates, network changes, panel physically moved, etc.)
- **Current status:** "My panel won't connect to the software"

**Common issues IT can resolve:**

- Panel is on a different network subnet than your computer
- Network firewall rules are blocking communication
- Panel needs a static IP address assignment
- Network topology has changed since the panel was installed

---

## Network Specifications (Reference)

For planning and troubleshooting purposes, here are the network specifications for Rosslare panels:

| Connection Type | Maximum Distance | Cable Type | Notes |
|---|---|---|---|
| **Ethernet (TCP/IP)** | 330 feet | Cat5e or Cat6 | Recommended for new installations |
| **RS-485** | 2,000 feet | 22 AWG 120 Ω STP | For older panel networks |

**System Scale:** AxTraxNG supports up to 1,024 panels across multiple networks (32 networks × 32 panels each).

---

## Prevention

- **Update firmware regularly:** New firmware includes network stability improvements and security patches
- **Use quality Ethernet cables:** Ensure cables are CAT5e or higher and fully inserted on both ends
- **Use static IP addresses:** Configure panels with static IPs to prevent conflicts and simplify troubleshooting
- **Maintain network documentation:** Keep a record of each panel's IP address, location, and hardware type
- **Use a backup power supply:** Connect panels to an uninterruptible power supply (UPS) to avoid sudden power loss during updates
- **Enable Windows Firewall:** AxTraxNG/Pro requires Windows Firewall to be enabled and properly configured
- **Test connectivity regularly:** Periodically verify all panels are reachable and responding
- **Restart routinely:** If issues recur periodically, schedule monthly restarts during maintenance windows

---

## Still Having Issues?

If none of these steps resolve your issue:

- **Note the panel model number** and IP address (if visible)
- **Check the firmware version** shown in the software
- **Document any error messages** displayed
- **Note when the issue started** and what changed (power outage, network changes, recent updates)
- **Contact support** with this information at [support contact info]

---

## Related Articles

- [How to Update Panel Firmware](KB_02_Firmware_Updates.md)
- [Troubleshooting: Panel Shows Offline in Software](advanced-troubleshooting.md)
- [Network Setup Guide for Access Control Panels](network-setup.md)
- [IP Address Configuration for AC-225 Panels](ac225-ip-setup.md)

---

## Revision History

| Date | Change |
|------|--------|
| May 1, 2026 | Subject matter expert review: Reordered solutions by effectiveness (power cycle first), simplified network troubleshooting steps, removed overly technical ARP/UDP verification, made Windows Firewall AC-825 specific, simplified firmware update to use panel test method |
| Apr 30, 2026 | Initial publication based on 64 support tickets |
