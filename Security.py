import ssl
import socket
from datetime import datetime
import requests


def get_ssl_expiry(domain):
    """Получает дату окончания SSL-сертификата для домена"""
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=domain)
    conn.settimeout(3.0)
    
    try:
        conn.connect((domain, 443))
        ssl_info = conn.getpeercert()
        expiry_date = datetime.strptime(ssl_info['notAfter'], '%b %d %H:%M:%S %Y %Z')
        return expiry_date
    except Exception as e:
        return f"Error: {e}"

def check_https(domain):
    """Проверяет, доступен ли сайт по HTTPS и проверяет наличие редиректа с HTTP на HTTPS"""
    try:
        response = requests.get(f'https://{domain}', timeout=5)
        if response.status_code == 200:
            return True
    except requests.exceptions.RequestException:
        pass
    return False

def run_security_checks(domain):
    """Запускает все проверки для домена"""
    ssl_expiry = get_ssl_expiry(domain)
    https_enabled = check_https(domain)

    results = {
        "domain": domain,
        "ssl_expiry": ssl_expiry,
        "https_enabled": https_enabled
    }
    return results


