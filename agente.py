import os
import google.generativeai as genai

API_KEY = "AQ.Ab8RN6LeTuxe52KmwhBv0NkvzaEhga6l9eZj0TJkJX5J2jB5Gg"

genai.configure(api_key=API_KEY)

# Nota: si usas la librería anterior, mantén 'gemini-1.5-flash' que es el nombre que reconoce internamente
model = genai.GenerativeModel('gemini-1.5-flash')

print("¡Hola! Soy tu agente inicial en la nube.")
print("¿Qué tarea quieres que analice o resuelva hoy?")

prompt = "Preséntate y dime 3 ideas sencillas para generar ingresos usando automatización."

response = model.generate_content(prompt)

print("\n--- Respuesta del Agente ---")
print(response.text)
