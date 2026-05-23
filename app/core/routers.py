from fastapi import APIRouter
from importlib import import_module
# from .config import settings
from .config import appconfig as settings
import os
# from app.api.v1.vehicle.routes import ( router as vehicle_router )

router = APIRouter()

# router.include_router(
#     vehicle_router,
#     tags=["Vehicle"]
# )

# Determine API versions: prefer explicit API_VERSIONS, fall back to APP_VERSION
api_versions = []
if getattr(settings, 'API_VERSIONS', None):
    api_versions = settings.API_VERSIONS
else:
    api_versions = [settings.APP_VERSION]

# Normalize versions (accept '1', '1.0.0', 'v1', comma-separated strings)
normalized_versions = []
for api_v in api_versions:
    if not api_v:
        continue
    if isinstance(api_v, str) and ',' in api_v:
        parts = [p.strip() for p in api_v.split(',') if p.strip()]
    elif isinstance(api_v, (list, tuple)):
        parts = list(api_v)
    else:
        parts = [api_v]
    for ver in parts:
        if not str(ver).startswith('v'):
            major = str(ver).split('.')[0]
            ver_name = f'v{major}'
        else:
            ver_name = str(ver)
        normalized_versions.append(ver_name)

for version in normalized_versions:
    try:
        version_module = import_module(f'app.api.{version}')
    except ModuleNotFoundError:
        # skip missing version packages
        continue

    module_names = [f.name for f in os.scandir(version_module.__path__[0]) if f.is_dir() and f.name != "__pycache__"]
    for module_name in module_names:
        routes_module = None
        for candidate in ("routes", "router", "services", "service"):
            try:
                routes_module = import_module(f'app.api.{version}.{module_name}.{candidate}')
                break
            except ModuleNotFoundError:
                routes_module = None
        if not routes_module:
            continue
        if hasattr(routes_module, 'router'):
            router.include_router(routes_module.router, prefix=f'/{version}/{module_name}', tags=[f'{version}-{module_name}'])
            