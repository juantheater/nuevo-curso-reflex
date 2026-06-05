import reflex as rx

"""
def social_link(label: str, href: str) -> rx.Component:
    return rx.link(rx.text(label, weight="bold"), href=href)
"""
"""
def socials() -> rx.Component:
    return rx.flex(
        social_link("IG", "/#"),
        social_link("X", "/#"),
        social_link("f", "/#"),
        social_link("in", "/#"),
        spacing="3",
        justify_content=["center", "center", "end"],
        width="100%",
    )
"""
def socials()->rx.Component:
    return rx.hstack(
        rx.link(
            rx.icon(tag="instagram", size=30, color="#E4405F"), 
            href="https://instagram.com",
            is_external=True
        ),
        rx.link(
            rx.icon(tag="twitter", size=30, color="#1DA1F2"), 
            href="https://twitter.com",
            is_external=True
        ),
        rx.link(
            rx.icon(tag="linkedin", size=30, color="#0A66C2"), 
            href="https://linkedin.com",
            is_external=True
        ),
        spacing="4",
    )

def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.divider(),
            rx.flex(
                rx.hstack(
                    rx.image(
                        src="https://web.reflex-assets.dev/other/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.text(
                        "© 2024 Reflex, Inc",
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                    ),
                    spacing="2",
                    align="center",
                    justify_content=["center", "center", "start"],
                    width="100%",
                ),
                socials(),
                spacing="4",
                flex_direction=["column", "column", "row"],
                width="100%",
            ),
            spacing="5",
            width="100%",
        ),
        width="100%",
    )