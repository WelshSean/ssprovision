# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "box-cutter/centos70"

 config.vm.define "cfhub" do |cfhub|
  cfhub.vm.hostname = "cfhub"
  cfhub.vm.network "private_network", ip: "192.168.10.2"
  end


 config.vm.define "web" do |web|
  web.vm.hostname = "web"
  web.vm.network "private_network", ip: "192.168.10.4"
  end



end
