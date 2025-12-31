import sys
import webbrowser
import json

def main():
    print("Welcome to TCK Interactive Shell!")
    print("""
  TTTTTT   CCC    K   K
    TT    C   C   K  K
    TT    C       K K
    TT    C       KK
    TT    C       K K
    TT    C   C   K  K
    TT     CCC    K   K
    """)
    print("Type '-h or --help' for a list of commands.")
    print("Structure: tck >> command [options] \n")
    print("Type 'exit' to exit or press Ctrl+C.\n")
    
    while True:
        try:
            comando = input("tck >> ").strip().lower()  # Prompt personalizado
            
            if comando == "exit":
                print("Good Bye!")
                break
            elif comando == "--help" or comando == "-h":
                mostrar_ayuda()
            elif comando.startswith("generate --fakeid") or comando.startswith("generate -f"):
                country_code = comando.split(" ")[2] if len(comando.split(" ")) > 2 else None
                if country_code == "us":
                    print("Generating fake ID for the United States...\n")
                    from fakeid import fkid_usa
                    fkid_usa.main(value=None)
                elif country_code == "uk":
                    print("Generating fake ID for the United Kingdom...\n")
                    from fakeid import fkid_uk
                    fkid_uk.main(value=None)
            elif comando.startswith("geoip -ip"):
                ip_address = comando.split(" ")[2] if len(comando.split(" ")) > 2 else None
                if ip_address:
                    print(f"Opening geolocation for IP: {ip_address}\n")
                    try:
                        url = f"https://ipinfo.io/{ip_address}/json"
                        # webbrowser.open(url)
                        j = json.loads(webbrowser.open(url).read())
                        for dato in j:
                            print('GeoLoc',f'{dato} : {j[dato]}')
                    except KeyError:
                        print("Error: Ha ocurrido algun error!!!!")
                else:
                    print("Please provide an IP address. Usage: geoip -ip <ip_address>")
            elif comando == "":
                continue  # Ignorar entradas vacías
            else:
                print(f"Comando no reconocido: {comando}. Escribe 'help' para ver opciones.")
                
        except KeyboardInterrupt:  # Captura Ctrl+C
            print("\n\nInterrupción detectada. ¡Hasta luego!")
            sys.exit(0)
        except EOFError:  # Captura Ctrl+D en algunos terminales
            print("\n\nFin de entrada. Saliendo.")
            break

def mostrar_ayuda():
    print("Available commands:")
    print("------------------------------------------------------------")
    print("Name of the command     | Syntax")
    print("Generates a fake ID     | generate --fakeid <country_code>")
    print("                                -f <country_code>")
    print("Ip geolocation tool     | geoip -ip <ip_address>")
    print("Shows this help message | --help     -h")
    print("Exits the application    exit")

if __name__ == "__main__":
    main()