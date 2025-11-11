import subprocess

def run(domain):
    cmd = ["naabu", "-host", domain, "-silent"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else f"❌ Naabu error: {result.stderr}"
