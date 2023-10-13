from os import system, listdir, path, remove
from colorama import init, Fore, Style
from urllib.request import urlopen
from shutil import copyfileobj
from subprocess import call
from tqdm.auto import tqdm
from requests import get
from time import sleep
from json import loads
from art import tprint


ram = 4

forgev = {
    "versions": {
        "1.20.2": "https://maven.minecraftforge.net/net/minecraftforge/forge/1.20.2-48.0.26/forge-1.20.2-48.0.26-installer.jar",
        '1.20.1': 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.20.1-47.1.0/forge-1.20.1-47.1.0-installer.jar', 
         '1.20': 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.20-46.0.14/forge-1.20-46.0.14-installer.jar', 
         '1.19.4': 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.19.4-45.1.0/forge-1.19.4-45.1.0-installer.jar', 
         '1.19.3': 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.19.3-44.1.0/forge-1.19.3-44.1.0-installer.jar', 
         '1.19.2': 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.19.2-43.2.0/forge-1.19.2-43.2.0-installer.jar', 
         '1.19.1': 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.19.1-42.0.9/forge-1.19.1-42.0.9-installer.jar', 
         '1.19': 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.19-41.1.0/forge-1.19-41.1.0-installer.jar', 
         '1.18.2': 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.18.2-40.2.0/forge-1.18.2-40.2.0-installer.jar', 
         '1.18.1': 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.18.1-39.1.0/forge-1.18.1-39.1.0-installer.jar', 
         '1.18': 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.18-38.0.17/forge-1.18-38.0.17-installer.jar', 
         '1.17.1': 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.17.1-37.1.1/forge-1.17.1-37.1.1-installer.jar', 
         '1.16.5': 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.16.5-36.2.34/forge-1.16.5-36.2.34-installer.jar', 
         '1.16.4': 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.16.4-35.1.4/forge-1.16.4-35.1.4-installer.jar', 
         '1.16.3': 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.16.3-34.1.0/forge-1.16.3-34.1.0-installer.jar', 
         '1.16.2': 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.16.2-33.0.61/forge-1.16.2-33.0.61-installer.jar', 
         '1.16.1': 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.16.1-32.0.108/forge-1.16.1-32.0.108-installer.jar', 
         '1.15.2': 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.15.2-31.2.57/forge-1.15.2-31.2.57-installer.jar', 
         '1.15.1': 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.15.1-30.0.51/forge-1.15.1-30.0.51-installer.jar', 
         '1.15': 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.15-29.0.4/forge-1.15-29.0.4-installer.jar', 
         '1.14.4': 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.14.4-28.2.26/forge-1.14.4-28.2.26-installer.jar', 
         '1.14.3': 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.14.3-27.0.60/forge-1.14.3-27.0.60-installer.jar', 
         '1.14.2': 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.14.2-36.0.63/forge-1.14.2-36.0.63-installer.jar', 
         '1.13.2': 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.13.2-25.0.223/forge-1.13.2-25.0.223-installer.jar', 
         '1.12.2': 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.12.2-14.23.5.2859/forge-1.12.2-14.23.5.2859-installer.jar'
    }
}

