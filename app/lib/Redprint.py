from flask import Blueprint


class Redprint:
    def __init__(self, name):
        self.name = name
        self.mounds = []

    def register_blueprint(self, bp: Blueprint, url_prefix=None):
        for f, rule, options in self.mounds:
            endpoint = options.pop('endpoint', f.__name__)
            print(endpoint)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)

    def route(self, rule, **options):
        def decorator(f):
            self.add_url_rule(rule, f, **options)
            return f
        return decorator

    def add_url_rule(self, rule, f, **options):
        self.mounds.append((f, rule, options))
