# #13547a
# #80d0c7

"""" Flet Responsivel Portifolio - Website """

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

)

def main(page: Page):
    # title
    page.title = "Flet Portfolio"



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
        if e.control.content.color == 'black':
            e.control.content.color = "white70"
            e.control.content.update()
        else:
            e.control.content.color = "black"
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
                            on_hover=lambda e:
                            _change_text_color(e),
                            content=Text(
                                "Sobre",
                                weight="w600",
                                color="black",
                            ),
                        ),
                        Container(
                            on_hover=lambda e:
                            _change_text_color(e),
                             content=Text(
                                "Contato",
                                weight="w600",
                                color="black",
                            ),
                        ),
                        Container(
                            on_hover=lambda e:
                            _change_text_color(e),
                            content=Text(
                                "Serviços",
                                weight="w600",
                                color="black",
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
                    "Framework Flet ",
                    color="white",
                    size=45,
                    weight="w600",
                    text_align="center",
                ),
            )
        ],
    )


    # main column
    _main_col = Column(horizontal_alignment="center")
    _main_col.controls.append(_nav)
    _main_col.controls.append(_min_nav)
    _main_col.controls.append(_title)

    # bg container
    _background = Container(
        height=page.height,
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
    flet.app(target=main)




