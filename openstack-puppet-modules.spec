Name:       openstack-puppet-modules
Epoch:      1
Version:    9.3.0
Release:    1%{?dist}
Summary:    Puppet modules to deploy OpenStack
License:    ASL 2.0

URL:        https://github.com/redhat-openstack/openstack-puppet-modules

BuildArch:  noarch

Requires:   puppet-aodh
Requires:   puppet-apache
Requires:   puppet-barbican
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
Requires:   puppet-oslo
Requires:   puppet-ovn
Requires:   puppet-pacemaker
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

%prep

%build

%install

%files

%changelog
* Wed Oct 26 2016 Jon Schlueter <jschluet@redhat.com> 1:9.3.0-1
- Update to 9.3.0

* Fri Sep 23 2016 Alfredo Moralejo <amoralej@redhat.com> 9.0.0-0.1.0b1
- Update to 9.0.0.0b1
