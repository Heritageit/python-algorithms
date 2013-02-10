def resolve_urlname(request):
        """Allows us to see what the matched urlname for this request 
        is within the template"""
        from django.core.urlresolvers import resolve
        try:
            res = resolve(request.path)

            if res:
                return res.url_name
        except:
            return {}
