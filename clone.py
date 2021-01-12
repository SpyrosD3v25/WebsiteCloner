import urllib.request

def clone(url):
    response = urllib.request.urlopen(url)
    html = response.read()

    print (html.decode())

    return html.decode()
    
html = clone("https://github.com/SpyrosD3v25/Port-Scanner")