paperv = {
    "versions": {
        "1.20.2": "https://api.papermc.io/v2/projects/paper/versions/1.20.2/builds/234/downloads/paper-1.20.2-234.jar",
        "1.20.1": "https://api.papermc.io/v2/projects/paper/versions/1.20.1/builds/172/downloads/paper-1.20.1-172.jar",
        "1.20": "https://api.papermc.io/v2/projects/paper/versions/1.20/builds/17/downloads/paper-1.20-17.jar",
        "1.19.4": "https://api.papermc.io/v2/projects/paper/versions/1.19.4/builds/550/downloads/paper-1.19.4-550.jar",
        "1.19.3": "https://api.papermc.io/v2/projects/paper/versions/1.19.3/builds/448/downloads/paper-1.19.3-448.jar",
        "1.19.2": "https://api.papermc.io/v2/projects/paper/versions/1.19.2/builds/307/downloads/paper-1.19.2-307.jar",
        "1.19.1": "https://api.papermc.io/v2/projects/paper/versions/1.19.1/builds/111/downloads/paper-1.19.1-111.jar",
        "1.19": "https://api.papermc.io/v2/projects/paper/versions/1.19/builds/81/downloads/paper-1.19-81.jar",
        "1.18.2": "https://api.papermc.io/v2/projects/paper/versions/1.18.2/builds/388/downloads/paper-1.18.2-388.jar",
        "1.18.1": "https://api.papermc.io/v2/projects/paper/versions/1.18.1/builds/216/downloads/paper-1.18.1-216.jar",
        "1.18": "https://api.papermc.io/v2/projects/paper/versions/1.18/builds/66/downloads/paper-1.18-66.jar",
        "1.17.1": "https://api.papermc.io/v2/projects/paper/versions/1.17.1/builds/411/downloads/paper-1.17.1-411.jar",
        "1.17": "https://api.papermc.io/v2/projects/paper/versions/1.17/builds/79/downloads/paper-1.17-79.jar",
        "1.16.5": "https://api.papermc.io/v2/projects/paper/versions/1.16.5/builds/794/downloads/paper-1.16.5-794.jar",
        "1.16.4": "https://api.papermc.io/v2/projects/paper/versions/1.16.4/builds/416/downloads/paper-1.16.4-416.jar",
        "1.16.3": "https://api.papermc.io/v2/projects/paper/versions/1.16.3/builds/253/downloads/paper-1.16.3-253.jar",
        "1.16.2": "https://api.papermc.io/v2/projects/paper/versions/1.16.2/builds/189/downloads/paper-1.16.2-189.jar",
        "1.16.1": "https://api.papermc.io/v2/projects/paper/versions/1.16.1/builds/138/downloads/paper-1.16.1-138.jar",
        "1.15.2": "https://api.papermc.io/v2/projects/paper/versions/1.15.2/builds/393/downloads/paper-1.15.2-393.jar",
        "1.14.4": "https://api.papermc.io/v2/projects/paper/versions/1.14.4/builds/245/downloads/paper-1.14.4-245.jar",
        "1.13.2": "https://api.papermc.io/v2/projects/paper/versions/1.13.2/builds/657/downloads/paper-1.13.2-657.jar",
        "1.12.2": "https://api.papermc.io/v2/projects/paper/versions/1.12.2/builds/1620/downloads/paper-1.12.2-1620.jar",
    }
}

init()


def setupServer():
    print(f"{Fore.CYAN}Running server setup...{Style.RESET_ALL}")
    call("run.bat")
    with open("eula.txt","w") as f:
        f.write("eula=true")
    input(f"{Fore.CYAN}Start server by running file run.bat, you can now delete main.py and setup.py\nEnter to remove main.py and exit setup... {Style.RESET_ALL}")
    remove("main.py")
    exit()

def setup():
    system("cls")
    print(Fore.CYAN)
    tprint("Settings")
    sleep(.1)
    print(Style.RESET_ALL,"\n")
    passed = None
    global ram
    while True:
        print(f"{Fore.GREEN}Choose the amount of ram your server can use. Between 1 and 64. default=4{Style.RESET_ALL}")
        i = input(f"{Fore.CYAN}Server_ram{Style.RESET_ALL}=")
        try:
            i = int(i)
            if i > 0 and i < 65:
                passed = True
        except:
            print(f"n{Fore.RED}Not a valid number{Style.RESET_ALL}")
            passed = False
        
        if passed:
            ram = i
            break
        else:
            print(f"{Fore.RED}Not a valid number{Style.RESET_ALL}")

    while True:
        i = input(f"""
{Fore.CYAN}What type of server do you want?{Style.RESET_ALL}

{Fore.CYAN}[0] {Fore.GREEN}Vanilla
{Fore.CYAN}[1] {Fore.GREEN}Plugins(PaperMC)
{Fore.CYAN}[2] {Fore.GREEN}Modded(Forge)
{Style.RESET_ALL}
""")
        try:
            i = int(i)
            if i >= 0 and i <=3:
                break
            else:
                print(f"{Fore.RED}Not a valid number{Style.RESET_ALL}")
        except:
            print(f"{Fore.RED}Not a valid number{Style.RESET_ALL}")

    while True:
        match i:
            case 0:
                vanilla()
                break
            case 1:
                paper()
                break
            case 2:
                forge()
                break
            case _:
                print(f"{Fore.RED}Invalid server type{Style.RESET_ALL}")
                    


