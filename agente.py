import os
import google.generativeai as genai

# Aquí pegas tu llave de API entre las comillas que sacaste en el Paso 1
API_KEY = "AQ.Ab8RN6IuxfDRRhhd29xF7QNjMdYqc90yTXXQqOXZD4niWoRJWwI"

genai.configure(api_key=API_KEY)

# Usamos un modelo gratuito y rápido de Gemini
model = genai.GenerativeModel('gemini-1.5-flash')

print("¡Hola! Soy tu agente inicial en la nube.")
print("¿Qué tarea quieres que analice o resuelva hoy?")

# Ejemplo de una pregunta o tarea inicial para el agente
prompt = "Preséntate y dime 3 ideas sencillas para generar ingresos usando automatización."

response = model.generate_content(prompt)

print("\n--- Respuesta del Agente ---")
print(response.text)
