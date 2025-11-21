def get_at_content(dna, sig_figs=2):
    """
    Calcula el contenido AT de una secuencia de ADN,
    redondeando a un número específico de cifras decimales.
    Parámetros:
    dna (str): Secuencia de ADN (ej. 'ATGCGC')
    sig_figs (int, opcional): número de cifras decimales (por defecto = 2)
    Retorna:
    float: contenido AT redondeado
    """
    dna = dna.upper()
    length = len(dna)
    a = dna.count('A')
    t = dna.count('T')
    at_content = (a + t) / length
    return round(at_content, sig_figs)