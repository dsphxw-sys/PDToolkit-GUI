#!/usr/bin/env python3
import subprocess
import os

tools = {
    "subfinder": "github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest",
    "nuclei": "github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest",
    "httpx": "github.com/projectdiscovery/httpx/cmd/httpx@latest",
    "naabu": "github.com/projectdiscovery/naabu/v2/cmd/naabu@latest",
    "katana": "github.com/projectdiscovery/katana/cmd/katana@latest"
}

print("🔧 Instalando herramientas de ProjectDiscovery...")

for tool, repo in tools.items():
    print(f"Instalando {tool}...")
    subprocess.run(["go", "install", "-v", repo], check=True)

print("✅ Todas las herramientas instaladas.")
