import builtwith
import whois

def detectar_tecnologias(url):
    """
    Detect technology's using builtwith
    """
    try:
        tecnologias = builtwith.parse(url)
        
        print(f"Analyzing: {url}")
        print("=" * 50)
        
        for categoria, techs in tecnologias.items():
            print(f"\n{categoria.upper()}:")
            for tech in techs:
                print(f"  - {tech}")
        
        return tecnologias
    except Exception as e:
        print(f"Error: {e}")
        return None

# Ejemplo de uso
if __name__ == "__main__":
    detectar_tecnologias()