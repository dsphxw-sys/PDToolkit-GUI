import shutil
import subprocess

def check_tools():
    tools = ["subfinder", "nuclei", "httpx", "naabu", "katana"]
    missing = [t for t in tools if not shutil.which(t)]
    if missing:
        print("⚠️ Herramientas no encontradas:", ", ".join(missing))
        print("Ejecuta: python install.py")
