from flask import session
from functools import wraps

def login_required(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    users = dict(session).get('profile', None)
    if users:
      return f(*args, **kwargs)
    else:
      return 'Connecte toi!'
  return decorated_function