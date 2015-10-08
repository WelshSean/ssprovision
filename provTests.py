#!/usr/bin/python

import unittest
import subprocess 

class LoggyTests(unittest.TestCase):

    def testApacheInstalled(self):
	rc = subprocess.call([ '/usr/local/bin/vagrant', 'ssh', 'web', '-c', 'rpm -q httpd' ]) 
        self.assertEqual(rc, 0)

    def testApacheRunning(self):
	rc = subprocess.call([ '/usr/local/bin/vagrant', 'ssh', 'web', '-c', 'pgrep httpd' ]) 
        self.assertEqual(rc, 0)

    def testApacheWorking(self):
        p = subprocess.Popen([ '/usr/bin/curl', 'localhost:8081'  ],  stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	rows = 0
        for line in p.stdout.readlines():
            rows = rows +1            
        retval = p.wait()
	self.assertEqual(retval, 0)
	self.assertNotEqual(rows,0)




def main():
    unittest.main()

if __name__ == '__main__':
    main()
