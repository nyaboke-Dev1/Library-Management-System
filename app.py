import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from library import Library
from models import Book, Member

library = Library()

# ─────────────────────────── Palette & Fonts ────────────────────────────────
BG_DARK      = "#0f1117"
BG_PANEL     = "#16192a"
BG_CARD      = "#1e2235"
ACCENT_GOLD  = "#c9a84c"
ACCENT_HOVER = "#e6c76a"
TEXT_PRIMARY  = "#f0ead6"
TEXT_MUTED    = "#7a8099"
BTN_DANGER   = "#8b2020"
BTN_DANGER_H = "#a83030"
BORDER       = "#2a2f45"

FONT_TITLE   = ("Georgia", 22, "bold")
FONT_SUBTITLE= ("Georgia", 10, "italic")
FONT_BTN     = ("Courier New", 11, "bold")
FONT_LABEL   = ("Courier New", 9)

# ─────────────────────────── Root Window ────────────────────────────────────
root = tk.Tk()
root.title("Library Management System")
root.geometry("760x520")
root.resizable(False, False)
root.configure(bg=BG_DARK)

# ─────────────────────────── Helper: Styled Dialog ──────────────────────────
def ask(prompt_title, prompt_text):
    """A dark-themed input dialog."""
    dlg = tk.Toplevel(root)
    dlg.title(prompt_title)
    dlg.configure(bg=BG_PANEL)
    dlg.geometry("360x160")
    dlg.resizable(False, False)
    dlg.grab_set()
    dlg.transient(root)

    # Centre over parent
    dlg.update_idletasks()
    x = root.winfo_x() + (root.winfo_width()  - 360) // 2
    y = root.winfo_y() + (root.winfo_height() - 160) // 2
    dlg.geometry(f"+{x}+{y}")

    tk.Label(dlg, text=prompt_text, bg=BG_PANEL, fg=TEXT_PRIMARY,
             font=FONT_LABEL, anchor="w").pack(padx=24, pady=(20, 6), fill="x")

    var = tk.StringVar()
    entry = tk.Entry(dlg, textvariable=var, bg=BG_CARD, fg=TEXT_PRIMARY,
                     insertbackground=ACCENT_GOLD, relief="flat",
                     font=FONT_LABEL, bd=0, highlightthickness=1,
                     highlightcolor=ACCENT_GOLD, highlightbackground=BORDER)
    entry.pack(padx=24, fill="x", ipady=6)
    entry.focus()

    result = [None]

    def confirm(event=None):
        result[0] = var.get().strip() or None
        dlg.destroy()

    def cancel(event=None):
        dlg.destroy()

    btn_frame = tk.Frame(dlg, bg=BG_PANEL)
    btn_frame.pack(pady=14, fill="x", padx=24)

    tk.Button(btn_frame, text="OK", bg=ACCENT_GOLD, fg=BG_DARK,
              font=FONT_BTN, relief="flat", bd=0,
              activebackground=ACCENT_HOVER, activeforeground=BG_DARK,
              command=confirm, width=8).pack(side="right", padx=(6, 0))
    tk.Button(btn_frame, text="Cancel", bg=BG_CARD, fg=TEXT_MUTED,
              font=FONT_BTN, relief="flat", bd=0,
              activebackground=BORDER, activeforeground=TEXT_PRIMARY,
              command=cancel, width=8).pack(side="right")

    entry.bind("<Return>", confirm)
    dlg.bind("<Escape>", cancel)
    dlg.wait_window()
    return result[0]


