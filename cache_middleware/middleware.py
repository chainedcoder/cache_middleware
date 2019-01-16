from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.cache import cache
from django.utils.deprecation import MiddlewareMixin


class GetCacheMiddleware(object):
    def process_request(self, request):
        key = request.path

        if key in settings.CACHE_URLS:
            print(key, "  Path")
            data = cache.get(key) if cache.has_key(key) else None
            if data is None:
                request._set_cache = True
                return None
            return data
        else:
            print("dont cache url")
            request._set_cache = False
            # return None


class CreateCacheMiddleware(object):
    def process_response(selfself, request, response):
        if hasattr(request, '_set_cache') and request._set_cache:
            print("Caching")
            key = request.path
            cache.set(key, response, settings.CACHE_URLS[key])

            return response
        return response


class CacheMiddleware(MiddlewareMixin,CreateCacheMiddleware, GetCacheMiddleware):
    pass