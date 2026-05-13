# How to Add, Manage, and Troubleshoot Access Cards and Credentials

**Last Updated:** April 30, 2026  
**Audience:** All Users  
**Products:** AxTraxNG, AxtraxPro, AC-Series Panels

## Overview

This guide covers how to add new access cards to your system, manage credentials, and resolve common issues like cards not working or readers rejecting valid cards.

---

## What Are Cards and Credentials?

**Card:** A physical credential (badge, key fob, card, or tag) that users swipe or tap on a reader to grant access.

**Credential:** The digital record in your software that associates a card ID with a user and their access permissions (which doors they can open, what times, etc.).

**Reader:** The device mounted near a door that reads the card and communicates with the panel.

---

## Part 1: Adding a New Access Card

### Step 1: Prepare the Card Information

Before you add a card, gather:

- **Card ID number** (often printed on the back of the card or key fob)
- **User name** (who the card belongs to)
- **Card type** (standard access card, biometric card, proximity card, etc.)
- **Facility code** (optional — identifies which facility this card is for, if using multiple locations)
- **Access permissions** (which doors they can open, time restrictions, etc.)

**How to find the card ID:**
- Many cards have the ID printed on the back (a long number)
- If not visible, you can "program" the card by tapping it on a reader in programming mode
- Check your card supplier documentation for the ID format

---

### Step 2: Add the Card to the Software

1. **Open your access control software** (AxTraxNG, AxtraxPro, etc.)
2. **Navigate to "Users," "Cards," or "Credentials"** (varies by software version)
3. **Click "Add New Card" or the "+" button**
4. **Fill in the card information:**
   - Card ID (the number on the card)
   - User name
   - Facility code (if required)
   - Start and end dates (when the card is active)
   - Access level or group (which doors they can open)
5. **Click "Save" or "Add Card"**
6. **The software will display a confirmation** message

---

### Step 3: Sync with Panel

For the card to work, the panel must receive the new credential.

1. **Select the panel** from the device list in your software
2. **Click "Upload Configuration," "Sync," or "Send to Panel"**
3. **Wait for the sync to complete** (typically 10-30 seconds)
4. **You should see a "Sync Complete" or "Success" message**

---

### Step 4: Test the Card

