# ssprovision
Provisioning of an environment using Vagrant and CFEngine


## PLEASE NOTE

If after "vagrant up" you end up with two virtual machines running CFE but with nothing interesting happening, please check that you are running version 3.7 of CFE. In order to enabled  autorun CFE forces you into some awful hackery. You need to do the following change to /var/cfengine/masterfiles/controls/3.7/def.cf


```
	#"services_autorun" expression => "!any";
      	"services_autorun" expression => "any";
```

this is documented on their website and it will break as soon as the Vagrant CFE provider decides to install version 3.8
