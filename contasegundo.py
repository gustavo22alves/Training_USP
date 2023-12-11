#CONTADOR DE SEGUNDOS

segundos_str = input("DIGITE O NUMERO DE SEGUNDOS QUE QUER CONVERTER: ")
total_segs = int(segundos_str)

dias = total_segs // 86400
dias_rest = total_segs % 86400
horas = dias_rest // 3600
hora_rest = dias_rest % 3600
minutos = hora_rest // 60
minutos_rest = hora_rest % 60
segundos = minutos_rest % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e ",segundos,"segundos")
