 


from googletrans import Translator

def translate_french_words(words):
    """
    Translate a list of French words to English.
    
    Args:
        words (list): List of French words to translate
        
    Returns:
        dict: Dictionary mapping French words to their English translations
    """
    translator = Translator()
    translation_dict = {}
    
    for word in words:
        # Translate from French to English
        translation = translator.translate(word, src='fr', dest='en')
        translation_dict[word] = translation.text
    
    return translation_dict

# Example usage
french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
translated_words = translate_french_words(french_words)
print(translated_words)