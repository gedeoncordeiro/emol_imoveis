def calcular_emolumentos_registro(hectares, consultas, arquivamentos, folhas_acrescidas):
    # Avaliação do imóvel
    valor_avaliacao = hectares * 6000

    # Emolumentos fixos
    detalhes = [
        ("16.1 - Prenotação", 41.24),
        ("16.5 - Desmembramento", 153.63),
        ("16.2 - Abertura de Matrícula", 97.16),
        ("16.22.4 - Averbação de Georreferenciamento", 530.76),
        ("16.22.2 - Averbação deferimento GEO", 127.87),
    ]

    # Tabela para 16.3.x (baseado no valor de avaliação)
    faixas_16_3 = [
        (0, 5680.06, 105.67),
        (5680.07, 7384.08, 133.20),
        (7384.09, 9230.10, 150.81),
        (9230.11, 11537.63, 187.16),
        (11537.64, 14422.04, 232.74),
        (14422.05, 18027.54, 291.81),
        (18027.55, 22534.42, 366.11),
        (22534.43, 28168.01, 458.20),
        (28168.02, 35210.02, 570.63),
        (35210.03, 44012.53, 714.14),
        (44012.54, 55015.63, 893.55),
        (55015.64, 68769.53, 1115.98),
        (68769.54, 85961.94, 1394.94),
        (85961.95, 107452.41, 1743.13),
        (107452.42, 134315.51, 2178.31),
        (134315.52, 167894.37, 2723.40),
        (167894.38, 209867.97, 3404.37),
        (209867.98, 262334.98, 4256.48),
        (262334.99, 327918.71, 5318.68),
        (327918.72, 409898.40, 6649.51),
        (409898.41, 512372.99, 8311.02),
        (512373.00, 640466.24, 10388.89),
        (640466.25, 800582.81, 12986.86),
        (800582.82, 1000728.50, 15420.99),
        (1000728.51, 1250910.66, 16457.60),
        (1250910.67, 1501092.79, 16951.25),
        (1501092.80, 1801311.33, 17459.84),
        (1801311.34, 2161573.60, 17983.68),
        (2161573.61, 2593888.35, 18523.21),
        (2593888.36, 3112666.02, 19078.89),
        (3112666.03, 3735199.22, 19651.18),
        (3735199.23, 4482239.07, 20240.78),
        (4482239.08, 5378686.89, 20847.90),
        (5378686.90, 6454424.25, 21473.41),
        (6454424.26, 7745309.11, 22117.60),
        (7745309.12, float('inf'), 22781.08)
    ]

    # Encontrar valor de 16.3.x
    valor_16_3 = 0
    for faixa in faixas_16_3:
        if faixa[0] <= valor_avaliacao <= faixa[1]:
            valor_16_3 = faixa[2]
            break
    detalhes.append(("16.3.x - Outorga de Título sob o valor", valor_16_3))

    # Emolumentos adicionais fixos
    detalhes.append(("16.22.2 - Averbação de Cláusulas", 127.87))
    detalhes.append(("16.22.2 - Averbação CAR", 127.87))
    detalhes.append(("16.24.4 - Certidão inteiro teor", 96.90))

    # Emolumentos variáveis
    valor_folhas_acrescidas = folhas_acrescidas * 9.64
    valor_consultas = consultas * 6.65
    valor_arquivamentos = arquivamentos * 6.55

    detalhes.append((f"16.24.4.1 - Folhas acrescidas ({folhas_acrescidas} folhas)", valor_folhas_acrescidas))
    detalhes.append((f"16.42 - Consultas públicas ({consultas} consultas)", valor_consultas))
    detalhes.append((f"16.39 - Arquivamentos ({arquivamentos} arquivamentos)", valor_arquivamentos))

    # Total
    total = sum(valor for _, valor in detalhes)

    return valor_avaliacao, detalhes, round(total, 2)

# --- Execução do programa ---
def main():
    try:
        hectares = float(input("Digite a quantidade de hectares: ").replace(",", "."))
        consultas = int(input("Digite a quantidade de consultas de documentos públicos: "))
        arquivamentos = int(input("Digite a quantidade de arquivamentos: "))
        folhas_acrescidas = int(input("Digite a quantidade de folhas acrescidas na certidão de inteiro teor: "))

        valor_avaliacao, detalhes, total_emolumentos = calcular_emolumentos_registro(
            hectares, consultas, arquivamentos, folhas_acrescidas
        )

        print("\n--- Detalhamento dos Emolumentos ---")
        print(f"Avaliação do imóvel: R$ {valor_avaliacao:.2f}\n")
        for nome_ato, valor_ato in detalhes:
            print(f"{nome_ato}: R$ {valor_ato:.2f}")

        print(f"\nTotal dos emolumentos para registro: R$ {total_emolumentos:.2f}")
    except ValueError:
        print("Valor inválido. Certifique-se de digitar números corretamente.")

if __name__ == "__main__":
    main()
