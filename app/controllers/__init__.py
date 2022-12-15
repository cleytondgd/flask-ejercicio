URL_SHORTEN_BASE_ROUTE = "v1"


def register_routes(api, app, root="v1"):
    from .user_controller import user_api
    from .entity_controller import entity_api
    api.add_namespace(user_api, path=f"/{URL_SHORTEN_BASE_ROUTE}")
    api.add_namespace(entity_api, path=f"/{URL_SHORTEN_BASE_ROUTE}")
