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


def clean_question(question):
    return question.strip().replace("* ", "").strip().replace(" ", "_").replace("¿", "").replace("?", "").replace("\"", ""). replace("/", "_"). replace('"', '').replace("\\\"", "").replace(".", "_").replace("__", "_").strip()


def save_question(question, folder):
    """
    Guarda una pregunta en un archivo JSON en la carpeta especificada.

    Args:
        question: La pregunta a guardar.
        folder: La carpeta en la que se guardará la pregunta.
    """
    question_filename = os.path.join(
        folder, clean_question(question) + ".json")
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
    answer_filename = os.path.join(
        folder, clean_question(question) + ".json")
    with open(answer_filename, "w", encoding="utf-8") as f:
        json.dump({"question": question, "answer": answer},
                  f, ensure_ascii=False, indent=2)


def should_save_generated_question(question):
    """
    Determina si se debe guardar la pregunta generada según ciertos criterios.

    Args:
        question: La pregunta generada.

    Returns:
        True si se debe guardar, False si no.
    """
    # Ejemplo de filtro: No guardar preguntas que contengan las palabras "objetivo" o "evaluación"
    filter1 = "objetivo".lower() not in question.lower(
    ) and "evaluación".lower() not in question.lower() and "evaluation".lower() not in question.lower()
    filter2 = "puedes intentar preguntas".lower() not in question.lower()
    filter3 = "tipo de problema que desea resolver con python".lower() not in question.lower()
    filter4 = "pregunta aleatoria".lower() not in question.lower()
    filter5 = "API de inteligencia artificial".lower() not in question.lower()
    return filter1 and filter2 and filter3 and filter4 and filter5


if __name__ == "__main__":
    # Preguntas y respuestas para las evaluaciones
    questions = [
        "¿Qué es una función en Python?",
        "¿Cómo se define una función en Python?",
        "¿Cómo se llama el parámetro de una función?",
    ]
    questions = []
    questions = [
        "¿Cuál es la función del código en el módulo saludos?",
        "¿Cómo se ejecutan las funciones y métodos de los módulos paquete.hola.saludos y paquete.adios.despedidas en el script script.py?",
        "Menciona tres módulos esenciales de Python según la presentación de la clase.",
        "Describe brevemente la clase Counter del módulo collections. Proporciona un ejemplo de su uso.",
        "Explica la utilidad del módulo datetime y muestra un ejemplo de cómo obtener la fecha y hora actual.",
        "¿Cuál es el propósito del módulo math en Python? Proporciona ejemplos de al menos dos funciones que ofrece.",
        "¿Qué proporciona el módulo random y cómo se puede utilizar para generar contenido aleatorio?",
        "¿Cómo se importan módulos en Python? Proporciona ejemplos de importación simple y con alias.",
        "Explica la diferencia entre módulos y paquetes en Python. Proporciona un ejemplo de cómo se crea un paquete.",
        "Menciona al menos dos librerías ampliamente usadas en Python, describiendo brevemente su propósito.",
    ]
    questToGen = 10
    for i in range(questToGen):
        answerGen = get_question_answer(
            "Petición-pregunta-evaluación", """
            Quiero una (solo una) pregunta aleatoria para una evaluación de los conocimientos de Python del estudiante (no quiero la respuesta a la pregunta en este Prompt, sino la pregunta).
            No responder con: Una pregunta de cómo puedo ayudarte.
            No poner el texto: Por favor, aquí tienes una pregunta aleatoria para una evaluación de Python.
            No poner el texto: ¿Cómo puedo ayudarte con la evaluación de Python?.
            No poner el texto: La pregunta aleatoria para una evaluación de Python es.
            No poner el texto: "Pregunta :". En tu respuesta, no quiero el texto "Pregunta: ", tampoco "Pregunta:".
            No poner el texto: "¿Cómo puedo ayudarte con la evaluación de Python?".
            No poner el texto: "* ".
            No poner el texto: "¿Cuál es el objetivo de tu evaluación de Python?".
            No quiero respuestas del tipo: "¿En qué nivel de conocimiento de Python tienes experiencia?".
            No quiero que respondas con el texto: "¿Cuál es el objetivo de tu evaluación de Python?".
            No quiero que respondas con el texto: "Aquí tienes...".
            Devolver solo la pregunta, ejemplo: ¿Para qué sirve return en una función?.
            De nuevo, ejemplo de pregunta: ¿Para qué sirve return en una función?.
            Solo quiero la pregunta. Quiero que me des una pregunta para un evaluación (prueba) de Python.
            """
        )
        if answerGen is not None:
            answerGen = answerGen.replace("\n", "").replace('"', '')
            if should_save_generated_question(answerGen):
                print("Pregunta generada: ", answerGen)
                questions.append(answerGen)
            else:
                print("Error en la respuesta: ",
                      answerGen, "Se genera reclamo")
                resp_complain = get_question_answer(
                    "Reclamo", "La respuesta: " + answerGen + " \nNo cumple con los requisitos solicitados. No vuelvas a responder eso en este contexto.")

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
        print(question[:20], answer[:20]
              if isinstance(answer, str) else 'None')
        if (answer is not None):
            save_question(question, preguntas_folder)
            save_question_answer(question, answer, respuestas_folder)
        else:
            print("ERROR: Pregunta sin respuesta: " + question)

    print("Las preguntas y respuestas se han guardado correctamente en formato JSON en las carpetas 'preguntas' y 'respuestas'.")
