
import sys

if len(sys.argv) == 3:
    contacto = sys.argv[1] # Guardamos string
    recompensa = int (sys.argv[2]) # Guardamos int

    print(f"Nuevo contrato recibido de:  {contacto}")
    print(f"Recompensa: {recompensa} eddies")

    if recompensa >= 5000:
        print ("Nivel de riesgo: ALTO")
    elif recompensa >= 1000:
        print ("Nivel de riesgo: MEDIO")
    else:
        print("Nivel de riesgo: BAJO")

else:
    print("Error - Faltan datos del contrato")
    



    
