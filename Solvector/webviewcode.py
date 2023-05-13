import webview

with open('temp.txt', 'r') as file:
    data = file.read().strip()

#Create window instance with link in temp file
window_1 = webview.create_window('Solvector', data)
webview.start()


