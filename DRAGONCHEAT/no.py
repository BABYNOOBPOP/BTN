#!/usr/bin/env python3
import os
import time
import subprocess
from termcolor import colored
import random
import sys

def clear_screen():
    os.system('clear')

def rainbow_banner():
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    banner_lines = [
        " ___    ___    _____  ___    _____  _   _    ",
        "(  _`\ |  _`\ (  _  )(  _`\ (  _  )( ) ( )   ",
        "| | ) || (_) )| (_) || ( (_)| ( ) || `\| |   ",
        "| | | )| ,  / |  _  || |___ | | | || , ` |   ",
        "| |_) || |\ \ | | | || (_, )| (_) || |`\ |   ",
        "(____/'(_) (_)(_) (_)(____/'(_____)(_) (_)   ",
        "                                             ",
        " ___    _   _  ___    _____  _____ ",
        "(  _`\ ( ) ( )(  _`\ (  _  )(_   _)",
        "| ( (_)| |_| || (_(_)| (_) |  | |  ",
        "| |  _ |  _  ||  _)_ |  _  |  | |  ",
        "| (_( )| | | || (_( )| | | |  | |  ",
        "(____/'(_) (_)(____/'(_) (_)  (_)  ",
        "                                   ",
        "                                   "
    ]
    
    for line in banner_lines:
        colored_line = ""
        for char in line:
            if char != ' ':
                colored_line += colored(char, random.choice(colors))
            else:
                colored_line += ' '
        print(colored_line)
    print("\n\n")

def clean_pubg_files(package):
    paths_to_remove = [
        f"/data/media/0/Android/data/{package}/files/TGPA",
        f"/storage/emulated/0/Android/data/{package}/cache/*",
        f"/storage/emulated/0/Android/data/{package}/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Screenshots/*",
        f"/storage/emulated/0/Android/data/{package}/files/log",
        f"/storage/emulated/0/Android/data/{package}/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/StatEventReportedFlag",
        f"/storage/emulated/0/Android/data/{package}/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/SaveGames/Chat/*",
        f"/storage/emulated/0/Android/data/{package}/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/WeaponDIY/*",
        f"/storage/emulated/0/Android/data/com.tencent.ig/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/VoiceBin/*",
        f"/storage/emulated/0/Android/data/{package}/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/RoleInfo/*",
        f"/storage/emulated/0/Android/data/{package}/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/GameErrorNoRecords",
        f"/storage/emulated/0/Android/data/{package}/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/*.ini",
        f"/storage/emulated/0/Android/data/{package}/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Paks/*.json",
        f"/storage/emulated/0/Android/data/{package}/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Logs/*",
        f"/storage/emulated/0/Android/data/{package}/files/iMSDK",
        f"/storage/emulated/0/Android/data/{package}/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Avatar/*",
        f"/storage/emulated/0/Android/data/{package}/files/*.log",
        f"/storage/emulated/0/Android/data/{package}/files/*.txt",
        f"/storage/emulated/0/Android/data/{package}/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Pandora/Logs",
        f"/storage/emulated/0/Android/data/{package}/files/hawk*",
        f"/storage/emulated/0/Android/data/{package}/files/cronet",
        f"/data/data/{package}/app_*",
        f"/data/data/{package}/cache",
        f"/data/data/{package}/files",
        f"/storage/emulated/0/Android/data/{package}/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Pandora/Cookies/*",
        f"/storage/emulated/0/Android/data/{package}/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Gamelet/*",
        f"/storage/emulated/0/Android/data/{package}/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Collision_Detection",
        f"/data/local/tmp/inject",
        f"/data/local/tmp/libBangjo.so"
    ]

    for path in paths_to_remove:
        try:
            if '*' in path:
                os.system(f"rm -rf {path}")
            else:
                if os.path.exists(path.replace('*', '')):
                    if os.path.isdir(path.replace('*', '')):
                        os.system(f"rm -rf {path}")
                    else:
                        os.remove(path)
        except Exception as e:
            pass

    # Create and set permissions for specific files/directories
    pandora_logs = f"/storage/emulated/0/Android/data/{package}/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Pandora/Logs"
    collision_detection = f"/storage/emulated/0/Android/data/{package}/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Collision_Detection"
    ano_tmp = f"/data/data/{package}/files/ano_tmp"
    
    for path in [pandora_logs, collision_detection]:
        try:
            if os.path.exists(path):
                os.system(f"rm -rf {path}")
            os.system(f"touch {path}")
            os.system(f"chmod 000 {path}")
        except:
            pass
    
    try:
        os.makedirs(f"/data/data/{package}/files", exist_ok=True)
        with open(ano_tmp, 'w') as f:
            pass
        os.chmod(ano_tmp, 0o000)
    except:
        pass