def info_popup(title, message):
    """A styled info popup."""
    popup = tk.Toplevel(root)
    popup.title(title)
    popup.configure(bg=BG_PANEL)
    popup.geometry("480x320")
    popup.resizable(False, False)
    popup.grab_set()
    popup.transient(root)
    popup.update_idletasks()
    x = root.winfo_x() + (root.winfo_width()  - 480) // 2
    y = root.winfo_y() + (root.winfo_height() - 320) // 2
    popup.geometry(f"+{x}+{y}")

    # Gold top bar
    tk.Frame(popup, bg=ACCENT_GOLD, height=3).pack(fill="x")

    tk.Label(popup, text=title, bg=BG_PANEL, fg=ACCENT_GOLD,
             font=("Georgia", 13, "bold"), anchor="w").pack(padx=20, pady=(16, 4), fill="x")

    frame = tk.Frame(popup, bg=BG_CARD, bd=0)
    frame.pack(padx=20, pady=6, fill="both", expand=True)

    text = tk.Text(frame, bg=BG_CARD, fg=TEXT_PRIMARY, font=FONT_LABEL,
                   relief="flat", bd=0, wrap="word",
                   selectbackground=ACCENT_GOLD, selectforeground=BG_DARK)
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=text.yview,
                              bg=BG_PANEL, troughcolor=BG_CARD, width=8)
    text.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    text.pack(fill="both", expand=True, padx=10, pady=10)
    text.insert("1.0", message)
    text.configure(state="disabled")

    tk.Button(popup, text="Close", bg=ACCENT_GOLD, fg=BG_DARK,
              font=FONT_BTN, relief="flat", bd=0,
              activebackground=ACCENT_HOVER, activeforeground=BG_DARK,
              command=popup.destroy, width=10).pack(pady=12)


# ─────────────────────────── Styled Button Factory ─────────────────────────
def make_button(parent, text, command, danger=False):
    normal_bg  = BTN_DANGER   if danger else BG_CARD
    hover_bg   = BTN_DANGER_H if danger else "#252a40"
    fg_color   = "#f0ead6"

    btn = tk.Button(
        parent, text=text, command=command,
        bg=normal_bg, fg=fg_color,
        activebackground=hover_bg, activeforeground=TEXT_PRIMARY,
        font=FONT_BTN, relief="flat", bd=0,
        anchor="w", padx=16, cursor="hand2",
        highlightthickness=0
    )

    def on_enter(e):
        btn.configure(bg=hover_bg, fg=ACCENT_GOLD if not danger else "#f0ead6")
    def on_leave(e):
        btn.configure(bg=normal_bg, fg=fg_color)

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn


# ────────────────────────── Status Bar ──────────────────────────────────────
status_var = tk.StringVar(value="Ready  •  No actions yet")

def set_status(msg):
    status_var.set(f"◈  {msg}")


# ────────────────────────── Action Functions ────────────────────────────────
def add_book_gui():
    title   = ask("Add Book", "Book title:")
    if not title: return
    author  = ask("Add Book", "Author name:")
    if not author: return
    book_no = ask("Add Book", "Book number / ISBN:")
    if not book_no: return
    book = Book(title, author, book_no)
    library.add_book(book)
    set_status(f'Book added → "{title}"')
    info_popup("Book Added", f'✓  "{title}" by {author}\n   ID: {book_no}\n\nSuccessfully added to the library.')

def register_member_gui():
    name      = ask("Register Member", "Member name:")
    if not name: return
    member_id = ask("Register Member", "Member ID:")
    if not member_id: return
    member = Member(member_id, name)
    library.register_member(member)
    set_status(f"Member registered → {name}")
    info_popup("Member Registered", f"✓  {name}\n   ID: {member_id}\n\nSuccessfully registered.")

def borrow_book_gui():
    member_id = ask("Borrow Book", "Member ID:")
    if not member_id: return
    book_no   = ask("Borrow Book", "Book number:")
    if not book_no: return
    library.borrow_book(member_id, book_no)
    set_status(f"Borrow processed — member {member_id}")

def return_book_gui():
    member_id = ask("Return Book", "Member ID:")
    if not member_id: return
    book_no   = ask("Return Book", "Book number:")
    if not book_no: return
    library.return_book(member_id, book_no)
    set_status(f"Return processed — member {member_id}")

