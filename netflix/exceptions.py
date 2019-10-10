class NetflixError(Exception):
    pass


class NetflixItemTypeError(NetflixError):
    """Netflix ID is not valid for object."""
