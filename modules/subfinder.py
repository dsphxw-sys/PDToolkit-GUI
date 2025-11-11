import subprocess

def run(domain):
    cmd = ["subfinder", "-d", domain, "-silent"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else f"❌ Subfinder error: {result.stderr}"
