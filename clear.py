#!/usr/bin/env python3

import os
import sys

def main():
    """
    Cleans up specified files from the game server's channels directory.
    """
    # List of files to remove, including file extensions.
    FILES_TO_CLEAN = ['.core', '.txt', 'syserr.log', 'syslog.log']

    # The base directory to start the cleanup from.
    # This assumes the script is run from the root of the game installation.
    base_dir = os.path.join(os.getcwd(), 'channels')

    print(f"Starting cleanup in '{base_dir}'...")

    if not os.path.exists(base_dir):
        print(f"Error: Directory '{base_dir}' not found.")
        sys.exit(1)

    # Use os.walk to recursively search for files.
    for root, dirs, files in os.walk(base_dir):
        # Determine if the current directory is a target for cleanup.
        is_target_dir = False
        if os.path.basename(root) in ['auth', 'db']:
            is_target_dir = True
        elif os.path.basename(os.path.dirname(root)).startswith('channel') and os.path.basename(root).startswith('core'):
            is_target_dir = True

        if is_target_dir:
            print(f"\nScanning '{os.path.relpath(root, base_dir)}'...")
            
            for filename in files:
                for file_to_clean in FILES_TO_CLEAN:
                    if filename.endswith(file_to_clean):
                        file_path = os.path.join(root, filename)
                        
                        try:
                            os.remove(file_path)
                            print(f"  - Removed '{os.path.relpath(file_path, base_dir)}'")
                        except OSError as e:
                            print(f"  - Error removing '{file_path}': {e}")
                            
    print("\nCleanup complete.")

if __name__ == "__main__":
    main()
