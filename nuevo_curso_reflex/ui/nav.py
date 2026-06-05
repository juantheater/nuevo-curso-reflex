import reflex as rx
from nuevo_curso_reflex.navigation.state import NavState
from nuevo_curso_reflex.navigation import routes


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(
            text, 
            size="4", 
            weight="medium"
        ), 
        href=url
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="pexels-pasi.jpg",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("Curso-Reflex", size="7", weight="bold"),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", routes.HOME),
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.button(
                                rx.text("Servicios", size="4", weight="medium"),
                                rx.icon("chevron-down"),
                                weight="medium",
                                variant="ghost",
                                size="3",
                            ),
                        ),
                        rx.menu.content(
                            rx.menu.item("Servicio 1"),
                            rx.menu.item("Servicio 2"),
                            rx.menu.item("Servicio 3"),
                        ),
                    ),
                    navbar_link(
                        "Base de Datos",
                        routes.DATABASE
                    ),
                    justify="end",
                    spacing="5",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="https://web.reflex-assets.dev/other/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("Curso-Reflex", size="6", weight="bold"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        rx.menu.item(
                            "Home",
                            on_click=NavState.to_home
                        ),
                        rx.menu.sub(
                            rx.menu.sub_trigger("Servicios"),
                            rx.menu.sub_content(
                                rx.menu.item("Servicio 1"),
                                rx.menu.item("Servicio 2"),
                                rx.menu.item("Servicio 3"),
                            ),
                        ),
                        rx.menu.item(
                            "Base de Datos",
                            on_click=NavState.to_data_base
                        ),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )