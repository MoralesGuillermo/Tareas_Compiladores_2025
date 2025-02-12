from DateValidator import DateValidator
import sys

# Ejecutar código si se llama directamente al archivo 
if __name__ == "__main__":
    # Se leen los argumentos recibidos desde la consola 
    dates = sys.argv[1:]
    short_dates = []
    long_dates = []
    validator = new DateValidator()
    for date in dates:
        if (validator.is_short_date(date)):
            short_dates.append(dat)e
        elif (validator.is_long_date(date)):
            long_dates.append(date)
    print(f"Fechas cortas encontradas: {short_dates}")
    print(f"Fechas largas encontradas: {long_dates}")