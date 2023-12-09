import requests
import json
import os


def get_question_answer(tipoPrompt, question):
    """
    Realiza una consulta al modelo ollama pythonLearning para obtener una respuesta a una pregunta.

    Args:
        question: La pregunta a la que se quiere obtener una respuesta.

    Returns:
        La respuesta del modelo ollama pythonLearning.
    """

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


def save_question(question, folder):
    """
    Guarda una pregunta en un archivo JSON en la carpeta especificada.

    Args:
        question: La pregunta a guardar.
        folder: La carpeta en la que se guardará la pregunta.
    """
    question_filename = os.path.join(
        folder, question.replace(" ", "_").replace("?", "")  + ".json")
    with open(question_filename, "w", encoding="utf-8") as f:
        json.dump({"question": question}, f, ensure_ascii=False, indent=2)


def save_question_answer(question, answer, folder):
    """
    Guarda una pregunta y su respuesta en un archivo JSON en la carpeta especificada.

    Args:
        question: La pregunta a guardar.
        answer: La respuesta a la pregunta.
        folder: La carpeta en la que se guardará la pregunta con su respuesta.
    """
    save_question(question, folder)
    answer_filename = os.path.join(
        folder, question.replace(" ", "_").replace("?", "") + ".json")
    with open(answer_filename, "w", encoding="utf-8") as f:
        json.dump({"question": question, "answer": answer},
                  f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    # Preguntas y respuestas para las evaluaciones
    questions = [
        "¿Qué es una función en Python?",
        "¿Cómo se define una función en Python?",
        "¿Cómo se llama el parámetro de una función?",
        "¿Qué es el valor de retorno de una función?",
        "¿Cómo se llama la instrucción que llama a una función?",
        "¿Cómo se pueden pasar argumentos a una función?",
        "¿Cómo se pueden devolver valores de una función?",
        "¿Cómo se pueden crear funciones anónimas en Python?",
        "¿Cómo se pueden crear funciones lambda en Python?",
    ]

    # Crear las carpetas si no existen
    preguntas_folder = "preguntas"
    respuestas_folder = "respuestas"
    os.makedirs(preguntas_folder, exist_ok=True)
    os.makedirs(respuestas_folder, exist_ok=True)

    # Obtener las respuestas del modelo ollama pythonLearning
    answers = []
    for question in questions:
        answer = get_question_answer("Pregunta", question)
        answers.append(answer)

    # Guardar las preguntas y respuestas en formato JSON
    for question, answer in zip(questions, answers):
        save_question(question, preguntas_folder)
        save_question_answer(question, answer, respuestas_folder)

    print("Las preguntas y respuestas se han guardado correctamente en formato JSON en las carpetas 'preguntas' y 'respuestas'.")
