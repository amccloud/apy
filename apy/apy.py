import requests

class Apy(object):
    def __init__(self, base_url=None, *args, **kwargs):
        self.__base_url__ = base_url or self.__base_url__
        self._args = []
        self._kwargs = {}
        self._base_args = list(map(unicode, args))
        self._base_kwargs = kwargs

    def __getattr__(self, name):
        self._args.append(self.__toarg__(unicode(name)))
        return self

    def __getitem__(self, name):
        self._args.append(name)
        return self

    def __call__(self, *args, **kwargs):
        args = self._base_args + self._args + list(args)
        kwargs.update(self._base_kwargs)
        kwargs.update(self._kwargs)

        for key in kwargs.keys():
            kwargs[self.__tokwarg__(unicode(key))] = kwargs.pop(key)

        url = self.__geturl__(*args, **kwargs)
        response = self.__request__(url, *args, **kwargs)

        self._args = []
        self._kwargs = {}

        return response

    def __toarg__(self, name):
        return name

    def __tokwarg__(self, name):
        return name

    def __geturl__(self, *args, **kwargs):
        url = self.__base_url__
        path = u'/'.join(args)

        if '%s' not in url:
            url = '%s%%s' % url

        url = url % path

        return url

    def __request__(self, url, *args, **kwargs):
        response = requests.get(url, params=kwargs)

        if not 200 <= response.status_code < 300:
            raise ValidationException(response.json)

        return response.json

class ValidationException(Exception):
    pass
