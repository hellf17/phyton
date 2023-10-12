'''
def extrair_campos_pagina(pdfData):
        texto = pdfData

        campos_desejados = {
            'Hb': r'HEMOGLOBINA \.{3,}: \s+ ([\d.,]+) \s+ g/dL',
            'Ht': r'HEMATÓCRITO \.{3,}: \s+ ([\d.,]+) \s+ %',
            'Leuco': r'LEUCÓCITOS \.{3,}: \s+ ([\d.,]+) \s+ /mm³',
            'Bastões': r'BASTÕES \.{3,}: \s+ ([\d.,]+) \s+ %',
            'Segm': r'SEGMENTADOS \.{3,}: \s+ ([\d.,]+) \s+ %',
            'Plaq': r'PLAQUETAS \.{3,}: \s+ ([\d.,]+) \s+ /mm³',
            'K+': r'POTÁSSIO [\s\S]*?RESULTADO\.{3,}: \s+ ([\d.,]+) \s+ mmol/L',
            'Na+': r'SÓDIO [\s\S]*?RESULTADO\.{3,}: \s+ ([\d.,]+) \s+ mmol/L',
            'Ca+': r'CÁLCIO [\s\S]*?RESULTADO\.{3,}: \s+ ([\d.,]+) \s+ mg/dL',
            'Mg+': r'MAGNÉSIO [\s\S]*?RESULTADO\.{3,}: \s+ ([\d.,]+) \s+ mg/dL',
            'Creat': r'CREATININA [\s\S]*?RESULTADO\.{3,}: \s+ ([\d.,]+) \s+ mg/dL',
            'Ur': r'URÉIA [\s\S]*?RESULTADO\.{3,}: \s+ ([\d.,]+) \s+ mg/dL',
            'PCR': r'PCR [\s\S]*?RESULTADO\.{3,}: \s+ ([\d.,]+) \s+ mg/dL',
            'RNI': r'TAP [\s\S]*?RNI\.{3,}: \s+ ([\d.,]+)',
            'TTPA': r'TTPA [\s\S]*?KPTT\.{3,}: \s+ ([\d.,]+) \s+ Segundos',
            'TGO': r'TGO [\s\S]*?RESULTADO\.{3,}: \s+ ([\d.,]+) \s+ U/L',
            'TGP': r'TGP [\s\S]*?RESULTADO\.{3,}: \s+ ([\d.,]+) \s+ U/L',
            'BT': r'BILIRRUBINA[\s\S]TOTAL\.{3,}: \s+ ([\d.,]+) \s+ mg/dL',
            'BD': r'BILIRRUBINA[\s\S]DIRETA\.{2,}: \s+ ([\d.,]+) \s+ mg/dL',
            'BI': r'BILIRRUBINA[\s\S]INDIRETA: \s+ ([\d.,]+) \s+ mg/dL',
            'GamaGT': r'GAMA [\s\S]*?: \s+ ([\d.,]+) \s +U/L',
            'FosfAlc': r'FOSFATASE [\s\S]*?: \s+ ([\d.,]+) \s+ U/L',
            'Amilase': r'AMILASE [\s\S]*?RESULTADO\.{3,}: \s+ ([\d.,]+) \s+ U/L',
            'Lipase': r'LIPASE [\s\S]*?RESULTADO\.{3,}: \s+ ([\d.,]+) \s+ U/L',
            'BNP': r'BNP [\s\S]*?: \s+ ([\d.,]+) \s+ pg/mL',
            'CK-MB': r'CK-MB [\s\S]*?RESULTADO\.{3,}: \s+ ([\d.,]+) \s+ U/L',
            'Tropo': r'TROPONINA [\s\S]*?RESULTADO\.{3,}: \s+ (.*?) \s+ ng/mL',
            'DengueIgM': r'DENGUE [\s\S]*? IgM [\s\S]*?: \s (Negativo|Positivo)',
            'DengueIgG': r'DENGUE [\s\S]*? IgG [\s\S]*?: \s (Negativo|Positivo)',
            'NS1': r'DENGUE [\s\S]*? NS1 [\s\S]*?: \s (Negativo|Positivo)',
            'Glicose jejum': r'GLICOSE[\s\S]*?JEJUM[\s\S]*?RESULTADO\.{3,}: \s+ ([\d.,]+) \s+ mg/dL',
            'HbA1c': r'Hb[\s\S]*?A1c[\s\S]*?: \s+ ([\d.,]+) \s+ %',
            'LDH': r'LDH[\s\S]*?: \s+ ([\d.,]+) \s+ U/L',
            'Proteinuria': r'PARCIAL[\s\S]DE[\s\S]URINA[\s\S]*?PROTEÍNAS[\s\S]*?(Ausente|\++)',
            'Cetonuria': r'PARCIAL[\s\S]DE[\s\S]URINA[\s\S]*?CORPOS[\s\S]CETÔNICOS\.+:\s*(Ausente|\++)',
            'Nitrito': r'PARCIAL[\s\S]DE[\s\S]URINA[\s\S]*?NITRITO\.+:\s*(Negativo|Positivo)',
            'Leucocituria': r'PARCIAL[\s\S]*?DE[\s\S]*?URINA[\s\S]*?LEUCÓCITOS\.+:\s*(([\d.,]+)-([\d.,]+))\s+P\/CAMPO',
            'Hematuria': r'PARCIAL[\s\S]DE[\s\S]URINA[\s\S]*?HEMÁCIAS\.+:\s*(([\d.,]+)-([\d.,]+))\s+P\/CAMPO',
            'Leveduras': r'PARCIAL[\s\S]DE[\s\S]URINA[\s\S]*?LEVEDURAS\.+:\s*(\w+)\s',
            'Bacteriuria': r'PARCIAL[\s\S]DE[\s\S]URINA[\s\S]*?BACTÉRIAS\.+:\s*(([A-Z][a-z]+))',
            'pH': r'GASOMETRIA[\s\S]*?pH\.{1,}: \s+ ([\d.,]{4})',
            'pCO2': r'GASOMETRIA[\s\S]*?pCO2[\.{1,}]?: \s+ ([\d.,]+) \s mmHg',
            'pO2': r'GASOMETRIA[\s\S]*?pO2\.{1,}: \s+ ([\d.,]+) \s mmHg',
            'HCO3-': r'GASOMETRIA[\s\S]*?HCO3[\s\S]act\.{1,}: \s+ ([\d.,]+) \s mmol/L',
            'SpO2': r'GASOMETRIA[\s\S]*?SATURAÇÃO[\s\S]DE[\s\S]O2\.{1,}: \s+ ([\d.,]+) \s %',

        }
        dados_extraidos = {}

        for campo, padrao in campos_desejados.items():
            correspondencia = re.search(padrao, texto, re.VERBOSE)
            if correspondencia:
                valor = correspondencia.group(1).strip()
                dados_extraidos[campo] = valor

        return dados_extraidos


try:
    dados_extraidos = {}

    resultados = []
    dados_extraidos['Nome'] = nome
    dados_extraidos['Identificador'] = identificador
    dados_extraidos['Data'] = data
    dados_extraidos['Hora'] = hora
    resultados.append(f"Nome: {nome}")
    resultados.append(f"Identificador: {identificador}")
    resultados.append(f"Data: {data}")
    resultados.append(f"Hora: {hora}")

    total_paginas = len(leitor.pages)

    for numero_da_pagina in range(total_paginas):
    dados_extraidos = extrair_campos_pagina(pdf_path, numero_da_pagina + 1)

    eas_fields_present = any(
        campo in dados_extraidos
        for campo in
        ['Proteinuria', 'Cetonuria', 'Nitrito', 'Leucocituria', 'Hematuria', 'Leveduras', 'Bacteriuria']
    )

    gaso_fields_present = any(
        campo in dados_extraidos
        for campo in
        ['pH', 'pCO2', 'pO2', 'HCO3-', 'SpO2']
    )

    if eas_fields_present:
        resultados.append('EAS:')
        for campo, valor in dados_extraidos.items():
            
            if campo in ['Proteinuria', 'Cetonuria', 'Nitrito', 'Leucocituria', 'Hematuria', 'Leveduras',
                        'Bacteriuria']:
                resultados.append(f'  {campo}: {valor}')

            else:
                resultados.append(f'{campo}: {valor}')
    else:
        if gaso_fields_present:
            resultados.append('Gasometria:')
            for campo, valor in dados_extraidos.items():
                if campo in ['pH', 'pCO2', 'pO2', 'HCO3-', 'SpO2']:
                    resultados.append(f'  {campo}: {valor}')

        else:
            for campo, valor in dados_extraidos.items():
                resultados.append(f'{campo}: {valor}')

    resultados_texto = '\n'.join(resultados)
    print(resultados_texto)

except Exception as e:
    print(f"Error: Contate o suporte {e}")
    input("Aperte enter para sair...")
'''
