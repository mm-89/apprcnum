# phonetic maps based on
# Glossaire des patois de la Suisse romande
# https://portail-gpsr.unine.ch/apex/f?p=101:23:15555252395139::NO:20:::

# some letters are unwriteble (e.g. a with a point above)
# some letter sounds are 'between' something, so
# there is not a precise phonetic for them

# Notes:
#
# Strange signs like  are automatically translate
# into a specific sign. You don't need to comment them.
# Same thind for sound 'between' something

# Commented lines are already checked with epitram to give
# the right results so than you don't need to replace

phonetic = {
    '': '/a̞/',  # Tra "a" e "ò" ????
    '': '/æ/',  # Tra "a" e "è" ????
    'e': '/ə/',   # Vocale media ????
    'ë': '/ɛ̈/',  # Tra "è" e /ə/ ????
    'ə': '/ə/',   # Vocale assordita
    'ì': '/ɪ/',   # Tra "é" e "i"
    'ò': '/ɔ/',   # "o" aperto
    'o': '/o/',    # Vocale media
    'ó': '/o̞/',   # "o" chiuso
    'ö': '/ø/',    # Tra "ò" e /ə/
    '': '/ø̞/',   # Eu aperto (fr. "peur")
    'œ': '/ø/',    # Vocale media
    '': '/y/',    # Eu chiuso (fr. "peu")
    'ou': '/u/',    # Come in francese
    '': '/o̞/',   # Tra "ó" e "ou"
    '': '/u̞/',   # Tra "ou" e "u"
    '': '/w/',    # Semivocale (fr. "ouate")
    'ù': '/ʏ/',    # Tra "œ́" e "u"
    '': '/j/',    # Semivocale (fr. "tuile")
    'ai': '/ɛɪ/',   # Diphthongue decrescente
    'éi': '/ɛɪ/',
    'ao': '/aʊ/',
    'aou': '/aʊ/',
    'iə': '/ɪə/',
    'aïn': '/ɛ̃/',  # Vocale nasale
    'aon': '/ãʊ̃/',
    'eïn': '/ɛ̃/',
    'in': '/ɛ̃/',
    'ïn': '/ĩ̃/',
    'oun': '/ũ/',
    'un': '/œ̃/',
    'ün': '/ʏ̃/',
    'X': '/ɑ̃/',   # Vocale accentuata ????
    '': '/ɛ̃/',   # Vocale accentuata
    'ă': '/a/',     # Vocale breve
    'ĕ': '/ɛ/',     # Vocale breve
    'ā': '/aː/',    # Vocale lunga
    'ē': '/eː/',    # Vocale lunga
    'b': '/b/',     # Consonante "b"
#    'ch': '/ʃ/',    # Come in francese
#    'd': '/d/',     # Come in francese
#    'f': '/f/',     # Come in francese
#    'j': '/ʒ/',     # Come in francese
#    'k': '/k/',     # Come in francese
#    'l': '/l/',     # Come in francese
#    'm': '/m/',     # Come in francese
#    'n': '/n/',     # Come in francese
#    'p': '/p/',     # Come in francese
#    'r': '/ʁ/',     # Come in francese (uvulare)
#    't': '/t/',     # Come in francese
#    'v': '/v/',     # Come in francese
#    'z': '/z/',     # Come in francese
#    'dj': '/dʒ/',   # Come in italiano
#    'dz': '/dz/',   # Come in italiano
    'g': '/g/',     # Sempre occlusiva (fr. "gai")
    'h': '/h/',     # Come in tedesco (fr. "Hund")
    'ḥ': '/χ/',     # Come in tedesco (fr. "ich")
    'ḣ': '/ʁ/',     # Come in tedesco (fr. "ach")
    '': '/ʁ/',     # L velare
    'ly': '/ʎ/',    # L mouillé
    'ṅ': '/ŋ/',     # Come in tedesco (fr. "eng")
    'ny': '/ɲ/',    # N mouillé
    's': '/s/',     # Sempre sorda
    'ṣ': '/θ/',     # Come in inglese (es. "thing")
    '': '/ʎ̞/',    # Tra /ṣ/ e /ly/
#    'tch': '/tʃ/',  # Come in italiano (es. "cento")
#    'ts': '/ts/',   # Come in tedesco (es. "Zeit")
    'y': '/j/',     # Semivocale (fr. "yeux")
    'ẓ': '/ð/',     # Come in inglese (es. "father")
#    '': '/ʁ̞/',    # Tra /ẓ/ e /ly/
#    '': '/ː/',     # Consonanti prolungate
#    '': '/ː/',     # Consonanti prolungate
}
