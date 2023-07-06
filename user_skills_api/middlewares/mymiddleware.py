from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.requests import Request


class AddMiddlewareUsed(BaseHTTPMiddleware):
    async def dispatch(cls,request:Request,call_next):
       response =  await call_next(request)
       response.headers["middleware_used"] = cls.__class__.__name__
       return response