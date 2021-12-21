import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


"""
['__class__', '__del__', '__delattr__', '__dir__', '__doc__', 
'__enter__', '__eq__', '__exit__', '__format__', '__ge__', 
'__getattribute__', '__getstate__', '__gt__', '__hash__',
 '__init__', '__init_subclass__', '__le__', '__lt__'e__', '__lt__', 
 '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
  '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__',
   '__subclasshook__', '__weakref__', '_accept', '_check_sendfile_params,
   _decref_socke', '_closed', '_decref_socketios', '_io_refs', '_real_close',
    '_sendfile_use_send', '_sendfile_use_sendfile', 'accept', 'bind', 'close',
     'connect', 'connect_ex', 'detach', 'dup', 'family', 'fileno', 
     'get_inheritable''', 'getsockna, 'getblocking', 'getpeername', 
     'getsockname', 'getsockopt', 'gettimeout', 'ioctl', 'listen', 
     'makefile', 'proto', 'recv', 'recv_into', 'recvfrom', 'recvfrom_into',
      'send', 'sendall', 'sendfile', 'sendto', 'set_inherbimeout', 'shaitable',
       'setblocking', 
'setsockopt', 'settimeout', 'share', 'shutdown', 'timeout', 'type']
"""

print(s.type)