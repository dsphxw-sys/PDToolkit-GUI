import subprocess

def run(domain):
    cmd = ["nuclei", "-u", f"https://{domain}", "-silent"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else f"❌ Nuclei error: {result.stderr}"
