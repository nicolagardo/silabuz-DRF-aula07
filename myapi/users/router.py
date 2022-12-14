from rest_framework.routers import Route, SimpleRouter

class CustomRouter(SimpleRouter):
    routes = [
        Route(
            url= r'^{prefix}$',
            mapping={'get':'get'},
            name= '{basename}-list',
            detail= False,
            initkwargs={'suffix':'List'}

    ),
        Route(
                url= r'^{prefix}$',
                mapping={'get':'retreive'},
                name= '{basename}-list',
                detail= True,
                initkwargs={'suffix':'Detail'}

        )

    ]