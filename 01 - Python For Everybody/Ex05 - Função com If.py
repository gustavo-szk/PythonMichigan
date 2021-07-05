def valorPorHora(h,r):
    if h > 40:
        p = 1.5 * r * (h - 40) + (40 *r)
    else:
        p = h * r
    return p

hrs = input("Digite as Horas:")
hr = float(hrs)
rphrs = input("Digite o Valor por Hora:")
rphr = float(rphrs)

p = valorPorHora(hr,rphr)
print('Pague: $',p)