# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "box-cutter/centos70"

 config.vm.define "cfhub" do |cfhub|
   cfhub.vm.hostname = "cfhub"
   cfhub.vm.network "private_network", ip: "192.168.10.2"
   cfhub.vm.provision "cfengine" do |cf|
     cf.am_policy_hub = true
     cf.policy_server_address = "192.168.10.2"
   end
 end


 config.vm.define "web" do |web|
   web.vm.hostname = "web"
   web.vm.network "private_network", ip: "192.168.10.4"
   web.vm.provision "cfengine" do |cf|
     cf.am_policy_hub = false
     cf.policy_server_address = "192.168.10.2"
   end
 end



end