1. **Go to the reader** that corresponds to the door you gave access to
2. **Swipe or tap the new card** on the reader
3. **The reader should beep or light up** (behavior varies by reader type)
4. **The door should unlock** (if it's the right time and the credential is active)
5. **If it doesn't work, go to Part 3: Troubleshooting**

---

## Part 2: Managing Existing Cards

### Disabling a Card (Without Deleting)

If an employee leaves but you want to keep their record:

1. **Go to Users > Cards** or **Credentials**
2. **Find the card in the list**
3. **Click to edit it**
4. **Change the "Status" to "Inactive" or "Disabled"**
5. **Set the "End Date" to today** (optional but recommended)
6. **Click "Save"**
7. **Sync the change to the panel** (Upload Configuration)

The card will no longer grant access, but the record remains in your system.

### Reassigning a Card to a New User

1. **Go to Users > Cards** or **Credentials**
2. **Find the card**
3. **Click to edit it**
4. **Change the "User Name" to the new person**
5. **Update access permissions** if needed
6. **Click "Save"**
7. **Sync to the panel**

The card is now assigned to the new user.

### Updating Card Access Permissions

1. **Go to Users > Cards**
2. **Find the card**
3. **Edit the "Access Group" or "Doors"** field
4. **Select which doors they should have access to**
5. **Set time restrictions if needed** (e.g., "Only weekdays 8am-6pm")
6. **Click "Save"**
7. **Sync to the panel**

---

## Part 3: Troubleshooting Card Issues

### Issue: Card Won't Work After Adding It

**Symptoms:** Card was just added but doesn't grant access. Reader beeps but door doesn't unlock.

**Cause:** The configuration wasn't synced to the panel, or the card was added but not activated.

**Fix:**
1. **Check the card status in software** — it should show as "Active"
2. **Verify the card end date** hasn't already passed
3. **Sync the configuration to the panel again** (Upload Configuration / Sync)
4. **Wait 30 seconds** for the sync to reach the readers
5. **Try the card again**

---

### Issue: New Codes Are Not Working

**Symptoms:** After adding new access codes in the software, the panel doesn't recognize them.

**Cause:** The panel firmware may need updating, or the synchronization failed.

**Fix:**
1. **Verify the panel firmware is current** (if showing version 0.0 or very old, update it first)
2. **Check that the panel is connected to the network** (see [Panel Connectivity](KB_01_Panel_Connectivity_Issues.md))
3. **Manually resync the configuration:**
   - Select the panel
   - Click "Upload Configuration" or "Sync"
   - Wait for completion
4. **If sync fails**, check the error message:
   - **"Panel Unreachable"** — Panel lost network connection (restart it)
   - **"Database Error"** — Try syncing again, or restart your software
5. **Try the card again after successful sync**

---

### Issue: Biometric Reader Sends Same ID for All Cards

**Symptoms:** No matter what card is swiped on a biometric reader, it sends the same facility code and card ID (usually "0" and "9999").

**Cause:** The biometric reader is not configured properly or lost its configuration.

**Fix:**
1. **Check the reader settings in your software:**
   - Go to Devices > Readers (or similar)
   - Find the biometric reader
   - Verify it's set to "Biometric mode" or "Card read mode" (not demo mode)
2. **If the setting shows wrong, update it:**
   - Change the mode to the correct setting
   - Click "Save" or "Apply"
   - Sync to the panel
3. **If still showing wrong IDs**, the reader may have lost its configuration:
   - Power cycle the reader (unplug for 30 seconds, plug back in)
   - Try swiping the card again
4. **If issue persists**, contact your reader's manufacturer or support team

---

### Issue: Cards Don't Stick on User Account

**Symptoms:** You add a card to a user, but when you open the user record later, the card is gone or shows as "unassigned."

**Cause:** This usually occurs if:
- The save didn't complete properly
- There's a database connection issue
- The user has too many cards assigned (some systems have limits)

**Fix:**
1. **Try adding the card again:**
   - Open the user record
   - Click "Add Card"
   - Select the card from the list
   - Click "Save"
   - **Do not navigate away** until you see a success message
2. **If it still doesn't stick**, restart your software:
   - Close the software completely
   - Reopen it
   - Go to the user and try adding the card again
3. **If using a PC that's been running for a while**, restart the computer:
   - This can resolve temporary database connection issues
   - After restart, try adding the card again
4. **Check your panel's database isn't full:**
   - Some systems have a limit on the number of cards
   - Contact support if you're hitting limits

---

### Issue: "Cannot Find Facility Code" or "Error Creating Card Design"

**Symptoms:** Error message appears when trying to add a card, saying "Facility code not found" or "Cannot edit card design."

**Cause:** The facility code associated with your panel hasn't been configured yet. The facility code is a required identifier that tells all readers which system they belong to.

**Fix:**
1. **Find your panel's facility code:**
   - Go to Devices > Panels or Device Configuration
   - Find your panel in the list (look for AC-215, AC-225, AC-425, or AC-825)
   - Look for a "Facility Code," "Site Code," or "FC" field
   - If blank or showing "0," you need to set one
2. **Set the facility code:**
   - Click to edit the panel
   - Enter a facility code (typically a number between 0-255)
   - This is usually a number provided by your installer, in your documentation, or printed on the back of your access cards
   - Click "Save"
3. **Sync the configuration to the panel:**
   - Select the panel
   - Click "Upload Configuration," "Send to Panel," or "Sync"
   - Wait for completion (typically 10-30 seconds)
4. **Try adding the card again**

**Card Format Information:**

Your access cards may use different formats depending on configuration:
- **Standard 26-bit format:** Uses facility code + card number (most common)
- **No facility code (26-bit):** Uses only card number without facility code (specialized installations)

**If you don't know your facility code:**
- Check your installation documentation or system notes
- Contact your system installer
- Look at the back of existing access cards (often printed there)
- Check with your security manager or facilities team

---

## Panel Card Capacity Reference

Different panel models support different numbers of cards and users:

| Panel Model | Max Users | Max Stored Events | Notes |
|---|---|---|---|
| **AC-215/225** | 30,000 users | 20,000 events | Entry-level 2-4 door panels |
| **AC-425** | 30,000 users | 20,000 events | Mid-range 4-8 door panels |
| **AC-825IP** | 60,000 users | 500,000 events | High-capacity with expansion support |

If you're hitting capacity limits on storing events or users, you may need to:
- Archive old event logs
- Migrate to a higher-capacity panel (AC-825IP)
- Disable automatic event logging for non-critical readers

---

## Prevention

- **Document your facility code** and keep it in an accessible location
- **Create a naming convention** for access groups (e.g., "Building A - All Doors" vs "Building A - Lobby Only")
- **Review access monthly** — remove cards for departed employees promptly and disable rather than delete
- **Test new cards immediately** after adding them to catch issues early
- **Keep a log** of who has access to sensitive doors and when access was granted
- **Use biometric readers** in high-security areas to reduce unauthorized card sharing
- **Monitor your card count** — if you approach panel capacity limits, plan for expansion
- **Back up your database regularly** — see your backup guide for procedures

---

## Still Having Issues?

If you're still experiencing problems:

- **Note the specific card ID** that's not working
- **Document the reader type** (model number if possible)
- **Note the error message** you received (with a screenshot if possible)
- **Confirm the panel is connected** to the network
- **Check the panel firmware version** (may need updating)
- **Contact support** with this information

---

## Related Articles

- [Panel Not Connecting to Network](KB_01_Panel_Connectivity_Issues.md)
- [How to Update Panel Firmware](KB_02_Firmware_Updates.md)
- [Reader Configuration Guide](reader-setup.md)
- [Troubleshooting Reader Errors & Beeping](reader-troubleshooting.md)
- [Access Group & Permission Management](access-groups.md)

---

## Revision History

| Date | Change |
|------|--------|
| Apr 30, 2026 | Initial publication based on 22 support tickets |
