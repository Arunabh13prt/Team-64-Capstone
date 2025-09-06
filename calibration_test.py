#!/usr/bin/env python3
"""
Calibration System Test Script

This script demonstrates the visual calibration system with blinking dots
at screen edges and center for accurate proctoring setup.

Usage:
    python calibration_test.py

Features:
- 9-point visual calibration system
- Blinking dots at screen edges and center
- Real-time eye tracking during calibration
- Adaptive threshold calculation
- Calibration data storage and loading
"""

import subprocess
import sys
import os
import json

def main():
    print("🎯 CALIBRATION SYSTEM TEST")
    print("=" * 50)
    print("This will run the proctoring system with calibration features.")
    print("\n📋 CALIBRATION INSTRUCTIONS:")
    print("1. Press 'k' to start calibration")
    print("2. Look at each blinking dot and press SPACE")
    print("3. Complete all 9 calibration points")
    print("4. System will calculate adaptive thresholds")
    print("5. Calibration data will be saved automatically")
    print("\n🎯 CALIBRATION POINTS:")
    print("• Center of screen")
    print("• Four corners (top-left, top-right, bottom-left, bottom-right)")
    print("• Four edges (top, bottom, left, right)")
    print("\n⚙️ CONTROLS:")
    print("• 'k' - Start calibration")
    print("• SPACE - Advance to next target")
    print("• 'l' - Load saved calibration")
    print("• 'q' - Quit")
    print("=" * 50)
    
    try:
        # Run the main script
        subprocess.run([sys.executable, "main.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running calibration system: {e}")
    except KeyboardInterrupt:
        print("\nCalibration test interrupted by user.")
    except FileNotFoundError:
        print("Error: main.py not found. Make sure you're in the correct directory.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def check_calibration_data():
    """Check if calibration data exists and display info."""
    if os.path.exists("calibration_data.json"):
        try:
            with open("calibration_data.json", 'r') as f:
                data = json.load(f)
            
            print("\n📁 EXISTING CALIBRATION DATA:")
            print(f"Screen size: {data['screen_bounds']['width']}x{data['screen_bounds']['height']}")
            print(f"Eye range X: {data['eye_range_x']}")
            print(f"Eye range Y: {data['eye_range_y']}")
            print(f"Adaptive threshold X: {data.get('adaptive_threshold_x', 'N/A')}")
            print(f"Adaptive threshold Y: {data.get('adaptive_threshold_y', 'N/A')}")
            print(f"Calibration timestamp: {data.get('calibration_timestamp', 'N/A')}")
            return True
        except Exception as e:
            print(f"Error reading calibration data: {e}")
            return False
    else:
        print("\n❌ No calibration data found.")
        return False

if __name__ == "__main__":
    print("🔍 Checking for existing calibration data...")
    has_calibration = check_calibration_data()
    
    if has_calibration:
        print("\n✅ Calibration data found!")
        print("You can run the system with existing calibration or recalibrate.")
    else:
        print("\n🎯 No calibration data found.")
        print("Calibration is recommended for best accuracy!")
    
    print("\nStarting calibration test...")
    main()
