import re

def camelcase_to_underscore(text, lower=True):
    text = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', text)
    text = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', text)

    if lower:
        text = text.lower()

    return text

def underscore_to_camelcase(text, capfirst=False):
    text = ''.join(word.capitalize() for word in text.split('_'))

    if not capfirst:
        text = text[0].lower() + text[1:]

    return text

def dot_to_underscore(text, lower=True):
    text = re.sub(r'\b\.+\b', '_', text)
    text = text.replace('.', '')

    if lower:
        text = text.lower()

    return text

def dot_to_camelcase(text, capfirst=False):
    text = dot_to_underscore(text, lower=False)
    text = underscore_to_camelcase(text, capfirst=capfirst)

    return text
