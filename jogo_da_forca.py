
import flet as ft 
import string
import random
from time import sleep

class dica(ft.UserControl):
    def __init__(self,dica:str):
        super().__init__()
        self.dica=dica
    def build(self):
        return ft.Container(
            padding=ft.padding.symmetric(vertical=20,horizontal=50),
            bgcolor=ft.colors.TRANSPARENT,
            content=ft.Text(value=f'Dica: {self.dica}',size=30,weight=ft.FontWeight.BOLD,color=ft.colors.BLACK)
        )
    
def letter_to_guess(letter):
    return  ft.Container(
        bgcolor=ft.colors.BLACK,
        width=50,
        height=50,
        border_radius=ft.border_radius.all(8),
        #configurações de cor,tamanho,alinhamento e conteudo de dentro do espaço da letras
        content=ft.Text(
            value=letter,
            color=ft.colors.WHITE,
            size=25,#codigo para ajustar a altura do _ dentro do bloco
            text_align=ft.TextAlign.CENTER,
        )
    )
            
                
def main(page:ft.Page):
    palvras_sorteio=["cobra","gato","cachorro",'girafa',"jacare","largato","leopardo","onca"]
    choiced=random.choice(palvras_sorteio).upper()
    page.bgcolor=ft.colors.BROWN_700
    def reset(e):
        vitima.data=0
        vitima.src='images/hangman_0.png'
        word.data=0
        nonlocal choiced
        choiced = random.choice(palvras_sorteio).upper()
        word.controls=[letter_to_guess("_")for letter in choiced]
        keyboard.content.controls=[
                dica(dica='É Um Animal'),
                ft.Row(
                wrap=True,#comando para as letras ficarem cabendo dentro do espaco do teclado.
                alignment=ft.MainAxisAlignment.CENTER,#alinhamento horizontal do teclado
                vertical_alignment=ft.CrossAxisAlignment.CENTER,#alinhamento vertical do teclado
                controls=[
                    ft.Container(
                        height=50,
                        disabled=False,
                        width=50,
                        border_radius=ft.border_radius.all(5),
                        content=ft.Text(
                            value=letter,
                            color=ft.colors.WHITE,
                            size=30,
                            text_align=ft.TextAlign.CENTER,
                            weight=ft.FontWeight.BOLD,
                        ),
                        #bgcolor=ft.colors.BLACK,#abaixo codigo q faz o degrade das letras
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=[ft.colors.BLACK54,ft.colors.BLACK],
                        ),
                        on_click=validar_letter
                    )for letter in string.ascii_uppercase
                        
                ]
            )
                ]
            
        page.update()
    
    def validar_letter(e):
        for pos,letter in enumerate(choiced):
            if e.control.content.value == letter:
                word.controls[pos]=letter_to_guess(letter=letter)
                word.data +=1
                word.update()
        if word.data == len(choiced):
            msg1=ft.AlertDialog(
                title=ft.Text(value="você venceu!."),
                open=True)
            page.add(msg1)
            reset(e)       
        if e.control.content.value not in choiced:
            vitima.data+=1
            if vitima.data > 7:
                msg=ft.AlertDialog(
                    title=ft.Text(value=f"você perdeu!\n a palavra escolhida era: {choiced}."),
                    open=True)
                page.add(msg)
                sleep(2)
                msg.open=False
                sleep(1)
                reset(e)
                
   
        erros=vitima.data
        vitima.src= f'images/hangman_{erros}.png'
        vitima.update()
        e.control.disabled = True
        e.control.gradient = ft.LinearGradient(colors=[ft.colors.GREY])
        e.control.update()
        
    vitima=ft.Image(
        data= 0,
        src='images/hangman_0.png',
        repeat=ft.ImageRepeat.NO_REPEAT,
        height=300,
                    )
    word=ft.Row(
        data=0,
        wrap=True,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            letter_to_guess("_") for letter in choiced
        ]    
        )
    game=ft.Container(
        col={'xs':12,'lg':6},#comando para fazer a renderização da tela correto.
        padding=ft.padding.all(50),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                vitima,
                word,
            ]
        )
    )
    keyboard=ft.Container(
        col={'xs':12,'lg':6},
        image_src='images/keyboard.png',
        image_repeat=ft.ImageRepeat.NO_REPEAT,
        image_fit=ft.ImageFit.FILL,
        padding=ft.padding.only(top=150,left=80,right=80,bottom=50),    
        content=ft.Column(
            controls=[
                dica(dica='É Um Animal'),
                ft.Row(
                wrap=True,#comando para as letras ficarem cabendo dentro do espaco do teclado.
                alignment=ft.MainAxisAlignment.CENTER,#alinhamento horizontal do teclado
                vertical_alignment=ft.CrossAxisAlignment.CENTER,#alinhamento vertical do teclado
                controls=[
                    ft.Container(
                        height=50,
                        disabled=False,
                        width=50,
                        border_radius=ft.border_radius.all(5),
                        content=ft.Text(
                            value=letter,
                            color=ft.colors.WHITE,
                            size=30,
                            text_align=ft.TextAlign.CENTER,
                            weight=ft.FontWeight.BOLD,
                        ),
                        #bgcolor=ft.colors.BLACK,#abaixo codigo q faz o degrade das letras
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=[ft.colors.BLACK54,ft.colors.BLACK],
                        ),
                        on_click=validar_letter
                    )for letter in string.ascii_uppercase
                        
                ]
            )
                ]
        )
    )
    botao_reset=ft.Container(
        padding=ft.padding.all(20),
        bgcolor=ft.colors.AMBER,
        content=ft.Text(value='resetar',color=ft.colors.BLACK,weight=ft.FontWeight.W_700,size=30,text_align=ft.TextAlign.CENTER),
        expand=False,
        border_radius=ft.border_radius.all(50),
        width=50,
        col=4,
        on_click=reset,
        
        
    )
    scene=ft.Image(col=12,src='images/scene.png')
    layout=ft.ResponsiveRow(
        columns=12,
        controls=[
            scene,
            game,
            keyboard,
            ft.Container(col={'lg':8,'xs':6}),
            botao_reset,
            scene,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )
    
    page.scroll= True
    page.add(layout)
if __name__=="__main__":
    ft.app(target=main,assets_dir="assets",view=ft.WEB_BROWSER) 