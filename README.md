# 🔍 **Web Technology & IP OSINT Toolkit**

Una herramienta completa de código abierto para análisis de tecnologías web e investigación OSINT de direcciones IP.

## 🌟 **Características Destacadas**

### 🕵️ **Detección de Tecnologías Web**
- **CMS**: WordPress, Joomla, Drupal, Shopify, Magento
- **Frameworks**: React, Angular, Vue.js, Django, Flask
- **Servidores**: Apache, Nginx, IIS, Cloudflare
- **Herramientas**: Google Analytics, CDNs, APIs, Librerías JS

### 🌐 **Investigación OSINT de IP**
- **Geolocalización**: País, ciudad, coordenadas, ISP
- **Escaneo de Puertos**: Detección de servicios activos
- **Información de Red**: WHOIS, DNS, ASN, hostname
- **Búsqueda en Bases de Datos**: Shodan, VirusTotal (con API)

### **Prerrequisitos**
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### 🚀**Clonar e Instalar**
```bash
# Clonar repositorio
git clone https://github.com/lrondan/TKCs.git
cd TKCs

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
```

### **Instalación en Windows**
```powershell
# PowerShell como administrador
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### **Instalación en Linux/Mac**
```bash
# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip3 install -r requirements.txt

# Dar permisos de ejecución
chmod +x *.py
```
## 🛡️ **Consideraciones de Seguridad y Ética**

### **Usos Permitidos**
- ✅ Auditorías de seguridad autorizadas
- ✅ Análisis de infraestructura propia
- ✅ Investigación académica
- ✅ Pruebas de penetración con permiso

### **Usos Prohibidos**
- ❌ Ataques no autorizados
- ❌ Violación de privacidad
- ❌ Espionaje industrial
- ❌ Ciberacoso


## 📄 **Licencia**
Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.