def download(url):
    with get(url, stream=True) as r:
        total_length = int(r.headers.get("Content-Length"))
        print("\n")
        with tqdm.wrapattr(r.raw, "read", total=total_length, desc=f"{Fore.CYAN}Downloading server.jar...{Fore.BLUE}", )as raw:
            with open("server.jar", 'wb') as output:
                copyfileobj(raw, output)
        print(Style.RESET_ALL)

    with open("run.bat","w") as f:
        text = f"java -Xmx{ram}G -jar server.jar nogui"
        f.writelines(text)
    
    i = input(f"{Fore.CYAN}Run automatic server setup? (y/n) {Style.RESET_ALL}")
    if i.lower() == "y":
        setupServer()
        exit()
    else:
        i = input(f"{Fore.CYAN}Start your server by running run.bat\nYou can now delete the files main.py and setup.py, Press Enter to exit...\n{Style.RESET_ALL}")
        exit()

def forge():
    system("cls")
    print(Fore.CYAN)
    tprint("Version")
    sleep(.1)
    print(Style.RESET_ALL)
    count = -1
    vers = []
    for line in forgev["versions"]:
        vers.append(line)
        count+=1
        print(f"{Fore.CYAN}[{count}] {Fore.BLUE}{line}")
    
    i = input(f"{Fore.GREEN}\nChoose a version number. Example: version=0 for [0] 1.20.1\n{Fore.CYAN}version{Style.RESET_ALL}=")
    ver = vers[int(i)]
    data = get(forgev["versions"][ver],allow_redirects=True)
    with open(f"{ver}.jar","wb") as f:
        f.write(data.content)

    call(f"java -jar {ver}.jar --installServer")
    if not path.isfile("run.bat"):
        dir = listdir()
        list = ["minecraft"]
        final = [nm for ps in list for nm in dir if ps in nm]
        
        with open("run.bat","w") as f:
            f.write(f"java -jar {final[0]} -Xmx{ram}G nogui")
    sleep(.5)
    lines = []
    for line in open("run.bat", "r"):
        if not "pause" in line.lower():
            lines.append(line)
    with open("run.bat", "w") as f:
        f.writelines(lines)
            
    sleep(.5)
    setupServer()

def paper():
    system("cls")
    print(Fore.CYAN)
    tprint("Version")
    sleep(.1)
    print(Style.RESET_ALL)
    count = -1
    ver = []
    for line in paperv["versions"]:
        ver.append(line)
        count+=1
        print(f"{Fore.CYAN}[{count}] {Fore.BLUE}{line}")
    
    i = input(f"{Fore.GREEN}\nChoose a version number. Example: version=0 for [0] 1.20.1\n{Fore.CYAN}version{Style.RESET_ALL}=")
    download_link = paperv["versions"][ver[int(i)]]
    download(download_link)

def vanilla():
    with urlopen("https://launchermeta.mojang.com/mc/game/version_manifest.json") as url:
        data = loads(url.read())
        versions = {}
        count = -1
        system("cls")
        print(Fore.CYAN)
        tprint("Version")
        print("\n")
        for line in data["versions"]:
            string = str(line["id"])
            result = ''.join([i for i in string if not i.isalpha()])
            if not result.isdigit():
                if not "-" in result:
                    if not "_" in result:
                        if not " " in result:
                            count+=1
                            versions[count] = result
        
        for x in versions:
            print(f"{Fore.CYAN}[{x}] {Fore.BLUE}{versions[x]}{Style.RESET_ALL}")

        print(f"{Fore.GREEN}Choose a version number. Example: version=0 for [0] 1.20.1")
        i = input(f"{Fore.CYAN}version{Style.RESET_ALL}=")
        downloadd = data["versions"][int(i)]["url"]
        with urlopen(downloadd) as url:
            data = loads(url.read().decode())
            download_link = data["downloads"]["server"]["url"]
            download(download_link)

if __name__ == "__main__":
    setup()
