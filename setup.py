from os import system

libraries = [
    "pip install colorama==0.4.6",
    "pip install tqdm==4.66.1",
    "pip install requests==2.31.0",
    "pip install art==6.0"
]

i=input("Do you want to install the required libraries? (y/n) ")
if i.lower() == "y":
    for lib in libraries:
        system(lib)
    i=input("Done!\nRun main.py? (y/n) ")
    if i.lower() == "y":
        system("python main.py")
        input("Enter to exit")
    else:
        input("Enter to exit... ")
        exit()
else:
    input("Enter to exit... ")
    exit()