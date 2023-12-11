# CONVERSOR DE SEG EM HORAS MINUTOS E SEGUNDOS

segundos_str = input("DIGITE O NUMERO DE SEGUNDOS QUE QUER CONVERTER: ")
total_segs = int(segundos_str)

horas = total_segs // 3600
hora_rest = total_segs % 3600
minutos = hora_rest // 60
minutos_rest = hora_rest % 60
segundos = minutos_rest // 60

print(horas,"horas,",minutos,"minutos e ",segundos,"segundos")
