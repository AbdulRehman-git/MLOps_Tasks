#!/bin/bash


SOURCE_DIR="/tmp"
DEST_DIR="/tmp/old_files"
LOG_FILE="/var/log/file_cleanup.log"


if [ ! -d "$DEST_DIR" ]; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Directory $DEST_DIR does not exist. Creating it." >> "$LOG_FILE"
    mkdir -p "$DEST_DIR"
fi


for log_file in "$SOURCE_DIR"/*.log; do
    if [ -e "$log_file" ]; then
        mv "$log_file" "$DEST_DIR"
        echo "$(date '+%Y-%m-%d %H:%M:%S') - Moved $log_file to $DEST_DIR." >> "$LOG_FILE"
    fi
done


echo "$(date '+%Y-%m-%d %H:%M:%S') - Moved .log files to: tmp/old_files" >> "$LOG_FILE"
