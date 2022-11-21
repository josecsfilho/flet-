# #13547a
# #80d0c7
# #0f172a s-9
# #475569 s-6


"""" Flet Responsivo"""

# modulos
from flet import(
    flet,
    Page,
    Column,
    Row,
    alignment,
    padding,
    ResponsiveRow,
    border,
    Container,
    Text,
    margin,
    LinearGradient,
    PopupMenuButton,
    PopupMenuItem,
    icons,
    Icon,
    IconButton,
    animation,
    transform,

)
import time
import flet as ft

def main(page: Page):
    # title
    page.title = "Flet"

    #
    def _animate_social(e):
        if e.data == "true":
            _icon_text_.offset, _icon_text_.opacity = transform.Offset(0, 0.05), 0
            _icon_text_.update()
            for btn in _social_button.controls[:]:
                btn.offset, btn.opacity = transform.Offset(0, 0.15), 100
                btn.update()
                time.sleep(0.1)
        else:
            for btn in _social_button.controls[:]:
                btn.offset, btn.opacity = transform.Offset(0, -0.9), 0
                btn.update()
                time.sleep(0.1)
            _icon_text_.offset, _icon_text_.opacity = transform.Offset(0, -1.1), 100
            _icon_text_.update()
            

    #
    def on_resize(e):
        

        if page.width <= 730:
            _nav.controls[0].visible = False
            _nav.update()
            _min_nav.visible = True
            _min_nav.update()
        else:
            _nav.controls[0].visible = True
            _nav.update()
            _min_nav.visible = False
            _min_nav.update()

    #
    def _change_text_color(e):
        if e.control.content.color == "white":
            e.control.content.color = "#475569"
            e.control.content.update()
        else:
            e.control.content.color = "white"
            e.control.content.update()

    # navbar
    _nav = Row(
        alignment="end",
        controls=[
            Container(
                padding=padding.only(right=20),
                height=64,
                content=Row(
                    controls=[
                        Container(
                            on_hover=lambda e: _change_text_color(e),
                            content=Text(
                                "Sobre",
                                weight="w600",
                                color="white",
                            ),
                        ),
                        Container(
                            on_hover=lambda e: _change_text_color(e),
                            content=Text(
                                "Contato",
                                weight="w600",
                                color="white",
                            ),
                        ),
                        Container(
                            on_hover=lambda e: _change_text_color(e),
                            content=Text(
                                "Serviços",
                                weight="w600",
                                color="white",
                            ),
                        ),
                    ]
                ),
            ),
        ],
    )                                                                            

    # minimizando navbar
    _min_nav = Row(
        visible=False,
        controls=[
            PopupMenuButton(
                items=[
                    PopupMenuItem(text="Sobre"),
                    PopupMenuItem(text="Contato"),
                    PopupMenuItem(text="Serviços"),
                ]
            )
        ],
    )

    #título
    _title = ResponsiveRow(
        alignment="center",
        controls=[
            Container(
                col={"xs": 12, "sm": 10, "md": 10, "lg": 10, "xl": 12},
                alignment=alignment.top_center,
                padding=20,
                content=Text(
                    "Framework Flet ", color="white", # Foi inserido cor do título.
                    size=45,
                    weight="w600",
                    text_align="center",
                ),
            )
        ],
    )

    # títilo heading
    _sub_title_ = ResponsiveRow(
        alignment="center",
        controls=[
            Container(
                col={"xs": 12, "sm": 10, "md": 10, "lg": 10, "xl": 12},
                padding=20, 
                alignment=alignment.top_center,
                content=Text(
                    "Seja bem vindo", color="white",
                    text_align="center",
                    size=16,
                    weight="w500",
                ),
            )
        ],
    )

    # botão midias sociais
    _icon_list_ = [icons.FACEBOOK, icons.SHARE_SHARP, icons.TIKTOK_SHARP]

    _social_button = Row(        
        alignment="center",
        vertical_alignment="center",        
    )

    _icon_text_ = Text(
        "Conecte!",
        size=16,
        color="white",
        weight="w800",
        animate_opacity=50,
        offset=transform.Offset(0, -1.1),
        animate_offset=animation.Animation(duration=1000, curve="elasticOut"),
    )
    
    for icon in _icon_list_:
        _icon = IconButton(
            icon=icon,
            icon_size=22,
            icon_color="white",
            offset=transform.Offset(0, -0.9),
            animate_offset=animation.Animation(duration=1000, curve="elasticOut"),
            animate_opacity=50,
            opacity=0,
        )
        _social_button.controls.append(_icon)

    _icon_container = Container(
        width=145, 
        height=50, 
        bgcolor="blue800",
        border_radius=8, #
        alignment=alignment.center,      
        on_hover=lambda e: _animate_social(e),
        content=Column(
            spacing=0, 
            alignment="center",
            horizontal_alignment="center",       
            controls=[
                _social_button,
                Row(
                    alignment="center",
                    controls=[
                        _icon_text_,
                    ],
                ),
            ],
        ),
    )

    # portifolio grid responsivo
    _items = ["ITEM ONE", "ITEM TWO", "ITEM THREE", "ITEM FOUR", "ITEM FIVE", "ITEM SIX"]
    _item_row = ResponsiveRow(alignment="start", spacing=20)
    _container_item = Container(
        padding=20,
        content=_item_row,
    )

    for item in _items:
        _item_container = Container(
            aspect_ratio=1,
            bgcolor="white",
            padding=35,
            border_radius=12,
            alignment=alignment.center,
            col={"xs": 12, "sm": 4, "md": 4, "lg": 6, "xl": 4},
            content=Container(
                aspect_ratio=1,
                border_radius=8,
                #bgcolor="black",
                alignment=alignment.center,
                content=Text(
                    f"{item}",
                    size=21,
                ),
            ),
        )
        _item_row.controls.append(_item_container)


    # main column
    _main_col = Column(horizontal_alignment="center", scroll="auto")
    _main_col.controls.append(_nav)
    _main_col.controls.append(_min_nav)
    _main_col.controls.append(_title)
    _main_col.controls.append(_sub_title_)    
    _main_col.controls.append(Container(padding=padding.only(top=10)))
    _main_col.controls.append(_icon_container)
    _main_col.controls.append(Container(padding=padding.only(bottom=40)))
    _main_col.controls.append(_container_item)

    # bg container
    _background = Container(
        height=page.height,
        expand=True,
        margin=-10,
        gradient=LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=["#13547a", "#80d0c7"],

        ),

        content=_main_col,
    )

    page.add(_background)

    # resize
    page.on_resize = on_resize

if __name__ == "__main__":
    flet.app(target=main, assets_dir="assets")




