# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/trusty64"

  config.vm.network "forwarded_port", guest: 3000, host: 3000

  config.vm.synced_folder "./", "/home/vagrant/YouBot"

  config.vm.provider "virtualbox" do |vb|
    vb.name = "YouBot"
    vb.memory = "1024"
  end

  config.vm.provision "shell" do |s|
  s.path = "bootstrap.sh"
  end
end
