
from matplotlib import *
import PySimpleGUI as sg
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import axes

def update_figure(data):
    axes = fig.axes
    x = 0.5 + np.arange(8)
    y = np.random.uniform(2, 7, len(x))
    axes[0].plot(x,y,'r-')
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack()

sg.theme('DarkTeal6')

table_content = []

layout = [
    [sg.Table(
        headings = ['Observações', 'Resultados'], 
        values = table_content,
        expand_x = True,
        hide_vertical_scroll = True,
        key = '-TABLE-')],
    [sg.Input(key = '-INPUT-', expand_x = True),sg.Button('Enviar')],
    [sg.Canvas(key = '-CANVAS-')]
]



window = sg.Window('Graph App', layout, finalize = True)
# matplotlib

fig = matplotlib.figure.Figure(figsize = (5,4))
fig.add_subplot(11).plot([],[])
figure_canvas_agg = FigureCanvasTkAgg(fig,window['-CANVAS-'].TKCanvas)
figure_canvas_agg.draw()
figure_canvas_agg.get_tk_widget().pack()



while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Enviar':
        new_value = values['-INPUT-']
        if new_value.isnumeric():
            table_content.append([len(table_content) + 1,float(new_value)])
            window['-TABLE-'].update(table_content)
            window['-INPUT-'].update('')
            update_figure(table_content)




window.close()    


