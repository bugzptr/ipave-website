#!/usr/bin/env python3
"""
Validate WOFF2 font files
"""
import struct
import os

def validate_woff2(filepath):
    """Validate WOFF2 file structure"""
    try:
        with open(filepath, 'rb') as f:
            # Read WOFF2 header (16 bytes)
            header = f.read(16)
            
            if len(header) < 16:
                return False, "File too short"
            
            # Check signature
            signature = header[0:4]
            if signature != b'wOF2':
                return False, f"Invalid signature: {signature}"
            
            # Read version (4 bytes, big-endian)
            version = struct.unpack('>I', header[4:8])[0]
            
            # Read totalSfntSize (4 bytes, big-endian)
            total_sfnt_size = struct.unpack('>I', header[8:12])[0]
            
            # Read numTables (2 bytes, big-endian)
            num_tables = struct.unpack('>H', header[12:14])[0]
            
            # Read reserved (2 bytes)
            reserved = struct.unpack('>H', header[14:16])[0]
            
            # Get file size
            file_size = os.path.getsize(filepath)
            
            return True, {
                'signature': signature.decode('ascii'),
                'version': hex(version),
                'total_sfnt_size': total_sfnt_size,
                'num_tables': num_tables,
                'reserved': reserved,
                'file_size': file_size,
                'header_valid': True
            }
    except Exception as e:
        return False, str(e)

# Test all WOFF2 files
fonts_to_test = [
    'assets/fonts/encode-sans-semi-condensed-400.woff2',
    'assets/fonts/encode-sans-semi-condensed-600.woff2',
    'assets/fonts/encode-sans-semi-condensed-700.woff2',
    'assets/fonts/encode-sans-semi-condensed-900.woff2',
    'assets/fonts/encode-sans-expanded-400.woff2',
    'assets/fonts/encode-sans-expanded-700.woff2',
    'assets/fonts/dm-sans-400.woff2',
    'assets/fonts/dm-sans-700.woff2',
]

print("WOFF2 File Validation Results:")
print("=" * 60)

all_valid = True
for font_path in fonts_to_test:
    if os.path.exists(font_path):
        is_valid, result = validate_woff2(font_path)
        font_name = os.path.basename(font_path)
        
        if is_valid:
            print(f"OK {font_name}")
            print(f"  Version: {result['version']}")
            print(f"  Tables: {result['num_tables']}")
            print(f"  File Size: {result['file_size']} bytes ({result['file_size']/1024:.2f} KB)")
        else:
            print(f"ERROR {font_name}: {result}")
            all_valid = False
        print()
    else:
        print(f"ERROR {font_path}: File not found")
        all_valid = False

if all_valid:
    print("All WOFF2 files have valid headers.")
    print("\nNote: Valid headers don't guarantee browser compatibility.")
    print("If browsers still show parsing errors, the files may need to be regenerated")
    print("from TTF sources using a proper WOFF2 converter.")
else:
    print("Some files have issues and may need to be regenerated.")

