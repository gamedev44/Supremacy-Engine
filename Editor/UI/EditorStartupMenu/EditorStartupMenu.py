import os
import sys
import subprocess
import pygame
import moderngl
import numpy as np
import json
from tkinter import Tk, filedialog

# Get the path of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Get the path of the parent directory of the current script
parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(script_dir)))

# Dynamically add the directory containing TextPatterns.py to the Python path
sys.path.insert(0, os.path.join(parent_dir, 'Engine', 'Fonts'))

# Now you can import the patterns
import TextPatterns

class EngineMenu:
    def __init__(self, size=(1280, 720)):
        pygame.init()
        self.screen_size = size
        self.screen = pygame.display.set_mode(self.screen_size, pygame.OPENGL | pygame.DOUBLEBUF)
        pygame.display.set_caption("Supremacy Engine - Launcher.exe")
        self.ctx = moderngl.create_context()
        self.ctx.viewport = (0, 0, self.screen_size[0], self.screen_size[1])
        self.ctx.enable(moderngl.BLEND)
        self.ctx.blend_func = moderngl.SRC_ALPHA, moderngl.ONE_MINUS_SRC_ALPHA
        self.setup_ui_shader()
        self.create_ui_geometry()
        
        # New: Intro screen state management
        self.config_path = os.path.join(script_dir, "config.json")
        self.config = self.load_config()
        if self.config.get("show_intro_message", True):
            self.state = "intro"
            self.show_message_checkbox = True
            self.message_text = (
                "Welcome to the Supremacy Engine Launcher.\n\n"
                "This engine framework is a personal project to explore graphics\n"
                "programming concepts and create a robust, modular foundation for\n"
                "future game development projects.\n\n"
                "Features\n"
                "  - Real-time Rendering (OpenGL)\n"
                "  - Material & Resource Management\n"
                "  - Particle & Object Systems\n"
                "  - Procedural Asset Generation\n"
                "  - Culling & Optimization Techniques\n\n"
                "Coming Soon\n"
                "  - PyBullet Physics\n"
                "  - Blender3D Plugin"
            )
        else:
            self.state = "menu"
        
        self.setup_menu()

    def load_config(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                return json.load(f)
        return {}

    def save_config(self):
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=4)

    def setup_ui_shader(self):
        self.ui_prog = self.ctx.program(
            vertex_shader='''
                #version 330 core
                in vec2 in_vert;
                uniform vec2 position;
                uniform vec2 size;
                uniform vec2 screen_size;
                void main() {
                    vec2 scaled_pos = (in_vert * size + position) / screen_size * 2.0 - 1.0;
                    scaled_pos.y = -scaled_pos.y;
                    gl_Position = vec4(scaled_pos, 0.0, 1.0);
                }
            ''',
            fragment_shader='''
                #version 330 core
                uniform vec3 color;
                uniform float alpha;
                out vec4 out_color;
                void main() {
                    out_color = vec4(color, alpha);
                }
            '''
        )
    
    def create_ui_geometry(self):
        quad_vertices = np.array([0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0], dtype=np.float32)
        indices = np.array([0, 1, 2, 0, 2, 3], dtype=np.uint32)
        self.ui_vbo = self.ctx.buffer(quad_vertices)
        self.ui_ibo = self.ctx.buffer(indices)
        self.ui_vao = self.ctx.vertex_array(
            self.ui_prog, [(self.ui_vbo, '2f', 'in_vert')], self.ui_ibo
        )

    def setup_menu(self):
        center_x = self.screen_size[0] // 2
        center_y = self.screen_size[1] // 2
        self.buttons = {
            "editor": {"rect": (center_x - 100, center_y - 25, 200, 50), "text": "OPEN EDITOR"},
            "quit": {"rect": (center_x - 100, center_y + 50, 200, 50), "text": "CLOSE LAUNCHER"},
            "reset": {"rect": (center_x - 100, center_y + 125, 200, 50), "text": "RESET SETTINGS"}
        }
        self.intro_button = {"rect": (self.screen_size[0] // 2 - 50, self.screen_size[1] - 80, 100, 40), "text": "CONTINUE"}
        self.checkbox_rect = (self.screen_size[0] // 2 - 120, self.screen_size[1] - 120, 15, 15)
        self.checkbox_text_pos = (self.screen_size[0] // 2 - 90, self.screen_size[1] - 125)
        self.scroll_y = 0

    def draw_rect(self, x, y, width, height, color, alpha=1.0):
        self.ui_prog['position'].value = (x, y)
        self.ui_prog['size'].value = (width, height)
        self.ui_prog['screen_size'].value = self.screen_size
        self.ui_prog['color'].value = color
        self.ui_prog['alpha'].value = alpha
        self.ui_vao.render()

    def draw_simple_text(self, text, x, y, size=20):
        patterns = TextPatterns.patterns
        
        pixel_size = size // 8
        char_width = 6 * pixel_size
        current_x = x
        for char in text.upper():
            if char in patterns:
                pattern = patterns[char]
                for row in range(5):
                    bits = pattern[row]
                    for col in range(5):
                        if bits & (1 << (4 - col)):
                            pixel_x = current_x + col * pixel_size
                            pixel_y = y + row * pixel_size
                            self.draw_rect(pixel_x, pixel_y, pixel_size, pixel_size, (1.0, 1.0, 1.0))
                current_x += char_width
            else:
                current_x += char_width
                
    def draw_menu(self):
        self.ctx.clear(0.1, 0.1, 0.1)
        # Draw main title
        title_text = "SUPREMACY ENGINE"
        title_width = len(title_text) * 12 * 2
        title_x = self.screen_size[0] // 2 - title_width // 2
        title_y = self.screen_size[1] // 2 - 200
        self.draw_simple_text(title_text, title_x, title_y, 32)
        
        # Draw developer name
        dev_text = "Developer Name: Asterisk"
        dev_width = len(dev_text) * 12
        dev_x = self.screen_size[0] // 2 - dev_width // 2
        dev_y = title_y + 60
        self.draw_simple_text(dev_text, dev_x, dev_y, 16)
        
        # Draw buttons
        for btn_id, btn_data in self.buttons.items():
            rect = btn_data["rect"]
            x, y, w, h = rect
            self.draw_rect(x, y, w, h, (0.15, 0.15, 0.15), 0.9)
            border_width = 2
            self.draw_rect(x, y - border_width, w, border_width, (0.5, 0.5, 0.5))
            self.draw_rect(x, y + h, w, border_width, (0.5, 0.5, 0.5))
            self.draw_rect(x - border_width, y, border_width, h, (0.5, 0.5, 0.5))
            self.draw_rect(x + w, y, border_width, h, (0.5, 0.5, 0.5))
            text_width = len(btn_data["text"]) * 12
            text_x = x + (w - text_width) // 2
            text_y = y + (h - 20) // 2
            self.draw_simple_text(btn_data["text"], text_x, text_y, 16)
    
    def draw_intro_screen(self):
        self.ctx.clear(0.1, 0.1, 0.1)
        # Draw main title
        title_text = "SUPREMACY ENGINE"
        title_width = len(title_text) * 12 * 2
        title_x = self.screen_size[0] // 2 - title_width // 2
        title_y = 50
        self.draw_simple_text(title_text, title_x, title_y, 32)

        # Draw intro message
        line_height = 30
        lines = self.message_text.split('\n')
        total_text_height = len(lines) * line_height
        
        intro_y = (self.screen_size[1] // 2) - (total_text_height // 2) - 100
        for line in lines:
            line_width = len(line) * 12
            line_x = self.screen_size[0] // 2 - line_width // 2
            self.draw_simple_text(line, line_x, intro_y, 16)
            intro_y += line_height

        # Draw "Continue" button
        rect = self.intro_button["rect"]
        x, y, w, h = rect
        self.draw_rect(x, y, w, h, (0.15, 0.15, 0.15), 0.9)
        border_width = 2
        self.draw_rect(x, y - border_width, w, border_width, (0.5, 0.5, 0.5))
        self.draw_rect(x, y + h, w, border_width, (0.5, 0.5, 0.5))
        self.draw_rect(x - border_width, y, border_width, h, (0.5, 0.5, 0.5))
        self.draw_rect(x + w, y, border_width, h, (0.5, 0.5, 0.5))
        text_width = len(self.intro_button["text"]) * 12
        text_x = x + (w - text_width) // 2
        text_y = y + (h - 20) // 2
        self.draw_simple_text(self.intro_button["text"], text_x, text_y, 16)

        # Draw checkbox
        cb_x, cb_y, cb_w, cb_h = self.checkbox_rect
        self.draw_rect(cb_x, cb_y, cb_w, cb_h, (0.15, 0.15, 0.15))
        if not self.config.get("show_intro_message", True):
            self.draw_rect(cb_x + 2, cb_y + 2, cb_w - 4, cb_h - 4, (0.8, 0.8, 0.8))
        self.draw_simple_text("DONT SHOW THIS MESSAGE AGAIN", self.checkbox_text_pos[0], self.checkbox_text_pos[1], 16)


    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.state == "menu":
                    self.handle_menu_click(event.pos)
                elif self.state == "intro":
                    self.handle_intro_click(event.pos)
            
        return True

    def handle_menu_click(self, pos):
        for btn_id, btn_data in self.buttons.items():
            rect = btn_data["rect"]
            if (rect[0] <= pos[0] <= rect[0] + rect[2] and rect[1] <= pos[1] <= rect[1] + rect[3]):
                if btn_id == "editor":
                    pygame.quit()
                    start_bat_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "start.bat"))
                    subprocess.Popen([start_bat_path], shell=True)
                    sys.exit()
                elif btn_id == "quit":
                    pygame.quit()
                    sys.exit()
                elif btn_id == "reset":
                    if os.path.exists(self.config_path):
                        os.remove(self.config_path)
                    print("Settings reset. Relaunching...")
                    # Relaunch the current script to show the intro message again
                    current_script = os.path.abspath(__file__)
                    subprocess.Popen([sys.executable, current_script], shell=True)
                    pygame.quit()
                    sys.exit()
                break

    def handle_intro_click(self, pos):
        # Handle "Continue" button click
        rect = self.intro_button["rect"]
        if (rect[0] <= pos[0] <= rect[0] + rect[2] and rect[1] <= pos[1] <= rect[1] + rect[3]):
            self.state = "menu"
            self.save_config()
            return
        
        # Handle "Don't show again" checkbox click
        cb_x, cb_y, cb_w, cb_h = self.checkbox_rect
        if (cb_x <= pos[0] <= cb_x + cb_w and cb_y <= pos[1] <= cb_y + cb_h):
            self.config["show_intro_message"] = not self.config.get("show_intro_message", True)


    def run(self):
        running = True
        while running:
            running = self.handle_input()
            if self.state == "intro":
                self.draw_intro_screen()
            elif self.state == "menu":
                self.draw_menu()
            pygame.display.flip()
        
        # Cleanup
        self.ui_vao.release()
        self.ui_vbo.release()
        self.ui_ibo.release()
        self.ui_prog.release()
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    try:
        menu = EngineMenu()
        menu.run()
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please ensure you have all dependencies installed from your requirements.txt file.")
