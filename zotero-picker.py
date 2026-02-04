#!/usr/bin/env python3
import requests
import subprocess
import sys

# Configuration
ZOTERO_URL = "http://127.0.0.1:23119/better-bibtex/export?/library;id:1/My%20Library.json"
ROFI_PROMPT = "Zotero Citation:"
# Set to 'xclip -selection clipboard' for X11 or 'wl-copy' for Wayland
COPY_COMMAND = "xclip -selection clipboard" 

def get_zotero_items():
    try:
        response = requests.get(ZOTERO_URL, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error: Could not connect to Zotero/Better BibTeX. Is Zotero running? \n{e}")
        sys.exit(1)

def format_item(item):
    """Formats a Zotero item into a readable string for Rofi."""
    key = item.get('citationKey') or item.get('id') or 'no-key'
    title = item.get('title', 'Unknown Title')
    
    # Extract authors
    creators = item.get('creators', [])
    authors = ", ".join([c.get('lastName', '') for c in creators if 'lastName' in c])
    
    # Extract year
    date = item.get('date', '')
    year = date[:4] if len(date) >= 4 else "n.d."
    
    return f"[{key}] {title} — {authors} ({year})", key

def main():
    items = get_zotero_items()
    print(items)
    
    # Create a mapping of the display string to the citation key
    display_list = []
    key_mapping = []
    
    for item in items:
        display_str, key = format_item(item)
        display_list.append(display_str)
        key_mapping.append(key)

    # Launch Rofi
    rofi_input = "\n".join(display_list).encode("utf-8")
    try:
        proc = subprocess.Popen(
            ["rofi", "-dmenu", "-i", "-p", ROFI_PROMPT, "-format", "i", "-fuzzy"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE
        )
        stdout, _ = proc.communicate(input=rofi_input)
        
        if stdout:
            selected_index = int(stdout.decode("utf-8").strip())
            selected_key = key_mapping[selected_index]
            
            # Copy to clipboard
            subprocess.run(COPY_COMMAND.split(), input=selected_key.encode("utf-8"))
            print(f"Copied: {selected_key}")
            
    except Exception as e:
        print(f"Selection cancelled or error occurred: {e}")

if __name__ == "__main__":
    main()
