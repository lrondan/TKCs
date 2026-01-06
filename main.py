import sys
import webbrowser
import json
from art import text2art
import requests

def main():
    print("Welcome to TCK Interactive Shell!")
    print(text2art("TCK"))
    print("Type '-h or --help' for a list of commands.")
    print("Structure: tck >> command [options] \n")
    print("Type 'exit' or 'q' to exit or press Ctrl+C.\n")
    mostrar_ayuda()
    
    while True:
        try:
            comando = input("tck >> ").strip().lower()            
            if comando == "exit" or comando == "q":
                print("Good Bye!")
                break
            elif comando == "--help" or comando == "-h":
                mostrar_ayuda()
            elif comando.startswith("geoip -ip"):
                ip_address = comando.split(" ")[2] if len(comando.split(" ")) > 2 else None
                if ip_address:
                    print(f"Opening geolocation for IP: {ip_address}\n")
                    try:
                        url = f"https://ipinfo.io/{ip_address}/json"
                        response = requests.get(url)
                        j = json.loads(response.text)
                        for dato in j:
                            print('GeoLoc',f'{dato} : {j[dato]}')
                    except KeyError:
                        print("Error: Something went wrong!!!!")
                else:
                    print("Please provide an IP address. Usage: geoip -ip <ip_address>")
            elif comando.startswith("domain -d"):
                domain_name = comando.split(" ")[2] if len(comando.split(" ")) > 2 else None
                if domain_name:
                    print(f"Resolving domain: {domain_name}\n")
                    from osint import resolver
                    resolver.main(domain_name)
                else:
                    print("Please provide a domain name. Usage: domain -d <domain_name>")
            elif comando.startswith("portscan -ip"):
                target_ip = comando.split(" ")[2] if len(comando.split(" ")) > 2 else None
                if target_ip:
                    print(f"Starting port scan on IP: {target_ip}\n")
                    from osint import ports
                    ports.escanear_puertos(target_ip, [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3306, 5432,8080])
                else:
                    print("Please provide an IP address. Usage: portscan -ip <ip_address>")
            elif comando.startswith("webtech -url"):
                url = comando.split(" ")[2] if len(comando.split(" ")) > 2 else None
                if url:
                    print(f"Analyzing web technologies for URL: {url}\n")
                    from osint import tech
                    tech.detectar_tecnologias(url)
                else:
                    print("Please provide a website URL. Usage: webtech -url <website_url>")
            elif comando == "":
                continue  # Ignorar entradas vacías
            else:
                print(f"Not registered command : {comando}. Write 'help' to see options.")
                
        except KeyboardInterrupt:  # Captura Ctrl+C
            print("\n\nKeyboard Interrupt detected. ¡Good Bye!")
            sys.exit(0)
        except EOFError:  # Captura Ctrl+D en algunos terminales
            print("\n\nEOF detected. ¡Good Bye!")
            break

def mostrar_ayuda():
    print("Available commands:")
    print("+---------------------------------------------------------------+")
    print("|Name of the command     | Syntax                               |")
    print("|------------------------+--------------------------------------|")
    print("|Ip geolocation tool     | geoip  -ip <ip_address>              |")
    print("|Domain resolver tool    | domain -d <domain_name>              |")
    print("|Port scanner tool       | portscan -ip <ip_address>            |")
    print("|Web technology lookup   | webtech -url <website_url>           |")
    print("|------------------------+--------------------------------------|")
    print("|Shows this help message | --help     -h                        |")
    print("|Exits the application   | exit       q                         |")
    print("+---------------------------------------------------------------+")

if __name__ == "__main__":
    main()