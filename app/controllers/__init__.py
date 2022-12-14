URL_SHORTEN_BASE_ROUTE = "v1"


def register_routes(api, app, root="v1"):
    '''
    register each different API entity(base route) with namespace
    '''
    from .user_controller import user_api
    api.add_namespace(user_api, path=f"/{URL_SHORTEN_BASE_ROUTE}")
