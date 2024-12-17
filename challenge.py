import time
import logging
import bisect

# Configuro el logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Cotizador:

    def __init__(self):
        self.data = {}  

    def actualizar_cotizacion(self, name, source, buy, sell, timestamp):
        
        # Valido datos
        if not isinstance(name, str) or not isinstance(source, str):
            logging.warning("Nombre o fuente inválidos")
            return
        if not (isinstance(buy, (int, float)) and isinstance(sell, (int, float)) and isinstance(timestamp, int)):
            logging.warning("Datos inválidos")
            return

        
        clave = (name, source)
        if clave not in self.data:
            self.data[clave] = []  

        # Inserto la cotización en orden
        bisect.insort(self.data[clave], {"buy": buy, "sell": sell, "timestamp": timestamp}, key=lambda x: x["timestamp"])

        logging.info(f"Actualizado: {name} ({source}) - Buy: {buy}, Sell: {sell}")

    def imprimir_ultima_cotizacion(self):
        print("\n--- Ultimas cotizaciones recibidas por cada empresa---")
        for (n, s), cotizaciones in self.data.items():
            ultimo = cotizaciones[-1] 
            print(f"Name: {n}, Source: {s}, Buy: {ultimo['buy']}, Sell: {ultimo['sell']}")
        print("--------------------------------------\n")


if __name__ == "__main__":
    
    cotizador = Cotizador()

    # Simulo recibir datos cada 5 segundos
    while True :
        print("\n--- Recibo Datos ---")
        
        datos_validacion = [

            # Datos de prueba
            {"name": 123, "buy": 105.22, "sell": 105.59, "timestamp": 1734367423775, "source": "A"},
            {"name": "BMA", "buy": "error", "sell": "error", "timestamp": 1734367423776, "source": "A"},
            {"name": "YPF", "buy": 120.00, "sell": 121.00, "timestamp": "error", "source": "B"},
            {"name": "BMA", "buy": 105.22, "sell": 105.59, "timestamp": 1734367423775, "source": "A"},
            {"name": "BMA", "buy": 105.30, "sell": 105.70, "timestamp": 1734367423773, "source": "A"},
            {"name": "BMA", "buy": 105.40, "sell": 105.80, "timestamp": 1734367423776, "source": "A"}, # ultima cotizacion 
            {"name": "YPF", "buy": 120.00, "sell": 121.00, "timestamp": 1734367423774, "source": "B"},
            {"name": "YPF", "buy": 120.50, "sell": 121.50, "timestamp": 1734367423777, "source": "B"},# ultima cotizacion
            {"name": "YPF", "buy": 120.10, "sell": 121.10, "timestamp": 1734367423776, "source": "B"},
            {"name": "GGAL", "buy": 130.00, "sell": 131.00, "timestamp": 1734367423772, "source": "A"},
            {"name": "GGAL", "buy": 130.50, "sell": 131.50, "timestamp": 1734367423773, "source": "A"},# ultima cotizacion  
            {"name": "GGAL", "buy": 130.25, "sell": 131.25, "timestamp": 1734367423771, "source": "A"}   
        ]

        for dato in datos_validacion:

            cotizador.actualizar_cotizacion(dato["name"], dato["source"], dato["buy"], dato["sell"], dato["timestamp"])

        print("---------------------\n")


        # imprimo luego de actualizar el ultimo
        cotizador.imprimir_ultima_cotizacion()
        time.sleep(5)