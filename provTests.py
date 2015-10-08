#!/usr/bin/python

import unittest
import subprocess 
import time

class provTests(unittest.TestCase):


    @classmethod
    def setUpClass(provTests):
        rc = subprocess.call([ '/usr/local/bin/vagrant', 'destroy', '-f' ])
        rc = subprocess.call([ '/usr/local/bin/vagrant', 'up' ])
        for i in range (1,10):
            print i,"!!!! Note sleeping for 1 minutes to let CFE do its stuff"
	    time.sleep(60)

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