def view_books_gui():
    books = library.get_all_books()
    if not books:
        info_popup("Library Catalogue", "The library has no books yet.")
        return
    lines = [f"{'ID':<12} {'Title':<28} {'Author':<20} Status",
             "─" * 70]
    for b in books:
        lines.append(f"{b.book_no:<12} {b.title:<28} {b.author:<20} {b.status}")
    set_status(f"{len(books)} book(s) in catalogue")
    info_popup("Library Catalogue", "\n".join(lines))

def view_members_gui():
    members = library.get_all_members()
    if not members:
        info_popup("Registered Members", "No members registered yet.")
        return
    lines = [f"{'ID':<12} {'Name':<24} Borrowed Books",
             "─" * 70]
    for m in members:
        borrowed = ", ".join(m.borrowed_books) if m.borrowed_books else "—"
        lines.append(f"{m.member_id:<12} {m.name:<24} {borrowed}")
    set_status(f"{len(members)} member(s) registered")
    info_popup("Registered Members", "\n".join(lines))


# ────────────────────────── Layout ──────────────────────────────────────────
# ── Left Sidebar ─────────────────────────────────────────────────────────────
sidebar = tk.Frame(root, bg=BG_PANEL, width=220)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

# Sidebar accent line
tk.Frame(sidebar, bg=ACCENT_GOLD, width=3).pack(side="right", fill="y")

# Branding
brand_frame = tk.Frame(sidebar, bg=BG_PANEL)
brand_frame.pack(pady=(30, 6), padx=20, fill="x")

tk.Label(brand_frame, text="📚", bg=BG_PANEL, fg=ACCENT_GOLD,
         font=("TkDefaultFont", 26)).pack(anchor="w")
tk.Label(brand_frame, text="LIBRARY", bg=BG_PANEL, fg=ACCENT_GOLD,
         font=("Courier New", 14, "bold")).pack(anchor="w")
tk.Label(brand_frame, text="Management System", bg=BG_PANEL, fg=TEXT_MUTED,
         font=FONT_SUBTITLE).pack(anchor="w")

tk.Frame(sidebar, bg=BORDER, height=1).pack(fill="x", padx=20, pady=14)

# Nav label
tk.Label(sidebar, text="ACTIONS", bg=BG_PANEL, fg=TEXT_MUTED,
         font=("Courier New", 8, "bold")).pack(anchor="w", padx=20, pady=(0, 8))

# Buttons
BUTTONS = [
    ("＋  Add Book",        add_book_gui,        False),
    ("⊕  Register Member", register_member_gui, False),
    ("⇣  Borrow Book",     borrow_book_gui,     False),
    ("⇡  Return Book",     return_book_gui,     False),
    ("≡  View Catalogue",  view_books_gui,      False),
    ("◉  View Members",    view_members_gui,    False),
]

for label, cmd, danger in BUTTONS:
    btn = make_button(sidebar, label, cmd, danger)
    btn.pack(fill="x", padx=12, pady=3, ipady=9)

tk.Frame(sidebar, bg=BORDER, height=1).pack(fill="x", padx=20, pady=14)

exit_btn = make_button(sidebar, "✕  Exit", root.destroy, danger=True)
exit_btn.pack(fill="x", padx=12, pady=3, ipady=9)

# ── Main Content Area ────────────────────────────────────────────────────────
main = tk.Frame(root, bg=BG_DARK)
main.pack(side="left", fill="both", expand=True)

# Top gold rule
tk.Frame(main, bg=ACCENT_GOLD, height=2).pack(fill="x")

# Header
header = tk.Frame(main, bg=BG_DARK)
header.pack(fill="x", padx=32, pady=(28, 0))

tk.Label(header, text="Welcome Back", bg=BG_DARK, fg=TEXT_PRIMARY,
         font=FONT_TITLE).pack(anchor="w")
tk.Label(header, text="Select an action from the sidebar to get started.",
         bg=BG_DARK, fg=TEXT_MUTED, font=FONT_SUBTITLE).pack(anchor="w", pady=(4, 0))

tk.Frame(main, bg=BORDER, height=1).pack(fill="x", padx=32, pady=20)

# ── Stats Cards ──────────────────────────────────────────────────────────────
cards_frame = tk.Frame(main, bg=BG_DARK)
cards_frame.pack(fill="x", padx=32)

