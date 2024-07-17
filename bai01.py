# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 14:06:23 2024

@author: SinhVien
"""

import tkinter as tk

def pause_recording():
    # Tạm dừng ghi
    status_label.config(text="Recording Paused")
    pass

def start_recording():
    # Bắt đầu ghi
    status_label.config(text="Recording...")
    pass



def stop_recording():
    # Dừng ghi
    status_label.config(text="Recording Stopped")
    pass

def update_status():
    # Cập nhật trạng thái ghi
    pass

root = tk.Tk()
root.title("Frame Recorder")
root.geometry("600x300")

# Cài đặt màu nền tùy chỉnh
root.configure(bg="#FF99CC")

# Tiêu đề
title_label = tk.Label(root, text="Frame Recorder", font=("Arial", 24, "bold"), bg="#FF99CC")
title_label.pack(pady=20)

# Đầu vào FPS
fps_frame = tk.Frame(root, bg="#FF99CC")
fps_frame.pack(pady=10)

fps_label = tk.Label(fps_frame, text="create an", bg="#FF99CC")
fps_label.pack(side=tk.LEFT, padx=10)

fps_entry = tk.Entry(fps_frame)
fps_entry.pack(side=tk.LEFT, padx=10)

fps_suffix_label = tk.Label(fps_frame, text="fps video", bg="#FF99CC")
fps_suffix_label.pack(side=tk.LEFT, padx=10)

# Nút
buttons_frame = tk.Frame(root, bg="#FF99CC")
buttons_frame.pack(pady=10)

pause_button = tk.Button(buttons_frame, text="Pause", command=pause_recording)
pause_button.pack(side=tk.LEFT, padx=10)

start_button = tk.Button(buttons_frame, text="Start", command=start_recording)
start_button.pack(side=tk.LEFT, padx=10)


stop_button = tk.Button(buttons_frame, text="End", command=stop_recording)
stop_button.pack(side=tk.LEFT, padx=10)

# Hiển thị trạng thái ghi
status_label = tk.Label(root, text="Recording Paused", bg="#FF99CC")
status_label.pack(pady=20)

# Cập nhật trạng thái ghi định kỳ
update_status()

root.mainloop()
