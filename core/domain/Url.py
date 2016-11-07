
class Url:

    def __init__(self, parent, url, scheme, netloc, path, params, query, fragment, username, password, hostname, port,
                 inspect, connected):
        self.parent = parent
        self.url = url
        self.scheme = scheme
        self.netloc = netloc
        self.path = path
        self.params = params
        self.query = query
        self.fragment = fragment
        self.username = username
        self.password = password
        self.hostname = hostname
        self.port = port
        self.inspect = inspect
        self.connected = connected

    def toDBCollection(self):
        return {
            'parent': self.parent,
            'url': self.url,
            'scheme': self.scheme,
            'netloc': self.netloc,
            'path': self.path,
            'params': self.params,
            'query': self.query,
            'fragment': self.fragment,
            'username': self.username,
            'password': self.password,
            'hostname': self.hostname,
            'port': self.port,
            'inspect': self.inspect,
            'connected': self.connected,
        }