def stat_card(parent, icon, label, value_getter):
    card = tk.Frame(parent, bg=BG_CARD, bd=0, highlightthickness=1,
                    highlightbackground=BORDER)
    card.pack(side="left", expand=True, fill="x", padx=(0, 12), ipady=12)

    tk.Label(card, text=icon, bg=BG_CARD, fg=ACCENT_GOLD,
             font=("TkDefaultFont", 20)).pack(pady=(12, 2))
    val_label = tk.Label(card, text=str(value_getter()), bg=BG_CARD,
                         fg=TEXT_PRIMARY, font=("Georgia", 22, "bold"))
    val_label.pack()
    tk.Label(card, text=label, bg=BG_CARD, fg=TEXT_MUTED,
             font=FONT_LABEL).pack(pady=(2, 12))
    return val_label

def book_count():
    try: return len(library.get_all_books())
    except: return 0

def member_count():
    try: return len(library.get_all_members())
    except: return 0

def borrowed_count():
    try: return sum(1 for b in library.get_all_books() if b.status != "Available")
    except: return 0

lbl_books   = stat_card(cards_frame, "📖", "Total Books",    book_count)
lbl_members = stat_card(cards_frame, "🪪", "Members",        member_count)
lbl_out     = stat_card(cards_frame, "📤", "Books Borrowed", borrowed_count)

def refresh_stats():
    try:
        lbl_books.configure(text=str(book_count()))
        lbl_members.configure(text=str(member_count()))
        lbl_out.configure(text=str(borrowed_count()))
    except:
        pass
    root.after(3000, refresh_stats)

refresh_stats()

# ── Recent Activity Panel ─────────────────────────────────────────────────────
tk.Frame(main, bg=BORDER, height=1).pack(fill="x", padx=32, pady=20)

tk.Label(main, text="SYSTEM LOG", bg=BG_DARK, fg=TEXT_MUTED,
         font=("Courier New", 8, "bold")).pack(anchor="w", padx=32)

log_frame = tk.Frame(main, bg=BG_CARD, highlightthickness=1,
                     highlightbackground=BORDER)
log_frame.pack(fill="both", expand=True, padx=32, pady=(8, 0))

log_text = tk.Text(log_frame, bg=BG_CARD, fg=TEXT_MUTED, font=("Courier New", 9),
                   relief="flat", bd=0, state="disabled", height=5,
                   wrap="word", insertbackground=ACCENT_GOLD,
                   selectbackground=ACCENT_GOLD)
log_text.pack(fill="both", expand=True, padx=12, pady=10)

log_entries = []
_orig_set_status = set_status

def set_status(msg):
    _orig_set_status(msg)
    status_var.set(f"◈  {msg}")
    log_text.configure(state="normal")
    log_entries.append(f"›  {msg}")
    if len(log_entries) > 50:
        log_entries.pop(0)
    log_text.delete("1.0", "end")
    log_text.insert("1.0", "\n".join(reversed(log_entries)))
    log_text.configure(state="disabled")

# Re-wire action functions to use the new set_status
def _wrap(fn, msg_fn):
    def wrapped():
        fn()
        set_status(msg_fn())
    return wrapped

# ── Status Bar ───────────────────────────────────────────────────────────────
status_bar = tk.Frame(root, bg=BG_PANEL, height=28)
status_bar.pack(side="bottom", fill="x")
tk.Frame(status_bar, bg=ACCENT_GOLD, height=1).pack(fill="x")
tk.Label(status_bar, textvariable=status_var, bg=BG_PANEL, fg=TEXT_MUTED,
         font=("Courier New", 8), anchor="w").pack(side="left", padx=16, pady=4)
tk.Label(status_bar, text="Library v2.0", bg=BG_PANEL, fg=BORDER,
         font=("Courier New", 8)).pack(side="right", padx=16, pady=4)

set_status("System ready  •  No actions yet")

# ─────────────────────────── Run ─────────────────────────────────────────────
root.mainloop()