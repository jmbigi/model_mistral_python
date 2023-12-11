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


def evalProf(preguntas, respuestas_profesor, respuestas_folder):
    for pregunta, respuesta in zip(preguntas, respuestas_profesor):
        prompt = f"""
    Dada la siguiente Pregunta y la siguiente Respuesta quiero la Nota del Profesor (entre 0,0 y 1,0).
    Respuesta incorrectas, deficientes o sin respuesta vale 0,0.
    Respuesta insuficiente vale 0,3 y 0,4.
    Respuesta aceptable vale 0,5 y 0,7.
    Respuesta excelente vale 0,7 y 1,0.    
    La Nota debe ser solo un número. Tu respuesta debe ser solo la Nota (puntaje, un número), y en Español.
    Pregunta: {pregunta["pregunta"]}
    Respuesta del Profesor: {respuesta["respuesta"]}
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


def evalIA(preguntas, respuestas_folder):
    answers = []
    for pregunta in preguntas:
        prompt = f"""
    Debes responder como Estudiante avanzado, como si fuera una Evaluación, sin preguntas ni comentarios, y en Español.
    En tu respuesta, no debes incluir la palabra Respuesta ni la palabra Pregunta.
    Pregunta: {pregunta["pregunta"]}
            """
        answer = get_question_answer("Pregunta", prompt)
        if answer:
            save_question_answer(
                question=pregunta["pregunta"], answer=answer, nota=1.0,
                folder=respuestas_folder, name='resultado_' +
                clean_question(pregunta["pregunta"])
            )
            answers.append(
                {"question": pregunta["pregunta"], "answer": answer})
        else:
            print(f"ERROR: Pregunta sin respuesta: {pregunta}")

    if len(answers) > 0:
        answer_filename = os.path.join(
            os.path.dirname(respuestas_profesor), 'respuestas_ia' + ".json")
        with open(answer_filename, "w", encoding="utf-8") as f:
            json.dump(answers,
                      f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    for i in range(100):
        respuestas_folder = "respuestas_prof"
        os.makedirs(respuestas_folder, exist_ok=True)

        respuestas_ia_folder = "respuestas_ia"
        os.makedirs(respuestas_ia_folder, exist_ok=True)

        # Cargar preguntas desde el archivo JSON
        with open("preguntas.json", "r", encoding="utf-8") as preguntas_file:
            preguntas_data = json.load(preguntas_file)
            preguntas = preguntas_data.get("preguntas", [])

        # Cargar respuestas del Profesor desde el archivo JSON
        with open("respuestas_profesor.json", "r", encoding="utf-8") as respuestas_file:
            respuestas_data = json.load(respuestas_file)
            respuestas_profesor = respuestas_data.get("respuestas", [])

        # evalProf(preguntas=preguntas, respuestas_profesor=respuestas_profesor, respuestas_folder=respuestas_folder)

        evalIA(preguntas=preguntas, respuestas_folder=respuestas_ia_folder)
