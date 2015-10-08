# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "box-cutter/centos70"

 config.vm.define "cfhub" do |cfhub|
   cfhub.vm.hostname = "cfhub"
   cfhub.vm.network "private_network", ip: "192.168.10.2"
   cfhub.vm.network :forwarded_port, guest: 80, host: 8080
   cfhub.vm.provision "cfengine" do |cf|
     cf.am_policy_hub = true
     cf.policy_server_address = "192.168.10.2"
     cf.files_path = "cfengine_files"       # Copy cfengine_files subdir of the vagrant root to /var/cfengine
   end
 end


 config.vm.define "web" do |web|
   web.vm.hostname = "web"
   web.vm.network "private_network", ip: "192.168.10.4"
   web.vm.network :forwarded_port, guest: 80, host: 8081
   web.vm.provision "cfengine" do |cf|
     cf.am_policy_hub = false
     cf.policy_server_address = "192.168.10.2"
     cf.classes = [ "webhost" ]    # This is documented on the Vagrant web page and should set a class but I cant get it to work 
   end
 end



end
