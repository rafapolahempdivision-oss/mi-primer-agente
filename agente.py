from google import genai

client = genai.Client(api_key="AQ.Ab8RN6LeTuxe52KmwhBv0NkvzaEhga6l9eZj0TJkJX5J2jB5Gg")

print("¡Hola! Soy tu agente inicial en la nube.")
print("¿Qué tarea quieres que analice o resuelva hoy?")

prompt = "Preséntate y dime 3 ideas sencillas para generar ingresos usando automatización."

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt,
)

print("\n--- Respuesta del Agente ---")
print(response.text)
