import tkinter as tk

from ui import setup_ui


def main():
    root = tk.Tk()
    root.title("Book Search and Recommendation")
    setup_ui(root)
    root.mainloop()

if __name__ == "__main__":
    main()