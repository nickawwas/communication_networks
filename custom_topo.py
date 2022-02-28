from mininet.net import Mininet, CLI

# Create Custom Topology in Mininet using Mid Level Python API
net = Mininet()

# Create Controller 
c0 = net.addController('c0')

# Create 4 Hosts
h1 = net.addHost('h1')
h2 = net.addHost('h2')
h3 = net.addHost('h3')
h4 = net.addHost('h4')

# Create 3 Switches
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')
s3 = net.addSwitch('s3')

# Create Links Between Hosts and Switches
net.addLink(h1, s1)
net.addLink(h2, s1)
net.addLink(h3, s3)
net.addLink(h4, s3)

# Create Links Between Switches
net.addLink(s1, s2)
net.addLink(s2, s3)

# Run Custom Network
net.start()

# Open Mininet CLI
CLI(net)

net.stop()
