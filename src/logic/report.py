import mysql.connector
import time
import os

def generate_report():
    print("Iniciando generación de reporte...")
    try:
        # Configuración desde variables de entorno
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'db'),
            database=os.getenv('DB_NAME', 'biblioteca_db'),
            user=os.getenv('DB_USER', 'user_donaciones'),
            password=os.getenv('DB_PASS', 'user_password')
        )
        cursor = conn.cursor()
        
        # Consulta para contar total de donaciones
        cursor.execute("SELECT COUNT(*) FROM donaciones")
        count = cursor.fetchone()[0]
        
        # Ruta del archivo en el volumen compartido
        report_path = "/app/reports/reporte.txt"
        
        # Escribir el reporte
        with open(report_path, "w") as f:
            f.write(f"REPORTE DE BIBLIOTECA\n")
            f.write(f"=====================\n")
            f.write(f"Total histórico de libros donados: {count}\n")
            f.write(f"Ultima actualización: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            
        print(f"Reporte generado exitosamente con {count} registros.")
        
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error al generar reporte: {e}")

if __name__ == "__main__":
    # Esperar a que la DB esté lista (simple delay)
    time.sleep(15) 
    while True:
        generate_report()
        # Se genera el reporte cada 60 segundos
        time.sleep(60)
