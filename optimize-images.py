#!/usr/bin/env python3
"""
Optimize images for better performance.
This script recompresses WebP images and creates optimized versions.
"""
import os
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("ERROR: Pillow is not installed.")
    print("Install it with: pip install Pillow")
    exit(1)

def optimize_webp(input_path, output_path=None, quality=75, max_size=None):
    """Optimize a WebP image with specified quality and optional resize."""
    try:
        img = Image.open(input_path)
        
        # Resize if max_size is specified
        if max_size:
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
        
        # Save with specified quality
        if output_path is None:
            output_path = input_path
        
        # Convert RGBA to RGB if needed (WebP supports both)
        if img.mode == 'RGBA':
            # Keep alpha channel for WebP
            img.save(output_path, 'WEBP', quality=quality, method=6)
        else:
            img.save(output_path, 'WEBP', quality=quality, method=6)
        
        original_size = Path(input_path).stat().st_size
        new_size = Path(output_path).stat().st_size
        savings = original_size - new_size
        savings_pct = (savings / original_size * 100) if original_size > 0 else 0
        
        print(f"  {Path(input_path).name}: {original_size/1024:.1f} KB -> {new_size/1024:.1f} KB ({savings_pct:.1f}% reduction)")
        return True
    except Exception as e:
        print(f"  ERROR processing {input_path}: {e}")
        return False

def create_hero_variants():
    """Create optimized hero background variants."""
    images_dir = Path("assets/images")
    hero_jpg = images_dir / "hero-background.jpg"
    
    if not hero_jpg.exists():
        print(f"Warning: {hero_jpg} not found, skipping hero optimization")
        return
    
    print("Optimizing hero background images...")
    
    # Desktop large: 1600x900
    optimize_webp(
        hero_jpg,
        images_dir / "hero-background-desktop-large.webp",
        quality=80,
        max_size=(1600, 900)
    )
    
    # Desktop standard: 1200x675
    optimize_webp(
        hero_jpg,
        images_dir / "hero-background-desktop.webp",
        quality=80,
        max_size=(1200, 675)
    )
    
    # Tablet: keep existing but reoptimize
    if (images_dir / "hero-background-tablet.webp").exists():
        optimize_webp(
            images_dir / "hero-background-tablet.webp",
            quality=80
        )
    
    # Mobile: keep existing but reoptimize
    if (images_dir / "hero-background-mobile.webp").exists():
        optimize_webp(
            images_dir / "hero-background-mobile.webp",
            quality=80
        )

def optimize_service_images():
    """Optimize service card images."""
    images_dir = Path("assets/images")
    
    # Map WebP files to their JPG sources for better compression
    service_sources = {
        "service-commercial-paving-800.webp": ("service-commercial-paving.jpg", (800, 533)),
        "service-commercial-paving-400.webp": ("service-commercial-paving.jpg", (400, 267)),
        "service-kerbing-800.webp": ("service-kerbing.jpg", (800, 533)),
        "service-kerbing-400.webp": ("service-kerbing.jpg", (400, 267)),
        "service-concrete-patios-800.webp": ("service-concrete-patios.jpg", (800, 533)),
        "service-concrete-patios-400.webp": ("service-concrete-patios.jpg", (400, 267)),
        "service-residential-driveways-800.webp": ("service-residential-driveways.jpg", (800, 533)),
        "service-residential-driveways-400.webp": ("service-residential-driveways.jpg", (400, 267)),
        "service-concrete-repair-800.webp": ("service-concrete-repair.jpg", (800, 533)),
        "service-concrete-repair-400.webp": ("service-concrete-repair.jpg", (400, 267)),
        "service-decorative-concrete-800.webp": ("service-decorative-concrete.jpg", (800, 533)),
        "service-decorative-concrete-400.webp": ("service-decorative-concrete.jpg", (400, 267)),
    }
    
    print("\nOptimizing service card images...")
    for webp_name, (jpg_name, size) in service_sources.items():
        webp_path = images_dir / webp_name
        jpg_path = images_dir / jpg_name
        
        if jpg_path.exists():
            # Optimize from JPG source
            optimize_webp(jpg_path, webp_path, quality=75, max_size=size)
        elif webp_path.exists():
            # Fallback to recompressing existing WebP
            optimize_webp(webp_path, quality=75, force_recompress=True)
        else:
            print(f"  Skipping {webp_name} (source not found)")

def optimize_gallery_images():
    """Optimize gallery images."""
    images_dir = Path("assets/images")
    
    # Map WebP files to their JPG sources
    gallery_sources = {
        "gallery-1-800.webp": ("gallery-1.jpg", (800, 549)),
        "gallery-1-400.webp": ("gallery-1.jpg", (400, 275)),
        "gallery-2-800.webp": ("gallery-2.jpg", (800, 549)),
        "gallery-2-400.webp": ("gallery-2.jpg", (400, 275)),
        "gallery-3-800.webp": ("gallery-3.jpg", (800, 549)),
        "gallery-3-400.webp": ("gallery-3.jpg", (400, 275)),
        "gallery-4-800.webp": ("gallery-4.jpg", (800, 549)),
        "gallery-4-400.webp": ("gallery-4.jpg", (400, 275)),
    }
    
    print("\nOptimizing gallery images...")
    for webp_name, (jpg_name, size) in gallery_sources.items():
        webp_path = images_dir / webp_name
        jpg_path = images_dir / jpg_name
        
        if jpg_path.exists():
            # Optimize from JPG source
            optimize_webp(jpg_path, webp_path, quality=75, max_size=size)
        elif webp_path.exists():
            # Fallback to recompressing existing WebP
            optimize_webp(webp_path, quality=75, force_recompress=True)
        else:
            print(f"  Skipping {webp_name} (source not found)")

def main():
    """Main function."""
    print("Image Optimization Script")
    print("=" * 50)
    
    create_hero_variants()
    optimize_service_images()
    optimize_gallery_images()
    
    print("\n" + "=" * 50)
    print("Optimization complete!")

if __name__ == "__main__":
    main()

