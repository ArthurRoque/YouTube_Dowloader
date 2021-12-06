from pytube import YouTube
import PySimpleGUI as gui
from pytube.cli import on_progress
from os  import getcwd


def download(link, path):
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()
    ys.download(path)


def window_1():
    layout = [
        [gui.Text('Inserir link: '), gui.Input(key='link')],
        [gui.Text('Inserir pasta onde o arquivo deve ser baixado: '), gui.Input(f'{getcwd()}'), gui.FolderBrowse(key='path')],
        [gui.Button('Download')]
    ]

    return gui.Window('YouTube Downloader', layout, finalize=True)


def window_2():
    layout2 = [
        [gui.Text('BAIXANDO...')],
        [gui.Text(
            'Não feche o programa. Essa janela sumirá quando o vídeo tiver sido baixado.')]
    ]
    return gui.Window('Baixando', layout2, finalize=True)


def window_3():
    layout3 = [
        [gui.Text('ERRO...')],
        [gui.Text(
            '''Não foi possível realizar o download. Verifique:

        --> Link enviado para dowload.
        --> Local indicado para dowload.
        --> Conexão com internet.
        ''')]
    ]
    return gui.Window('Erro', layout3, finalize=True)


if __name__ == '__main__':
    window1, window2, window3 = window_1(), None, None
    while True:
        window, event, values = gui.read_all_windows()

        # CLOSE THE PROGRAM
        if window == window1 and event == gui.WIN_CLOSED:
            window1.close()
            break

        # GO TO NEXT WINDOW
        if window == window1 and event == 'Download':
            try:
                window2 = window_2()
                download(values['link'], values['path'])
                window2.hide()
            except:
                window2.close()
                window3 = window_3()
                

        # CLOSE SOME WINDOW
        if window == window2 and event == gui.WIN_CLOSED:
            window2.close()
        if window == window3 and event == gui.WIN_CLOSED:
            window3.close()
