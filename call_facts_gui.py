import tkinter as tk
from tkinter import scrolledtext
import requests
import json
import os


class OllamaGUI:
    def __init__(self, master):
        self.master = master
        master.title("Ollama API Interface")

        self.question_label = tk.Label(master, text="Ingrese hecho:")
        self.question_label.pack()

        self.question_entry = scrolledtext.ScrolledText(master, width=100, height=15)
        self.question_entry.pack()

        self.get_answer_button = tk.Button(master, text="Obtener respuesta", command=self.get_answer)
        self.get_answer_button.pack()

        self.answer_label = tk.Label(master, text="Respuesta:")
        self.answer_label.pack()

        self.answer_text = scrolledtext.ScrolledText(master, width=100, height=15)
        self.answer_text.pack()

    def get_answer(self):
        question = self.question_entry.get("1.0", tk.END).strip()
        if question:
            answer = get_question_answer("Hecho", question)
            self.answer_text.delete("1.0", tk.END)
            self.answer_text.insert(tk.END, answer)
        else:
            self.answer_text.delete("1.0", tk.END)
            self.answer_text.insert(tk.END, "Por favor, ingrese un hecho.")


def get_question_answer(tipoPrompt, question):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "pythonLearning",
        "prompt": tipoPrompt + ": " + question,
        "stream": False
    }
    response = requests.post(url, data=json.dumps(data))
    response_json = response.json()
    if response_json["done"]:
        answer = response_json["response"]
    else:
        answer = "Error al obtener la respuesta."
    return answer


if __name__ == "__main__":
    root = tk.Tk()
    gui = OllamaGUI(root)
    root.mainloop()
