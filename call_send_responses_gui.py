import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import requests
import json
import os
import random

class OllamaGUI:

    def __init__(self, master):
        self.master = master
        master.title("Ollama API Interface")

        # Carpeta de respuestas
        self.folder_frame = tk.Frame(master)
        self.folder_frame.pack(pady=10)

        self.folder_label = tk.Label(self.folder_frame, text="Carpeta de respuestas:")
        self.folder_label.pack(side=tk.LEFT)

        self.folder_path = tk.StringVar()
        self.folder_entry = tk.Entry(self.folder_frame, textvariable=self.folder_path, state='disabled', width=65)
        self.folder_entry.pack(side=tk.LEFT)

        self.browse_button = tk.Button(self.folder_frame, text="Explorar", command=self.browse_folder)
        self.browse_button.pack(side=tk.LEFT, padx=(10, 0))

        # Cuadro de entrada para la cantidad de respuestas a enviar
        self.quantity_label = tk.Label(master, text="Cantidad de respuestas a enviar:")
        self.quantity_label.pack()

        self.quantity_entry = tk.Entry(master)
        self.quantity_entry.pack()

        # Botón para enviar respuestas
        self.send_button = tk.Button(master, text="Enviar Respuestas", command=self.send_responses)
        self.send_button.pack(pady=(10, 0))

        # Etiqueta de estado
        self.status_label = tk.Label(master, text="")
        self.status_label.pack()

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_entry.config(state='normal')
            self.folder_entry.delete(0, tk.END)
            self.folder_entry.insert(0, folder_path)
            self.folder_entry.config(state='disabled')

    def send_responses(self):
        folder_path = self.folder_entry.get()
        if os.path.exists(folder_path):
            responses = []
            for filename in os.listdir(folder_path):
                if filename.endswith(".json"):
                    file_path = os.path.join(folder_path, filename)
                    with open(file_path, "r", encoding="utf-8") as file:
                        response_data = json.load(file)
                        responses.append(response_data)

            # Verificar que la entrada de cantidad sea un número entero
            try:
                quantity_to_send = int(self.quantity_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese una cantidad válida.")
                return

            # Mezclar las respuestas
            random.shuffle(responses)

            # Enviar respuestas a la API (limitar según la cantidad ingresada)
            success_count = 0
            for response_data in responses[:quantity_to_send]:
                response = send_to_ollama("Hecho", response_data)
                if response:
                    success_count += 1

            self.status_label.config(text=f"{success_count} respuestas enviadas con éxito.")
        else:
            self.status_label.config(text="La carpeta no existe.")

def send_to_ollama(tipoPrompt, response_data):
    pregunta = response_data["question"]
    respuesta = response_data["answer"]
    data = {
        "model": "pythonLearning",
        "prompt": tipoPrompt + ": " + pregunta + " \n " + respuesta,
        "stream": False
    }
    url = "http://localhost:11434/api/generate"
    response = requests.post(url, data=json.dumps(data))
    response_json = response.json()
    if response_json["done"]:
        return True
    else:
        return False

if __name__ == "__main__":
    root = tk.Tk()
    gui = OllamaGUI(root)
    root.mainloop()
