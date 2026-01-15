# Manual to Automation Workflow Mapping

## Purpose
This document demonstrates how a simple manual DNA library preparation workflow
can be translated into structured, automation-compatible steps.

This is a conceptual design intended for learning and simulation purposes only.

---

## Manual Protocol Overview
A simplified DNA library preparation workflow typically includes:
1. Sample normalisation
2. Enzymatic reaction setup
3. Incubation
4. Cleanup and transfer

These steps are usually performed manually using pipettes and timers.

---

## Automation-Oriented Breakdown

### Step 1: Sample Normalisation
- Input: DNA samples with measured concentrations
- Manual action:
  - Measure DNA concentration
  - Dilute samples to a target concentration
- Automation translation:
  - Read concentration values from metadata
  - Calculate dilution volumes
  - Transfer calculated volumes to a new plate
- QC checkpoint:
  - Final concentration within acceptable range

---

### Step 2: Enzymatic Reaction Setup
- Inputs:
  - Normalised DNA
  - Enzyme mix
  - Reaction buffer
- Manual action:
  - Pipette reagents into each well
- Automation translation:
  - Dispense fixed reagent volumes
  - Mix contents
- QC checkpoint:
  - All required reagents added

---

### Step 3: Incubation
- Manual action:
  - Incubate samples for a defined time and temperature
- Automation translation:
  - Track incubation time
  - Prevent next step until incubation completes
- QC checkpoint:
  - Incubation completed successfully

---

### Step 4: Cleanup and Transfer
- Manual action:
  - Perform cleanup and elute DNA
- Automation translation:
  - Transfer eluate to a new plate
- QC checkpoint:
  - Expected volume recovered

