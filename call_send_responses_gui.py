import tkinter as tk
from tkinter import scrolledtext
import requests
import json
import os

class OllamaGUI:
    def __init__(self, master):
        self.master = master
        master.title("Ollama API Interface")

        self.folder_label = tk.Label(master, text="Carpeta de respuestas:")
        self.folder_label.pack()

        self.folder_entry = tk.Entry(master)
        self.folder_entry.pack()

        self.send_button = tk.Button(master, text="Enviar Respuestas", command=self.send_responses)
        self.send_button.pack()

        self.status_label = tk.Label(master, text="")
        self.status_label.pack()

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

            # Enviar respuestas a la API
            success_count = 0
            for response_data in responses:
                response = send_to_ollama("Hecho", response_data)
                if response:
                    success_count += 1

            self.status_label.config(text=f"{success_count} respuestas enviadas con éxito.")
        else:
            self.status_label.config(text="La carpeta no existe.")

def send_to_ollama(tipoPrompt, response_data):
    pregunta = response_data["question"]
    respuesta = response_data["respuesta"]
    data = {
        "model": "pythonLearning",
        "prompt": tipoPrompt + ": " + pregunta + " \n " + respuesta,
        "stream": False
    }
    response = requests.post(url, data=json.dumps(data))

    url = "http://localhost:11434/api/generate"
    response = requests.post(url, data=json.dumps(data))
    response_json = response.json()
    print(response_json)
    if response_json["done"]:
        return True
    else:
        return False

if __name__ == "__main__":
    root = tk.Tk()
    gui = OllamaGUI(root)
    root.mainloop()
