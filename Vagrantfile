Vagrant.require_version ">= 2.0.0"
Vagrant.configure("2") do |config|
 config.vm.box = "centos/7"
 config.vm.provision "shell", inline: "sudo yum install -y git python3-pip"
  config.vm.provision "ansible" do |ansible|
  ansible.verbose = "v"
  ansible.playbook = "/Users/tarchibald/projects/skillsoft_test1/ansible/setup.yaml"
  config.vm.network :forwarded_port, guest: 8080, host: 8086
  config.vm.network :forwarded_port, guest: 80, host: 9090
  end 
end