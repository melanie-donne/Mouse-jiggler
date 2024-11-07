import tkinter as tk
import pyautogui
import threading
import time

class MouseMoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Le bougeur de souris")
        
        # Configuration de la fenêtre principale
        self.root.geometry("300x250")
        self.root.configure(bg="#FADADD")  # Fond rose clair

        # Variables de contrôle
        self.running = False
        self.thread = None  # Stockage du thread pour éviter des conflits
        self.selected_button = None  # Garde la trace du bouton sélectionné

        # Création d'un cadre pour les boutons
        button_frame = tk.Frame(root, bg="#FADADD")
        button_frame.pack(expand=True)  # Centre le cadre verticalement

        # Style de base des boutons
        self.default_button_style = {
            "font": ("Helvetica", 12, "bold"), 
            "bg": "#C084F5", 
            "fg": "white",  # Couleur de texte toujours blanche
            "bd": 0, 
            "relief": "flat", 
            "width": 15, 
            "height": 2,
            "activebackground": "#8C75D7",  # Couleur de fond lors du clic
            "activeforeground": "white"       # Couleur de texte lors du clic
        }
        
        # Création des boutons
        self.play_button = tk.Button(button_frame, text="Play", command=self.start_movement, 
                                     **self.default_button_style)
        self.play_button.pack(pady=10)  # Espace vertical de 10 pixels entre les boutons
        
        self.pause_button = tk.Button(button_frame, text="Pause", command=self.stop_movement, 
                                      **self.default_button_style)
        self.pause_button.pack(pady=10)  # Espace vertical de 10 pixels entre les boutons

        # Ajouter un bouton pour quitter
        self.quit_button = tk.Button(button_frame, text="Quit", command=self.quit_app, 
                                     **self.default_button_style)
        self.quit_button.pack(pady=10)  # Espace vertical de 10 pixels entre les boutons

        # Ajouter les événements de clic et de survol
        self.play_button.bind("<ButtonPress>", lambda e: self.on_button_press(self.play_button))
        self.pause_button.bind("<ButtonPress>", lambda e: self.on_button_press(self.pause_button))
        self.quit_button.bind("<ButtonPress>", lambda e: self.on_button_press(self.quit_button))

        # Ajout des effets de survol (hover)
        self.play_button.bind("<Enter>", self.on_hover_play)
        self.play_button.bind("<Leave>", self.on_leave_play)
        self.pause_button.bind("<Enter>", self.on_hover_pause)
        self.pause_button.bind("<Leave>", self.on_leave_pause)
        self.quit_button.bind("<Enter>", self.on_hover_quit)
        self.quit_button.bind("<Leave>", self.on_leave_quit)

    def move_mouse(self):
        while self.running:
            pyautogui.move(5, 0)  # Déplace la souris de 5 pixels à droite
            time.sleep(0.5)       # Pause d'une demi-seconde
            pyautogui.move(-5, 0) # Déplace la souris de 5 pixels à gauche
            time.sleep(0.5)       # Pause d'une demi-seconde

    def start_movement(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.move_mouse)
            self.thread.start()

    def stop_movement(self):
        self.running = False
        if self.thread is not None:
            self.thread.join()  # Attend la fin du thread avant de continuer

    def quit_app(self):
        self.stop_movement()
        self.root.quit()  # Ferme proprement l'application

    # Gestion des événements de survol pour Play
    def on_hover_play(self, event):
        if self.selected_button != self.play_button:
            self.play_button.config(bg="#8C75D7")  # Violet plus foncé au survol

    def on_leave_play(self, event):
        if self.selected_button != self.play_button:
            self.play_button.config(bg="#C084F5")  # Retour à la couleur violette claire

    # Gestion des événements de survol pour Pause
    def on_hover_pause(self, event):
        if self.selected_button != self.pause_button:
            self.pause_button.config(bg="#8C75D7")  # Violet plus foncé au survol

    def on_leave_pause(self, event):
        if self.selected_button != self.pause_button:
            self.pause_button.config(bg="#C084F5")  # Retour à la couleur violette claire

    # Gestion des événements de survol pour Quit
    def on_hover_quit(self, event):
        if self.selected_button != self.quit_button:
            self.quit_button.config(bg="#8C75D7")  # Rouge plus foncé au survol

    def on_leave_quit(self, event):
        if self.selected_button != self.quit_button:
            self.quit_button.config(bg="#C084F5")  # Retour à la couleur rouge claire

    # Gestion des événements de clic sur les boutons
    def on_button_press(self, button):
        # Réinitialiser la couleur des autres boutons
        if self.selected_button:
            self.selected_button.config(bg="#C084F5", fg="white")  # Retour à la couleur par défaut
        button.config(bg="#8C75D7", fg="white")  # Changer la couleur du bouton lors du clic
        self.selected_button = button  # Mettre à jour le bouton sélectionné

# Création de l'interface principale
root = tk.Tk()
app = MouseMoverApp(root)

# Lancement de l'interface
root.mainloop()
