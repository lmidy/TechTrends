# set up the default terminal
ENV["TERM"]="linux"
default_box = "opensuse/Leap-15.2.x86_64"
box_version = "15.2.31.247"

Vagrant.configure("2") do |config|
  
  # set the image for the vagrant box
 config.vm.define "master" do |master|
     master.vm.box = default_box
     master.vm.box_version = box_version
     master.vm.hostname = "master"
     master.vm.network 'private_network', ip: "192.168.63.255",  virtualbox__intnet: true
     #master.vm.network "forwarded_port", guest: 22, host: 2222, id: "ssh", disabled: true
     #master.vm.network "forwarded_port", guest: 22, host: 2000 # Master Node SSH
     master.vm.network "forwarded_port", guest: 6443, host: 6443 # API Access
     for p in 30000..30100 # expose NodePort IP's
        master.vm.network "forwarded_port", guest: p, host: p, protocol: "tcp"
        end
     master.vm.provider "virtualbox" do |vb|
       # v.memory = "3072"
       vb.memory = "2048"
       vb.cpus = 4
       vb.name = "k3s"
       vb.gui = true
       vb.customize ["modifyvm", :id, "--ioapic", "on"]
     end
    end
end