def inject_lib(package):
    try:
        # Copy inject and libBangjo.so to /data/local/tmp
        os.system("cp assets/inject /data/local/tmp/")
        os.system("cp assets/libBangjo.so /data/local/tmp/")
        os.system("chmod 777 /data/local/tmp/inject")
        os.system("chmod 777 /data/local/tmp/libBangjo.so")
        
        # Start the package activity
        subprocess.run(["am", "start", f"{package}/com.epicgames.ue4.SplashActivity"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(3)
        
        # Run the inject command
        os.system(f"su -c /data/local/tmp/inject -n {package} -so /data/local/tmp/libBangjo.so")
        time.sleep(1)
        
        # Clean up
        os.remove("/data/local/tmp/inject")
        os.remove("/data/local/tmp/libBangjo.so")
    except Exception as e:
        print(f"Error during injection: {e}")

def inject_lib1(package):
    try:
        # Alternative injection method
        os.system("cp assets/libBangjo.so /data/local/tmp/")
        os.system("chmod 777 /data/local/tmp/libBangjo.so")
        
        # Start the package activity
        subprocess.run(["am", "start", f"{package}/com.epicgames.ue4.SplashActivity"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(3)
        
        # Find the process ID
        pid = subprocess.getoutput(f"pidof {package}")
        if not pid:
            print("Process not found!")
            return
            
        # Inject using alternative method
        os.system(f"su -c 'export LD_PRELOAD=/data/local/tmp/libBangjo.so; kill -CONT {pid}'")
        time.sleep(1)
        
        # Clean up
        os.remove("/data/local/tmp/libBangj.so")
    except Exception as e:
        print(f"Error during injection: {e}")

def random_rainbow_color():
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    return random.choice(colors)

def colored_box_char(char):
    return colored(char, random_rainbow_color())

def rainbow_double_line(length, colors):
    colored_line = []
    for i in range(length):
        color = colors[i % len(colors)]
        colored_line.append(colored('═', color))
    return ''.join(colored_line)

def draw_rainbow_box():
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    
    box_chars = {
        'tl': colored_box_char('╔'),  
        'tr': colored_box_char('╗'),
        'bl': colored_box_char('╚'), 
        'br': colored_box_char('╝'), 
        'v': colored_box_char('║'),   
        'h': colored_box_char('═'),   
        'c': colored_box_char('╬')    
    }
    
    # Top section
    top_line = rainbow_double_line(23, colors)
    print(f"{box_chars['tl']}{top_line}{box_chars['tr']}")
    print(f"{box_chars['v']}{' ' * 23}{box_chars['v']}")
    print(f"{box_chars['v']} 1. {'com.tencent.ig'.ljust(19)}{box_chars['v']}")
    print(f"{box_chars['v']}{' ' * 23}{box_chars['v']}")
    
    # Middle connector
    right_line = rainbow_double_line(23, colors)
    print(f"{box_chars['bl']}{rainbow_double_line(23, colors)}{box_chars['c']}{right_line}{box_chars['tr']}")
    
    # Right box
    print(f"{' ' * 24}{box_chars['v']}{' ' * 23}{box_chars['v']}")
    print(f"{' ' * 24}{box_chars['v']}  2. {'com.pubg.krmobile'.ljust(18)}{box_chars['v']}")
    print(f"{' ' * 24}{box_chars['v']}{' ' * 23}{box_chars['v']}")
    
    # Left box continuation
    left_line = rainbow_double_line(23, colors)
    print(f"{box_chars['tl']}{left_line}{box_chars['c']}{rainbow_double_line(23, colors)}{box_chars['br']}")
    
    # Left box
    print(f"{box_chars['v']}{' ' * 23}{box_chars['v']}")
    print(f"{box_chars['v']} 3. {'com.vng.pubgmobile'.ljust(19)}{box_chars['v']}")
    print(f"{box_chars['v']}{' ' * 23}{box_chars['v']}")
    
    # Bottom connector
    print(f"{box_chars['bl']}{rainbow_double_line(23, colors)}{box_chars['c']}{rainbow_double_line(23, colors)}{box_chars['tr']}")
    
    # Final right box
    print(f"{' ' * 24}{box_chars['v']}{' ' * 23}{box_chars['v']}")
    print(f"{' ' * 24}{box_chars['v']}  4. {'com.rekoo.pubgm'.ljust(18)}{box_chars['v']}")
    print(f"{' ' * 24}{box_chars['v']}{' ' * 23}{box_chars['v']}")
    print(f"{' ' * 24}{box_chars['bl']}{rainbow_double_line(23, colors)}{box_chars['br']}")

def rainbow_frame(title, options=None):
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    max_length = len(title)
    
    # Find longest option text if options are provided
    if options:
        for idx, opt in enumerate(options, 1):
            option_text = f"{idx}. {opt}"
            if len(option_text) > max_length:
                max_length = len(option_text)
    
    width = max_length + 4  # padding

    # Top border
    border = ""
    for i, char in enumerate("═" * width):
        border += colored(char, colors[i % len(colors)])
    print(border)

    # Title line
    side_left = colored("║", colors[0])
    side_right = colored("║", colors[-1])
    print(f"{side_left} {title.ljust(max_length)} {side_right}")

    # Option lines
    if options:
        for idx, opt in enumerate(options, 1):
            option_text = f"{idx}. {opt}"
            print(f"{side_left} {option_text.ljust(max_length)} {side_right}")

    # Bottom border
    print(border)


def main():
    clear_screen()
    rainbow_banner()

    # Step 1: Choose Injection Method
    methods = ["Method 1", "Method 2"]
    rainbow_frame("➤ CHOOSE INJECTION METHOD")
    rainbow_frame("➤",methods)

    while True:
        try:
            method_choice = int(input("\n\nChoice method): "))
            if 1 <= method_choice <= len(methods):
                break
            else:
                print(colored("Invalid selection, try again.", 'red'))
        except ValueError:
            print(colored("Please enter a valid number.", 'red'))
            

    clear_screen()
    rainbow_banner()
    package_names = [
        "com.tencent.ig",
        "com.pubg.krmobile",
        "com.vng.pubgmobile",
        "com.rekoo.pubgm",
    ]
    rainbow_frame("➤ CHOOSE PUBG PACKAGE")
    print("\n")
    
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    
    box_chars = {
        'tl': colored_box_char('╔'),  
        'tr': colored_box_char('╗'),
        'bl': colored_box_char('╚'), 
        'br': colored_box_char('╝'), 
        'v': colored_box_char('║'),   
        'h': colored_box_char('═'),   
        'c': colored_box_char('╬')    
    }
    
    # Top section
    top_line = rainbow_double_line(23, colors)
    print(f"{box_chars['tl']}{top_line}{box_chars['tr']}")
    print(f"{box_chars['v']}{' ' * 23}{box_chars['v']}")
    print(f"{box_chars['v']} 1. {package_names[0].ljust(19)}{box_chars['v']}")
    print(f"{box_chars['v']}{' ' * 23}{box_chars['v']}")
    
    # Middle connector
    right_line = rainbow_double_line(23, colors)
    print(f"{box_chars['bl']}{rainbow_double_line(23, colors)}{box_chars['c']}{right_line}{box_chars['tr']}")
    
    # Right box
    print(f"{' ' * 24}{box_chars['v']}{' ' * 23}{box_chars['v']}")
    print(f"{' ' * 24}{box_chars['v']}  2. {package_names[1].ljust(18)}{box_chars['v']}")
    print(f"{' ' * 24}{box_chars['v']}{' ' * 23}{box_chars['v']}")
    
    # Left box continuation
    left_line = rainbow_double_line(23, colors)
    print(f"{box_chars['tl']}{left_line}{box_chars['c']}{rainbow_double_line(23, colors)}{box_chars['br']}")
    
    # Left box
    print(f"{box_chars['v']}{' ' * 23}{box_chars['v']}")
    print(f"{box_chars['v']} 3. {package_names[2].ljust(19)}{box_chars['v']}")
    print(f"{box_chars['v']}{' ' * 23}{box_chars['v']}")
    
    # Bottom connector
    print(f"{box_chars['bl']}{rainbow_double_line(23, colors)}{box_chars['c']}{rainbow_double_line(23, colors)}{box_chars['tr']}")
    
    # Final right box
    print(f"{' ' * 24}{box_chars['v']}{' ' * 23}{box_chars['v']}")
    print(f"{' ' * 24}{box_chars['v']}  4. {package_names[3].ljust(18)}{box_chars['v']}")
    print(f"{' ' * 24}{box_chars['v']}{' ' * 23}{box_chars['v']}")
    print(f"{' ' * 24}{box_chars['bl']}{rainbow_double_line(23, colors)}{box_chars['br']}")
    
    print()
    
    while True:
        try:
            choice = int(input("Enter your choice : "))
            if 1 <= choice <= len(package_names):
                selected_package = package_names[choice-1]
                break
            else:
                print("Invalid selection, try again.")
        except ValueError:
            print("Please enter a number.")
    
    clean_pubg_files(selected_package)
    inject_lib(selected_package)

    # Step 3: Clean and Inject
    print(colored(f"\nCleaning files for {selected_package}...", 'cyan'))
    clean_pubg_files(selected_package)

    if method_choice == 1:
        print(colored("\nInjecting using Method 1...", 'cyan'))
        inject_lib(selected_package)
    else:
        print(colored("\nInjecting using Method 2...", 'cyan'))
        inject_lib1(selected_package)

    print(colored("\n✅ Operation completed successfully!", 'green'))


if __name__ == "__main__":
    main()    
    
    
    
    






