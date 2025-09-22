#!/usr/bin/env python3
"""
Civic Sense Project Launcher
Starts the PHP development server with proper environment setup
"""

import os
import sys
import subprocess
import signal
import time
from pathlib import Path

class CivicSenseLauncher:
    def __init__(self):
        self.project_dir = Path(__file__).parent
        self.php_exe = "php"
        self.server_process = None
        
    def start_server(self):
        """Start PHP development server"""
        print("🚀 Starting Civic Sense Project...")
        print("📁 Project directory:", self.project_dir)
        print("🐘 PHP executable:", self.php_exe)
        
        # Change to project directory
        os.chdir(self.project_dir)
        
        # Start PHP server
        try:
            self.server_process = subprocess.Popen([
                self.php_exe, "-S", "127.0.0.1:8000", "-t", str(self.project_dir)
            ])
            
            print("✅ Server started successfully!")
            print("🌐 Access your application at: http://127.0.0.1:8000")
            print("📋 Press Ctrl+C to stop the server")
            
            # Wait for server to start
            time.sleep(2)
            
            # Keep running until interrupted
            try:
                self.server_process.wait()
            except KeyboardInterrupt:
                print("\n🛑 Stopping server...")
                self.stop_server()
                
        except Exception as e:
            print(f"❌ Failed to start server: {e}")
            sys.exit(1)
    
    def stop_server(self):
        """Stop the PHP server"""
        if self.server_process:
            self.server_process.terminate()
            self.server_process.wait()
            print("✅ Server stopped")

if __name__ == "__main__":
    launcher = CivicSenseLauncher()
    launcher.start_server()
