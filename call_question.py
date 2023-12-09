import requests
import json
import os


def get_question_answer(question):
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
        "prompt": question,
        "stream": False
    }
    response = requests.post(url, data=json.dumps(data))
    response_json = response.json()
    if response_json["done"]:
        answer = response_json["response"]
    else:
        answer = None
    return answer


def save_question_answer(question, answer):
    """
    Guarda una pregunta y su respuesta en un archivo.

    Args:
        question: La pregunta a guardar.
        answer: La respuesta a la pregunta.
    """

    question_filename = question.replace(" ", "_") + ".txt"
    with open(question_filename, "w") as f:
        f.write(question + "\n")
        f.write(answer)


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

    # Obtener las respuestas del modelo ollama pythonLearning

    answers = []
    for question in questions:
        answer = get_question_answer(question)
        answers.append(answer)

    # Guardar las preguntas y respuestas

    for question, answer in zip(questions, answers):
        save_question_answer(question, answer)

    print("Las preguntas y respuestas se han guardado correctamente.")
