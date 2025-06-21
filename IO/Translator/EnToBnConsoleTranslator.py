from EnToBnFileTranslator import ensure_model_installed, get_translator

print('Please enter English text:')
input_text = input()

ensure_model_installed("en", "bn")
translator = get_translator("en", "bn")
translated_text = translator.translate(input_text)
print(f"✅ Translation completed: ('{translated_text}').")
