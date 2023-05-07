import webview

with open('temp.txt', 'r') as file:
    data = file.read()

window_1 = webview.create_window('Solvector', f'{data}')
webview.start()
