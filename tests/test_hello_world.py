import unittest
import os
from procslink import RPCPeer


class HelloWorldTestCase(unittest.TestCase):
    def test_hello_world(self):
        pid = os.fork()
        if pid == 0:
            class MyAPI(object):
                def hello(self, name):
                    s = "Hello, %s!" % name
                    print(s)
                    return s
            rpc_server = RPCPeer()
            print("Server's nl_pid is %s." % rpc_server.nl_pid)
            rpc_server.register_functions_in_object(MyAPI())
            rpc_server.run_server_forever()
        else:
            rpc_client = RPCPeer()
            rpc_client.talk_to(pid).hello("Rayson Zhu")
            os.wait4(pid, 0)
