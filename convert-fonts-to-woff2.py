#!/usr/bin/env python3
"""
Convert TTF font files to WOFF2 format.
This script processes all TTF files in assets/fonts/ and generates WOFF2 versions.
Run this script whenever TTF fonts are updated or new fonts are added.
"""
import os
import sys
from pathlib import Path

def convert_ttf_to_woff2(ttf_path, output_dir=None):
    """Convert a single TTF file to WOFF2 format."""
    try:
        from fontTools.ttLib import woff2
        
        ttf_path = Path(ttf_path)
        if output_dir:
            output_path = Path(output_dir) / f"{ttf_path.stem}.woff2"
        else:
            output_path = ttf_path.parent / f"{ttf_path.stem}.woff2"
        
        print(f"Converting {ttf_path.name}...", end=" ")
        woff2.compress(str(ttf_path), str(output_path))
        
        # Get file sizes for comparison
        ttf_size = ttf_path.stat().st_size
        woff2_size = output_path.stat().st_size
        compression_ratio = (1 - woff2_size / ttf_size) * 100
        
        print(f"✓ ({woff2_size/1024:.2f} KB, {compression_ratio:.1f}% smaller)")
        return True
    except ImportError:
        print("ERROR: fonttools[woff] is not installed.")
        print("Install it with: pip install fonttools[woff]")
        return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False

def main():
    """Main function to convert all TTF files in assets/fonts/."""
    fonts_dir = Path("assets/fonts")
    
    if not fonts_dir.exists():
        print(f"ERROR: Fonts directory not found: {fonts_dir}")
        sys.exit(1)
    
    # Find all TTF files
    ttf_files = list(fonts_dir.glob("*.ttf"))
    
    if not ttf_files:
        print(f"No TTF files found in {fonts_dir}")
        sys.exit(0)
    
    print(f"Found {len(ttf_files)} TTF file(s) to convert:\n")
    
    success_count = 0
    failed_files = []
    
    for ttf_file in sorted(ttf_files):
        # Skip if WOFF2 already exists and is newer (optional optimization)
        woff2_file = ttf_file.parent / f"{ttf_file.stem}.woff2"
        if woff2_file.exists():
            if woff2_file.stat().st_mtime > ttf_file.stat().st_mtime:
                print(f"Skipping {ttf_file.name} (WOFF2 is newer)")
                continue
        
        if convert_ttf_to_woff2(ttf_file):
            success_count += 1
        else:
            failed_files.append(ttf_file.name)
    
    print(f"\n{'='*60}")
    print(f"Conversion complete: {success_count}/{len(ttf_files)} successful")
    
    if failed_files:
        print(f"\nFailed files:")
        for file in failed_files:
            print(f"  - {file}")
        sys.exit(1)
    else:
        print("All fonts converted successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()

