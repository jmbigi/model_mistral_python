import requests
import json
import os


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
        answer = None
    return answer


def save_question(question, folder, name):
    question_filename = os.path.join(
        folder, name + ".json")
    with open(question_filename, "w", encoding="utf-8") as f:
        json.dump({"question": question}, f, ensure_ascii=False, indent=2)


def save_question_answer(question, answer, nota, folder, name):
    answer_filename = os.path.join(
        folder, name + ".json")
    with open(answer_filename, "w", encoding="utf-8") as f:
        json.dump({"question": question, "answer": answer, "score": nota},
                  f, ensure_ascii=False, indent=2)


def clean_question(question):
    return question.strip().replace("* ", "").strip().replace(" ", "_").replace("¿", "").replace("?", "").replace("\"", ""). replace("/", "_"). replace('"', '').replace("\\\"", "").replace(".", "_").replace("__", "_").strip()


if __name__ == "__main__":
    for i in range(5):
        respuestas_folder = "respuestas_estud"
        os.makedirs(respuestas_folder, exist_ok=True)

        # Cargar preguntas desde el archivo JSON
        with open("preguntas.json", "r", encoding="utf-8") as preguntas_file:
            preguntas_data = json.load(preguntas_file)
            preguntas = preguntas_data.get("preguntas", [])

        # Cargar respuestas del estudiante desde el archivo JSON
        with open("respuestas_estudiante.json", "r", encoding="utf-8") as respuestas_file:
            respuestas_data = json.load(respuestas_file)
            respuestas_estudiante = respuestas_data.get("respuestas", [])

        for pregunta, respuesta in zip(preguntas, respuestas_estudiante):
            prompt = f"""
    Dada la siguiente Pregunta y la siguiente Respuesta quiero la Nota del Estudiante (entre 0,0 y 1,0).
    La Nota debe ser solo un número. Tu respuesta debe ser solo la Nota (puntaje, un número), y en Español. También necesito la Nota Final (promedio de las últimas 10 notas en las preguntas).
    Pregunta: {pregunta["pregunta"]}
    Respuesta del Estudiante: {respuesta["respuesta"]}
            """
            answerGrade = get_question_answer("Nota", prompt)
            if answerGrade:
                save_question_answer(
                    question=pregunta["pregunta"], answer=respuesta["respuesta"], nota=answerGrade,
                    folder=respuestas_folder, name='resultado_' +
                    clean_question(pregunta["pregunta"])
                )
            else:
                print(f"ERROR: Pregunta sin respuesta: {pregunta}")
