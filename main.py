import flet as ft
from pages.navbar import NavBar


def show_text(e):
    pass



_body = ft.Container(
    bgcolor='white',
    content=ft.GridView(#expand=True,
        padding=10,
                        expand=True,
                    runs_count=5,
                    max_extent=350,
                    #child_aspect_ratio=1.0,
                    #spacing=10,
                    #run_spacing=3,
        controls=[
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'images\1af089210c743292b0593a00618eb950.jpg',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'images\1af089210c743292b0593a00618eb950.jpg',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\6b1e2306a566a69a2f72a8b5285c75b1.jpg',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\6b1e2306a566a69a2f72a8b5285c75b1.jpg',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\6b1e2306a566a69a2f72a8b5285c75b1.jpg',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\6b1e2306a566a69a2f72a8b5285c75b1.jpg',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\6b1e2306a566a69a2f72a8b5285c75b1.jpg',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\6b1e2306a566a69a2f72a8b5285c75b1.jpg',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\6b1e2306a566a69a2f72a8b5285c75b1.jpg',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\6b1e2306a566a69a2f72a8b5285c75b1.jpg',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\6b1e2306a566a69a2f72a8b5285c75b1.jpg',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\6b1e2306a566a69a2f72a8b5285c75b1.jpg',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\6b1e2306a566a69a2f72a8b5285c75b1.jpg',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\6b1e2306a566a69a2f72a8b5285c75b1.jpg',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\6b1e2306a566a69a2f72a8b5285c75b1.jpg',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\6b1e2306a566a69a2f72a8b5285c75b1.jpg',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\6b1e2306a566a69a2f72a8b5285c75b1.jpg',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\6b1e2306a566a69a2f72a8b5285c75b1.jpg',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\6b1e2306a566a69a2f72a8b5285c75b1.jpg',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\6b1e2306a566a69a2f72a8b5285c75b1.jpg',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\6b1e2306a566a69a2f72a8b5285c75b1.jpg',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\6b1e2306a566a69a2f72a8b5285c75b1.jpg',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\6b1e2306a566a69a2f72a8b5285c75b1.jpg',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\american bully splash art.png',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\american bully splash art.png',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\american bully splash art.png',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\american bully splash art.png',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\american bully splash art.png',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\american bully splash art.png',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\american bully splash art.png',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\american bully splash art.png',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\american bully splash art.png',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\american bully splash art.png',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\american bully splash art.png',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\american bully splash art.png',fit=ft.ImageFit.CONTAIN)),
            ft.Container(border_radius=30,width=200,height=200,content=ft.Image(src=r'assets\images\american bully splash art.png',fit=ft.ImageFit.CONTAIN)),
        ]   
    )
)

def main(page: ft.Page):
    page.title = 'Movie App'
    page.bgcolor = 'black'
    page.padding = 0
    page.scroll = 'adaptive'
    page.appbar = ft.AppBar(bgcolor='white',
                            toolbar_height=50,
        title=ft.Container(padding=10,
                           content=ft.Text('For Account',
                                           weight='bold',
                                           color='black',size=12)),
        actions=[
            ft.Container(padding=10,
                         content=ft.TextField(
                             label='Search movies',
                                    content_padding=ft.padding.all(10),
                                    color='black',
                                    text_style=ft.TextStyle(
                                        weight=ft.FontWeight.W_200,                     
            ))),
            ft.Container(
                on_hover=lambda e: show_text(e),
                         content=ft.IconButton(
                             ft.icons.SEARCH,
                                icon_color='black',
                                icon_size=25,  
                                on_click=lambda e: show_text(e)))
        ]
    )
    page.navigation_bar = ft.NavigationBar(bgcolor='white',
                                           height=60,
                                           selected_index=0,
                                           
                                           
                                           
            destinations=[
                ft.NavigationDestination(
                        icon=ft.icons.HOME,
                    label="Home",
                ),
                ft.NavigationDestination(
                     icon=ft.icons.PLAYLIST_PLAY,
                    label="New & Hot"
                ),
                ft.NavigationDestination(
                     icon=ft.icons.FAVORITE,
                    label="Favorite"
                ),
                ft.NavigationDestination(
                        icon=ft.icons.PERSON,
                    label="My Account"
                ),
            ]
        )
    page.add(_body)

if __name__=='__main__':
    ft.app(target=main,assets_dir='assets')