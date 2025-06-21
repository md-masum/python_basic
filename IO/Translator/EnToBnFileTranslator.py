from argostranslate import package, translate

# Step 1: Check if en→bn is installed
def is_model_installed(from_code="en", to_code="bn"):
    translate.load_installed_languages()
    installed_languages = translate.get_installed_languages()

    from_lang = next((lang for lang in installed_languages if lang.code == from_code), None)
    to_lang = next((lang for lang in installed_languages if lang.code == to_code), None)

    if from_lang and to_lang:
        try:
            _ = from_lang.get_translation(to_lang)
            return True
        except Exception:
            return False
    return False

# Step 2: Download and install if not present
def ensure_model_installed(from_code="en", to_code="bn"):
    if not is_model_installed(from_code, to_code):
        print("🔄 Translation model not found, downloading...")
        package.update_package_index()
        available_packages = package.get_available_packages()
        for pkg in available_packages:
            if pkg.from_code == from_code and pkg.to_code == to_code:
                download_path = pkg.download()
                package.install_from_path(download_path)
                print("✅ Model installed successfully.")
                return
        raise Exception("❌ English to Bangla model not found in Argos package index.")
    else:
        print("✅ English to Bangla model already installed.")

# Step 3: Load translation model
def get_translator(from_code="en", to_code="bn"):
    translate.load_installed_languages()
    from_lang = next(lang for lang in translate.get_installed_languages() if lang.code == from_code)
    to_lang = next(lang for lang in translate.get_installed_languages() if lang.code == to_code)
    return from_lang.get_translation(to_lang)

# Step 4: File translate function
def translate_file(input_file="SourceFile.txt", output_file="DestinationFile.txt"):
    # Ensure model is ready
    ensure_model_installed("en", "bn")

    # Get translator
    translator = get_translator("en", "bn")

    # Read input
    with open(input_file, "r", encoding="utf-8") as infile:
        source_text = infile.read()

    # Translate
    translated_text = translator.translate(source_text)

    # Save output
    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.write(translated_text)

    print(f"✅ Translation completed and saved to '{output_file}'.")

# Run the function
if __name__ == "__main__":
    translate_file()
