"""
=============================================================================
LAB 1.3 — Secure Environment & File Operations
=============================================================================

SCENARIO:
    You're a Jira Admin building a script that:
      1. Loads API credentials securely from environment variables
      2. Validates that all required config is present before proceeding
      3. Scans a directory for old Jira backup files (.xml)
      4. Reports file sizes and identifies files older than 30 days
      5. Logs everything properly (not just print statements)

WHY THIS MATTERS:
    - NEVER hardcode passwords/tokens in your scripts
    - Production scripts need proper logging (not print)
    - File operations are common in admin/DevOps work
    - Custom exceptions make your scripts professional

PYTHON CONCEPTS YOU'LL PRACTICE:
    1. os.getenv()              — Read environment variables
    2. os.path / pathlib.Path   — File and directory operations
    3. Custom Exceptions        — class MyError(Exception): pass
    4. sys.exit()               — Clean script termination
    5. logging module           — Professional logging with levels
    6. datetime & timedelta     — Date calculations
    7. os.path.getmtime()       — File modification time
    8. Functions (def)          — Reusable blocks of code

LOGGING LEVELS (from least to most severe):
    DEBUG    → Detailed diagnostic info
    INFO     → Confirmation that things are working
    WARNING  → Something unexpected, but script continues
    ERROR    → Something failed
    CRITICAL → Script cannot continue

REFERENCE — os.path vs pathlib.Path:
    os.path (traditional):
        os.listdir(path)           → list filenames
        os.path.join(dir, file)    → combine paths
        os.path.getsize(path)      → file size in bytes
        os.path.getmtime(path)     → modification time

    pathlib.Path (modern):
        path.iterdir()             → iterate over directory
        path / "file.txt"          → combine paths (uses / operator!)
        path.stat().st_size        → file size in bytes
        path.suffix                → file extension (.xml, .json)
=============================================================================
"""

import os
import sys
import logging
from pathlib import Path
from datetime import datetime, timedelta

# SETUP: Create output directory
script_dir = os.path.dirname(__file__)
output_dir = os.path.join(script_dir, "output")
os.makedirs(output_dir, exist_ok=True)

# ===========================================================================
# TASK 1: Set up the logging module
# ===========================================================================
# Configure logging to output to BOTH console AND a file (output/lab1_3.log)
# Use format: "%(asctime)s [%(levelname)s] %(message)s"
#
# Hints:
#   logging.basicConfig(
#       level=logging.DEBUG,
#       format="%(asctime)s [%(levelname)s] %(message)s",
#       handlers=[
#           logging.StreamHandler(),                    # Console
#           logging.FileHandler("path/to/file.log")     # File
#       ]
#   )
#   logger = logging.getLogger("JiraAdmin")
#   logger.info("This is an info message")
#   logger.warning("This is a warning")
#   logger.error("This is an error")

# YOUR CODE HERE:


# ===========================================================================
# TASK 2: Define a Custom Exception
# ===========================================================================
# Create a ConfigurationError exception class.
#
# Hints:
#   class ConfigurationError(Exception):
#       """Raised when required configuration is missing."""
#       pass

# YOUR CODE HERE:


# ===========================================================================
# TASK 3: Load and validate environment variables
# ===========================================================================
# Check that JIRA_DOMAIN, JIRA_EMAIL, and API_TOKEN are set.
# Load them from the .env file (at jira/.env) by reading line by line.
# If any are missing, raise your ConfigurationError (or print a warning).
#
# Hints for manual .env parsing:
#   with open(env_file, "r") as f:
#       for line in f:
#           line = line.strip()
#           if "=" in line:
#               key, value = line.split("=", 1)  # split on first = only
#               os.environ[key.strip()] = value.strip().strip('"')
#
#   Then check: os.getenv("JIRA_DOMAIN")
#   Mask secrets in logs: value[:8] + "..." (only show first 8 chars)

# YOUR CODE HERE:


# ===========================================================================
# TASK 4: Build API URLs using string concatenation and f-strings
# ===========================================================================
# Using the JIRA_DOMAIN from env vars, build these URLs:
#   1. Search URL:  {domain}/rest/api/3/search
#   2. Issue URL:   {domain}/rest/api/3/issue/KAN-101
#
# Try all 3 methods:
#   Method 1: domain + "/rest/api/3/search"          (concatenation)
#   Method 2: f"{domain}/rest/api/3/search"           (f-string)
#   Method 3: "{}/rest/api/3/search".format(domain)   (.format)

# YOUR CODE HERE:


# ===========================================================================
# TASK 5: Create sample files and scan a directory
# ===========================================================================
# Create a "jira_backups" folder inside output/ with these sample files:
#   jira_backup_2026_08_01.xml
#   jira_backup_2026_07_15.xml
#   jira_backup_2026_06_01.xml
#   project_config.json
#   user_export.csv
#
# Then list all files with their size and modification date.
# Try both os.path AND pathlib.Path approaches.
#
# Hints for creating sample files:
#   with open(filepath, "w") as f:
#       f.write(f"Sample data for {filename}\n" * 100)
#
# Hints for listing:
#   for filename in os.listdir(directory):
#       size = os.path.getsize(os.path.join(directory, filename))

# YOUR CODE HERE:


# ===========================================================================
# TASK 6: Find files older than 30 days
# ===========================================================================
# Calculate cutoff date: datetime.now() - timedelta(days=30)
# Compare each .xml file's modification time against the cutoff.
#
# Hints:
#   mod_time = datetime.fromtimestamp(os.path.getmtime(filepath))
#   if mod_time < cutoff_date:
#       # this file is old
#
# Note: Since you just created the files, they'll all be "recent".
# That's expected! The logic is what matters.

# YOUR CODE HERE:


# ===========================================================================
# TASK 7: Write a function to format file sizes
# ===========================================================================
# Create a function: def format_file_size(size_bytes):
# Convert bytes → "3.4 KB" or "1.2 MB" or "2.1 GB"
#
# Hints:
#   1 KB = 1024 bytes
#   1 MB = 1024 * 1024 bytes
#   1 GB = 1024 * 1024 * 1024 bytes
#   f"{size_bytes / 1024:.1f} KB"  ← :.1f means 1 decimal place

# YOUR CODE HERE:


# ===========================================================================
# TASK 8: Generate a cleanup report file
# ===========================================================================
# Write a backup_audit_report.txt with:
#   - Timestamp, directory path, total files, total size
#   - List of XML files and whether they're old or recent
#
# YOUR CODE HERE:


print("\n✅ Lab 1.3 Complete!")
print("🎉 Phase 1 Complete! You're ready for Phase 2 — Jira REST API Operations")
