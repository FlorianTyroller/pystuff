import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as ScrolledText
from tkinter import Canvas, Text, Scrollbar

import socket
import threading
import json
import math
from pathlib import Path
from PIL import Image, ImageTk

from board.board import Board
from board.edge import Edge
from board.corner import Corner
from board.tile import Tile
from players.player import Player


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x300")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.network_manager = NetworkManager('192.168.178.21', 34742, self)  # Configure your server IP and port
        self.network_manager.connect()

        self.frames = {}
        
        self.setup_frames()

    def setup_frames(self):
        self.frames['name_menu'] = AccountCreation(self.root, self)
        self.frames['main_menu'] = MainMenu(self.root, self)
        self.frames['create_lobby'] = LobbyCreation(self.root, self)
        self.frames['join_lobby'] = LobbyList(self.root, self)
        self.frames['lobby'] = Lobby(self.root, self)
        self.frames['game'] = Game(self.root, self)

        self.frames['name_menu'].grid(row=0, column=0, sticky="nsew", pady=20, padx=60)
        self.frames['main_menu'].grid(row=0, column=0, sticky="nsew", pady=20, padx=60)
        self.frames['create_lobby'].grid(row=0, column=0, sticky="nsew", pady=20, padx=60)
        self.frames['join_lobby'].grid(row=0, column=0, sticky="nsew", pady=20, padx=60)
        self.frames['lobby'].grid(row=0, column=0, sticky="nsew", pady=20, padx=60)
        self.frames['game'].grid(row=0, column=0, sticky="nsew", pady=20, padx=60)
        
        self.raise_frame('name_menu')

    def raise_frame(self, frame_name):
        frame = self.frames.get(frame_name)
        if frame:
            self.root.geometry(frame.geometry)
            frame.tkraise()


