import socket
import sys

def escanear_puertos(ip_objetivo, puertos):
    print(f"\n--- Starting scan : {ip_objetivo} ---\n")
    
    for puerto in puertos:
        # Crear un objeto socket
        # AF_INET = IPv4, SOCK_STREAM = TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) # Esperar máximo 1 segundo por respuesta
        
        try:
            # Intentar conectar (devuelve 0 si tiene éxito)
            resultado = s.connect_ex((ip_objetivo, puerto))
            
            if resultado == 0:
                print(f"[+] Port {puerto}: OPEN")
                
                # Intentar obtener el banner (servicio)
                try:
                    s.send(b'HEAD / HTTP/1.0\r\n\r\n') # Enviar datos basura para provocar respuesta
                    banner = s.recv(1024).decode().strip()
                    if banner:
                        print(f"    |_ Service is up (Banner): {banner[:50]}...") # Mostrar primeros 50 caracteres
                except:
                    print("    |_ Could not retrieve banner.")
            else:
                # Opcional: imprimir puertos cerrados
                pass
                
        except KeyboardInterrupt:
            print("\nScan stopped by user.")
            sys.exit()
        except Exception as e:
            print(f"Error scanning port {puerto}: {e}")
        finally:
            s.close()

if __name__ == "__main__":
    escanear_puertos()
    # Lista de puertos comunes a escanear
    # 21: FTP, 22: SSH, 80: HTTP, 443: HTTPS, 3306: MySQL, etc.
    
