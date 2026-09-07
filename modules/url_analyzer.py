from urllib.parse import urlparse
import ipaddress

def parse_url(url):
    url = url.strip()

    if not url:
        return None

    if "://" not in url:
        url = "https://" + url

    parsed = urlparse(url)

    return{
        "scheme":parsed.scheme,
        "hostname":parsed.hostname,
        "port":parsed.port,
        "path":parsed.path
    }

def check_https(url):
    result = parse_url(url)

    if result is None:
        return False

    return result["scheme"] == "https" 

def is_ip_address(url):
    result = parse_url(url)

    if result is None or result["hostname"] is None:
        return False

    try:
        ipaddress.ip_address(result["hostname"])
        return True
    
    except ValueError:
        return False

def has_suspicious_port(url):
    result = parse_url(url)

    if result is None:
        return False

    port = result["port"]

    if port is None:
        return False

    return port not in [80, 443]

def has_at_symbol(url):
    if not url:
        return False

    return "@" in url

def is_url_too_long(url, max_length = 75):
    if not url:
        return False

    return len(url) > max_length

def analyze_url(url):
    parsed = parse_url(url)

    if parsed is None:
        return None

    return{
        "url":url,
        "scheme":parsed["scheme"],
        "hostname":parsed["hostname"],
        "port":parsed["port"],
        "path":parsed["path"],
        "uses_https":check_https(url),
        "uses_ip_address":is_ip_address(url),
        "suspicious_port":has_suspicious_port(url),
        "has_at_symbol":has_at_symbol(url),
        "too_long":is_url_too_long(url),
        "risk_score":calculate_risk_score(url),
        "risk_level":get_risk_level(url)
    }

def calculate_risk_score(url):
    if parse_url(url) is None:
        return None

    score = 0

    if not check_https(url):
        score = score + 1

    if is_ip_address(url):
        score = score + 2

    if has_suspicious_port(url):
        score = score + 1

    if has_at_symbol(url):
        score = score + 2

    if is_url_too_long(url):
        score = score + 1

    return score

def get_risk_level(url):
    result = calculate_risk_score(url)

    if result is None:
        return "Invalid"

    if result <= 1:
        return "Low"

    elif result <= 3:
        return "Medium"

    else:
        return "High"