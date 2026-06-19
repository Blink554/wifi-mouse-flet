import socket
import pyautogui

# CRITICAL: Disable PyAutoGUI delays for instant reaction times
pyautogui.PAUSE = 0.0
pyautogui.FAILSAFE = False

def start_server():
    # Local PC testing configuration
    IP_ADDRESS = "127.0.0.1"  
    PORT = 61234

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((IP_ADDRESS, PORT))
    
    print(f"=== PC UDP SERVER RUNNING ===")
    print(f"Listening on {IP_ADDRESS}:{PORT}...")
    print("Testing clean click releases. Watch your cursor!\n")

    while True:
        try:
            data, address = server.recvfrom(1024)
            command = data.decode('utf-8')
            print(f"[Signal] {command}", flush=True)
            
            if command == "left_click":
                # Force an explicit press and instant hardware release
                pyautogui.mouseDown(button='left')
                pyautogui.mouseUp(button='left')
                
            elif command == "double_click":
                # Clean native double click execution with an explicit interval
                pyautogui.click(clicks=1, interval=1)
                
            elif command == "right_click":
                pyautogui.rightClick()
                
        except KeyboardInterrupt:
            print("\nShutting down server.")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    start_server()