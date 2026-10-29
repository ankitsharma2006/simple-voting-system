"""
Simple Voting System - GUI Application
---------------------------------------
Three core sections matching:
1. Add Candidates - Enter candidate names
2. Vote - Cast a vote
3. Result - Show vote count and winner
"""

import tkinter as tk
from tkinter import ttk, messagebox

class VotingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Voting System")
        self.geometry("900x560")
        self.minsize(800, 500)
        self.configure(bg="#f4f6f9")

        # Candidate data structure: {name: vote_count}
        self.candidates = {"Alice": 0, "Bob": 0}
        self.selected_vote_candidate = tk.StringVar(value="")

        self.setup_styles()
        self.create_widgets()
        self.refresh_all_views()

    def setup_styles(self):
        style = ttk.Style(self)
        style.theme_use("clam")

        # Configure generic colors
        style.configure("TLabel", background="#ffffff", font=("Segoe UI", 10))
        style.configure("Header.TLabel", background="#1e293b", foreground="#ffffff", font=("Segoe UI", 16, "bold"))
        style.configure("SubHeader.TLabel", background="#1e293b", foreground="#94a3b8", font=("Segoe UI", 9))
        style.configure("CardTitle.TLabel", background="#ffffff", foreground="#0f172a", font=("Segoe UI", 12, "bold"))
        style.configure("CardDesc.TLabel", background="#ffffff", foreground="#64748b", font=("Segoe UI", 9))
        
        # Primary Action Button
        style.configure("Primary.TButton", font=("Segoe UI", 10, "bold"), background="#2563eb", foreground="#ffffff")
        style.map("Primary.TButton", background=[("active", "#1d4ed8")])

        # Success Action Button
        style.configure("Success.TButton", font=("Segoe UI", 11, "bold"), background="#16a34a", foreground="#ffffff")
        style.map("Success.TButton", background=[("active", "#15803d")])

        # Danger Action Button
        style.configure("Danger.TButton", font=("Segoe UI", 9), background="#ef4444", foreground="#ffffff")
        style.map("Danger.TButton", background=[("active", "#dc2626")])

    def create_widgets(self):
        # 1. Top Header Banner
        header_frame = tk.Frame(self, bg="#1e293b", height=70)
        header_frame.pack(fill="x", side="top")
        header_frame.pack_propagate(False)

        title_lbl = ttk.Label(header_frame, text="Simple Voting System", style="Header.TLabel")
        title_lbl.pack(anchor="w", padx=25, pady=(12, 0))

        sub_lbl = ttk.Label(
            header_frame, 
            text="Add Candidates  |  Vote (Cast a vote)  |  Result (Show vote count)", 
            style="SubHeader.TLabel"
        )
        sub_lbl.pack(anchor="w", padx=25)

        # 2. Main Content 3-Column Layout
        content_frame = tk.Frame(self, bg="#f4f6f9")
        content_frame.pack(fill="both", expand=True, padx=20, pady=15)
        content_frame.columnconfigure(0, weight=1)
        content_frame.columnconfigure(1, weight=1)
        content_frame.columnconfigure(2, weight=1)
        content_frame.rowconfigure(0, weight=1)

        # ---------------- Column 1: Add Candidates ----------------
        self.create_candidates_column(content_frame)

        # ---------------- Column 2: Vote ----------------
        self.create_vote_column(content_frame)

        # ---------------- Column 3: Results ----------------
        self.create_results_column(content_frame)

        # 3. Footer Bar
        footer_frame = tk.Frame(self, bg="#e2e8f0", height=35)
        footer_frame.pack(fill="x", side="bottom")
        footer_frame.pack_propagate(False)

        self.status_var = tk.StringVar(value="System Ready. Add candidates or cast your vote.")
        status_lbl = tk.Label(footer_frame, textvariable=self.status_var, bg="#e2e8f0", fg="#475569", font=("Segoe UI", 9))
        status_lbl.pack(side="left", padx=20, pady=6)

    def create_candidates_column(self, parent):
        card = tk.Frame(parent, bg="#ffffff", highlightthickness=1, highlightbackground="#e2e8f0", bd=0)
        card.grid(row=0, column=0, sticky="nsew", padx=8, pady=5)

        # Header inside card
        header = tk.Frame(card, bg="#ffffff")
        header.pack(fill="x", padx=15, pady=(15, 8))
        ttk.Label(header, text="1. Add Candidates", style="CardTitle.TLabel").pack(anchor="w")
        ttk.Label(header, text="Enter candidate names to register", style="CardDesc.TLabel").pack(anchor="w")

        # Entry input
        entry_frame = tk.Frame(card, bg="#ffffff")
        entry_frame.pack(fill="x", padx=15, pady=5)
        
        self.candidate_entry = ttk.Entry(entry_frame, font=("Segoe UI", 10))
        self.candidate_entry.pack(side="left", fill="x", expand=True, ipady=3)
        self.candidate_entry.bind("<Return>", lambda event: self.add_candidate())

        add_btn = ttk.Button(entry_frame, text="Add", style="Primary.TButton", command=self.add_candidate)
        add_btn.pack(side="right", padx=(6, 0))

        # List of existing candidates
        list_lbl = ttk.Label(card, text="Current Candidates:", style="CardDesc.TLabel")
        list_lbl.pack(anchor="w", padx=15, pady=(10, 4))

        list_container = tk.Frame(card, bg="#ffffff")
        list_container.pack(fill="both", expand=True, padx=15, pady=(0, 10))

        self.candidate_listbox = tk.Listbox(
            list_container,
            font=("Segoe UI", 10),
            bd=1,
            relief="solid",
            highlightthickness=0,
            selectbackground="#2563eb",
            selectforeground="#ffffff"
        )
        self.candidate_listbox.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(list_container, orient="vertical", command=self.candidate_listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.candidate_listbox.config(yscrollcommand=scrollbar.set)

        # Delete button
        del_btn = ttk.Button(card, text="Remove Selected", command=self.remove_candidate)
        del_btn.pack(fill="x", padx=15, pady=(0, 15))

    def create_vote_column(self, parent):
        card = tk.Frame(parent, bg="#ffffff", highlightthickness=1, highlightbackground="#e2e8f0", bd=0)
        card.grid(row=0, column=1, sticky="nsew", padx=8, pady=5)

        header = tk.Frame(card, bg="#ffffff")
        header.pack(fill="x", padx=15, pady=(15, 8))
        ttk.Label(header, text="2. Vote", style="CardTitle.TLabel").pack(anchor="w")
        ttk.Label(header, text="Choose a candidate and cast your vote", style="CardDesc.TLabel").pack(anchor="w")

        # Scrollable container for radio buttons
        self.radio_container = tk.Frame(card, bg="#ffffff")
        self.radio_container.pack(fill="both", expand=True, padx=15, pady=10)

        # Cast Vote Button
        cast_btn = ttk.Button(card, text="Cast Vote", style="Success.TButton", command=self.cast_vote)
        cast_btn.pack(fill="x", padx=15, pady=(0, 15), ipady=4)

    def create_results_column(self, parent):
        card = tk.Frame(parent, bg="#ffffff", highlightthickness=1, highlightbackground="#e2e8f0", bd=0)
        card.grid(row=0, column=2, sticky="nsew", padx=8, pady=5)

        header = tk.Frame(card, bg="#ffffff")
        header.pack(fill="x", padx=15, pady=(15, 8))
        ttk.Label(header, text="3. Result", style="CardTitle.TLabel").pack(anchor="w")
        ttk.Label(header, text="Live vote counts and election standing", style="CardDesc.TLabel").pack(anchor="w")

        # Winner / Leader Banner
        self.winner_banner = tk.Label(
            card,
            text="No votes cast yet",
            bg="#f1f5f9",
            fg="#1e293b",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            padx=10,
            pady=8
        )
        self.winner_banner.pack(fill="x", padx=15, pady=(5, 10))

        # Result Treeview (Table)
        tree_frame = tk.Frame(card, bg="#ffffff")
        tree_frame.pack(fill="both", expand=True, padx=15, pady=0)

        columns = ("candidate", "votes", "percent")
        self.result_tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=8)
        self.result_tree.heading("candidate", text="Candidate")
        self.result_tree.heading("votes", text="Votes")
        self.result_tree.heading("percent", text="Share")

        self.result_tree.column("candidate", width=110, anchor="w")
        self.result_tree.column("votes", width=50, anchor="center")
        self.result_tree.column("percent", width=65, anchor="e")

        self.result_tree.pack(side="left", fill="both", expand=True)

        tree_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=self.result_tree.yview)
        tree_scroll.pack(side="right", fill="y")
        self.result_tree.config(yscrollcommand=tree_scroll.set)

        # Total Votes Label
        self.total_lbl = tk.Label(card, text="Total Votes: 0", bg="#ffffff", fg="#475569", font=("Segoe UI", 9, "bold"))
        self.total_lbl.pack(anchor="w", padx=15, pady=(8, 4))

        # Reset All Votes Button
        reset_btn = ttk.Button(card, text="Reset Votes to 0", style="Danger.TButton", command=self.reset_votes)
        reset_btn.pack(fill="x", padx=15, pady=(0, 15))

    def add_candidate(self):
        name = self.candidate_entry.get().strip()
        if not name:
            messagebox.showwarning("Input Required", "Please enter a candidate name.")
            return

        for existing in self.candidates:
            if existing.lower() == name.lower():
                messagebox.showerror("Duplicate", f"Candidate '{name}' already exists.")
                return

        self.candidates[name] = 0
        self.candidate_entry.delete(0, tk.END)
        self.status_var.set(f"Added candidate: {name}")
        self.refresh_all_views()

    def remove_candidate(self):
        selection = self.candidate_listbox.curselection()
        if not selection:
            messagebox.showinfo("Select Candidate", "Please select a candidate to remove.")
            return

        name = self.candidate_listbox.get(selection[0])
        if messagebox.askyesno("Confirm Removal", f"Are you sure you want to remove '{name}'?"):
            del self.candidates[name]
            if self.selected_vote_candidate.get() == name:
                self.selected_vote_candidate.set("")
            self.status_var.set(f"Removed candidate: {name}")
            self.refresh_all_views()

    def cast_vote(self):
        chosen = self.selected_vote_candidate.get()
        if not chosen:
            messagebox.showwarning("Select Candidate", "Please select a candidate to vote for.")
            return

        if chosen not in self.candidates:
            messagebox.showerror("Error", "Selected candidate is no longer available.")
            return

        self.candidates[chosen] += 1
        self.status_var.set(f"Success: Vote recorded for '{chosen}'!")
        messagebox.showinfo("Vote Cast", f"Your vote for '{chosen}' has been recorded!")
        self.refresh_all_views()

    def reset_votes(self):
        if not self.candidates:
            return
        if messagebox.askyesno("Reset Votes", "Are you sure you want to reset all vote counts to 0?"):
            for candidate in self.candidates:
                self.candidates[candidate] = 0
            self.status_var.set("All vote counts have been reset to 0.")
            self.refresh_all_views()

    def refresh_all_views(self):
        # 1. Refresh Candidate Listbox
        self.candidate_listbox.delete(0, tk.END)
        for name in self.candidates:
            self.candidate_listbox.insert(tk.END, name)

        # 2. Refresh Vote Radio Buttons
        for widget in self.radio_container.winfo_children():
            widget.destroy()

        if not self.candidates:
            no_lbl = tk.Label(self.radio_container, text="No candidates registered.\nAdd candidates first.", bg="#ffffff", fg="#94a3b8")
            no_lbl.pack(pady=20)
        else:
            for name in self.candidates:
                rb = tk.Radiobutton(
                    self.radio_container,
                    text=name,
                    value=name,
                    variable=self.selected_vote_candidate,
                    bg="#ffffff",
                    activebackground="#f1f5f9",
                    font=("Segoe UI", 10),
                    anchor="w"
                )
                rb.pack(fill="x", padx=10, pady=3)

        # 3. Refresh Results Table & Leader Banner
        for row in self.result_tree.get_children():
            self.result_tree.delete(row)

        total_votes = sum(self.candidates.values())
        self.total_lbl.config(text=f"Total Votes: {total_votes}")

        if not self.candidates:
            self.winner_banner.config(text="No candidates registered", bg="#f1f5f9", fg="#64748b")
        elif total_votes == 0:
            self.winner_banner.config(text="No votes cast yet", bg="#f1f5f9", fg="#64748b")
            for name, count in self.candidates.items():
                self.result_tree.insert("", tk.END, values=(name, count, "0.0%"))
        else:
            max_votes = max(self.candidates.values())
            winners = [name for name, v in self.candidates.items() if v == max_votes]

            if max_votes > 0:
                if len(winners) == 1:
                    self.winner_banner.config(
                        text=f"Leader: {winners[0]} ({max_votes} votes)",
                        bg="#dcfce7",
                        fg="#15803d"
                    )
                else:
                    self.winner_banner.config(
                        text=f"Tie: {', '.join(winners)} ({max_votes} ea.)",
                        bg="#fef3c7",
                        fg="#b45309"
                    )
            else:
                self.winner_banner.config(text="No votes cast yet", bg="#f1f5f9", fg="#64748b")

            for name, count in sorted(self.candidates.items(), key=lambda item: item[1], reverse=True):
                pct = (count / total_votes * 100) if total_votes > 0 else 0
                self.result_tree.insert("", tk.END, values=(name, count, f"{pct:.1f}%"))


if __name__ == "__main__":
    app = VotingApp()
    app.mainloop()
