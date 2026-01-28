#!/bin/bash
set -e

TARGET="/home/student"
SNAPSHOT="/home/.snapshots/student-clean"

# Ensure nothing is mounted or in use
umount -l "$TARGET" 2>/dev/null || true

# Delete current student home
btrfs subvolume delete "$TARGET"

# Restore snapshot
btrfs subvolume snapshot "$SNAPSHOT" "$TARGET"

# Fix ownership
chown -R student:student "$TARGET"
