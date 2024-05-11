IMG_REFS = set()
player_colors = ["black", "blue", "green", "orange", "red", "white"]
players: List[Player] = [Player(f"Player {i}", i, standard_board_config) for i in range(4)]

def main() -> None:
    game_board: Board = Board()
    
    c_key = ((0, -1), (0, 0),(1,-1))
    game_board.corners[c_key].set_building('settlement')
    game_board.corners[c_key].set_owner(random.randint(0,3))
    c_key = ((0, 0), (0, 1),(1,0))
    game_board.corners[c_key].set_building('city')
    game_board.corners[c_key].set_owner(random.randint(0,3))
        
        
    game_board.edges[((-2, -1), (-1, -1))].set_owner(random.randint(0,3))
    game_board.edges[((-2, 0), (-1, 0))].set_owner(random.randint(0,3))
    game_board.edges[((-2, 1), (-1, 1))].set_owner(random.randint(0,3))
    game_board.edges[((-2, 0), (-1, -1))].set_owner(random.randint(0,3))
    game_board.edges[((-2, 1), (-1, 0))].set_owner(random.randint(0,3))
    game_board.edges[((-1, 0), (-1, 1))].set_owner(random.randint(0,3))

    # Main window setup
    root = tk.Tk()
    w = 1500
    h = 1000
    size = 30
    canvas = tk.Canvas(root, width=w, height=h, background='white')
    canvas.pack()
    #Assuming a Board object called 'game_board' and size of each hex side
    draw_board(canvas, game_board, size, w // 2, h // 2)
    #draw_valid_roads(canvas, game_board, size, w // 2, h // 2, 0)
    root.mainloop()

def hex_to_pixel(coord, size, xoffset, yoffset):
    q, r = coord
    x = size * (math.sqrt(3) * q + math.sqrt(3)/2 * r) + xoffset  # Horizontal distance combining q and r
    y = - size * (3/2 * r) + yoffset  # Vertical distance using r only

    return x, y

def draw_board(canvas, board, size, xoffset, yoffset):
    draw_tiles(canvas, board, size, xoffset, yoffset)
    draw_edges(canvas, board, size, xoffset, yoffset)
    draw_corners(canvas, board, size, xoffset, yoffset)

def draw_valid_roads(canvas, board, size, xoffset, yoffset, player_id):
    valid_road_keys = players[player_id].get_valid_road_pos(board.edges, board.corners)

    for key in valid_road_keys:
        edge = board.edges[key]
        start_pixel = hex_to_pixel(edge.tile1_coord, size, xoffset, yoffset)
        end_pixel = hex_to_pixel(edge.tile2_coord, size, xoffset, yoffset)
        draw_edge(canvas, start_pixel, end_pixel, size, color=player_colors[player_id])

def draw_tiles(canvas, board, size, xoffset, yoffset):
    for tile in board.tiles.values():
        x, y = hex_to_pixel(tile.get_coords(), size, xoffset, yoffset)
        draw_tile(canvas, x, y, size, tile.resource, tile.number)


def draw_edges(canvas, board, size, xoffset, yoffset):
    for edge_k in board.edges:
        if board.edges[edge_k].is_available():
            continue
        print(edge_k)
        start_pixel = hex_to_pixel(edge_k[0], size, xoffset, yoffset)
        end_pixel = hex_to_pixel(edge_k[1], size, xoffset, yoffset)
        draw_edge(canvas, start_pixel, end_pixel, size)
    

def draw_corners(canvas, board, size, xoffset, yoffset):
    for corner in board.corners.values():
        # Assuming corner is an object with a method get_coords that returns coordinates
        corner_coords = corner.get_coords()
        x, y = hex_to_pixel(corner_coords, size, xoffset, yoffset)

        if corner.building == 'settlement':
            path = f"C:/Users/Flori/Desktop/pypy/projects/catan/assets/pngs/settlements/settlement_{player_colors[corner.owner_id]}.png"
            place_image_on_canvas(canvas, path, x, y, size, size, 0.5)
        elif corner.building == 'city':
            path = f"C:/Users/Flori/Desktop/pypy/projects/catan/assets/pngs/cities/city_{player_colors[corner.owner_id]}.png"
            place_image_on_canvas(canvas, path, x, y, size, size, 0.5)
        else:
            canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='white')


def draw_edge(canvas, start, end, size, color = None):
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
    path = f"C:/Users/Flori/Desktop/pypy/projects/catan/assets/pngs/roads/road_blue.png"
    place_image_on_canvas(canvas, path, mid_x, mid_y, size, size, 0.6, rotation=angle_deg)

    """
    # Calculate endpoints of the edge line
    edge_x1 = mid_x + size / 2 * math.cos(angle)
    edge_y1 = mid_y + size / 2 * math.sin(angle)
    edge_x2 = mid_x - size / 2 * math.cos(angle)
    edge_y2 = mid_y - size / 2 * math.sin(angle)

    # Draw the edge
    if not color:
        canvas.create_line(edge_x1, edge_y1, edge_x2, edge_y2, fill='black', width=3)
    else:
        canvas.create_line(edge_x1, edge_y1, edge_x2, edge_y2, fill=color, width=3)
    """


def place_image_on_canvas(canvas, path, x, y, width, height, scale, rotation = 0):
    height = int(scale*height)
    width = int(scale*width)
    

    """
    Load an image from the specified path, resize it, and place it on the canvas
    at the specified coordinates (x, y) with the specified width and height.
    """
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
    canvas.create_image(x, y, image=tk_image, anchor='nw')
    
    # Return the image object to keep a reference
    IMG_REFS.add(tk_image)


def draw_tile(canvas, x, y, size, r_type, number = None):
    scale = 2
    # Create hexagon points
    path = f"C:/Users/Flori/Desktop/pypy/projects/catan/assets/pngs/tiles/tile_{r_type}.png"
    place_image_on_canvas(canvas, path, x, y, 0.866 * size, size, scale)
    # Calculate text positioning and draw text
    text_y_offset = 20  # Vertical offset for the second text line
    canvas.create_text(x, y, text=r_type, fill='white', font=('Helvetica', '12', 'bold'))
    if number:
        canvas.create_text(x, y + text_y_offset, text=number, fill='white', font=('Helvetica', '12', 'bold'))

    



if __name__ == "__main__":
    main()
