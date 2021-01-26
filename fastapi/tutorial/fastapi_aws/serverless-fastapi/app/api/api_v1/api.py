from fastapi import APIRouter

from .endpoints import users
# from .models import model

router = APIRouter()

router.include_router(users.router, prefix="/users", tags=["Users"])
# router.include_router(model.router, prefix="/model", tags=["Models"])
#router.include_router(users.router, prefix="/posts", tags=["Posts"])