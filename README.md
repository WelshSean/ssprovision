# ssprovision
Provisioning of an environment using Vagrant and CFEngine


## PLEASE NOTE

If after "vagrant up" you end up with two virtual machines running CFE but with nothing interesting happening, please check that you are running version 3.7 of CFE. In order to enabled  autorun CFE forces you into some hackery. You need to do the following change to /var/cfengine/masterfiles/controls/3.7/def.cf


```
	#"services_autorun" expression => "!any";
      	"services_autorun" expression => "any";
```

this is documented on their website and it will break as soon as the Vagrant CFE provider decides to install version 3.8

## Functionality

Running "vagrant up" in this directory will create two virtual machines:

* cfhub - this is the CFEngine hub - Vagrant will copy the code in the cfengine_files subdrectory into /var/cfengine/masterfiles
* web - vagrant will bootstrap this host to cfhub over the private network and the resulting delivered CFE code from the hub will install Apache
* localhost:8080 is forwarded to cfhub:80
* localhost:8081 is forwarded to web:80
* A private network is setup between the hosts on 192.168.2.0/24
