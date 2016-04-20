Name:       openstack-puppet-modules
Epoch:      1
Version:    XXX
Release:    XXX
Summary:    Puppet modules to deploy OpenStack
License:    Apache-2.0

URL:        https://github.com/redhat-openstack/openstack-puppet-modules

BuildArch:  noarch

Requires:   puppet-aodh
Requires:   puppet-apache
Requires:   puppet-cassandra
Requires:   puppet-ceilometer
Requires:   puppet-ceph
Requires:   puppet-certmonger
Requires:   puppet-cinder
Requires:   puppet-collectd
Requires:   puppet-concat
Requires:   puppet-contrail
Requires:   puppet-corosync
Requires:   puppet-datacat
Requires:   puppet-elasticsearch
Requires:   puppet-firewall
Requires:   puppet-fluentd
Requires:   puppet-git
Requires:   puppet-glance
Requires:   puppet-gnocchi
Requires:   puppet-haproxy
Requires:   puppet-heat
Requires:   puppet-horizon
Requires:   puppet-inifile
Requires:   puppet-ironic
Requires:   puppet-java
Requires:   puppet-kafka
Requires:   puppet-keystone
Requires:   puppet-kibana3
Requires:   puppet-kmod
Requires:   puppet-manila
Requires:   puppet-memcached
Requires:   puppet-midonet
Requires:   puppet-mistral
Requires:   puppet-module-data
Requires:   puppet-keepalived
Requires:   puppet-mongodb
Requires:   puppet-mysql
Requires:   puppet-n1k-vsm
Requires:   puppet-neutron
Requires:   puppet-nova
Requires:   puppet-nssdb
Requires:   puppet-ntp
Requires:   puppet-opendaylight
Requires:   puppet-openstack_extras
Requires:   puppet-openstacklib
Requires:   puppet-pacemaker
Requires:   puppet-qpid
Requires:   puppet-rabbitmq
Requires:   puppet-redis
Requires:   puppet-remote
Requires:   puppet-rsync
Requires:   puppet-sahara
Requires:   puppet-sensu
Requires:   puppet-snmp
Requires:   puppet-ssh
Requires:   puppet-staging
Requires:   puppet-stdlib
Requires:   puppet-swift
Requires:   puppet-sysctl
Requires:   puppet-tempest
Requires:   puppet-timezone
Requires:   puppet-tomcat
Requires:   puppet-tripleo
Requires:   puppet-trove
Requires:   puppet-tuskar
Requires:   puppet-uchiwa
Requires:   puppet-vcsrepo
Requires:   puppet-vlan
Requires:   puppet-vswitch
Requires:   puppet-xinetd
Requires:   puppet-zaqar
Requires:   puppet-zookeeper
Requires:   puppet >= 2.7.0

%description
Metapackage for OpenStack Puppet Modules

#%prep
#%setup -q -n openstack-puppet-modules-1.0

%build

%install

%files

%changelog
