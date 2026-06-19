import socket
import flet as ft

def main(page: ft.Page):
    page.title = "Wi-Fi Mouse Controller"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Local PC testing configuration
    PC_IP = "127.0.0.1" 
    PORT = 61234

    udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_command(cmd):
        try:
            udp_client.sendto(cmd.encode('utf-8'), (PC_IP, PORT))
            status.value = f"Sent: {cmd}"
            status.color = ft.Colors.GREEN
        except Exception as e:
            status.value = f"Error: {e}"
            status.color = ft.Colors.RED
        page.update()

    status = ft.Text("Testing Clicks", size=16, color=ft.Colors.BLUE_GREY)
    
    page.add(
        ft.Column([
            status,
            ft.ElevatedButton("Left Click", on_click=lambda e: send_command("left_click"), width=200),
            ft.ElevatedButton("Double Click", on_click=lambda e: send_command("double_click"), width=200),
            ft.ElevatedButton("Right Click", on_click=lambda e: send_command("right_click"), width=200),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15)
    )

if __name__ == "__main__":
    ft.app(target=main)