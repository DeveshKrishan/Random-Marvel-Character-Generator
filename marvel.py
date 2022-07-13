import urllib.parse, hashlib, urllib.request, json

PUBLIC_KEY = "FILL OUT"
PRIVATE_KEY = "FILL OUT"

super_heroes = [
    #These are Marvel characters that have a description to them. In the JSON response, there are many characters that 
    #have empty descriptions. The list contains all characters that have descriptions.
    'Spider-Man (Marvel Zombies)', "Speed", "Spider-Girl (May Parker)", "A-Bomb (HAS)", "Abomination (Emil Blonsky)", 
    "Adam Warlock", "Agent X (Nijo)", "Banshee (Theresa Rourke)", "Baron Mordo (Karl Mordo)", "Battlestar", "Captain America"
    "Captain America/Steve Rogers (MAA)", "Daredevil", "Falcon", "Falcon/Sam Wilson (MAA)", "Fantastic Four", "Ken Ellis",
    "Pete Wisdom", "Talkback (Chase Stein)", "Talos", "Tarantula (Luis Alvarez)", "Taskmaster", "Taurus (Cornelius van Lunt)",
    "Tenebrous", "Terrax", "Terror", "U-Go Girl", "U.S. Agent", "Uatu The Watcher", "Ulik", "Ultimate Spider-Man (USM)",
    "Ultimo", "Ultron", "Umar", "Unicorn", "Union Jack (Brian Falsworth)", "Union Jack (Joseph Chapman)", "Unus", "Yellow Claw",
    "Yellowjacket (Hank Pym)", "Yondu", "X-23", "X-Man", "X-Men", "X-Ray (James Darnell)", "Xorn (Kuan-Yin Xorn)", "Zarek",
    "Zeus", "Zombie (Simon Garth)", "Zuras", "Zzzax" ]

def show_name_desc(name) -> None:
    '''Given a name of a Marvel character, returns the name, description, and image of the character.'''
    url = create_url(name)
    for i in obtain_result(url)['data']['results']:
        if i['thumbnail'] != "":
            return [i['name'], i['description'], i['thumbnail']]

def create_url(name):
    '''Creates the appropiate URL.'''
    ts = "1"
    url = "http://gateway.marvel.com/v1/public/characters?"
    query_parameters = {
        'ts': ts, 
        'name': name,
        'apikey': PUBLIC_KEY,
        'hash': hashlib.md5((ts + PRIVATE_KEY + PUBLIC_KEY).encode('utf-8')).hexdigest()
    }
    return url + urllib.parse.urlencode(query_parameters)

def obtain_result(url: str) -> dict:
    '''Given a URL, this function recieves a JSON response and converts it to a dictionary. If a 
    response is given, the connection is closed.'''
    response = None
    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        json_item = response.read().decode(encoding = 'utf-8')
        return json.loads(json_item)
    finally:
        if response != None:
            response.close()

if __name__ == "__main__":
    show_name_desc()