class AccountCreation(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.geometry = "500x300"

        label = ctk.CTkLabel(self, text="Your Name", font=("Roboto", 18))
        label.pack(pady=12)

        # Entry for lobby name
        self.name_entry = ctk.CTkEntry(self, placeholder_text="Name")
        self.name_entry.pack(pady=12)

        enter_button = ctk.CTkButton(self, text="Enter ", command=self.create_acc)
        enter_button.pack(pady=12, padx=10)

    def create_acc(self):
        name = self.name_entry.get()  
        if name:  
            message = {"type": "set_name", "content": name}
            self.controller.network_manager.send_message(message)
        else:
            print("Please enter a name.")

        
class MainMenu(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.geometry = "500x300"

        label = ctk.CTkLabel(self, text="Catan", font=("Roboto", 24))
        label.pack(pady=12)

        join_button = ctk.CTkButton(self, text="Join Game", command=lambda: controller.raise_frame('join_lobby'))
        join_button.pack(pady=12)

        create_button = ctk.CTkButton(self, text="Create Game", command=lambda: controller.raise_frame('create_lobby'))
        create_button.pack(pady=12)

        exit_button = ctk.CTkButton(self, text="Exit", command=self.exit_app)
        exit_button.pack(pady=12)

    def exit_app(self):
        self.master.quit()


class LobbyCreation(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.geometry = "500x300"

        label = ctk.CTkLabel(self, text="Create a Lobby", font=("Roboto", 18))
        label.pack(pady=12)


        # Entry for lobby name
        self.lobby_name_entry = ctk.CTkEntry(self, placeholder_text="Enter Lobby Name")
        self.lobby_name_entry.pack(pady=12)

        create_lobby_button = ctk.CTkButton(self, text="Create Lobby", command=self.create_lobby)
        create_lobby_button.pack(pady=12, padx=10)

        back_button = ctk.CTkButton(self, text="Back to Main Menu", command=lambda: controller.raise_frame('main_menu'))
        back_button.pack(pady=12, padx=10)

    def create_lobby(self):
        lobby_name = self.lobby_name_entry.get()  # Get the text from the entry widget
        if lobby_name:  # Check if the lobby name is not empty
            message = {"type": "create_lobby", "content": lobby_name}
            self.controller.network_manager.send_message(message)
        else:
            print("Please enter a lobby name.")


class LobbyList(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.geometry = "600x400"
        self.grid_columnconfigure(0, weight=1)  # Allows middle column to expand more

        # Header Label
        label = ctk.CTkLabel(self, text="Join a Lobby", font=("Roboto", 18))
        label.grid(row=0, column=0, columnspan=3, pady=12, sticky='new')

        # Treeview for lobbies
        self.lobby_tree = ttk.Treeview(self, columns=('Lobby ID', 'Lobby Name', 'Participants'), show='headings')
        self.lobby_tree.heading('Lobby ID', text='ID')
        self.lobby_tree.heading('Lobby Name', text='Name')
        self.lobby_tree.heading('Participants', text='Participants')
        self.lobby_tree.column('Lobby ID', stretch=tk.YES)
        self.lobby_tree.column('Lobby Name', stretch=tk.YES)
        self.lobby_tree.column('Participants', stretch=tk.YES)
        self.lobby_tree.grid(row=1, column=0, columnspan=3, padx=20, pady=10, sticky='nsew')

        # Join Selected Lobby Button
        join_lobby_button = ctk.CTkButton(self, text="Join Selected Lobby", command=self.join_lobby)
        join_lobby_button.grid(row=2, column=0, padx=10, pady=12, sticky='ew')

        # Refresh Lobby List Button
        refresh_button = ctk.CTkButton(self, text="Refresh Lobbies", command=self.refresh_lobbies)
        refresh_button.grid(row=2, column=1, padx=10, pady=12, sticky='ew')

        # Back to Main Menu Button
        back_button = ctk.CTkButton(self, text="Back to Main Menu", command=lambda: controller.raise_frame('main_menu'))
        back_button.grid(row=2, column=2, padx=10, pady=12, sticky='ew')

    def join_lobby(self):
        selected_item = self.lobby_tree.selection()
        if selected_item:
            lobby_id = self.lobby_tree.item(selected_item, 'values')[0]
            self.controller.network_manager.send_message({
                "type": "join_lobby",
                "content": lobby_id
            })
    
    def update_lobbies(self, lobbies):
        # Here you would clear the existing tree and reload data
        self.lobby_tree.delete(*self.lobby_tree.get_children())

        for lobby in lobbies:
            # Example of adding new data (this would typically come from a server)
            self.lobby_tree.insert('', 'end', values=(lobby['id'], lobby['name'], len(lobby["participants"])))
    


    def refresh_lobbies(self):
        self.controller.network_manager.send_message({
                "type": "get_lobbies",
                "content": None
        })
           

class Lobby(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.geometry = "650x400"

        self.grid_columnconfigure(1, weight=1)  # Gives the chat display more room to expand
        self.grid_rowconfigure(1, weight=1)  # Allows the chat and participants list to expand

        # Display the lobby name
        self.lobby_name_label = ctk.CTkLabel(self, text="Lobby Name", font=("Roboto", 18))
        self.lobby_name_label.grid(row=0, column=0, columnspan=2, pady=12, padx=20, sticky="new")

        # List of participants (using Tkinter Listbox styled to match CTk)
        self.participants_list = tk.Listbox(self, bg=ctk.CTk().cget('bg'), fg="white", relief='flat', bd=0, font=("Roboto", 10))
        self.participants_list.grid(row=1, column=0, padx=(20, 10), pady=12, sticky="nsew")

        # Chat area
        self.chat_display = ScrolledText.ScrolledText(self, height=5, state='disabled', bg=ctk.CTk().cget('bg'), fg="white", borderwidth=0)
        self.chat_display.grid(row=1, column=1, padx=(10, 20), pady=12, sticky="nsew")

        # Entry widget for sending messages
        self.chat_entry = ctk.CTkEntry(self, placeholder_text="Type your message here...")
        self.chat_entry.grid(row=2, column=0, columnspan=2, padx=20, pady=(0, 10), sticky="ew")
        self.chat_entry.bind("<Return>", self.send_chat_message)  # Bind the Enter key to send_chat_message

        # Start game button
        self.start_game_button = ctk.CTkButton(self, text="Start Game", command=self.start_game)
        self.start_game_button.grid(row=3, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="ew")


    def update_lobby(self, l_id, name, participants):
        """Update the lobby name and the list of participants."""
        self.lobby_id = l_id
        self.lobby_name_label.configure(text = name)
        self.participants_list.delete(0, 'end')
        for participant in participants:
            self.participants_list.insert('end', participant)

    def send_chat_message(self, event=None):
        """Send the current message in the chat entry to the server."""
        if self.lobby_id is None:
            return
        message = self.chat_entry.get()
        if message:
            # Assuming there's a method in controller to handle sending messages
            self.controller.network_manager.send_message({
                "type": "send_lobby_chat",
                "content": {'lobby_id': self.lobby_id, 'chat': message}
            })
            self.chat_entry.delete(0, 'end')  # Clear the entry field

    def display_chat_message(self, message, user):
        """Display a message in the chat area."""
        self.chat_display.config(state='normal')
        self.chat_display.insert('end', user + ": " + message + '\n')
        self.chat_display.config(state='disabled')
        self.chat_display.yview('end')  # Auto-scroll to the bottom

    def start_game(self):
        self.controller.network_manager.send_message({
                "type": "start_game",
                "content": self.lobby_id
            })


class Game(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.geometry = "1000x1000"
        self.player_colors = ["black", "blue", "green", "orange", "red", "white"]
        self.img_refs = set()
        self.playerdict = None
        self.board = None
        self.size = 50
        self.base_dir = Path(__file__).resolve().parent  # Adjust the traversal according to your project structure


        # Set the grid configuration
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, minsize=120)  # Row for various controls
        for i in range(8):
            if i < 7:
                self.grid_columnconfigure(i, weight=1, minsize=100)  # More weight to game canvas columns
            else:
                self.grid_columnconfigure(i, weight=0)  # Less weight to chat column, previously minsize=50

        # Main game canvas
        self.canvas = Canvas(self, bg='white')
        self.canvas.grid(row=0, column=0, columnspan=7, rowspan=6, sticky="nsew")  # Ensure it spans most columns

        # In-game chat log
        self.chat_log = Text(self, bg="lightgrey", state='disabled', wrap="word")
        self.chat_log.grid(row=0, column=7, rowspan=7, sticky="nsew")  # Only on the last column

        # Scrollbar for chat log
        chat_scrollbar = Scrollbar(self, command=self.chat_log.yview)
        chat_scrollbar.grid(row=0, column=8, rowspan=7, sticky='nse')  # Right next to chat log
        self.chat_log.config(yscrollcommand=chat_scrollbar.set)

        # Various game controls (e.g., buttons for game actions)
        self.game_controls = ctk.CTkFrame(self)
        self.game_controls.grid(row=7, column=0, columnspan=7, sticky="nsew")
        example_button = ctk.CTkButton(self.game_controls, text="Action Button", command=self.some_game_action)
        example_button.pack(pady=10, padx=10)

    def hex_to_pixel(self, coord, xoffset, yoffset):
        q, r = coord
        x = self.size * (math.sqrt(3) * q + math.sqrt(3)/2 * r) + xoffset  # Horizontal distance combining q and r
        y = - self.size * (3/2 * r) + yoffset  # Vertical distance using r only

        return x, y

    def render_board(self):
        self.img_refs = set()
        w = 800
        h = 800
        
        self.draw_board(w // 2, h // 2)

    def draw_board(self, xoffset, yoffset):
        self.draw_tiles(xoffset, yoffset)
        self.draw_edges(xoffset, yoffset)
        self.draw_corners(xoffset, yoffset)

    def draw_corners(self, xoffset, yoffset):
        for corner in self.board.corners.values():
            # Assuming corner is an object with a method get_coords that returns coordinates
            corner_coords = corner.get_coords()
            x, y = self.hex_to_pixel(corner_coords, xoffset, yoffset)

            if corner.building == 'settlement':
                path = f"{self.base_dir}/assets/pngs/cities/city_{self.player_colors[corner.owner_id]}.png"
                self.place_image_on_canvas( path, x, y, self.size, self.size, 0.5)
            else:
                self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='white')

    def draw_edges(self, xoffset, yoffset):
        for edge_k in self.board.edges:
            if self.board.edges[edge_k].is_available():
                continue
            start_pixel = self.hex_to_pixel(edge_k[0], xoffset, yoffset)
            end_pixel = self.hex_to_pixel(edge_k[1], xoffset, yoffset)
            self.draw_edge(start_pixel, end_pixel)

    def draw_edge(self, start, end, color = None):
        # Calculate midpoint
        #print(start, end)
        mid_x = (start[0] + end[0]) / 2
        mid_y = (start[1] + end[1]) / 2

        if start[1] == end[1]:
            angle_deg = 0
        elif start[1] < end[1]:
            angle_deg = -60
        else:
            angle_deg = 60 
        path = f"{self.base_dir}/assets/pngs/roads/road_blue.png"
        self.place_image_on_canvas(path, mid_x, mid_y, self.size, self.size, 0.6, rotation=angle_deg)

    def draw_tiles(self, xoffset, yoffset):
        for tile in self.board.tiles.values():
            x, y = self.hex_to_pixel(tile.get_coords(), xoffset, yoffset)
            self.draw_tile(x, y, tile.resource, tile.number)

    def draw_tile(self, x, y, r_type, number = None):
        scale = 2
        # Create hexagon points
        path = f"{self.base_dir}/assets/pngs/tiles/tile_{r_type}.png"
        self.place_image_on_canvas(path, x, y, 0.866 * self.size, self.size, scale)
        # Calculate text positioning and draw text
        text_y_offset = 20  # Vertical offset for the second text line
        self.canvas.create_text(x, y, text=r_type, fill='white', font=('Helvetica', '12', 'bold'))
        if number:
            self.canvas.create_text(x, y + text_y_offset, text=number, fill='white', font=('Helvetica', '12', 'bold'))

    def place_image_on_canvas(self, path, x, y, width, height, scale, rotation = 0):
        height = int(scale*height)
        width = int(scale*width)

        # Load and resize the image
        original_image = Image.open(path)
        resized_image = original_image.resize((width, height), Image.ANTIALIAS)
        
        if rotation != 0:
            # Rotate the image
            resized_image = resized_image.rotate(rotation, expand=True)
            x -= width / 1.5
            y -= height / 1.5
        else:
            x -= width / 2
            y -= height / 2

        # Convert the image for Tkinter
        tk_image = ImageTk.PhotoImage(resized_image)
        
        # Place the image on the canvas
        self.canvas.create_image(x, y, image=tk_image, anchor='nw')
        
        # Return the image object to keep a reference
        self.img_refs.add(tk_image)

    def update_board(self, board_d):
        self.board = Board.from_dict(board_d)
        self.render_board()
    
    def update_player(self, player):
        self.playerdict = player_d 

    def some_game_action(self):
        print("Action performed!")

    def display_chat_message(self, message):
        """Display a message in the chat area."""
        self.chat_display.config(state='normal')
        self.chat_display.insert('end', message + '\n')
        self.chat_display.config(state='disabled')
        self.chat_display.yview('end')  # Auto-scroll to the bottom

class NetworkManager:
    def __init__(self, host, port, controller):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.controller = controller  # Store the controller reference
        self.connected = False

    def connect(self):
        self.connected = True
        try:
            self.client_socket.connect((self.host, self.port))
            self.connected = True
            threading.Thread(target=self.receive_message, daemon=True).start()
        except Exception as e:
            print(f"Failed to connect to server: {e}")

    def send_message(self, message):
        print(message)
        if self.connected:
            try:
                self.client_socket.sendall(json.dumps(message).encode('utf-8'))
            except Exception as e:
                print(f"Failed to send message: {e}")

    def receive_message(self):
        buffer = ""
        while self.connected:
            try:
                part = self.client_socket.recv(1024).decode('utf-8')
                if not part:
                    print("Connection closed by the server")
                    self.connected = False
                    break

                buffer += part

                while '\n' in buffer:
                    message, _, buffer = buffer.partition('\n')
                    if message:
                        try:
                            json_message = json.loads(message)
                            print(json_message)
                            self.handle_message(json_message)
                        except json.JSONDecodeError as e:
                            print(f"JSON decode error: {e} - Message: {message}")
            except Exception as e:
                print(f"Error receiving message: {e}")
                self.connected = False

    def handle_message(self, message):
        if message['type'] == 'get_lobbies':
            lobbies = message['content']
            self.controller.frames['join_lobby'].update_lobbies(lobbies)

        elif message['type'] == 'show_game':
            self.controller.raise_frame('game')

        elif message['type'] == 'update_player':
            self.controller.frames['game'].update_player(message['content'])

        elif message['type'] == 'update_board':
            self.controller.frames['game'].update_board(message['content'])

        elif message['type'] == 'recieve_game_chat':
            chat = message['content']['chat']
            self.controller.frames['game'].display_chat_message(chat)

        elif message['type'] == 'join_lobby':
            self.controller.raise_frame('lobby')

        elif message['type'] == 'show_menu':
            self.controller.raise_frame('main_menu')

        elif message['type'] =='lobby_info':
            l_id = message['content']['id']
            l_name = message['content']['name']
            l_part = message['content']['participants']
            self.controller.frames['lobby'].update_lobby(l_id, l_name, l_part)
            
        elif message['type'] =='recieve_lobby_chat':
            chat = message['content']['chat']
            user = message['content']['user']
            self.controller.frames['lobby'].display_chat_message(chat, user)
    def close_connection(self):
        self.connected = False
        self.client_socket.close()

if __name__ == "__main__":
    root = ctk.CTk()
    app = GameApp(root)
    root.mainloop()
