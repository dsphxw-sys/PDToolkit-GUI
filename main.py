import customtkinter as ctk
from modules import subfinder, nuclei, httpx, naabu, katana, notify
from utils import exporter, installer
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class PDKitGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PDKit-GUI | ProjectDiscovery Toolkit")
        self.geometry("900x600")

        self.domain = ctk.StringVar()

        ctk.CTkLabel(self, text="Dominio objetivo:").pack(pady=10)
        ctk.CTkEntry(self, textvariable=self.domain, width=400).pack()

        self.tool_frame = ctk.CTkFrame(self)
        self.tool_frame.pack(pady=10)

        tools = ["Subfinder", "Nuclei", "HTTPX", "Naabu", "Katana"]
        for tool in tools:
            ctk.CTkButton(self.tool_frame, text=f"Ejecutar {tool}", command=lambda t=tool: self.run_tool(t)).pack(side="left", padx=5)

        self.output = ctk.CTkTextbox(self, width=850, height=350)
        self.output.pack(pady=10)

        ctk.CTkButton(self, text="Exportar JSON", command=lambda: exporter.save_json(self.output.get("1.0", "end"))).pack(pady=5)

    def run_tool(self, tool):
        domain = self.domain.get()
        if not domain:
            self.log("⚠️ Introduce un dominio.")
            return
        threading.Thread(target=self.execute_tool, args=(tool, domain)).start()

    def execute_tool(self, tool, domain):
        self.log(f"🔍 Ejecutando {tool} sobre {domain}...")
        try:
            if tool == "Subfinder":
                result = subfinder.run(domain)
            elif tool == "Nuclei":
                result = nuclei.run(domain)
            elif tool == "HTTPX":
                result = httpx.run(domain)
            elif tool == "Naabu":
                result = naabu.run(domain)
            elif tool == "Katana":
                result = katana.run(domain)
            else:
                result = "❌ Herramienta no soportada."
            self.log(result)
        except Exception as e:
            self.log(f"❌ Error: {e}")

    def log(self, text):
        self.output.insert("end", text + "\n")
        self.output.see("end")

if __name__ == "__main__":
    installer.check_tools()
    app = PDKitGUI()
    app.mainloop()
